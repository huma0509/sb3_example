# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61gent.proto\x12\tapi.agent\"\x1d\n\x0bStepRequest\x12\x0e\n\x06\x41\x63tion\x18\x01 \x01(\x05\"A\n\x0cStepResponse\x12\r\n\x05State\x18\x01 \x03(\x05\x12\x0e\n\x06Reward\x18\x02 \x01(\x02\x12\x12\n\nTerminated\x18\x03 \x01(\x08\"\x0e\n\x0cResetRequest\"\x1e\n\rResetResponse\x12\r\n\x05State\x18\x01 \x03(\x05\x32\x87\x01\n\x0c\x41gentService\x12\x39\n\x04Step\x12\x16.api.agent.StepRequest\x1a\x17.api.agent.StepResponse\"\x00\x12<\n\x05Reset\x12\x17.api.agent.ResetRequest\x1a\x18.api.agent.ResetResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'agent_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STEPREQUEST._serialized_start=26
  _STEPREQUEST._serialized_end=55
  _STEPRESPONSE._serialized_start=57
  _STEPRESPONSE._serialized_end=122
  _RESETREQUEST._serialized_start=124
  _RESETREQUEST._serialized_end=138
  _RESETRESPONSE._serialized_start=140
  _RESETRESPONSE._serialized_end=170
  _AGENTSERVICE._serialized_start=173
  _AGENTSERVICE._serialized_end=308
# @@protoc_insertion_point(module_scope)
