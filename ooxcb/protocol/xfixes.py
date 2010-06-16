# auto generated. yay.
import ooxcb
from ooxcb.resource import get_internal
from ooxcb.types import SIZES, make_array, build_list
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
from struct import pack, unpack, calcsize
from ooxcb.protocol.xproto import Window, GContext, Cursor
from ooxcb.protocol.render import Picture
from ooxcb.util import Mixin

def unpack_from_stream(fmt, stream, offset=0):
    if offset:
        stream.seek(offset, 1)
    s = stream.read(calcsize(fmt))
    return unpack(fmt, s)


MAJOR_VERSION = 4
MINOR_VERSION = 0
key = ooxcb.ExtensionKey("XFIXES")

class SelectionEventMask(object):
    SetSelectionOwner = 1
    SelectionWindowDestroy = 2
    SelectionClientClose = 4

class SaveSetMode(object):
    Insert = 0
    Delete = 1

class CursorNotify(object):
    DisplayCursor = 0

class SelectionEvent(object):
    SetSelectionOwner = 0
    SelectionWindowDestroy = 1
    SelectionClientClose = 2

class SaveSetMapping(object):
    Map = 0
    Unmap = 1

class SaveSetTarget(object):
    Nearest = 0
    Root = 1

class CursorNotifyMask(object):
    DisplayCursor = 1

class BadRegion(ooxcb.ProtocolException):
    pass

class CursorNotifyEvent(ooxcb.Event):
    event_name = "on_cursor_notify"
    opcode = 1
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 1
        self.subtype = None
        self.window = None
        self.cursor_serial = None
        self.timestamp = None
        self.name = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIIIIxxxxxxxxxxxx", stream)
        self.response_type = _unpacked[0]
        self.subtype = _unpacked[1]
        self.window = Window(self.conn, _unpacked[2])
        self.cursor_serial = _unpacked[3]
        self.timestamp = _unpacked[4]
        self.name = self.conn.atoms.get_by_id(_unpacked[5])
        self.event_target = self.window

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIIIIxxxxxxxxxxxx", self.response_type, self.subtype, get_internal(self.window), self.cursor_serial, self.timestamp, get_internal(self.name)))
        stream.write("\0" * (32 - (stream.tell() - root)))

class WindowMixin(Mixin):
    target_class = Window
    def change_save_set_checked(self, mode, target, map):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBBxI", mode, target, map, window))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, True, True), \
            ooxcb.VoidCookie())

    def change_save_set(self, mode, target, map):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBBBxI", mode, target, map, window))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, True, False), \
            ooxcb.VoidCookie())

    def select_selection_input_checked(self, selection, event_mask):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", window, selection, event_mask))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, True), \
            ooxcb.VoidCookie())

    def select_selection_input(self, selection, event_mask):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", window, selection, event_mask))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, False), \
            ooxcb.VoidCookie())

    def select_cursor_input_checked(self, event_mask):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", window, event_mask))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, True), \
            ooxcb.VoidCookie())

    def select_cursor_input(self, event_mask):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", window, event_mask))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, False), \
            ooxcb.VoidCookie())

    def set_shape_region_checked(self, dest_kind, x_offset, y_offset, region):
        dest = get_internal(self)
        region = get_internal(region)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxxhhI", dest, dest_kind, x_offset, y_offset, region))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 21, True, True), \
            ooxcb.VoidCookie())

    def set_shape_region(self, dest_kind, x_offset, y_offset, region):
        dest = get_internal(self)
        region = get_internal(region)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIBxxxhhI", dest, dest_kind, x_offset, y_offset, region))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 21, True, False), \
            ooxcb.VoidCookie())

    def hide_cursor_checked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 29, True, True), \
            ooxcb.VoidCookie())

    def hide_cursor(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 29, True, False), \
            ooxcb.VoidCookie())

    def show_cursor_checked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 30, True, True), \
            ooxcb.VoidCookie())

    def show_cursor(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 30, True, False), \
            ooxcb.VoidCookie())

