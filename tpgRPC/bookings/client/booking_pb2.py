# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='booking.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rbooking.proto\"\x14\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"\x14\n\x06UserID\x12\n\n\x02id\x18\x01 \x01(\t\".\n\x0cShowTimeData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x10\n\x08idMovies\x18\x02 \x01(\t\"+\n\x0b\x44\x61tesMovies\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\":\n\x0b\x42ookingData\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x1b\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\x0c.DatesMovies\"\x07\n\x05\x45mpty2\xde\x01\n\x07\x42ooking\x12\'\n\x0c\x43reatBooking\x12\x07.UserID\x1a\x0c.BookingData\"\x00\x12\"\n\rDeleteBooking\x12\x07.UserID\x1a\x06.Empty\"\x00\x12+\n\x0fGetListBookings\x12\x06.Empty\x1a\x0c.BookingData\"\x00\x30\x01\x12-\n\x12GetBookingByUserID\x12\x07.UserID\x1a\x0c.BookingData\"\x00\x12*\n\x0eGetMovieByTime\x12\x05.Date\x1a\r.ShowTimeData\"\x00\x30\x01\x62\x06proto3'
)




_DATE = _descriptor.Descriptor(
  name='Date',
  full_name='Date',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='Date.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=17,
  serialized_end=37,
)


_USERID = _descriptor.Descriptor(
  name='UserID',
  full_name='UserID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UserID.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=39,
  serialized_end=59,
)


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
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=61,
  serialized_end=107,
)


_DATESMOVIES = _descriptor.Descriptor(
  name='DatesMovies',
  full_name='DatesMovies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='DatesMovies.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='movies', full_name='DatesMovies.movies', index=1,
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
  serialized_start=109,
  serialized_end=152,
)


_BOOKINGDATA = _descriptor.Descriptor(
  name='BookingData',
  full_name='BookingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='BookingData.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dates', full_name='BookingData.dates', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=154,
  serialized_end=212,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=214,
  serialized_end=221,
)

_BOOKINGDATA.fields_by_name['dates'].message_type = _DATESMOVIES
DESCRIPTOR.message_types_by_name['Date'] = _DATE
DESCRIPTOR.message_types_by_name['UserID'] = _USERID
DESCRIPTOR.message_types_by_name['ShowTimeData'] = _SHOWTIMEDATA
DESCRIPTOR.message_types_by_name['DatesMovies'] = _DATESMOVIES
DESCRIPTOR.message_types_by_name['BookingData'] = _BOOKINGDATA
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), {
  'DESCRIPTOR' : _DATE,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:Date)
  })
_sym_db.RegisterMessage(Date)

UserID = _reflection.GeneratedProtocolMessageType('UserID', (_message.Message,), {
  'DESCRIPTOR' : _USERID,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:UserID)
  })
_sym_db.RegisterMessage(UserID)

ShowTimeData = _reflection.GeneratedProtocolMessageType('ShowTimeData', (_message.Message,), {
  'DESCRIPTOR' : _SHOWTIMEDATA,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:ShowTimeData)
  })
_sym_db.RegisterMessage(ShowTimeData)

DatesMovies = _reflection.GeneratedProtocolMessageType('DatesMovies', (_message.Message,), {
  'DESCRIPTOR' : _DATESMOVIES,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:DatesMovies)
  })
_sym_db.RegisterMessage(DatesMovies)

BookingData = _reflection.GeneratedProtocolMessageType('BookingData', (_message.Message,), {
  'DESCRIPTOR' : _BOOKINGDATA,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:BookingData)
  })
_sym_db.RegisterMessage(BookingData)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)



_BOOKING = _descriptor.ServiceDescriptor(
  name='Booking',
  full_name='Booking',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=224,
  serialized_end=446,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreatBooking',
    full_name='Booking.CreatBooking',
    index=0,
    containing_service=None,
    input_type=_USERID,
    output_type=_BOOKINGDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBooking',
    full_name='Booking.DeleteBooking',
    index=1,
    containing_service=None,
    input_type=_USERID,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetListBookings',
    full_name='Booking.GetListBookings',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_BOOKINGDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBookingByUserID',
    full_name='Booking.GetBookingByUserID',
    index=3,
    containing_service=None,
    input_type=_USERID,
    output_type=_BOOKINGDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMovieByTime',
    full_name='Booking.GetMovieByTime',
    index=4,
    containing_service=None,
    input_type=_DATE,
    output_type=_SHOWTIMEDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKING)

DESCRIPTOR.services_by_name['Booking'] = _BOOKING

# @@protoc_insertion_point(module_scope)
