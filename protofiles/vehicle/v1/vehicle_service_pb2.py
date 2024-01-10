# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vehicle/v1/vehicle_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
import uprotocol_options_pb2 as uprotocol__options__pb2
from vehicle.v1 import vehicle_topics_pb2 as vehicle_dot_v1_dot_vehicle__topics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n vehicle/v1/vehicle_service.proto\x12\nvehicle.v1\x1a\x17google/rpc/status.proto\x1a\x17uprotocol_options.proto\x1a\x1fvehicle/v1/vehicle_topics.proto\"L\n\x15ResetTripMeterRequest\x12\x33\n\ntrip_meter\x18\x01 \x01(\x0e\x32\x1f.vehicle.v1.TripMeter.Resources\",\n\x17SetTransportModeRequest\x12\x11\n\tis_active\x18\x01 \x01(\x08\"\\\n\x17TraveledDistanceOptions\x12;\n\x04name\x18\x01 \x01(\x0e\x32&.vehicle.v1.TraveledDistance.ResourcesB\x05\x82\xce\x18\x01*:\x04\xe0\xc7\x18\x00\"Y\n\x10TripMeterOptions\x12?\n\x04name\x18\x01 \x01(\x0e\x32\x1f.vehicle.v1.TripMeter.ResourcesB\x10\x82\xce\x18\x0ctrip_meter.*:\x04\xe0\xc7\x18\n\"T\n\x13VehicleSpeedOptions\x12\x37\n\x04name\x18\x01 \x01(\x0e\x32\".vehicle.v1.VehicleSpeed.ResourcesB\x05\x82\xce\x18\x01*:\x04\xe0\xc7\x18\x14\"P\n\x11TheftAlertOptions\x12\x35\n\x04name\x18\x01 \x01(\x0e\x32 .vehicle.v1.TheftAlert.ResourcesB\x05\x82\xce\x18\x01*:\x04\xe0\xc7\x18\x1e\"X\n\x15\x43ollisionAlertOptions\x12\x39\n\x04name\x18\x01 \x01(\x0e\x32$.vehicle.v1.CollisionAlert.ResourcesB\x05\x82\xce\x18\x01*:\x04\xe0\xc7\x18(\"b\n\x13VehicleUsageOptions\x12\x45\n\x04name\x18\x01 \x01(\x0e\x32\".vehicle.v1.VehicleUsage.ResourcesB\x13\x82\xce\x18\x0fvehicle_usage.*:\x04\xe0\xc7\x18\x32\x32\xc4\x01\n\x07Vehicle\x12M\n\x0eResetTripMeter\x12!.vehicle.v1.ResetTripMeterRequest\x1a\x12.google.rpc.Status\"\x04\xc0\xc1\x18\x01\x12Q\n\x10SetTransportMode\x12#.vehicle.v1.SetTransportModeRequest\x1a\x12.google.rpc.Status\"\x04\xc0\xc1\x18\x02\x1a\x17\xa2\xbb\x18\x07vehicle\xa8\xbb\x18\x01\xb0\xbb\x18\x00\xb8\xbb\x18\x0e\x42\"\n\x1eorg.covesa.uservice.vehicle.v1P\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vehicle.v1.vehicle_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036org.covesa.uservice.vehicle.v1P\001'
  _TRAVELEDDISTANCEOPTIONS.fields_by_name['name']._options = None
  _TRAVELEDDISTANCEOPTIONS.fields_by_name['name']._serialized_options = b'\202\316\030\001*'
  _TRAVELEDDISTANCEOPTIONS._options = None
  _TRAVELEDDISTANCEOPTIONS._serialized_options = b'\340\307\030\000'
  _TRIPMETEROPTIONS.fields_by_name['name']._options = None
  _TRIPMETEROPTIONS.fields_by_name['name']._serialized_options = b'\202\316\030\014trip_meter.*'
  _TRIPMETEROPTIONS._options = None
  _TRIPMETEROPTIONS._serialized_options = b'\340\307\030\n'
  _VEHICLESPEEDOPTIONS.fields_by_name['name']._options = None
  _VEHICLESPEEDOPTIONS.fields_by_name['name']._serialized_options = b'\202\316\030\001*'
  _VEHICLESPEEDOPTIONS._options = None
  _VEHICLESPEEDOPTIONS._serialized_options = b'\340\307\030\024'
  _THEFTALERTOPTIONS.fields_by_name['name']._options = None
  _THEFTALERTOPTIONS.fields_by_name['name']._serialized_options = b'\202\316\030\001*'
  _THEFTALERTOPTIONS._options = None
  _THEFTALERTOPTIONS._serialized_options = b'\340\307\030\036'
  _COLLISIONALERTOPTIONS.fields_by_name['name']._options = None
  _COLLISIONALERTOPTIONS.fields_by_name['name']._serialized_options = b'\202\316\030\001*'
  _COLLISIONALERTOPTIONS._options = None
  _COLLISIONALERTOPTIONS._serialized_options = b'\340\307\030('
  _VEHICLEUSAGEOPTIONS.fields_by_name['name']._options = None
  _VEHICLEUSAGEOPTIONS.fields_by_name['name']._serialized_options = b'\202\316\030\017vehicle_usage.*'
  _VEHICLEUSAGEOPTIONS._options = None
  _VEHICLEUSAGEOPTIONS._serialized_options = b'\340\307\0302'
  _VEHICLE._options = None
  _VEHICLE._serialized_options = b'\242\273\030\007vehicle\250\273\030\001\260\273\030\000\270\273\030\016'
  _VEHICLE.methods_by_name['ResetTripMeter']._options = None
  _VEHICLE.methods_by_name['ResetTripMeter']._serialized_options = b'\300\301\030\001'
  _VEHICLE.methods_by_name['SetTransportMode']._options = None
  _VEHICLE.methods_by_name['SetTransportMode']._serialized_options = b'\300\301\030\002'
  _RESETTRIPMETERREQUEST._serialized_start=131
  _RESETTRIPMETERREQUEST._serialized_end=207
  _SETTRANSPORTMODEREQUEST._serialized_start=209
  _SETTRANSPORTMODEREQUEST._serialized_end=253
  _TRAVELEDDISTANCEOPTIONS._serialized_start=255
  _TRAVELEDDISTANCEOPTIONS._serialized_end=347
  _TRIPMETEROPTIONS._serialized_start=349
  _TRIPMETEROPTIONS._serialized_end=438
  _VEHICLESPEEDOPTIONS._serialized_start=440
  _VEHICLESPEEDOPTIONS._serialized_end=524
  _THEFTALERTOPTIONS._serialized_start=526
  _THEFTALERTOPTIONS._serialized_end=606
  _COLLISIONALERTOPTIONS._serialized_start=608
  _COLLISIONALERTOPTIONS._serialized_end=696
  _VEHICLEUSAGEOPTIONS._serialized_start=698
  _VEHICLEUSAGEOPTIONS._serialized_end=796
  _VEHICLE._serialized_start=799
  _VEHICLE._serialized_end=995
# @@protoc_insertion_point(module_scope)
