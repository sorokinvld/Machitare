# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/streaming.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proto/streaming.proto\x12\tstreaming\"L\n\nVideoFrame\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\"e\n\nAudioChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x12\n\nsampleRate\x18\x02 \x01(\x05\x12\x10\n\x08\x62itDepth\x18\x03 \x01(\x05\x12\x10\n\x08\x63hannels\x18\x04 \x01(\x05\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\"&\n\x05\x45vent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\x8a\x01\n\nStreamData\x12&\n\x05video\x18\x01 \x01(\x0b\x32\x15.streaming.VideoFrameH\x00\x12&\n\x05\x61udio\x18\x02 \x01(\x0b\x32\x15.streaming.AudioChunkH\x00\x12!\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x10.streaming.EventH\x00\x42\t\n\x07payloadb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.streaming_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VIDEOFRAME']._serialized_start=36
  _globals['_VIDEOFRAME']._serialized_end=112
  _globals['_AUDIOCHUNK']._serialized_start=114
  _globals['_AUDIOCHUNK']._serialized_end=215
  _globals['_EVENT']._serialized_start=217
  _globals['_EVENT']._serialized_end=255
  _globals['_STREAMDATA']._serialized_start=258
  _globals['_STREAMDATA']._serialized_end=396
# @@protoc_insertion_point(module_scope)
