# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sgotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rsgotify.proto\"q\n\x0bSpotifyAuth\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x12\n\ntoken_type\x18\x02 \x01(\t\x12\r\n\x05scope\x18\x03 \x01(\t\x12\x12\n\nexpires_in\x18\x04 \x01(\x05\x12\x15\n\rrefresh_token\x18\x05 \x01(\t\"#\n\x10SpotifyAuthReply\x12\x0f\n\x07message\x18\x01 \x01(\t2?\n\x07Sgotify\x12\x34\n\x0fSendSpotifyAuth\x12\x0c.SpotifyAuth\x1a\x11.SpotifyAuthReply\"\x00\x42\x0bZ\t./sgotifyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sgotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\t./sgotify'
  _SPOTIFYAUTH._serialized_start=17
  _SPOTIFYAUTH._serialized_end=130
  _SPOTIFYAUTHREPLY._serialized_start=132
  _SPOTIFYAUTHREPLY._serialized_end=167
  _SGOTIFY._serialized_start=169
  _SGOTIFY._serialized_end=232
# @@protoc_insertion_point(module_scope)
