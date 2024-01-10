# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vehicle/chassis/v1/chassis_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
import uprotocol_options_pb2 as uprotocol__options__pb2
import uservices_options_pb2 as uservices__options__pb2
from vehicle.chassis.v1 import chassis_topics_pb2 as vehicle_dot_chassis_dot_v1_dot_chassis__topics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(vehicle/chassis/v1/chassis_service.proto\x12\x12vehicle.chassis.v1\x1a\x17google/rpc/status.proto\x1a\x17uprotocol_options.proto\x1a\x17uservices_options.proto\x1a\'vehicle/chassis/v1/chassis_topics.proto\"^\n\x11UpdateTireRequest\x12*\n\x1cis_leak_notification_enabled\x18\x01 \x01(\x08\x42\x04\xd0\x8c\x19\x01\x12\x1d\n\x0fis_leak_present\x18\x02 \x01(\x08\x42\x04\xd0\x8c\x19\x01\"Z\n\x0bTireOptions\x12\x45\n\rresource_name\x18\x01 \x01(\x0e\x32\".vehicle.chassis.v1.Tire.ResourcesB\n\x82\xce\x18\x06tire.*:\x04\xe0\xc7\x18\x00\"w\n\x1cTractionControlSystemOptions\x12Q\n\rresource_name\x18\x01 \x01(\x0e\x32\x33.vehicle.chassis.v1.TractionControlSystem.ResourcesB\x05\x82\xce\x18\x01*:\x04\xe0\xc7\x18\n\"\x8d\x01\n\'ElectronicStabilityControlSystemOptions\x12\\\n\rresource_name\x18\x01 \x01(\x0e\x32>.vehicle.chassis.v1.ElectronicStabilityControlSystem.ResourcesB\x05\x82\xce\x18\x01*:\x04\xe0\xc7\x18\x14\x32q\n\x07\x43hassis\x12M\n\nUpdateTire\x12%.vehicle.chassis.v1.UpdateTireRequest\x1a\x12.google.rpc.Status\"\x04\xc0\xc1\x18\x01\x1a\x17\xa2\xbb\x18\x07\x63hassis\xa8\xbb\x18\x01\xb0\xbb\x18\x00\xb8\xbb\x18\x14\x42*\n&org.covesa.uservice.vehicle.chassis.v1P\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vehicle.chassis.v1.chassis_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&org.covesa.uservice.vehicle.chassis.v1P\001'
  _UPDATETIREREQUEST.fields_by_name['is_leak_notification_enabled']._options = None
  _UPDATETIREREQUEST.fields_by_name['is_leak_notification_enabled']._serialized_options = b'\320\214\031\001'
  _UPDATETIREREQUEST.fields_by_name['is_leak_present']._options = None
  _UPDATETIREREQUEST.fields_by_name['is_leak_present']._serialized_options = b'\320\214\031\001'
  _TIREOPTIONS.fields_by_name['resource_name']._options = None
  _TIREOPTIONS.fields_by_name['resource_name']._serialized_options = b'\202\316\030\006tire.*'
  _TIREOPTIONS._options = None
  _TIREOPTIONS._serialized_options = b'\340\307\030\000'
  _TRACTIONCONTROLSYSTEMOPTIONS.fields_by_name['resource_name']._options = None
  _TRACTIONCONTROLSYSTEMOPTIONS.fields_by_name['resource_name']._serialized_options = b'\202\316\030\001*'
  _TRACTIONCONTROLSYSTEMOPTIONS._options = None
  _TRACTIONCONTROLSYSTEMOPTIONS._serialized_options = b'\340\307\030\n'
  _ELECTRONICSTABILITYCONTROLSYSTEMOPTIONS.fields_by_name['resource_name']._options = None
  _ELECTRONICSTABILITYCONTROLSYSTEMOPTIONS.fields_by_name['resource_name']._serialized_options = b'\202\316\030\001*'
  _ELECTRONICSTABILITYCONTROLSYSTEMOPTIONS._options = None
  _ELECTRONICSTABILITYCONTROLSYSTEMOPTIONS._serialized_options = b'\340\307\030\024'
  _CHASSIS._options = None
  _CHASSIS._serialized_options = b'\242\273\030\007chassis\250\273\030\001\260\273\030\000\270\273\030\024'
  _CHASSIS.methods_by_name['UpdateTire']._options = None
  _CHASSIS.methods_by_name['UpdateTire']._serialized_options = b'\300\301\030\001'
  _UPDATETIREREQUEST._serialized_start=180
  _UPDATETIREREQUEST._serialized_end=274
  _TIREOPTIONS._serialized_start=276
  _TIREOPTIONS._serialized_end=366
  _TRACTIONCONTROLSYSTEMOPTIONS._serialized_start=368
  _TRACTIONCONTROLSYSTEMOPTIONS._serialized_end=487
  _ELECTRONICSTABILITYCONTROLSYSTEMOPTIONS._serialized_start=490
  _ELECTRONICSTABILITYCONTROLSYSTEMOPTIONS._serialized_end=631
  _CHASSIS._serialized_start=633
  _CHASSIS._serialized_end=746
# @@protoc_insertion_point(module_scope)
