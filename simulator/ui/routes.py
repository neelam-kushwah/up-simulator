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

import html
import json
import os
from urllib.parse import unquote

from flask import redirect, render_template, request, send_file, url_for

from simulator.ui import blueprint
from simulator.ui.utils import adb_utils
from simulator.utils import constant
from simulator.utils.vehicle_service_utils import get_all_configured_someip_service, get_all_running_service
from tdk.helper import someip_helper

run_directory = os.path.dirname(os.path.abspath(__file__))
run_directory = run_directory.split(os.sep)[:-2]
run_directory = os.sep.join(run_directory)


@blueprint.route("/")
def route_default():
    return redirect(url_for("simulator_blueprint.route_configuration"))


@blueprint.route("/configuration.html")
def route_configuration():
    device_info = {"Image": "", "Build_date": "", "Build_id": "", "Model": ""}
    emu_status = "Emulator is not running.."
    try:
        device = adb_utils.get_emulator_device()
        if device is not None:
            status = device.shell("getprop init.svc.bootanim")
            if status.__contains__("stopped"):
                emu_status = "Emulator is running"
                device_info = {
                    "Avd_name": device.shell("getprop ro.boot.qemu.avd_name"),
                    "Image": device.shell("getprop ro.product.bootimage.name"),
                    "Build_date": device.shell("getprop ro.bootimage.build.date"),
                    "Model": device.shell("getprop ro.product.model"),
                }
            else:
                emu_status = "Emulator is loading"

    except Exception:
        pass

    return render_template(
        "home/configuration.html",
        segment=get_segment(request),
        device_info=device_info,
        emu_status=emu_status,
    )


@blueprint.route("/pub-sub.html")
def route_pubsub():
    services_json_path = os.path.join(
        run_directory,
        constant.UI_JSON_DIR,
        constant.SERVICES_JSON_FILE_NAME,
    )
    pubsub_json_path = os.path.join(
        run_directory,
        constant.UI_JSON_DIR,
        constant.PUB_SUB_JSON_FILE_NAME,
    )

    f = open(pubsub_json_path)
    pubsub = json.load(f)
    f.close()
    f = open(services_json_path)
    services = json.load(f)
    f.close()

    return render_template(
        "home/pub-sub.html",
        segment=get_segment(request),
        services=services,
        pubsub=pubsub,
        json_proto={},
    )


@blueprint.route("/rpc-logger.html")
def route_rpc_logger():
    try:
        f = open(os.path.join(run_directory, "simulator", constant.FILENAME_RPC_LOGGER))
        data = f.read()
        f.close()
        data = f"[{data}]"
    except Exception:
        data = ""
    return render_template("home/rpc-logger.html", rpc_calls=data, segment=get_segment(request))


@blueprint.route("/downloadPubSubReport")
def download_pub_file():
    filename = os.getcwd() + "/pubsub_logger.txt"
    if os.path.isfile(filename):
        return send_file(filename, as_attachment=True)
    else:
        return ""


@blueprint.route("/downloadRPCReport")
def download_rpc_file():
    filename = os.getcwd() + "/rpc_logger.txt"
    if os.path.isfile(filename):
        return send_file(filename, as_attachment=True)
    else:
        return ""


@blueprint.route("/pubsub-logger.html")
def route_pubsub_logger():
    try:
        f = open(os.path.join(run_directory, "simulator", constant.FILENAME_PUBSUB_LOGGER))
        data = f.read()
        f.close()
        data = f"[{data}]"
    except Exception:
        data = ""
    return render_template("home/pub-sub-logger.html", data=data, segment=get_segment(request))


@blueprint.route("/send-rpc.html")
def route_send_rpc():
    services_json_path = os.path.join(
        run_directory,
        constant.UI_JSON_DIR,
        constant.SERVICES_JSON_FILE_NAME,
    )
    rpc_json_path = os.path.join(run_directory, constant.UI_JSON_DIR, constant.RPC_JSON_FILE_NAME)

    f = open(rpc_json_path)
    rpcs = json.load(f)
    f.close()
    f = open(services_json_path)
    services = json.load(f)
    f.close()

    return render_template(
        "home/send-rpc.html",
        segment=get_segment(request),
        services=services,
        rpcs=rpcs,
    )


@blueprint.route("/mockservice.html")
def route_mockservices():
    return render_template("home/mockservice.html", segment=get_segment(request))


# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split("/")[-1]
        if segment == "":
            segment = "index"
        return segment
    except Exception:
        return None


@blueprint.route("/getuiconfiguration")
def getconfiguration():
    try:
        resource = str(request.args.get("resource"))
        service = str(unquote(request.args.get("service")))
        ui = json.loads(service)
        layout = None
        for i in ui:
            for key, value in i.items():
                if resource == key:
                    layout = value
                    break

        return layout
    except Exception as e:
        print(f"Exception:{e}")
        return None


@blueprint.route("/getmockservices")
def get_mock_services():
    env = str(request.args.get("env"))
    transport = str(request.args.get("transport"))
    mockservice_pkgs = []
    json_path = os.path.join(
        run_directory,
        constant.UI_JSON_DIR,
        constant.SERVICES_JSON_FILE_NAME,
    )
    f = open(json_path)
    mockservices = json.load(f)
    f.close()
    for m in mockservices:
        if m["name"] not in [
            "core.udiscovery",
            "core.utelemetry",
            "core.usubscription",
        ] and (m["name"] in someip_helper.someip_entity or env == "Someip" or transport != "SOME/IP"):
            pkgs = {"entity": m["name"], "name": m["display_name"]}
            mockservice_pkgs.append(pkgs)
    if env == "Someip":
        running_services = get_all_configured_someip_service()
        someip_helper.temp_someip_entity = running_services
    else:
        running_services = get_all_running_service()

    return {
        "result": True,
        "pkgs_mock": mockservice_pkgs,
        "running": running_services,
    }


@blueprint.route("/updateservicestatus")
def update_service_status():
    entity_to_remove = request.args["entity"]
    print(entity_to_remove)
    try:
        from simulator.utils.vehicle_service_utils import stop_service

        stop_service(entity_to_remove)
    except Exception:
        pass
    return {"result": True, "entity": html.escape(entity_to_remove)}


@blueprint.route("/updatesomeipservicestatus")
def update_someip_service_status():
    entity_to_remove = request.args["entity"]
    print(entity_to_remove)
    try:
        from simulator.utils.vehicle_service_utils import remove_service_from_someip

        remove_service_from_someip(entity_to_remove)
    except Exception:
        pass
    return {"result": True, "entity": html.escape(entity_to_remove)}
