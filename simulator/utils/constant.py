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

import os.path

NAMESPACE = "/simulator"

SERVICE_PROTO_SUFFIX = "_service.proto"
TOPIC_PROTO_SUFFIX = "_topics.proto"
UI_JSON_DIR = os.path.join("simulator", "target", "ui_json")
SERVICES_JSON_FILE_NAME = "services.json"
PUB_SUB_JSON_FILE_NAME = "pub-sub.json"
RPC_JSON_FILE_NAME = "rpc.json"


FILENAME_RPC_LOGGER = "rpc_logger.txt"
FILENAME_PUBSUB_LOGGER = "pubsub_logger.txt"

API_START_SERVICE = "start-service"
API_STOP_ALL_SERVICE = "stop_all_mockservices"
API_PUBLISH = "publish"
API_SENDRPC = "sendrpc"
API_SUBSCRIBE = "subscribe"
API_SET_ZENOH_CONFIG = "set_zenoh_config"
API_SET_SOMEIP_CONFIG = "set_someip_config"
API_SET_UTRANSPORT = "set_utransport"
API_RESET = "reset"
API_CONFIGURE_SOMEIP_SERVICE = "configure_service_someip"
CALLBACK_CONFIGURE_SOMEIP_SERVICE = "configure_service_someip_callback"

CALLBACK_START_SERVICE = "start_service_callback"
CALLBACK_SENDRPC = "sendrpc_callback"
CALLBACK_RPCLOGGER = "rpc_logger_callback"
CALLBACK_PUBSUB_LOGGER = "pub_sub_logger_callback"
CALLBACK_SENDRPC_EXC = "onSendRPCException"
CALLBACK_SENDRPC_RESPONSE = "sendrpc_response_callback"
CALLBACK_SUBSCRIBE_STATUS_SUCCESS = "subscribe_callback_success"
CALLBACK_SUBSCRIBE_STATUS_FAILED = "subscribe_callback_fail"
CALLBACK_EXCEPTION_SUBSCRIBE = "onSubException"
CALLBACK_PUBLISH_STATUS_SUCCESS = "publish_callback_success"
CALLBACK_PUBLISH_STATUS_FAILED = "publish_callback_fail"
CALLBACK_EXCEPTION_PUBLISH = "onPubException"
CALLBACK_ONEVENT_RECEIVE = "onTopicUpdate"
CALLBACK_GENERIC_ERROR = "onError"
CALLBACK_ON_SET_TRANSPORT = "onSetTransport"

KEY_MESSAGE = "message"
KEY_CODE = "code"
KEY_STATUS = "status"
KEY_METHODNAME = "methodname"
KEY_REQUEST = "request"
KEY_RESPONSE = "response"
KEY_DATA = "data"
KEY_RPCCOUNT = "rpccount"
KEY_SUCCESSRPC = "successrpc"
KEY_FAILEDRPC = "failedrpc"
KEY_ISFAILED = "isfailed"
KEY_TIME = "time"