class FetchRegionCookie(ooxcb.Cookie):
    pass

class FetchRegionReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.extents = None
        self.rectangles = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        self.extents = RECTANGLE.create_from_stream(self.conn, stream)
        stream.seek(ooxcb.type_pad(8, stream.tell() - root), 1)
        self.rectangles = ooxcb.List(self.conn, stream, self.length, RECTANGLE, 8)

    def build(self, stream):
        count = 0
        count += 8
        self.extents.build(stream)
        count += 16
        build_list(self.conn, stream, self.rectangles, RECTANGLE)

class RegionError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)

    def read(self, stream):
        self._address = stream.address

    def build(self, stream):
        count = 0

class xfixesExtension(ooxcb.Extension):
    header = "xfixes"
    def query_version(self, client_major_version, client_minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", client_major_version, client_minor_version))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, True), \
            QueryVersionCookie(),
            QueryVersionReply)

    def query_version_unchecked(self, client_major_version, client_minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", client_major_version, client_minor_version))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, False), \
            QueryVersionCookie(),
            QueryVersionReply)

    def get_cursor_image(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, False, True), \
            GetCursorImageCookie(),
            GetCursorImageReply)

    def get_cursor_image_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, False, False), \
            GetCursorImageCookie(),
            GetCursorImageReply)

    def create_region_checked(self, region, rectangles):
        rectangles_len = len(rectangles)
        region = get_internal(region)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", region))
        rectangles.build(buf)
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, True, True), \
            ooxcb.VoidCookie())

    def create_region(self, region, rectangles):
        rectangles_len = len(rectangles)
        region = get_internal(region)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", region))
        rectangles.build(buf)
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, True, False), \
            ooxcb.VoidCookie())

    def create_region_from_bitmap_checked(self, region, bitmap):
        region = get_internal(region)
        bitmap = get_internal(bitmap)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", region, bitmap))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 6, True, True), \
            ooxcb.VoidCookie())

    def create_region_from_bitmap(self, region, bitmap):
        region = get_internal(region)
        bitmap = get_internal(bitmap)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", region, bitmap))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 6, True, False), \
            ooxcb.VoidCookie())

    def create_region_from_window_checked(self, region, window, kind):
        region = get_internal(region)
        window = get_internal(window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIBxxx", region, window, kind))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 7, True, True), \
            ooxcb.VoidCookie())

    def create_region_from_window(self, region, window, kind):
        region = get_internal(region)
        window = get_internal(window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIBxxx", region, window, kind))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 7, True, False), \
            ooxcb.VoidCookie())

    def create_region_from_g_c_checked(self, region, gc):
        region = get_internal(region)
        gc = get_internal(gc)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", region, gc))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 8, True, True), \
            ooxcb.VoidCookie())

    def create_region_from_g_c(self, region, gc):
        region = get_internal(region)
        gc = get_internal(gc)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", region, gc))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 8, True, False), \
            ooxcb.VoidCookie())

    def create_region_from_picture_checked(self, region, picture):
        region = get_internal(region)
        picture = get_internal(picture)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", region, picture))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 9, True, True), \
            ooxcb.VoidCookie())

    def create_region_from_picture(self, region, picture):
        region = get_internal(region)
        picture = get_internal(picture)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", region, picture))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 9, True, False), \
            ooxcb.VoidCookie())

    def get_cursor_name(self, cursor):
        cursor = get_internal(cursor)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cursor))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 24, False, True), \
            GetCursorNameCookie(),
            GetCursorNameReply)

    def get_cursor_name_unchecked(self, cursor):
        cursor = get_internal(cursor)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cursor))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 24, False, False), \
            GetCursorNameCookie(),
            GetCursorNameReply)

    def get_cursor_image_and_name(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 25, False, True), \
            GetCursorImageAndNameCookie(),
            GetCursorImageAndNameReply)

    def get_cursor_image_and_name_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 25, False, False), \
            GetCursorImageAndNameCookie(),
            GetCursorImageAndNameReply)

class GetCursorNameReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.atom = None
        self.nbytes = None
        self.name = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxIHxxxxxxxxxxxxxxxxxx", stream)
        self.atom = self.conn.atoms.get_by_id(_unpacked[0])
        self.nbytes = _unpacked[1]
        self.name = ooxcb.List(self.conn, stream, self.nbytes, 'B', 1).to_string()

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxIHxxxxxxxxxxxxxxxxxx", get_internal(self.atom), self.nbytes))
        count += 32
        build_list(self.conn, stream, self.name, 'B')

class QueryVersionCookie(ooxcb.Cookie):
    pass

class Region(ooxcb.Resource):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def destroy_checked(self):
        region = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", region))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 10, True, True), \
            ooxcb.VoidCookie())

    def destroy(self):
        region = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", region))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 10, True, False), \
            ooxcb.VoidCookie())

    def set_checked(self, rectangles):
        rectangles_len = len(rectangles)
        region = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", region))
        rectangles.build(buf)
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 11, True, True), \
            ooxcb.VoidCookie())

    def set(self, rectangles):
        rectangles_len = len(rectangles)
        region = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", region))
        rectangles.build(buf)
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 11, True, False), \
            ooxcb.VoidCookie())

    def copy_checked(self, destination):
        source = get_internal(self)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", source, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 12, True, True), \
            ooxcb.VoidCookie())

    def copy(self, destination):
        source = get_internal(self)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", source, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 12, True, False), \
            ooxcb.VoidCookie())

    def union_checked(self, source2, destination):
        source1 = get_internal(self)
        source2 = get_internal(source2)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", source1, source2, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 13, True, True), \
            ooxcb.VoidCookie())

    def union(self, source2, destination):
        source1 = get_internal(self)
        source2 = get_internal(source2)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", source1, source2, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 13, True, False), \
            ooxcb.VoidCookie())

    def intersect_checked(self, source2, destination):
        source1 = get_internal(self)
        source2 = get_internal(source2)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", source1, source2, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 14, True, True), \
            ooxcb.VoidCookie())

    def intersect(self, source2, destination):
        source1 = get_internal(self)
        source2 = get_internal(source2)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", source1, source2, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 14, True, False), \
            ooxcb.VoidCookie())

    def subtract_checked(self, source2, destination):
        source1 = get_internal(self)
        source2 = get_internal(source2)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", source1, source2, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 15, True, True), \
            ooxcb.VoidCookie())

    def subtract(self, source2, destination):
        source1 = get_internal(self)
        source2 = get_internal(source2)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", source1, source2, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 15, True, False), \
            ooxcb.VoidCookie())

    def invert_checked(self, bounds, destination):
        source = get_internal(self)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", source))
        bounds.build(buf)
        buf.write(pack("=I", destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 16, True, True), \
            ooxcb.VoidCookie())

    def invert(self, bounds, destination):
        source = get_internal(self)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", source))
        bounds.build(buf)
        buf.write(pack("=I", destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 16, True, False), \
            ooxcb.VoidCookie())

    def translate_checked(self, dx, dy):
        region = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIhh", region, dx, dy))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 17, True, True), \
            ooxcb.VoidCookie())

    def translate(self, dx, dy):
        region = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIhh", region, dx, dy))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 17, True, False), \
            ooxcb.VoidCookie())

    def extents_checked(self, destination):
        source = get_internal(self)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", source, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 18, True, True), \
            ooxcb.VoidCookie())

    def extents(self, destination):
        source = get_internal(self)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", source, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 18, True, False), \
            ooxcb.VoidCookie())

    def fetch(self):
        region = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", region))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 19, False, True), \
            FetchRegionCookie(),
            FetchRegionReply)

    def fetch_unchecked(self):
        region = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", region))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 19, False, False), \
            FetchRegionCookie(),
            FetchRegionReply)

    def expand_checked(self, destination, left, right, top, bottom):
        source = get_internal(self)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIHHHH", source, destination, left, right, top, bottom))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 28, True, True), \
            ooxcb.VoidCookie())

    def expand(self, destination, left, right, top, bottom):
        source = get_internal(self)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIHHHH", source, destination, left, right, top, bottom))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 28, True, False), \
            ooxcb.VoidCookie())

    @classmethod
    def create(cls, conn, rectangles):
        rid = conn.generate_id()
        region = cls(conn, rid)
        conn.xfixes.create_region_checked(region, rectangles).check()
        conn.add_to_cache(rid, region)
        return region

    @classmethod
    def create_from_bitmap(cls, conn, bitmap):
        rid = conn.generate_id()
        region = cls(conn, rid)
        conn.xfixes.create_region_from_bitmap_checked(region, bitmap).check()
        conn.add_to_cache(rid, region)
        return region

    @classmethod
    def create_from_window(cls, conn, window, kind):
        rid = conn.generate_id()
        region = cls(conn, rid)
        conn.xfixes.create_region_from_window_checked(region, window, kind).check()
        conn.add_to_cache(rid, region)
        return region

    @classmethod
    def create_from_gc(cls, conn, gc):
        rid = conn.generate_id()
        region = cls(conn, rid)
        conn.xfixes.create_region_from_g_c_checked(region, gc).check()
        conn.add_to_cache(rid, region)
        return region

    @classmethod
    def create_from_picture(cls, conn, picture):
        rid = conn.generate_id()
        region = cls(conn, rid)
        conn.xfixes.create_region_from_picture_checked(region, picture).check()
        conn.add_to_cache(rid, region)
        return region

