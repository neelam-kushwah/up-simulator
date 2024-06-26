"""
SPDX-FileCopyrightText: Copyright (c) 2024 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
SPDX-FileType: SOURCE
SPDX-License-Identifier: Apache-2.0
"""

import json
import logging
import threading
import traceback

from flask_socketio import SocketIO
from google.protobuf import any_pb2
from google.protobuf.json_format import MessageToDict
from uprotocol.proto.uattributes_pb2 import CallOptions
from uprotocol.proto.umessage_pb2 import UMessage
from uprotocol.proto.upayload_pb2 import UPayload, UPayloadFormat
from uprotocol.proto.uri_pb2 import UResource
from uprotocol.rpc.rpcmapper import RpcMapper
from uprotocol.transport.ulistener import UListener
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer

from simulator.core import protobuf_autoloader
from simulator.core.vehicle_service_utils import (
    get_entity_from_descriptor,
    get_service_instance_from_entity,
    start_service,
)
from simulator.ui.utils import common_handlers
from simulator.utils import constant
from simulator.utils.common_util import verify_all_checks

logger = logging.getLogger("Simulator")


class SocketUtility:
    def __init__(self, socket_io, transport_layer):
        self.socketio = socket_io
        self.oldtopic = ""
        self.last_published_data = None
        self.transport_layer = transport_layer
        self.lock_pubsub = threading.Lock()
        self.lock_rpc = threading.Lock()
        self.lock_pubsub = threading.Lock()
        self.lock_service = threading.Lock()

    def execute_send_rpc(self, json_sendrpc):
        try:
            status = verify_all_checks()
            if status == "":
                methodname = json_sendrpc["methodname"]
                serviceclass = json_sendrpc["serviceclass"]
                mask = json.loads(json_sendrpc["mask"])
                data = json_sendrpc["data"]
                json_data = json.loads(data)

                req_cls = protobuf_autoloader.get_request_class(serviceclass, methodname)
                res_cls = protobuf_autoloader.get_response_class(serviceclass, methodname)

                if bool(mask):
                    json_data["update_mask"] = {"paths": mask}

                message = protobuf_autoloader.populate_message(serviceclass, req_cls, json_data)
                version = 1

                method_uri = protobuf_autoloader.get_rpc_uri_by_name(serviceclass, methodname, version)
                any_obj = any_pb2.Any()
                any_obj.Pack(message)
                payload_data = any_obj.SerializeToString()
                payload = UPayload(
                    value=payload_data,
                    format=UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF_WRAPPED_IN_ANY,
                )
                method_uri = LongUriSerializer().deserialize(method_uri)
                method_uri.entity.MergeFrom(
                    get_entity_from_descriptor(protobuf_autoloader.entity_descriptor[method_uri.entity.name])
                )

                method_uri.resource.MergeFrom(
                    UResource(
                        id=protobuf_autoloader.get_method_id_from_method_name(
                            method_uri.entity.name, method_uri.resource.instance
                        )
                    )
                )
                res_future = self.transport_layer.invoke_method(method_uri, payload, CallOptions(ttl=15000))
                sent_data = MessageToDict(message)

                message = "Successfully send rpc request for " + methodname
                if self.transport_layer.get_transport() == "Zenoh":
                    message = "Successfully send rpc request for " + methodname + " to Zenoh"
                res = {"msg": message, "data": sent_data}
                self.socketio.emit(
                    constant.CALLBACK_SENDRPC,
                    res,
                    namespace=constant.NAMESPACE,
                )
                if res_future is not None:
                    response = RpcMapper.map_response(res_future, res_cls)
                    common_handlers.rpc_response_handler(self.socketio, response.result())
            else:
                self.socketio.emit(
                    constant.CALLBACK_GENERIC_ERROR,
                    status,
                    namespace=constant.NAMESPACE,
                )

        except Exception:
            log = traceback.format_exc()
            self.socketio.emit(
                constant.CALLBACK_SENDRPC_EXC,
                log,
                namespace=constant.NAMESPACE,
            )

    def execute_publish(self, json_publish):
        try:
            status = verify_all_checks()
            if status == "":
                topic = json_publish["topic"]
                data = json_publish["data"]
                service_class = json_publish["service_class"]

                json_data = json.loads(data)
                service_instance = get_service_instance_from_entity(service_class)
                if service_instance is not None:
                    message, status = service_instance.publish(topic, json_data)
                    self.last_published_data = MessageToDict(message)
                    common_handlers.publish_status_handler(
                        self.socketio,
                        self.lock_pubsub,
                        self.transport_layer.get_transport(),
                        topic,
                        status.code,
                        status.message,
                        self.last_published_data,
                    )

                    self.socketio.emit(
                        constant.CALLBACK_PUBLISH_STATUS_SUCCESS,
                        {
                            "msg": "Publish Data  ",
                            "data": self.last_published_data,
                        },
                        namespace=constant.NAMESPACE,
                    )

                else:
                    self.socketio.emit(
                        constant.CALLBACK_GENERIC_ERROR,
                        "Service is not running. Please start mock service.",
                        namespace=constant.NAMESPACE,
                    )

            else:
                self.socketio.emit(
                    constant.CALLBACK_GENERIC_ERROR,
                    status,
                    namespace=constant.NAMESPACE,
                )

        except Exception:
            log = traceback.format_exc()
            self.socketio.emit(
                constant.CALLBACK_EXCEPTION_PUBLISH,
                log,
                namespace=constant.NAMESPACE,
            )

    def start_mock_service(self, json_service):
        status = verify_all_checks()
        if status == "":

            def handler(rpc_request, method_name, json_data, rpcdata):
                common_handlers.rpc_logger_handler(
                    self.socketio,
                    self.lock_rpc,
                    rpc_request,
                    method_name,
                    json_data,
                    rpcdata,
                )

            try:
                status = start_service(json_service["entity"], handler)
                self.socketio.emit(
                    constant.CALLBACK_START_SERVICE,
                    {"entity": json_service["entity"], "status": status},
                    namespace=constant.NAMESPACE,
                )
            except Exception as ex:
                logger.error("Exception:", exc_info=ex)
        else:
            print(status)

    def execute_subscribe(self, json_subscribe):
        topic = json_subscribe["topic"]
        try:
            status = verify_all_checks()
            if status == "":
                new_topic = LongUriSerializer().deserialize(topic)
                new_topic.entity.MergeFrom(
                    get_entity_from_descriptor(protobuf_autoloader.entity_descriptor[new_topic.entity.name])
                )
                new_topic.resource.MergeFrom(UResource(id=protobuf_autoloader.get_topic_id_from_topicuri(topic)))

                status = self.transport_layer.register_listener(
                    new_topic,
                    SubscribeUListener(
                        self.socketio,
                        self.transport_layer.get_transport(),
                        self.lock_pubsub,
                    ),
                )
                if status is None:
                    common_handlers.subscribe_status_handler(
                        self.socketio,
                        self.lock_pubsub,
                        self.transport_layer.get_transport(),
                        topic,
                        0,
                        "Ok",
                    )
                else:
                    common_handlers.subscribe_status_handler(
                        self.socketio,
                        self.lock_pubsub,
                        self.transport_layer.get_transport(),
                        topic,
                        status.code,
                        status.message,
                    )

            else:
                self.socketio.emit(
                    constant.CALLBACK_GENERIC_ERROR,
                    status,
                    namespace=constant.NAMESPACE,
                )

        except Exception:
            log = traceback.format_exc()
            self.socketio.emit(
                constant.CALLBACK_EXCEPTION_SUBSCRIBE,
                log,
                namespace=constant.NAMESPACE,
            )


class SubscribeUListener(UListener):
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, socketio: SocketIO, utransport: str, lock_pubsub: threading.Lock):
        if not self._initialized:
            self.__socketio = socketio
            self.__utransport = utransport
            self.__lock_pubsub = lock_pubsub
            self._initialized = True

    def on_receive(self, msg: UMessage):
        print("onreceive")
        common_handlers.on_receive_event_handler(
            self.__socketio,
            self.__lock_pubsub,
            self.__utransport,
            LongUriSerializer().serialize(msg.attributes.source),
            msg.payload,
        )
