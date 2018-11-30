# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/firestore_v1beta1/proto/common.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/firestore_v1beta1/proto/common.proto",
    package="google.firestore.v1beta1",
    syntax="proto3",
    serialized_pb=_b(
        '\n1google/cloud/firestore_v1beta1/proto/common.proto\x12\x18google.firestore.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"#\n\x0c\x44ocumentMask\x12\x13\n\x0b\x66ield_paths\x18\x01 \x03(\t"e\n\x0cPrecondition\x12\x10\n\x06\x65xists\x18\x01 \x01(\x08H\x00\x12\x31\n\x0bupdate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x42\x10\n\x0e\x63ondition_type"\xb3\x02\n\x12TransactionOptions\x12J\n\tread_only\x18\x02 \x01(\x0b\x32\x35.google.firestore.v1beta1.TransactionOptions.ReadOnlyH\x00\x12L\n\nread_write\x18\x03 \x01(\x0b\x32\x36.google.firestore.v1beta1.TransactionOptions.ReadWriteH\x00\x1a&\n\tReadWrite\x12\x19\n\x11retry_transaction\x18\x01 \x01(\x0c\x1aS\n\x08ReadOnly\x12/\n\tread_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x42\x16\n\x14\x63onsistency_selectorB\x06\n\x04modeB\xb9\x01\n\x1c\x63om.google.firestore.v1beta1B\x0b\x43ommonProtoP\x01ZAgoogle.golang.org/genproto/googleapis/firestore/v1beta1;firestore\xa2\x02\x04GCFS\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Firestore\\V1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_DOCUMENTMASK = _descriptor.Descriptor(
    name="DocumentMask",
    full_name="google.firestore.v1beta1.DocumentMask",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="field_paths",
            full_name="google.firestore.v1beta1.DocumentMask.field_paths",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=142,
    serialized_end=177,
)


_PRECONDITION = _descriptor.Descriptor(
    name="Precondition",
    full_name="google.firestore.v1beta1.Precondition",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="exists",
            full_name="google.firestore.v1beta1.Precondition.exists",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="update_time",
            full_name="google.firestore.v1beta1.Precondition.update_time",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="condition_type",
            full_name="google.firestore.v1beta1.Precondition.condition_type",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=179,
    serialized_end=280,
)


_TRANSACTIONOPTIONS_READWRITE = _descriptor.Descriptor(
    name="ReadWrite",
    full_name="google.firestore.v1beta1.TransactionOptions.ReadWrite",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="retry_transaction",
            full_name="google.firestore.v1beta1.TransactionOptions.ReadWrite.retry_transaction",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=459,
    serialized_end=497,
)

_TRANSACTIONOPTIONS_READONLY = _descriptor.Descriptor(
    name="ReadOnly",
    full_name="google.firestore.v1beta1.TransactionOptions.ReadOnly",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="read_time",
            full_name="google.firestore.v1beta1.TransactionOptions.ReadOnly.read_time",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="consistency_selector",
            full_name="google.firestore.v1beta1.TransactionOptions.ReadOnly.consistency_selector",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=499,
    serialized_end=582,
)

_TRANSACTIONOPTIONS = _descriptor.Descriptor(
    name="TransactionOptions",
    full_name="google.firestore.v1beta1.TransactionOptions",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="read_only",
            full_name="google.firestore.v1beta1.TransactionOptions.read_only",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="read_write",
            full_name="google.firestore.v1beta1.TransactionOptions.read_write",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_TRANSACTIONOPTIONS_READWRITE, _TRANSACTIONOPTIONS_READONLY],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="mode",
            full_name="google.firestore.v1beta1.TransactionOptions.mode",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=283,
    serialized_end=590,
)

