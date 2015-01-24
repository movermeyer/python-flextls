"""

"""
from flextls.protocol import Protocol
from flextls.field import UByteField, UShortField, VectorListUByteField, VectorUShortField
from flextls.field import UByteEnumField, UShortEnumField, VectorListUShortField
from flextls.field import SignatureAndHashAlgorithmField
from flextls.field import ServerNameListField


class Extension(Protocol):
    def __init__(self, **kwargs):
        Protocol.__init__(self, **kwargs)
        self.fields = [
            UShortEnumField(
                "type",
                None,
                {
                    13: "signature_algorithms",
                    65535: None
                }
            ),
            UShortField("length", 0),
        ]
        self.payload_identifier_field = "type"
        self.payload_length_field = "length"


class ServerNameIndication(Protocol):
    def __init__(self, **kwargs):
        Protocol.__init__(self, **kwargs)
        self.fields = [
            ServerNameListField("server_name_list"),
        ]

    @classmethod
    def decode(cls, data, connection_state=None, payload_auto_decode=True):
        obj = cls(
            connection_state=connection_state
        )
        if len(data) > 0:
            data = obj.dissect(data)

        return (obj, data)

    def encode(self):
        if len(self.server_name_list) == 0:
            return b""
        else:
            return self.assemble()


Extension.add_payload_type(0x0000, ServerNameIndication)


class Heartbeat(Protocol):
    def __init__(self, **kwargs):
        Protocol.__init__(self, **kwargs)
        self.fields = [
            UByteEnumField(
                "mode",
                None,
                {
                    1: "peer_allowed_to_send",
                    2: "peer_not_allowed_to_send",
                    255: None
                }
            ),
        ]


Extension.add_payload_type(0x000f, Heartbeat)


class EllipticCurves(Protocol):
    def __init__(self, **kwargs):
        Protocol.__init__(self, **kwargs)
        self.fields = [
            VectorListUShortField(
                "elliptic_curve_list",
                item_class=UShortField,
                item_class_args=[None, None]
            ),
        ]

Extension.add_payload_type(0x000a, EllipticCurves)


class EcPointFormats(Protocol):
    def __init__(self, **kwargs):
        Protocol.__init__(self, **kwargs)
        self.fields = [
            VectorListUByteField(
                "point_format_list",
                item_class=UByteField,
                item_class_args=[None, None]
            ),
        ]

Extension.add_payload_type(0x000b, EcPointFormats)


class SignatureAlgorithms(Protocol):
    def __init__(self, **kwargs):
        Protocol.__init__(self, **kwargs)
        self.fields = [
            VectorListUShortField(
                "supported_signature_algorithms",
                item_class=SignatureAndHashAlgorithmField,
                item_class_args=[None, None]
            ),
        ]

Extension.add_payload_type(0x000d, SignatureAlgorithms)


class SessionTicketTLS(Protocol):
    def __init__(self, **kwargs):
        Protocol.__init__(self, **kwargs)
        self.fields = [
            VectorUShortField("data"),
        ]

    @classmethod
    def decode(cls, data, connection_state=None, payload_auto_decode=True):
        obj = cls(
            connection_state=connection_state
        )
        if len(data) > 0:
            data = obj.dissect(data)

        return (obj, data)

    def encode(self):
        if len(self.data) == 0:
            return b""
        else:
            return self.assemble()

Extension.add_payload_type(0x0023, SessionTicketTLS)
