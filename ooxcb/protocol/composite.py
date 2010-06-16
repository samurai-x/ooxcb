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
from ooxcb.protocol.xfixes import Region
from ooxcb.util import Mixin

def unpack_from_stream(fmt, stream, offset=0):
    if offset:
        stream.seek(offset, 1)
    s = stream.read(calcsize(fmt))
    return unpack(fmt, s)


MAJOR_VERSION = 0
MINOR_VERSION = 3
key = ooxcb.ExtensionKey("Composite")

class Redirect(object):
    Automatic = 0
    Manual = 1

class GetOverlayWindowReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.overlay_win = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxIxxxxxxxxxxxxxxxxxxxx", stream)
        self.overlay_win = Window(self.conn, _unpacked[0])

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxIxxxxxxxxxxxxxxxxxxxx", get_internal(self.overlay_win)))

class WindowMixin(Mixin):
    target_class = Window
    def redirect_checked(self, update=Redirect.Automatic):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", window, update))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, True, True), \
            ooxcb.VoidCookie())

    def redirect(self, update=Redirect.Automatic):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", window, update))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, True, False), \
            ooxcb.VoidCookie())

    def redirect_subwindows_checked(self, update=Redirect.Automatic):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", window, update))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, True), \
            ooxcb.VoidCookie())

    def redirect_subwindows(self, update=Redirect.Automatic):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", window, update))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, False), \
            ooxcb.VoidCookie())

    def unredirect_checked(self, update=Redirect.Automatic):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", window, update))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, True), \
            ooxcb.VoidCookie())

    def unredirect(self, update=Redirect.Automatic):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", window, update))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, False), \
            ooxcb.VoidCookie())

    def unredirect_subwindows_checked(self, update=Redirect.Automatic):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", window, update))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, True), \
            ooxcb.VoidCookie())

    def unredirect_subwindows(self, update=Redirect.Automatic):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", window, update))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, False), \
            ooxcb.VoidCookie())

    def name_pixmap_checked(self, pixmap):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", window, pixmap))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 6, True, True), \
            ooxcb.VoidCookie())

    def name_pixmap(self, pixmap):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", window, pixmap))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 6, True, False), \
            ooxcb.VoidCookie())

    def get_overlay_window(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 7, False, True), \
            GetOverlayWindowCookie(),
            GetOverlayWindowReply)

    def get_overlay_window_unchecked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 7, False, False), \
            GetOverlayWindowCookie(),
            GetOverlayWindowReply)

    def release_overlay_window_checked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 8, True, True), \
            ooxcb.VoidCookie())

    def release_overlay_window(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 8, True, False), \
            ooxcb.VoidCookie())

class QueryVersionReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.major_version = None
        self.minor_version = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxIIxxxxxxxxxxxxxxxx", stream)
        self.major_version = _unpacked[0]
        self.minor_version = _unpacked[1]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxIIxxxxxxxxxxxxxxxx", self.major_version, self.minor_version))

class QueryVersionCookie(ooxcb.Cookie):
    pass

class GetOverlayWindowCookie(ooxcb.Cookie):
    pass

class RegionMixin(Mixin):
    target_class = Region
    @classmethod
    def create_from_border_clip(cls, conn, window):
        rid = conn.generate_id()
        region = cls(conn, rid)
        conn.composite.create_region_from_border_clip_checked(region, window).check()
        conn.add_to_cache(rid, region)
        return region

class compositeExtension(ooxcb.Extension):
    header = "composite"
    def query_version(self, client_major_version, client_minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", client_major_version, client_minor_version))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, True), \
            QueryVersionCookie(),
            QueryVersionReply)

    def query_version_unchecked(self, client_major_version, client_minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", client_major_version, client_minor_version))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, False), \
            QueryVersionCookie(),
            QueryVersionReply)

    def create_region_from_border_clip_checked(self, region, window):
        region = get_internal(region)
        window = get_internal(window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", region, window))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, True, True), \
            ooxcb.VoidCookie())

    def create_region_from_border_clip(self, region, window):
        region = get_internal(region)
        window = get_internal(window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", region, window))
        return self.conn.composite.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, True, False), \
            ooxcb.VoidCookie())

_events = {
}

_errors = {
}

for ev in _events.itervalues():
    if isinstance(ev.event_target_class, str):
        ev.event_target_class = globals()[ev.event_target_class]

ooxcb._add_ext(key, compositeExtension, _events, _errors)
def mixin():
    WindowMixin.mixin()
    RegionMixin.mixin()