_PRECONDITION.fields_by_name[
    "update_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PRECONDITION.oneofs_by_name["condition_type"].fields.append(
    _PRECONDITION.fields_by_name["exists"]
)
_PRECONDITION.fields_by_name["exists"].containing_oneof = _PRECONDITION.oneofs_by_name[
    "condition_type"
]
_PRECONDITION.oneofs_by_name["condition_type"].fields.append(
    _PRECONDITION.fields_by_name["update_time"]
)
_PRECONDITION.fields_by_name[
    "update_time"
].containing_oneof = _PRECONDITION.oneofs_by_name["condition_type"]
_TRANSACTIONOPTIONS_READWRITE.containing_type = _TRANSACTIONOPTIONS
_TRANSACTIONOPTIONS_READONLY.fields_by_name[
    "read_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRANSACTIONOPTIONS_READONLY.containing_type = _TRANSACTIONOPTIONS
_TRANSACTIONOPTIONS_READONLY.oneofs_by_name["consistency_selector"].fields.append(
    _TRANSACTIONOPTIONS_READONLY.fields_by_name["read_time"]
)
_TRANSACTIONOPTIONS_READONLY.fields_by_name[
    "read_time"
].containing_oneof = _TRANSACTIONOPTIONS_READONLY.oneofs_by_name["consistency_selector"]
_TRANSACTIONOPTIONS.fields_by_name[
    "read_only"
].message_type = _TRANSACTIONOPTIONS_READONLY
_TRANSACTIONOPTIONS.fields_by_name[
    "read_write"
].message_type = _TRANSACTIONOPTIONS_READWRITE
_TRANSACTIONOPTIONS.oneofs_by_name["mode"].fields.append(
    _TRANSACTIONOPTIONS.fields_by_name["read_only"]
)
_TRANSACTIONOPTIONS.fields_by_name[
    "read_only"
].containing_oneof = _TRANSACTIONOPTIONS.oneofs_by_name["mode"]
_TRANSACTIONOPTIONS.oneofs_by_name["mode"].fields.append(
    _TRANSACTIONOPTIONS.fields_by_name["read_write"]
)
_TRANSACTIONOPTIONS.fields_by_name[
    "read_write"
].containing_oneof = _TRANSACTIONOPTIONS.oneofs_by_name["mode"]
DESCRIPTOR.message_types_by_name["DocumentMask"] = _DOCUMENTMASK
DESCRIPTOR.message_types_by_name["Precondition"] = _PRECONDITION
DESCRIPTOR.message_types_by_name["TransactionOptions"] = _TRANSACTIONOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DocumentMask = _reflection.GeneratedProtocolMessageType(
    "DocumentMask",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DOCUMENTMASK,
        __module__="google.cloud.firestore_v1beta1.proto.common_pb2",
        __doc__="""A set of field paths on a document. Used to restrict a get or update
  operation on a document to a subset of its fields. This is different
  from standard field masks, as this is always scoped to a
  [Document][google.firestore.v1beta1.Document], and takes in account the
  dynamic nature of [Value][google.firestore.v1beta1.Value].
  
  
  Attributes:
      field_paths:
          The list of field paths in the mask. See
          [Document.fields][google.firestore.v1beta1.Document.fields]
          for a field path syntax reference.
  """,
        # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.DocumentMask)
    ),
)
_sym_db.RegisterMessage(DocumentMask)

Precondition = _reflection.GeneratedProtocolMessageType(
    "Precondition",
    (_message.Message,),
    dict(
        DESCRIPTOR=_PRECONDITION,
        __module__="google.cloud.firestore_v1beta1.proto.common_pb2",
        __doc__="""A precondition on a document, used for conditional operations.
  
  
  Attributes:
      condition_type:
          The type of precondition.
      exists:
          When set to ``true``, the target document must exist. When set
          to ``false``, the target document must not exist.
      update_time:
          When set, the target document must exist and have been last
          updated at that time.
  """,
        # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.Precondition)
    ),
)
_sym_db.RegisterMessage(Precondition)

TransactionOptions = _reflection.GeneratedProtocolMessageType(
    "TransactionOptions",
    (_message.Message,),
    dict(
        ReadWrite=_reflection.GeneratedProtocolMessageType(
            "ReadWrite",
            (_message.Message,),
            dict(
                DESCRIPTOR=_TRANSACTIONOPTIONS_READWRITE,
                __module__="google.cloud.firestore_v1beta1.proto.common_pb2",
                __doc__="""Options for a transaction that can be used to read and write documents.
    
    
    Attributes:
        retry_transaction:
            An optional transaction to retry.
    """,
                # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.TransactionOptions.ReadWrite)
            ),
        ),
        ReadOnly=_reflection.GeneratedProtocolMessageType(
            "ReadOnly",
            (_message.Message,),
            dict(
                DESCRIPTOR=_TRANSACTIONOPTIONS_READONLY,
                __module__="google.cloud.firestore_v1beta1.proto.common_pb2",
                __doc__="""Options for a transaction that can only be used to read documents.
    
    
    Attributes:
        consistency_selector:
            The consistency mode for this transaction. If not set,
            defaults to strong consistency.
        read_time:
            Reads documents at the given time. This may not be older than
            60 seconds.
    """,
                # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.TransactionOptions.ReadOnly)
            ),
        ),
        DESCRIPTOR=_TRANSACTIONOPTIONS,
        __module__="google.cloud.firestore_v1beta1.proto.common_pb2",
        __doc__="""Options for creating a new transaction.
  
  
  Attributes:
      mode:
          The mode of the transaction.
      read_only:
          The transaction can only be used for read operations.
      read_write:
          The transaction can be used for both read and write
          operations.
  """,
        # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.TransactionOptions)
    ),
)
_sym_db.RegisterMessage(TransactionOptions)
_sym_db.RegisterMessage(TransactionOptions.ReadWrite)
_sym_db.RegisterMessage(TransactionOptions.ReadOnly)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b(
        "\n\034com.google.firestore.v1beta1B\013CommonProtoP\001ZAgoogle.golang.org/genproto/googleapis/firestore/v1beta1;firestore\242\002\004GCFS\252\002\036Google.Cloud.Firestore.V1Beta1\312\002\036Google\\Cloud\\Firestore\\V1beta1"
    ),
)
# @@protoc_insertion_point(module_scope)
