# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: showtime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import booking_pb2 as booking__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='showtime.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eshowtime.proto\x1a\rbooking.proto\".\n\x0cShowTimeData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x10\n\x08idMovies\x18\x02 \x03(\t2b\n\x08Showtime\x12\'\n\rGetshowmovies\x12\x05.Date\x1a\r.ShowTimeData\"\x00\x12-\n\x10GetListShowtimes\x12\x06.Empty\x1a\r.ShowTimeData\"\x00\x30\x01\x62\x06proto3'
  ,
  dependencies=[booking__pb2.DESCRIPTOR,])




_SHOWTIMEDATA = _descriptor.Descriptor(
  name='ShowTimeData',
  full_name='ShowTimeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='ShowTimeData.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idMovies', full_name='ShowTimeData.idMovies', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['ShowTimeData'] = _SHOWTIMEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShowTimeData = _reflection.GeneratedProtocolMessageType('ShowTimeData', (_message.Message,), {
  'DESCRIPTOR' : _SHOWTIMEDATA,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:ShowTimeData)
  })
_sym_db.RegisterMessage(ShowTimeData)



_SHOWTIME = _descriptor.ServiceDescriptor(
  name='Showtime',
  full_name='Showtime',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=81,
  serialized_end=179,
  methods=[
  _descriptor.MethodDescriptor(
    name='Getshowmovies',
    full_name='Showtime.Getshowmovies',
    index=0,
    containing_service=None,
    input_type=booking__pb2._DATE,
    output_type=_SHOWTIMEDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetListShowtimes',
    full_name='Showtime.GetListShowtimes',
    index=1,
    containing_service=None,
    input_type=booking__pb2._EMPTY,
    output_type=_SHOWTIMEDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SHOWTIME)

DESCRIPTOR.services_by_name['Showtime'] = _SHOWTIME

# @@protoc_insertion_point(module_scope)
