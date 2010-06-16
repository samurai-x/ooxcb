# auto generated. yay.
import ooxcb
from ooxcb.resource import get_internal
from ooxcb.types import SIZES, make_array, build_list
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
from struct import pack, unpack, calcsize

def unpack_from_stream(fmt, stream, offset=0):
    if offset:
        stream.seek(offset, 1)
    s = stream.read(calcsize(fmt))
    return unpack(fmt, s)


MAJOR_VERSION = 0
MINOR_VERSION = 0
key = ooxcb.ExtensionKey("BIG-REQUESTS")

class EnableReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.maximum_request_length = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxI", stream)
        self.maximum_request_length = _unpacked[0]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxI", self.maximum_request_length))

class bigreqExtension(ooxcb.Extension):
    header = "bigreq"
    def enable(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.bigreq.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, True), \
            EnableCookie(),
            EnableReply)

    def enable_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.bigreq.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, False), \
            EnableCookie(),
            EnableReply)

class EnableCookie(ooxcb.Cookie):
    pass

_events = {
}

_errors = {
}

for ev in _events.itervalues():
    if isinstance(ev.event_target_class, str):
        ev.event_target_class = globals()[ev.event_target_class]

ooxcb._add_ext(key, bigreqExtension, _events, _errors)
def mixin():
    pass


