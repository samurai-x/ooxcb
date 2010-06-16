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


MAJOR_VERSION = 1
MINOR_VERSION = 1
key = ooxcb.ExtensionKey("SHAPE")

class SK(object):
    Bounding = 0
    Clip = 1
    Input = 2

class SO(object):
    Set = 0
    Union = 1
    Intersect = 2
    Subtract = 3
    Invert = 4

class shapeExtension(ooxcb.Extension):
    header = "shape"
    def query_version(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, True), \
            QueryVersionCookie(),
            QueryVersionReply)

    def query_version_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, False), \
            QueryVersionCookie(),
            QueryVersionReply)

class WindowMixin(Mixin):
    target_class = Window
    def shape_rectangles_checked(self, operation, destination_kind, ordering, x_offset, y_offset, rectangles):
        rectangles_len = len(rectangles)
        destination_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBBxIhh", operation, destination_kind, ordering, destination_window, x_offset, y_offset))
        rectangles.build(buf)
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, True, True), \
            ooxcb.VoidCookie())

    def shape_rectangles(self, operation, destination_kind, ordering, x_offset, y_offset, rectangles):
        rectangles_len = len(rectangles)
        destination_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBBxIhh", operation, destination_kind, ordering, destination_window, x_offset, y_offset))
        rectangles.build(buf)
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, True, False), \
            ooxcb.VoidCookie())

    def shape_mask_checked(self, operation, destination_kind, x_offset, y_offset, source_bitmap):
        destination_window = get_internal(self)
        source_bitmap = get_internal(source_bitmap)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBxxIhhI", operation, destination_kind, destination_window, x_offset, y_offset, source_bitmap))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, True), \
            ooxcb.VoidCookie())

    def shape_mask(self, operation, destination_kind, x_offset, y_offset, source_bitmap):
        destination_window = get_internal(self)
        source_bitmap = get_internal(source_bitmap)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBxxIhhI", operation, destination_kind, destination_window, x_offset, y_offset, source_bitmap))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, False), \
            ooxcb.VoidCookie())

    def shape_combine_checked(self, operation, destination_kind, source_kind, x_offset, y_offset, source_window):
        destination_window = get_internal(self)
        source_window = get_internal(source_window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBBxIhhI", operation, destination_kind, source_kind, destination_window, x_offset, y_offset, source_window))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, True), \
            ooxcb.VoidCookie())

    def shape_combine(self, operation, destination_kind, source_kind, x_offset, y_offset, source_window):
        destination_window = get_internal(self)
        source_window = get_internal(source_window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBBxIhhI", operation, destination_kind, source_kind, destination_window, x_offset, y_offset, source_window))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, False), \
            ooxcb.VoidCookie())

    def shape_offset_checked(self, destination_kind, x_offset, y_offset):
        destination_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIhh", destination_kind, destination_window, x_offset, y_offset))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, True), \
            ooxcb.VoidCookie())

    def shape_offset(self, destination_kind, x_offset, y_offset):
        destination_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIhh", destination_kind, destination_window, x_offset, y_offset))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, False), \
            ooxcb.VoidCookie())

    def shape_query_extents(self):
        destination_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", destination_window))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, False, True), \
            QueryExtentsCookie(),
            QueryExtentsReply)

    def shape_query_extents_unchecked(self):
        destination_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", destination_window))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, False, False), \
            QueryExtentsCookie(),
            QueryExtentsReply)

    def shape_select_input_checked(self, enable):
        destination_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", destination_window, enable))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 6, True, True), \
            ooxcb.VoidCookie())

    def shape_select_input(self, enable):
        destination_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", destination_window, enable))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 6, True, False), \
            ooxcb.VoidCookie())

    def shape_input_selected(self):
        destination_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", destination_window))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 7, False, True), \
            InputSelectedCookie(),
            InputSelectedReply)

    def shape_input_selected_unchecked(self):
        destination_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", destination_window))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 7, False, False), \
            InputSelectedCookie(),
            InputSelectedReply)

    def shape_get_rectangles(self, source_kind):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", window, source_kind))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 8, False, True), \
            GetRectanglesCookie(),
            GetRectanglesReply)

    def shape_get_rectangles_unchecked(self, source_kind):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxx", window, source_kind))
        return self.conn.shape.send_request(ooxcb.Request(self.conn, buf.getvalue(), 8, False, False), \
            GetRectanglesCookie(),
            GetRectanglesReply)

class QueryVersionReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.major_version = None
        self.minor_version = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHH", stream)
        self.major_version = _unpacked[0]
        self.minor_version = _unpacked[1]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHH", self.major_version, self.minor_version))

class QueryVersionCookie(ooxcb.Cookie):
    pass

class NotifyEvent(ooxcb.Event):
    event_name = "on_notify"
    opcode = 0
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 0
        self.shape_kind = None
        self.affected_window = None
        self.extents_x = None
        self.extents_y = None
        self.extents_width = None
        self.extents_height = None
        self.server_time = None
        self.shaped = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIhhHHIBxxxxxxxxxxx", stream)
        self.response_type = _unpacked[0]
        self.shape_kind = _unpacked[1]
        self.affected_window = Window(self.conn, _unpacked[2])
        self.extents_x = _unpacked[3]
        self.extents_y = _unpacked[4]
        self.extents_width = _unpacked[5]
        self.extents_height = _unpacked[6]
        self.server_time = _unpacked[7]
        self.shaped = _unpacked[8]
        self.event_target = self.affected_window

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIhhHHIBxxxxxxxxxxx", self.response_type, self.shape_kind, get_internal(self.affected_window), self.extents_x, self.extents_y, self.extents_width, self.extents_height, self.server_time, self.shaped))
        stream.write("\0" * (32 - (stream.tell() - root)))

class GetRectanglesReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.ordering = None
        self.rectangles_len = None
        self.rectangles = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxI", stream)
        self.ordering = _unpacked[0]
        self.rectangles_len = _unpacked[1]
        self.rectangles = ooxcb.List(self.conn, stream, self.rectangles_len, RECTANGLE, 8)

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxI", self.ordering, self.rectangles_len))
        count += 12
        build_list(self.conn, stream, self.rectangles, RECTANGLE)

class QueryExtentsCookie(ooxcb.Cookie):
    pass

class InputSelectedReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.enabled = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxx", stream)
        self.enabled = _unpacked[0]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxx", self.enabled))

class QueryExtentsReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.bounding_shaped = None
        self.clip_shaped = None
        self.bounding_shape_extents_x = None
        self.bounding_shape_extents_y = None
        self.bounding_shape_extents_width = None
        self.bounding_shape_extents_height = None
        self.clip_shape_extents_x = None
        self.clip_shape_extents_y = None
        self.clip_shape_extents_width = None
        self.clip_shape_extents_height = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxBBxxhhHHhhHH", stream)
        self.bounding_shaped = _unpacked[0]
        self.clip_shaped = _unpacked[1]
        self.bounding_shape_extents_x = _unpacked[2]
        self.bounding_shape_extents_y = _unpacked[3]
        self.bounding_shape_extents_width = _unpacked[4]
        self.bounding_shape_extents_height = _unpacked[5]
        self.clip_shape_extents_x = _unpacked[6]
        self.clip_shape_extents_y = _unpacked[7]
        self.clip_shape_extents_width = _unpacked[8]
        self.clip_shape_extents_height = _unpacked[9]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxBBxxhhHHhhHH", self.bounding_shaped, self.clip_shaped, self.bounding_shape_extents_x, self.bounding_shape_extents_y, self.bounding_shape_extents_width, self.bounding_shape_extents_height, self.clip_shape_extents_x, self.clip_shape_extents_y, self.clip_shape_extents_width, self.clip_shape_extents_height))

class GetRectanglesCookie(ooxcb.Cookie):
    pass

class InputSelectedCookie(ooxcb.Cookie):
    pass

_events = {
    0: NotifyEvent,
}

_errors = {
}

for ev in _events.itervalues():
    if isinstance(ev.event_target_class, str):
        ev.event_target_class = globals()[ev.event_target_class]

ooxcb._add_ext(key, shapeExtension, _events, _errors)
def mixin():
    WindowMixin.mixin()