class PictureMixin(Mixin):
    target_class = Picture
    def set_clip_region_checked(self, region, x_origin, y_origin):
        picture = get_internal(self)
        region = get_internal(region)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", picture, region, x_origin, y_origin))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 22, True, True), \
            ooxcb.VoidCookie())

    def set_clip_region(self, region, x_origin, y_origin):
        picture = get_internal(self)
        region = get_internal(region)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", picture, region, x_origin, y_origin))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 22, True, False), \
            ooxcb.VoidCookie())

class GetCursorImageReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.xhot = None
        self.yhot = None
        self.cursor_serial = None
        self.cursor_image = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxhhHHHHIxxxxxxxx", stream)
        self.x = _unpacked[0]
        self.y = _unpacked[1]
        self.width = _unpacked[2]
        self.height = _unpacked[3]
        self.xhot = _unpacked[4]
        self.yhot = _unpacked[5]
        self.cursor_serial = _unpacked[6]
        self.cursor_image = ooxcb.List(self.conn, stream, (self.width * self.height), 'I', 4)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxhhHHHHIxxxxxxxx", self.x, self.y, self.width, self.height, self.xhot, self.yhot, self.cursor_serial))
        count += 32
        build_list(self.conn, stream, self.cursor_image, 'I')

class GContextMixin(Mixin):
    target_class = GContext
    def set_clip_region_checked(self, region, x_origin, y_origin):
        gc = get_internal(self)
        region = get_internal(region)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", gc, region, x_origin, y_origin))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 20, True, True), \
            ooxcb.VoidCookie())

    def set_clip_region(self, region, x_origin, y_origin):
        gc = get_internal(self)
        region = get_internal(region)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", gc, region, x_origin, y_origin))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 20, True, False), \
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

