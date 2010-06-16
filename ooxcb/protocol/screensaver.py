# auto generated. yay.
import ooxcb
from ooxcb.resource import get_internal
from ooxcb.types import SIZES, make_array, build_list
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
from struct import pack, unpack, calcsize
from ooxcb.protocol.xproto import Drawable, Window
from ooxcb.util import Mixin

def unpack_from_stream(fmt, stream, offset=0):
    if offset:
        stream.seek(offset, 1)
    s = stream.read(calcsize(fmt))
    return unpack(fmt, s)


MAJOR_VERSION = 1
MINOR_VERSION = 1
key = ooxcb.ExtensionKey("MIT-SCREEN-SAVER")

class Kind(object):
    Blanked = 0
    Internal = 1
    External = 2

class State(object):
    Off = 0
    On = 1
    Cycle = 2
    Disabled = 3

class CW(object):
    BackPixmap = 1
    BackPixel = 2
    BorderPixmap = 4
    BorderPixel = 8
    BitGravity = 16
    WinGravity = 32
    BackingStore = 64
    BackingPlanes = 128
    BackingPixel = 256
    OverrideRedirect = 512
    SaveUnder = 1024
    EventMask = 2048
    DontPropagate = 4096
    Colormap = 8192
    Cursor = 16384

class Event(object):
    NotifyMask = 1
    CycleMask = 2

class WindowMixin(Mixin):
    target_class = Window

class QueryVersionReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.server_major_version = None
        self.server_minor_version = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHHxxxxxxxxxxxxxxxxxxxx", stream)
        self.server_major_version = _unpacked[0]
        self.server_minor_version = _unpacked[1]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHHxxxxxxxxxxxxxxxxxxxx", self.server_major_version, self.server_minor_version))

class screensaverExtension(ooxcb.Extension):
    header = "screensaver"
    def query_version(self, client_major_version, client_minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBxx", client_major_version, client_minor_version))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, True), \
            QueryVersionCookie(),
            QueryVersionReply)

    def query_version_unchecked(self, client_major_version, client_minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBxx", client_major_version, client_minor_version))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, False), \
            QueryVersionCookie(),
            QueryVersionReply)

    def suspend_checked(self, suspend):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxx", suspend))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, True, True), \
            ooxcb.VoidCookie())

    def suspend(self, suspend):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxx", suspend))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, True, False), \
            ooxcb.VoidCookie())

