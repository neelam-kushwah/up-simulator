"""
SPDX-FileCopyrightText: 2024 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at

    http://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
"""

from dataclasses import dataclass, field
from typing import Optional, Type

import google.protobuf.any_pb2 as any_pb2
import google.protobuf.message as message

from uprotocol.v1.uattributes_pb2 import (
    UPayloadFormat,
)
import struct
from google.protobuf.descriptor import FieldDescriptor

import google.type.timeofday_pb2  #  Import external Protobuf messages
@dataclass(frozen=True)
class UPayload:
    data: bytes = field(default_factory=bytes)
    format: UPayloadFormat = UPayloadFormat.UPAYLOAD_FORMAT_UNSPECIFIED

    # Define EMPTY as a class-level constant
    EMPTY: Optional['UPayload'] = None

    @staticmethod
    def is_empty(payload: Optional['UPayload']) -> bool:
        return payload is None or (payload.data == b'' and payload.format == UPayloadFormat.UPAYLOAD_FORMAT_UNSPECIFIED)

    @staticmethod
    def pack_to_any(message: message.Message) -> 'UPayload':
        if message is None:
            return UPayload.EMPTY
        any_message = any_pb2.Any()
        any_message.Pack(message)
        serialized_data = any_message.SerializeToString()
        return UPayload(data=serialized_data, format=UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF_WRAPPED_IN_ANY)

    @staticmethod
    def pack_to_someip_serialization(message: message.Message) -> 'UPayload':
        if message is None:
            return UPayload.EMPTY
        serialized_data = UPayload.serialize_someip(message)  # Use SOME/IP serialization
        return UPayload(data=serialized_data, format=UPayloadFormat.UPAYLOAD_FORMAT_SOMEIP)

    @staticmethod
    def pack(message: message.Message) -> 'UPayload':
        if message is None:
            return UPayload.EMPTY
        return UPayload(message.SerializeToString(), UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF)

    @staticmethod
    def pack_from_data_and_format(data: bytes, format: UPayloadFormat) -> 'UPayload':
        return UPayload(data, format)

    @staticmethod
    def unpack(payload: Optional['UPayload'], clazz: Type[message.Message]) -> Optional[message.Message]:
        if payload is None:
            return None
        return UPayload.unpack_data_format(payload.data, payload.format, clazz)

    @staticmethod
    def unpack_data_format(
        data: bytes, format: UPayloadFormat, clazz: Type[message.Message]
    ) -> Optional[message.Message]:
        format = format if format is not None else UPayloadFormat.UPAYLOAD_FORMAT_UNSPECIFIED
        if data is None or len(data) == 0:
            return None
        try:
            if format == UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF_WRAPPED_IN_ANY:
                message = clazz()
                any_message = any_pb2.Any()
                any_message.ParseFromString(data)
                any_message.Unpack(message)
                return message
            elif format == UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF:
                message = clazz()
                message.ParseFromString(data)
                return message
            elif format == UPayloadFormat.UPAYLOAD_FORMAT_SOMEIP:
                message = UPayload.deserialize_someip(data, clazz)
                return message
            else:
                return None
        except Exception:
            return None

    @staticmethod
    def serialize_someip(message):
        """
        Serializes a Protobuf message in a SOME/IP-compatible format.
        Ensures all fields are explicitly set and no fields are omitted.

        :param message: Protobuf message object
        :return: Serialized byte string
        """
        serialized_data = b""

        for field in message.DESCRIPTOR.fields:
            field_name = field.name
            field_value = getattr(message, field_name)

            # Ensure all fields have explicit default values
            if field.label != FieldDescriptor.LABEL_REPEATED:
                try:
                    if not message.HasField(field_name):
                        continue  # Skip fields that are absent
                except ValueError:
                    pass  # Primitive types don’t support HasField()

            # Convert field to binary format
            if field.type in [FieldDescriptor.TYPE_INT32, FieldDescriptor.TYPE_INT64]:
                serialized_data += struct.pack("!i", field_value)
            elif field.type == FieldDescriptor.TYPE_BOOL:
                serialized_data += struct.pack("!?", field_value)
            elif field.type == FieldDescriptor.TYPE_STRING:
                serialized_data += struct.pack(f"!H{len(field_value)}s", len(field_value), field_value.encode())
            elif field.type == FieldDescriptor.TYPE_ENUM:
                serialized_data += struct.pack("!i", field_value)
            elif field.type in [FieldDescriptor.TYPE_FLOAT, FieldDescriptor.TYPE_DOUBLE]:
                serialized_data += struct.pack("!f", field_value)
            elif field.type == FieldDescriptor.TYPE_MESSAGE:
                #  Fix: Add length prefix before serializing nested messages
                nested_serialized = UPayload.serialize_someip(field_value)
                serialized_data += struct.pack("!I", len(nested_serialized))
                serialized_data += nested_serialized
            else:
                print(f"⚠️ Skipping unsupported field: {field_name}")

        return serialized_data

    @staticmethod
    def deserialize_someip(serialized_data, message_class):
        """
        Deserializes SOME/IP formatted binary data into a Protobuf message.

        :param serialized_data: The byte string serialized using SOME/IP format
        :param message_class: The Protobuf class type (e.g., Timer, SeatMassage)
        :return: Deserialized Protobuf message object
        """
        message = message_class()
        offset = 0
        print(f"🔹 Deserializing SOME/IP data for message: {message_class.__name__}")

        for field in message.DESCRIPTOR.fields:
            field_name = field.name
            field_type = field.type

            # Deserialize based on field type
            if field_type in [FieldDescriptor.TYPE_INT32, FieldDescriptor.TYPE_INT64]:
                field_value = struct.unpack_from("!i", serialized_data, offset)[0]
                offset += 4
            elif field_type == FieldDescriptor.TYPE_BOOL:
                field_value = struct.unpack_from("!?", serialized_data, offset)[0]
                offset += 1
            elif field_type == FieldDescriptor.TYPE_STRING:
                str_length = struct.unpack_from("!H", serialized_data, offset)[0]
                offset += 2
                field_value = serialized_data[offset:offset + str_length].decode()
                offset += str_length
            elif field_type == FieldDescriptor.TYPE_ENUM:
                field_value = struct.unpack_from("!i", serialized_data, offset)[0]
                offset += 4
            elif field_type in [FieldDescriptor.TYPE_FLOAT, FieldDescriptor.TYPE_DOUBLE]:
                field_value = struct.unpack_from("!f", serialized_data, offset)[0]
                offset += 4
            elif field_type == FieldDescriptor.TYPE_MESSAGE:
                #  Ensure correct nested class resolution
                if field.message_type.full_name == "google.type.TimeOfDay":
                    nested_message_class = google.type.timeofday_pb2.TimeOfDay
                else:
                    nested_message_class = getattr(message_class, field.message_type.name, None)

                if nested_message_class is None:
                    print(f"⚠️ Could not find message class for {field.message_type.name}")
                    continue

                #  Read length of the nested message first
                nested_size = struct.unpack_from("!I", serialized_data, offset)[0]
                offset += 4
                nested_data = serialized_data[offset:offset + nested_size]
                offset += nested_size

                #  Recursively deserialize the nested message
                nested_message = UPayload.deserialize_someip(nested_data, nested_message_class)

                #  Use `.CopyFrom()` to assign correctly
                getattr(message, field_name).CopyFrom(nested_message)
                continue  # Skip setting the value at the end of the loop

            else:
                print(f"⚠️ Skipping unsupported field: {field_name}")
                continue  # Ignore unsupported types

            setattr(message, field_name, field_value)  #  Assign simple values

        print(f" Deserialized message: {message}")
        return message


# Initialize EMPTY outside the class definition
UPayload.EMPTY = UPayload(data=bytes(), format=UPayloadFormat.UPAYLOAD_FORMAT_UNSPECIFIED)
