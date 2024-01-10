# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vehicle/body/cabin_climate/v1/cabin_climate_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
import uprotocol_options_pb2 as uprotocol__options__pb2
from vehicle.body.cabin_climate.v1 import cabin_climate_properties_pb2 as vehicle_dot_body_dot_cabin__climate_dot_v1_dot_cabin__climate__properties__pb2
from vehicle.body.cabin_climate.v1 import cabin_climate_topics_pb2 as vehicle_dot_body_dot_cabin__climate_dot_v1_dot_cabin__climate__topics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9vehicle/body/cabin_climate/v1/cabin_climate_service.proto\x12\x1dvehicle.body.cabin_climate.v1\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\x1a\x17uprotocol_options.proto\x1a<vehicle/body/cabin_climate/v1/cabin_climate_properties.proto\x1a\x38vehicle/body/cabin_climate/v1/cabin_climate_topics.proto\"t\n\x0e\x43limateCommand\x12\x31\n\x04zone\x18\x01 \x01(\x0b\x32#.vehicle.body.cabin_climate.v1.Zone\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x8f\x01\n\x1bUpdateSystemSettingsRequest\x12?\n\x08settings\x18\x01 \x01(\x0b\x32-.vehicle.body.cabin_climate.v1.SystemSettings\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\xaf\x01\n\x15SetTemperatureRequest\x12\x38\n\x02id\x18\x01 \x01(\x0e\x32,.vehicle.body.cabin_climate.v1.Zone.Resource\x12\x13\n\x0btemperature\x18\x02 \x01(\x02\x12G\n\x11temperature_state\x18\x03 \x01(\x0e\x32,.vehicle.body.cabin_climate.v1.AutomaticMode\"<\n\x16SetTemperatureResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\"t\n\rSetFanRequest\x12\x38\n\x02id\x18\x01 \x01(\x0e\x32,.vehicle.body.cabin_climate.v1.Zone.Resource\x12\x11\n\tfan_speed\x18\x02 \x01(\x05\x12\x16\n\x0eis_fan_auto_on\x18\x03 \x01(\x08\"4\n\x0eSetFanResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\"\xed\x01\n\x19SetAirDistributionRequest\x12\x38\n\x02id\x18\x01 \x01(\x0e\x32,.vehicle.body.cabin_climate.v1.Zone.Resource\x12H\n\x10\x61ir_distribution\x18\x02 \x01(\x0e\x32..vehicle.body.cabin_climate.v1.AirDistribution\x12L\n\x16\x61ir_distribution_state\x18\x03 \x01(\x0e\x32,.vehicle.body.cabin_climate.v1.AutomaticMode\"@\n\x1aSetAirDistributionResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\"`\n\x0fSetPowerRequest\x12\x38\n\x02id\x18\x01 \x01(\x0e\x32,.vehicle.body.cabin_climate.v1.Zone.Resource\x12\x13\n\x0bis_power_on\x18\x02 \x01(\x08\"6\n\x10SetPowerResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\"b\n\x0eSetLockRequest\x12\x38\n\x02id\x18\x01 \x01(\x0e\x32,.vehicle.body.cabin_climate.v1.Zone.Resource\x12\x16\n\x0eis_zone_locked\x18\x02 \x01(\x08\"5\n\x0fSetLockResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\"\x80\x01\n\x15SystemSettingsOptions\x12U\n\rresource_name\x18\x01 \x01(\x0e\x32\x37.vehicle.body.cabin_climate.v1.SystemSettings.ResourcesB\x05\x82\xce\x18\x01*:\x10\xe0\xc7\x18\x00\x88\xf4\x1a\x01\xe0\xf4\x1a\x01\xd8\xf4\x1a\x01\"\x9f\x01\n\x0cZonesOptions\x12K\n\rresource_name\x18\x01 \x01(\x0e\x32-.vehicle.body.cabin_climate.v1.Zones.ResourceB\x05\x82\xce\x18\x01*:B\xe0\xc7\x18\n\xe5\xf3\x1a\x00\x00\x80\x41\xed\xf3\x1a\x00\x00\xf8\x41\xf0\xf3\x1a\x08\xf8\xf3\x1a\x08\x80\xf4\x1a\x01\x90\xf4\x1a\x01\x98\xf4\x1a\x00\xa0\xf4\x1a\x00\xa8\xf4\x1a\x01\xb0\xf4\x1a\x00\xb8\xf4\x1a\x00\xc0\xf4\x1a\x01\xc8\xf4\x1a\x00\xd0\xf4\x1a\x00\x32\xfe\x06\n\x10\x42odyCabinclimate\x12`\n\x15\x45xecuteClimateCommand\x12-.vehicle.body.cabin_climate.v1.ClimateCommand\x1a\x12.google.rpc.Status\"\x04\xc0\xc1\x18\x01\x12l\n\x14UpdateSystemSettings\x12:.vehicle.body.cabin_climate.v1.UpdateSystemSettingsRequest\x1a\x12.google.rpc.Status\"\x04\xc0\xc1\x18\x02\x12\x83\x01\n\x0eSetTemperature\x12\x34.vehicle.body.cabin_climate.v1.SetTemperatureRequest\x1a\x35.vehicle.body.cabin_climate.v1.SetTemperatureResponse\"\x04\xc0\xc1\x18\x03\x12k\n\x06SetFan\x12,.vehicle.body.cabin_climate.v1.SetFanRequest\x1a-.vehicle.body.cabin_climate.v1.SetFanResponse\"\x04\xc0\xc1\x18\x04\x12\x8f\x01\n\x12SetAirDistribution\x12\x38.vehicle.body.cabin_climate.v1.SetAirDistributionRequest\x1a\x39.vehicle.body.cabin_climate.v1.SetAirDistributionResponse\"\x04\xc0\xc1\x18\x05\x12q\n\x08SetPower\x12..vehicle.body.cabin_climate.v1.SetPowerRequest\x1a/.vehicle.body.cabin_climate.v1.SetPowerResponse\"\x04\xc0\xc1\x18\x06\x12n\n\x07SetLock\x12-.vehicle.body.cabin_climate.v1.SetLockRequest\x1a..vehicle.body.cabin_climate.v1.SetLockResponse\"\x04\xc0\xc1\x18\x07\x1a\x32\xa2\xbb\x18\x12\x62ody.cabin_climate\xa8\xbb\x18\x01\xb0\xbb\x18\x02\xb8\xbb\x18\x05\xa8\xf5\x1a\x02\xb0\xf5\x1a\x00\xb8\xf5\x1a\x00\xc0\xf5\x1a\x01\x42\x35\n1org.covesa.uservice.vehicle.body.cabin_climate.v1P\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vehicle.body.cabin_climate.v1.cabin_climate_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n1org.covesa.uservice.vehicle.body.cabin_climate.v1P\001'
  _SYSTEMSETTINGSOPTIONS.fields_by_name['resource_name']._options = None
  _SYSTEMSETTINGSOPTIONS.fields_by_name['resource_name']._serialized_options = b'\202\316\030\001*'
  _SYSTEMSETTINGSOPTIONS._options = None
  _SYSTEMSETTINGSOPTIONS._serialized_options = b'\340\307\030\000\210\364\032\001\340\364\032\001\330\364\032\001'
  _ZONESOPTIONS.fields_by_name['resource_name']._options = None
  _ZONESOPTIONS.fields_by_name['resource_name']._serialized_options = b'\202\316\030\001*'
  _ZONESOPTIONS._options = None
  _ZONESOPTIONS._serialized_options = b'\340\307\030\n\345\363\032\000\000\200A\355\363\032\000\000\370A\360\363\032\010\370\363\032\010\200\364\032\001\220\364\032\001\230\364\032\000\240\364\032\000\250\364\032\001\260\364\032\000\270\364\032\000\300\364\032\001\310\364\032\000\320\364\032\000'
  _BODYCABINCLIMATE._options = None
  _BODYCABINCLIMATE._serialized_options = b'\242\273\030\022body.cabin_climate\250\273\030\001\260\273\030\002\270\273\030\005\250\365\032\002\260\365\032\000\270\365\032\000\300\365\032\001'
  _BODYCABINCLIMATE.methods_by_name['ExecuteClimateCommand']._options = None
  _BODYCABINCLIMATE.methods_by_name['ExecuteClimateCommand']._serialized_options = b'\300\301\030\001'
  _BODYCABINCLIMATE.methods_by_name['UpdateSystemSettings']._options = None
  _BODYCABINCLIMATE.methods_by_name['UpdateSystemSettings']._serialized_options = b'\300\301\030\002'
  _BODYCABINCLIMATE.methods_by_name['SetTemperature']._options = None
  _BODYCABINCLIMATE.methods_by_name['SetTemperature']._serialized_options = b'\300\301\030\003'
  _BODYCABINCLIMATE.methods_by_name['SetFan']._options = None
  _BODYCABINCLIMATE.methods_by_name['SetFan']._serialized_options = b'\300\301\030\004'
  _BODYCABINCLIMATE.methods_by_name['SetAirDistribution']._options = None
  _BODYCABINCLIMATE.methods_by_name['SetAirDistribution']._serialized_options = b'\300\301\030\005'
  _BODYCABINCLIMATE.methods_by_name['SetPower']._options = None
  _BODYCABINCLIMATE.methods_by_name['SetPower']._serialized_options = b'\300\301\030\006'
  _BODYCABINCLIMATE.methods_by_name['SetLock']._options = None
  _BODYCABINCLIMATE.methods_by_name['SetLock']._serialized_options = b'\300\301\030\007'
  _CLIMATECOMMAND._serialized_start=296
  _CLIMATECOMMAND._serialized_end=412
  _UPDATESYSTEMSETTINGSREQUEST._serialized_start=415
  _UPDATESYSTEMSETTINGSREQUEST._serialized_end=558
  _SETTEMPERATUREREQUEST._serialized_start=561
  _SETTEMPERATUREREQUEST._serialized_end=736
  _SETTEMPERATURERESPONSE._serialized_start=738
  _SETTEMPERATURERESPONSE._serialized_end=798
  _SETFANREQUEST._serialized_start=800
  _SETFANREQUEST._serialized_end=916
  _SETFANRESPONSE._serialized_start=918
  _SETFANRESPONSE._serialized_end=970
  _SETAIRDISTRIBUTIONREQUEST._serialized_start=973
  _SETAIRDISTRIBUTIONREQUEST._serialized_end=1210
  _SETAIRDISTRIBUTIONRESPONSE._serialized_start=1212
  _SETAIRDISTRIBUTIONRESPONSE._serialized_end=1276
  _SETPOWERREQUEST._serialized_start=1278
  _SETPOWERREQUEST._serialized_end=1374
  _SETPOWERRESPONSE._serialized_start=1376
  _SETPOWERRESPONSE._serialized_end=1430
  _SETLOCKREQUEST._serialized_start=1432
  _SETLOCKREQUEST._serialized_end=1530
  _SETLOCKRESPONSE._serialized_start=1532
  _SETLOCKRESPONSE._serialized_end=1585
  _SYSTEMSETTINGSOPTIONS._serialized_start=1588
  _SYSTEMSETTINGSOPTIONS._serialized_end=1716
  _ZONESOPTIONS._serialized_start=1719
  _ZONESOPTIONS._serialized_end=1878
  _BODYCABINCLIMATE._serialized_start=1881
  _BODYCABINCLIMATE._serialized_end=2775
# @@protoc_insertion_point(module_scope)