class DrawableMixin(Mixin):
    target_class = Drawable
    def query_info(self):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", drawable))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, False, True), \
            QueryInfoCookie(),
            QueryInfoReply)

    def query_info_unchecked(self):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", drawable))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, False, False), \
            QueryInfoCookie(),
            QueryInfoReply)

    def select_input_checked(self, event_mask):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", drawable, event_mask))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, True), \
            ooxcb.VoidCookie())

    def select_input(self, event_mask):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", drawable, event_mask))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, False), \
            ooxcb.VoidCookie())

    def set_attributes_checked(self, x, y, width, height, border_width, _class, depth, visual, value_mask, value_list):
        value_mask, value_list = 0, []
        if "back_pixmap" in values:
            value_mask |= 1
            value_list.append(get_internal(values["back_pixmap"]))
        if "back_pixel" in values:
            value_mask |= 2
            value_list.append(values["back_pixel"])
        if "border_pixmap" in values:
            value_mask |= 4
            value_list.append(values["border_pixmap"])
        if "border_pixel" in values:
            value_mask |= 8
            value_list.append(values["border_pixel"])
        if "bit_gravity" in values:
            value_mask |= 16
            value_list.append(values["bit_gravity"])
        if "win_gravity" in values:
            value_mask |= 32
            value_list.append(values["win_gravity"])
        if "backing_store" in values:
            value_mask |= 64
            value_list.append(values["backing_store"])
        if "backing_planes" in values:
            value_mask |= 128
            value_list.append(values["backing_planes"])
        if "backing_pixel" in values:
            value_mask |= 256
            value_list.append(values["backing_pixel"])
        if "override_redirect" in values:
            value_mask |= 512
            value_list.append(values["override_redirect"])
        if "save_under" in values:
            value_mask |= 1024
            value_list.append(values["save_under"])
        if "event_mask" in values:
            value_mask |= 2048
            value_list.append(values["event_mask"])
        if "dont_propagate" in values:
            value_mask |= 4096
            value_list.append(values["dont_propagate"])
        if "colormap" in values:
            value_mask |= 8192
            value_list.append(get_internal(values["colormap"]))
        if "cursor" in values:
            value_mask |= 16384
            value_list.append(get_internal(values["cursor"]))
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIhhHHHBBII", drawable, x, y, width, height, border_width, _class, depth, visual, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, True), \
            ooxcb.VoidCookie())

    def set_attributes(self, x, y, width, height, border_width, _class, depth, visual, value_mask, value_list):
        value_mask, value_list = 0, []
        if "back_pixmap" in values:
            value_mask |= 1
            value_list.append(get_internal(values["back_pixmap"]))
        if "back_pixel" in values:
            value_mask |= 2
            value_list.append(values["back_pixel"])
        if "border_pixmap" in values:
            value_mask |= 4
            value_list.append(values["border_pixmap"])
        if "border_pixel" in values:
            value_mask |= 8
            value_list.append(values["border_pixel"])
        if "bit_gravity" in values:
            value_mask |= 16
            value_list.append(values["bit_gravity"])
        if "win_gravity" in values:
            value_mask |= 32
            value_list.append(values["win_gravity"])
        if "backing_store" in values:
            value_mask |= 64
            value_list.append(values["backing_store"])
        if "backing_planes" in values:
            value_mask |= 128
            value_list.append(values["backing_planes"])
        if "backing_pixel" in values:
            value_mask |= 256
            value_list.append(values["backing_pixel"])
        if "override_redirect" in values:
            value_mask |= 512
            value_list.append(values["override_redirect"])
        if "save_under" in values:
            value_mask |= 1024
            value_list.append(values["save_under"])
        if "event_mask" in values:
            value_mask |= 2048
            value_list.append(values["event_mask"])
        if "dont_propagate" in values:
            value_mask |= 4096
            value_list.append(values["dont_propagate"])
        if "colormap" in values:
            value_mask |= 8192
            value_list.append(get_internal(values["colormap"]))
        if "cursor" in values:
            value_mask |= 16384
            value_list.append(get_internal(values["cursor"]))
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIhhHHHBBII", drawable, x, y, width, height, border_width, _class, depth, visual, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, False), \
            ooxcb.VoidCookie())

    def unset_attributes_checked(self):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", drawable))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, True), \
            ooxcb.VoidCookie())

    def unset_attributes(self):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", drawable))
        return self.conn.screensaver.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, False), \
            ooxcb.VoidCookie())

class NotifyEvent(ooxcb.Event):
    event_name = "on_notify"
    opcode = 0
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 0
        self.code = None
        self.state = None
        self.sequence_number = None
        self.time = None
        self.root = None
        self.window = None
        self.kind = None
        self.forced = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxBxHIIIBBxxxxxxxxxxxxxx", stream)
        self.response_type = _unpacked[0]
        self.code = _unpacked[1]
        self.state = _unpacked[2]
        self.sequence_number = _unpacked[3]
        self.time = _unpacked[4]
        self.root = Window(self.conn, _unpacked[5])
        self.window = Window(self.conn, _unpacked[6])
        self.kind = _unpacked[7]
        self.forced = _unpacked[8]
        self.event_target = self.window

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxBxHIIIBBxxxxxxxxxxxxxx", self.response_type, self.code, self.state, self.sequence_number, self.time, get_internal(self.root), get_internal(self.window), self.kind, self.forced))
        stream.write("\0" * (32 - (stream.tell() - root)))

class QueryVersionCookie(ooxcb.Cookie):
    pass

class QueryInfoCookie(ooxcb.Cookie):
    pass

class QueryInfoReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.state = None
        self.saver_window = None
        self.ms_until_server = None
        self.ms_since_user_input = None
        self.event_mask = None
        self.kind = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxIIIIBxxxxxxx", stream)
        self.state = _unpacked[0]
        self.saver_window = Window(self.conn, _unpacked[1])
        self.ms_until_server = _unpacked[2]
        self.ms_since_user_input = _unpacked[3]
        self.event_mask = _unpacked[4]
        self.kind = _unpacked[5]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxIIIIBxxxxxxx", self.state, get_internal(self.saver_window), self.ms_until_server, self.ms_since_user_input, self.event_mask, self.kind))

_events = {
    0: NotifyEvent,
}

_errors = {
}

for ev in _events.itervalues():
    if isinstance(ev.event_target_class, str):
        ev.event_target_class = globals()[ev.event_target_class]

ooxcb._add_ext(key, screensaverExtension, _events, _errors)
def mixin():
    DrawableMixin.mixin()
    WindowMixin.mixin()


