# auto generated. yay.
import ooxcb
from ooxcb.resource import get_internal
from ooxcb.types import SIZES, make_array, build_list
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
from struct import pack, unpack, calcsize
from ooxcb.protocol.xproto import Window
from ooxcb.util import Mixin

def unpack_from_stream(fmt, stream, offset=0):
    if offset:
        stream.seek(offset, 1)
    s = stream.read(calcsize(fmt))
    return unpack(fmt, s)


MAJOR_VERSION = 2
MINOR_VERSION = 1
key = ooxcb.ExtensionKey("XTEST")

class Cursor(object):
    _None = 0
    Current = 1

class GetVersionReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.major_version = None
        self.minor_version = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxH", stream)
        self.major_version = _unpacked[0]
        self.minor_version = _unpacked[1]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxH", self.major_version, self.minor_version))

class WindowMixin(Mixin):
    target_class = Window
    def compare_cursor(self, cursor):
        window = get_internal(self)
        cursor = get_internal(cursor)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", window, cursor))
        return self.conn.xtest.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, False, True), \
            CompareCursorCookie(),
            CompareCursorReply)

    def compare_cursor_unchecked(self, cursor):
        window = get_internal(self)
        cursor = get_internal(cursor)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", window, cursor))
        return self.conn.xtest.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, False, False), \
            CompareCursorCookie(),
            CompareCursorReply)

class xtestExtension(ooxcb.Extension):
    header = "xtest"
    def get_version(self, major_version, minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxH", major_version, minor_version))
        return self.conn.xtest.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, True), \
            GetVersionCookie(),
            GetVersionReply)

    def get_version_unchecked(self, major_version, minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxH", major_version, minor_version))
        return self.conn.xtest.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, False), \
            GetVersionCookie(),
            GetVersionReply)

    def fake_input_checked(self, type, detail=0, time=0, window=None, rootX=0, rootY=0, deviceid=0):
        window = get_internal(window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBxxIIxxxxxxxxHHxxxxxxxB", type, detail, time, window, rootX, rootY, deviceid))
        return self.conn.xtest.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, True), \
            ooxcb.VoidCookie())

    def fake_input(self, type, detail=0, time=0, window=None, rootX=0, rootY=0, deviceid=0):
        window = get_internal(window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBxxIIxxxxxxxxHHxxxxxxxB", type, detail, time, window, rootX, rootY, deviceid))
        return self.conn.xtest.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, False), \
            ooxcb.VoidCookie())

    def grab_control_checked(self, impervious):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxx", impervious))
        return self.conn.xtest.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, True), \
            ooxcb.VoidCookie())

    def grab_control(self, impervious):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxx", impervious))
        return self.conn.xtest.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, False), \
            ooxcb.VoidCookie())

class CompareCursorReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.same = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxx", stream)
        self.same = _unpacked[0]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxx", self.same))

class CompareCursorCookie(ooxcb.Cookie):
    pass

class GetVersionCookie(ooxcb.Cookie):
    pass

_events = {
}

_errors = {
}

for ev in _events.itervalues():
    if isinstance(ev.event_target_class, str):
        ev.event_target_class = globals()[ev.event_target_class]

ooxcb._add_ext(key, xtestExtension, _events, _errors)
def mixin():
    WindowMixin.mixin()