class SelectionNotifyEvent(ooxcb.Event):
    event_name = "on_selection_notify"
    opcode = 0
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 0
        self.subtype = None
        self.window = None
        self.owner = None
        self.selection = None
        self.timestamp = None
        self.selection_timestamp = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIIIIIxxxxxxxx", stream)
        self.response_type = _unpacked[0]
        self.subtype = _unpacked[1]
        self.window = Window(self.conn, _unpacked[2])
        self.owner = Window(self.conn, _unpacked[3])
        self.selection = self.conn.atoms.get_by_id(_unpacked[4])
        self.timestamp = _unpacked[5]
        self.selection_timestamp = _unpacked[6]
        self.event_target = self.owner

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIIIIIxxxxxxxx", self.response_type, self.subtype, get_internal(self.window), get_internal(self.owner), get_internal(self.selection), self.timestamp, self.selection_timestamp))
        stream.write("\0" * (32 - (stream.tell() - root)))

class GetCursorImageAndNameReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.xhot = None
        self.yhot = None
        self.cursor_serial = None
        self.cursor_atom = None
        self.nbytes = None
        self.name = []
        self.cursor_image = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=xxxxxxxxhhHHHHIIHxx", stream)
        self.x = _unpacked[0]
        self.y = _unpacked[1]
        self.width = _unpacked[2]
        self.height = _unpacked[3]
        self.xhot = _unpacked[4]
        self.yhot = _unpacked[5]
        self.cursor_serial = _unpacked[6]
        self.cursor_atom = self.conn.atoms.get_by_id(_unpacked[7])
        self.nbytes = _unpacked[8]
        self.name = ooxcb.List(self.conn, stream, self.nbytes, 'B', 1).to_string()
        stream.seek(ooxcb.type_pad(4, stream.tell() - root), 1)
        self.cursor_image = ooxcb.List(self.conn, stream, (self.width * self.height), 'I', 4)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxhhHHHHIIHxx", self.x, self.y, self.width, self.height, self.xhot, self.yhot, self.cursor_serial, get_internal(self.cursor_atom), self.nbytes))
        count += 32
        build_list(self.conn, stream, self.name, 'B')
        build_list(self.conn, stream, self.cursor_image, 'I')

class GetCursorImageCookie(ooxcb.Cookie):
    pass

class GetCursorNameCookie(ooxcb.Cookie):
    pass

class GetCursorImageAndNameCookie(ooxcb.Cookie):
    pass

class CursorMixin(Mixin):
    target_class = Cursor
    def set_name_checked(self, name):
        if isinstance(name, unicode):
            name = name.encode("utf-8")
        nbytes = len(name)
        name = map(ord, name)
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 23, True, True), \
            ooxcb.VoidCookie())

    def set_name(self, name):
        if isinstance(name, unicode):
            name = name.encode("utf-8")
        nbytes = len(name)
        name = map(ord, name)
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 23, True, False), \
            ooxcb.VoidCookie())

    def change_checked(self, destination):
        source = get_internal(self)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", source, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 26, True, True), \
            ooxcb.VoidCookie())

    def change(self, destination):
        source = get_internal(self)
        destination = get_internal(destination)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", source, destination))
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 26, True, False), \
            ooxcb.VoidCookie())

    def change_by_name_checked(self, name):
        if isinstance(name, unicode):
            name = name.encode("utf-8")
        nbytes = len(name)
        name = map(ord, name)
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 27, True, True), \
            ooxcb.VoidCookie())

    def change_by_name(self, name):
        if isinstance(name, unicode):
            name = name.encode("utf-8")
        nbytes = len(name)
        name = map(ord, name)
        return self.conn.xfixes.send_request(ooxcb.Request(self.conn, buf.getvalue(), 27, True, False), \
            ooxcb.VoidCookie())

_events = {
    1: CursorNotifyEvent,
    0: SelectionNotifyEvent,
}

_errors = {
    0: (RegionError, BadRegion),
}

for ev in _events.itervalues():
    if isinstance(ev.event_target_class, str):
        ev.event_target_class = globals()[ev.event_target_class]

ooxcb._add_ext(key, xfixesExtension, _events, _errors)
def mixin():
    CursorMixin.mixin()
    PictureMixin.mixin()
    WindowMixin.mixin()
    GContextMixin.mixin()


