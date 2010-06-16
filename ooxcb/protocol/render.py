# auto generated. yay.
import ooxcb
from ooxcb.resource import get_internal
from ooxcb.types import SIZES, make_array, build_list
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
from struct import pack, unpack, calcsize
from ooxcb.protocol.xproto import Drawable, Screen
from ooxcb.util import Mixin

def unpack_from_stream(fmt, stream, offset=0):
    if offset:
        stream.seek(offset, 1)
    s = stream.read(calcsize(fmt))
    return unpack(fmt, s)


MAJOR_VERSION = 0
MINOR_VERSION = 10
key = ooxcb.ExtensionKey("RENDER")

class Repeat(object):
    _None = 0
    Normal = 1
    Pad = 2
    Reflect = 3

class PictOp(object):
    Clear = 0
    Src = 1
    Dst = 2
    Over = 3
    OverReverse = 4
    In = 5
    InReverse = 6
    Out = 7
    OutReverse = 8
    Atop = 9
    AtopReverse = 10
    Xor = 11
    Add = 12
    Saturate = 13
    DisjointClear = 16
    DisjointSrc = 15
    DisjointDst = 16
    DisjointOver = 17
    DisjointOverReverse = 18
    DisjointIn = 19
    DisjointInReverse = 20
    DisjointOut = 21
    DisjointOutReverse = 22
    DisjointAtop = 23
    DisjointAtopReverse = 24
    DisjointXor = 25
    ConjointClear = 32
    ConjointSrc = 27
    ConjointDst = 28
    ConjointOver = 29
    ConjointOverReverse = 30
    ConjointIn = 31
    ConjointInReverse = 32
    ConjointOut = 33
    ConjointOutReverse = 34
    ConjointAtop = 35
    ConjointAtopReverse = 36
    ConjointXor = 37

class PictType(object):
    Indexed = 0
    Direct = 1

class SubPixel(object):
    Unknown = 0
    HorizontalRGB = 1
    HorizontalBGR = 2
    VerticalRGB = 3
    VerticalBGR = 4
    _None = 5

class CP(object):
    Repeat = 1
    AlphaMap = 2
    AlphaXOrigin = 4
    AlphaYOrigin = 8
    ClipXOrigin = 16
    ClipYOrigin = 32
    ClipMask = 64
    GraphicsExposure = 128
    SubwindowMode = 256
    PolyEdge = 512
    PolyMode = 1024
    Dither = 2048
    ComponentAlpha = 4096

class PolyEdge(object):
    Sharp = 0
    Smooth = 1

class PolyMode(object):
    Precise = 0
    Imprecise = 1

class BadGlyph(ooxcb.ProtocolException):
    pass

class PictFormatError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)

    def read(self, stream):
        self._address = stream.address

    def build(self, stream):
        count = 0

class Directformat(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.red_shift = None
        self.red_mask = None
        self.green_shift = None
        self.green_mask = None
        self.blue_shift = None
        self.blue_mask = None
        self.alpha_shift = None
        self.alpha_mask = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=HHHHHHHH", stream)
        self.red_shift = _unpacked[0]
        self.red_mask = _unpacked[1]
        self.green_shift = _unpacked[2]
        self.green_mask = _unpacked[3]
        self.blue_shift = _unpacked[4]
        self.blue_mask = _unpacked[5]
        self.alpha_shift = _unpacked[6]
        self.alpha_mask = _unpacked[7]

    def build(self, stream):
        count = 0
        stream.write(pack("=HHHHHHHH", self.red_shift, self.red_mask, self.green_shift, self.green_mask, self.blue_shift, self.blue_mask, self.alpha_shift, self.alpha_mask))

class ScreenMixin(Mixin):
    target_class = Screen
    def get_render_pictformat(self):
        reply = self.conn.render.query_pict_formats().reply()
        screen_num = self.conn.setup.roots.index(self)
        render_screen = reply.screens[screen_num]
        for d in render_screen.depths:
            if d.depth == self.root_depth:
                for v in d.visuals:
                    if v.visual == self.root_visual:
                        return v.format
        raise Exception("Failed to find an appropriate Render pictformat!")

class GlyphSetError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)

    def read(self, stream):
        self._address = stream.address

    def build(self, stream):
        count = 0

class BadPicture(ooxcb.ProtocolException):
    pass

class QueryVersionCookie(ooxcb.Cookie):
    pass

class Pictdepth(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.depth = None
        self.num_visuals = None
        self.visuals = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=BxHxxxx", stream)
        self.depth = _unpacked[0]
        self.num_visuals = _unpacked[1]
        self.visuals = ooxcb.List(self.conn, stream, self.num_visuals, Pictvisual, 8)
        self.size = stream.tell() - root

    def build(self, stream):
        count = 0
        stream.write(pack("=BxHxxxx", self.depth, self.num_visuals))
        count += 8
        build_list(self.conn, stream, self.visuals, Pictvisual)

class PictureError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)

    def read(self, stream):
        self._address = stream.address

    def build(self, stream):
        count = 0

class Picture(ooxcb.Resource):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def change_checked(self, **values):
        value_mask, value_list = 0, []
        if "repeat" in values:
            value_mask |= 1
            value_list.append(values["repeat"])
        if "alpha_map" in values:
            value_mask |= 2
            value_list.append(get_internal(values["alpha_map"]))
        if "alpha_x_origin" in values:
            value_mask |= 4
            value_list.append(values["alpha_x_origin"])
        if "alpha_y_origin" in values:
            value_mask |= 8
            value_list.append(values["alpha_y_origin"])
        if "clip_x_origin" in values:
            value_mask |= 16
            value_list.append(values["clip_x_origin"])
        if "clip_y_origin" in values:
            value_mask |= 32
            value_list.append(values["clip_y_origin"])
        if "clip_mask" in values:
            value_mask |= 64
            value_list.append(get_internal(values["clip_mask"]))
        if "graphics_exposure" in values:
            value_mask |= 128
            value_list.append(values["graphics_exposure"])
        if "subwindow_mode" in values:
            value_mask |= 256
            value_list.append(values["subwindow_mode"])
        if "poly_edge" in values:
            value_mask |= 512
            value_list.append(values["poly_edge"])
        if "poly_mode" in values:
            value_mask |= 1024
            value_list.append(values["poly_mode"])
        if "dither" in values:
            value_mask |= 2048
            value_list.append(get_internal(values["dither"]))
        if "component_alpha" in values:
            value_mask |= 4096
            value_list.append(values["component_alpha"])
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", picture, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, True, True), \
            ooxcb.VoidCookie())

    def change(self, **values):
        value_mask, value_list = 0, []
        if "repeat" in values:
            value_mask |= 1
            value_list.append(values["repeat"])
        if "alpha_map" in values:
            value_mask |= 2
            value_list.append(get_internal(values["alpha_map"]))
        if "alpha_x_origin" in values:
            value_mask |= 4
            value_list.append(values["alpha_x_origin"])
        if "alpha_y_origin" in values:
            value_mask |= 8
            value_list.append(values["alpha_y_origin"])
        if "clip_x_origin" in values:
            value_mask |= 16
            value_list.append(values["clip_x_origin"])
        if "clip_y_origin" in values:
            value_mask |= 32
            value_list.append(values["clip_y_origin"])
        if "clip_mask" in values:
            value_mask |= 64
            value_list.append(get_internal(values["clip_mask"]))
        if "graphics_exposure" in values:
            value_mask |= 128
            value_list.append(values["graphics_exposure"])
        if "subwindow_mode" in values:
            value_mask |= 256
            value_list.append(values["subwindow_mode"])
        if "poly_edge" in values:
            value_mask |= 512
            value_list.append(values["poly_edge"])
        if "poly_mode" in values:
            value_mask |= 1024
            value_list.append(values["poly_mode"])
        if "dither" in values:
            value_mask |= 2048
            value_list.append(get_internal(values["dither"]))
        if "component_alpha" in values:
            value_mask |= 4096
            value_list.append(values["component_alpha"])
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", picture, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, True, False), \
            ooxcb.VoidCookie())

    def set_clip_rectangles_checked(self, clip_x_origin, clip_y_origin, rectangles):
        rectangles_len = len(rectangles)
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIhh", picture, clip_x_origin, clip_y_origin))
        for elt in rectangles:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 6, True, True), \
            ooxcb.VoidCookie())

    def set_clip_rectangles(self, clip_x_origin, clip_y_origin, rectangles):
        rectangles_len = len(rectangles)
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIhh", picture, clip_x_origin, clip_y_origin))
        for elt in rectangles:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 6, True, False), \
            ooxcb.VoidCookie())

    def free_checked(self):
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 7, True, True), \
            ooxcb.VoidCookie())

    def free(self):
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 7, True, False), \
            ooxcb.VoidCookie())

    def composite_checked(self, op, mask, dst, width, height, src_x=0, src_y=0, mask_x=0, mask_y=0, dst_x=0, dst_y=0):
        src = get_internal(self)
        mask = get_internal(mask)
        dst = get_internal(dst)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIhhhhhhHH", op, src, mask, dst, src_x, src_y, mask_x, mask_y, dst_x, dst_y, width, height))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 8, True, True), \
            ooxcb.VoidCookie())

    def composite(self, op, mask, dst, width, height, src_x=0, src_y=0, mask_x=0, mask_y=0, dst_x=0, dst_y=0):
        src = get_internal(self)
        mask = get_internal(mask)
        dst = get_internal(dst)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIhhhhhhHH", op, src, mask, dst, src_x, src_y, mask_x, mask_y, dst_x, dst_y, width, height))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 8, True, False), \
            ooxcb.VoidCookie())

    def trapezoids_checked(self, op, dst, traps, mask_format=None, src_x=0, src_y=0):
        traps_len = len(traps)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIhh", op, src, dst, mask_format, src_x, src_y))
        for elt in traps:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 10, True, True), \
            ooxcb.VoidCookie())

    def trapezoids(self, op, dst, traps, mask_format=None, src_x=0, src_y=0):
        traps_len = len(traps)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIhh", op, src, dst, mask_format, src_x, src_y))
        for elt in traps:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 10, True, False), \
            ooxcb.VoidCookie())

    def triangles_checked(self, op, dst, triangles, mask_format=None, src_x=0, src_y=0):
        triangles_len = len(triangles)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIhh", op, src, dst, mask_format, src_x, src_y))
        for elt in triangles:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 11, True, True), \
            ooxcb.VoidCookie())

    def triangles(self, op, dst, triangles, mask_format=None, src_x=0, src_y=0):
        triangles_len = len(triangles)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIhh", op, src, dst, mask_format, src_x, src_y))
        for elt in triangles:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 11, True, False), \
            ooxcb.VoidCookie())

    def tri_strip_checked(self, op, dst, points, mask_format=None, src_x=0, src_y=0):
        points_len = len(points)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIhh", op, src, dst, mask_format, src_x, src_y))
        for elt in points:
            buf.write(pack("=ii", *elt))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 12, True, True), \
            ooxcb.VoidCookie())

    def tri_strip(self, op, dst, points, mask_format=None, src_x=0, src_y=0):
        points_len = len(points)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIhh", op, src, dst, mask_format, src_x, src_y))
        for elt in points:
            buf.write(pack("=ii", *elt))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 12, True, False), \
            ooxcb.VoidCookie())

    def tri_fan_checked(self, op, dst, points, mask_format=None, src_x=0, src_y=0):
        points_len = len(points)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIhh", op, src, dst, mask_format, src_x, src_y))
        for elt in points:
            buf.write(pack("=ii", *elt))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 13, True, True), \
            ooxcb.VoidCookie())

    def tri_fan(self, op, dst, points, mask_format=None, src_x=0, src_y=0):
        points_len = len(points)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIhh", op, src, dst, mask_format, src_x, src_y))
        for elt in points:
            buf.write(pack("=ii", *elt))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 13, True, False), \
            ooxcb.VoidCookie())

    def composite_glyphs8_checked(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0):
        glyphcmds_len = len(glyphcmds)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        glyphset = get_internal(glyphset)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIIhh", op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(make_array(glyphcmds, "B"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 23, True, True), \
            ooxcb.VoidCookie())

    def composite_glyphs8(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0):
        glyphcmds_len = len(glyphcmds)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        glyphset = get_internal(glyphset)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIIhh", op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(make_array(glyphcmds, "B"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 23, True, False), \
            ooxcb.VoidCookie())

    def composite_glyphs16_checked(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0):
        glyphcmds_len = len(glyphcmds)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        glyphset = get_internal(glyphset)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIIhh", op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(make_array(glyphcmds, "B"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 24, True, True), \
            ooxcb.VoidCookie())

    def composite_glyphs16(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0):
        glyphcmds_len = len(glyphcmds)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        glyphset = get_internal(glyphset)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIIhh", op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(make_array(glyphcmds, "B"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 24, True, False), \
            ooxcb.VoidCookie())

    def composite_glyphs32_checked(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0):
        glyphcmds_len = len(glyphcmds)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        glyphset = get_internal(glyphset)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIIhh", op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(make_array(glyphcmds, "B"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 25, True, True), \
            ooxcb.VoidCookie())

    def composite_glyphs32(self, op, dst, glyphset, glyphcmds, mask_format=None, src_x=0, src_y=0):
        glyphcmds_len = len(glyphcmds)
        src = get_internal(self)
        dst = get_internal(dst)
        mask_format = get_internal(mask_format)
        glyphset = get_internal(glyphset)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxIIIIhh", op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(make_array(glyphcmds, "B"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 25, True, False), \
            ooxcb.VoidCookie())

    def fill_rectangles_checked(self, op, color, rects):
        rects_len = len(rects)
        dst = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxI", op, dst))
        color.build(buf)
        for elt in rects:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 26, True, True), \
            ooxcb.VoidCookie())

    def fill_rectangles(self, op, color, rects):
        rects_len = len(rects)
        dst = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBxxxI", op, dst))
        color.build(buf)
        for elt in rects:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 26, True, False), \
            ooxcb.VoidCookie())

    def set_transform_checked(self, transform):
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        transform.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 28, True, True), \
            ooxcb.VoidCookie())

    def set_transform(self, transform):
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        transform.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 28, True, False), \
            ooxcb.VoidCookie())

    def set_filter_checked(self, filter, values):
        filter_len = len(filter)
        values_len = len(values)
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHxx", picture, filter_len))
        buf.write(make_array(filter, "B"))
        buf.write(make_array(values, "i"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 30, True, True), \
            ooxcb.VoidCookie())

    def set_filter(self, filter, values):
        filter_len = len(filter)
        values_len = len(values)
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHxx", picture, filter_len))
        buf.write(make_array(filter, "B"))
        buf.write(make_array(values, "i"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 30, True, False), \
            ooxcb.VoidCookie())

    def add_traps_checked(self, traps, x_off=0, y_off=0):
        traps_len = len(traps)
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIhh", picture, x_off, y_off))
        for elt in traps:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 32, True, True), \
            ooxcb.VoidCookie())

    def add_traps(self, traps, x_off=0, y_off=0):
        traps_len = len(traps)
        picture = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIhh", picture, x_off, y_off))
        for elt in traps:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 32, True, False), \
            ooxcb.VoidCookie())

    @classmethod
    def create(cls, conn, drawable, format, **values):
        pid = conn.generate_id()
        pict = cls(conn, pid)
        value_mask, value_list = 0, []
        if "repeat" in values:
            value_mask |= 1
            value_list.append(values["repeat"])
        if "alpha_map" in values:
            value_mask |= 2
            value_list.append(get_internal(values["alpha_map"]))
        if "alpha_x_origin" in values:
            value_mask |= 4
            value_list.append(values["alpha_x_origin"])
        if "alpha_y_origin" in values:
            value_mask |= 8
            value_list.append(values["alpha_y_origin"])
        if "clip_x_origin" in values:
            value_mask |= 16
            value_list.append(values["clip_x_origin"])
        if "clip_y_origin" in values:
            value_mask |= 32
            value_list.append(values["clip_y_origin"])
        if "clip_mask" in values:
            value_mask |= 64
            value_list.append(get_internal(values["clip_mask"]))
        if "graphics_exposure" in values:
            value_mask |= 128
            value_list.append(values["graphics_exposure"])
        if "subwindow_mode" in values:
            value_mask |= 256
            value_list.append(values["subwindow_mode"])
        if "poly_edge" in values:
            value_mask |= 512
            value_list.append(values["poly_edge"])
        if "poly_mode" in values:
            value_mask |= 1024
            value_list.append(values["poly_mode"])
        if "dither" in values:
            value_mask |= 2048
            value_list.append(get_internal(values["dither"]))
        if "component_alpha" in values:
            value_mask |= 4096
            value_list.append(values["component_alpha"])
        conn.render.create_picture_checked(pict, drawable, format, value_mask, value_list).check()
        conn.add_to_cache(pid, pict)
        return pict

    @classmethod
    def create_solid_fill(cls, conn, color):
        pid = conn.generate_id()
        pict = cls(conn, pid)
        conn.render.create_solid_fill_checked(pict, color).check()
        conn.add_to_cache(pid, pict)
        return pict

    @classmethod
    def create_linear_gradient(cls, p1, p2, num_stops, stops, colors):
        pid = conn.generate_id()
        pict = cls(conn, pid)
        conn.render.create_linear_gradient_checked(pict, p1, p2, num_stops, stops, colors).check()
        conn.add_to_cache(pid, pict)
        return pict

    @classmethod
    def create_radial_gradient(cls, p1, p2, num_stops, stops, colors):
        pid = conn.generate_id()
        pict = cls(conn, pid)
        conn.render.create_radial_gradient_checked(pict, inner, outer, inner_radius, outer_radius, num_stops, stops, colors).check()
        conn.add_to_cache(pid, pict)
        return pict

    @classmethod
    def create_conical_gradient(cls, center, angle, num_stops, stops, colors):
        pid = conn.generate_id()
        pict = cls(conn, pid)
        conn.render.create_conical_gradient_checked(pict,p1, p2, num_stops, stops, colors).check()
        conn.add_to_cache(pid, pict)
        return pict

class Triangle(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.p1 = None
        self.p2 = None
        self.p3 = None

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        self.p1 = Pointfix.create_from_stream(self.conn, stream)
        stream.seek(ooxcb.type_pad(8, stream.tell() - root), 1)
        self.p2 = Pointfix.create_from_stream(self.conn, stream)
        stream.seek(ooxcb.type_pad(8, stream.tell() - root), 1)
        self.p3 = Pointfix.create_from_stream(self.conn, stream)

    def build(self, stream):
        count = 0
        self.p1.build(stream)
        self.p2.build(stream)
        self.p3.build(stream)

class Glyphset(ooxcb.Resource):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def reference_checked(self, existing):
        gsid = get_internal(self)
        existing = get_internal(existing)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", gsid, existing))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 18, True, True), \
            ooxcb.VoidCookie())

    def reference(self, existing):
        gsid = get_internal(self)
        existing = get_internal(existing)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", gsid, existing))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 18, True, False), \
            ooxcb.VoidCookie())

    def free_checked(self):
        glyphset = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", glyphset))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 19, True, True), \
            ooxcb.VoidCookie())

    def free(self):
        glyphset = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", glyphset))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 19, True, False), \
            ooxcb.VoidCookie())

    def add_glyphs_checked(self, glyphids, glyphs, data):
        glyphs_len = len(glyphs)
        data_len = len(data)
        glyphset = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", glyphset, glyphs_len))
        buf.write(make_array(glyphids, "I"))
        for elt in glyphs:
            elt.build(buf)
        buf.write(make_array(data, "B"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 20, True, True), \
            ooxcb.VoidCookie())

    def add_glyphs(self, glyphids, glyphs, data):
        glyphs_len = len(glyphs)
        data_len = len(data)
        glyphset = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", glyphset, glyphs_len))
        buf.write(make_array(glyphids, "I"))
        for elt in glyphs:
            elt.build(buf)
        buf.write(make_array(data, "B"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 20, True, False), \
            ooxcb.VoidCookie())

    def free_glyphs_checked(self, glyphs):
        glyphs_len = len(glyphs)
        glyphset = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", glyphset))
        buf.write(make_array(glyphs, "I"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 22, True, True), \
            ooxcb.VoidCookie())

    def free_glyphs(self, glyphs):
        glyphs_len = len(glyphs)
        glyphset = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", glyphset))
        buf.write(make_array(glyphs, "I"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 22, True, False), \
            ooxcb.VoidCookie())

class Pictvisual(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.visual = None
        self.format = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=II", stream)
        self.visual = _unpacked[0]
        self.format = self.conn.get_from_cache_fallback(_unpacked[1], Pictformat)

    def build(self, stream):
        count = 0
        stream.write(pack("=II", self.visual, get_internal(self.format)))

class Spanfix(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.l = None
        self.r = None
        self.y = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=iii", stream)
        self.l = _unpacked[0]
        self.r = _unpacked[1]
        self.y = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=iii", self.l, self.r, self.y))

class DrawableMixin(Mixin):
    target_class = Drawable
    def query_filters(self):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", drawable))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 29, False, True), \
            QueryFiltersCookie(),
            QueryFiltersReply)

    def query_filters_unchecked(self):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", drawable))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 29, False, False), \
            QueryFiltersCookie(),
            QueryFiltersReply)

class Pictscreen(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.num_depths = None
        self.fallback = None
        self.depths = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=II", stream)
        self.num_depths = _unpacked[0]
        self.fallback = self.conn.get_from_cache_fallback(_unpacked[1], Pictformat)
        self.depths = ooxcb.List(self.conn, stream, self.num_depths, Pictdepth, -1)
        self.size = stream.tell() - root

    def build(self, stream):
        count = 0
        stream.write(pack("=II", self.num_depths, get_internal(self.fallback)))
        count += 8
        build_list(self.conn, stream, self.depths, Pictdepth)

class Animcursorelt(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.cursor = None
        self.delay = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=II", stream)
        self.cursor = self.conn.get_from_cache_fallback(_unpacked[0], CURSOR)
        self.delay = _unpacked[1]

    def build(self, stream):
        count = 0
        stream.write(pack("=II", get_internal(self.cursor), self.delay))

class GlyphSet(object):
    @classmethod
    def create(cls, conn, format):
        gsid = conn.generate_id()
        gs = cls(conn, gsid)
        conn.render.create_glyph_set_checked(gs, format).check()
        conn.add_to_cache(gsid, gs)
        return gs

class renderExtension(ooxcb.Extension):
    header = "render"
    def query_version(self, client_major_version, client_minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", client_major_version, client_minor_version))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, True), \
            QueryVersionCookie(),
            QueryVersionReply)

    def query_version_unchecked(self, client_major_version, client_minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", client_major_version, client_minor_version))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, False), \
            QueryVersionCookie(),
            QueryVersionReply)

    def query_pict_formats(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, False, True), \
            QueryPictFormatsCookie(),
            QueryPictFormatsReply)

    def query_pict_formats_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, False, False), \
            QueryPictFormatsCookie(),
            QueryPictFormatsReply)

    def create_picture_checked(self, pid, drawable, format, value_mask, value_list):
        pid = get_internal(pid)
        drawable = get_internal(drawable)
        format = get_internal(format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIII", pid, drawable, format, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, True), \
            ooxcb.VoidCookie())

    def create_picture(self, pid, drawable, format, value_mask, value_list):
        pid = get_internal(pid)
        drawable = get_internal(drawable)
        format = get_internal(format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIII", pid, drawable, format, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, False), \
            ooxcb.VoidCookie())

    def create_glyph_set_checked(self, gsid, format):
        gsid = get_internal(gsid)
        format = get_internal(format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", gsid, format))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 17, True, True), \
            ooxcb.VoidCookie())

    def create_glyph_set(self, gsid, format):
        gsid = get_internal(gsid)
        format = get_internal(format)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", gsid, format))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 17, True, False), \
            ooxcb.VoidCookie())

    def create_cursor_checked(self, cid, source, x, y):
        source = get_internal(source)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIHH", cid, source, x, y))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 27, True, True), \
            ooxcb.VoidCookie())

    def create_cursor(self, cid, source, x, y):
        source = get_internal(source)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIHH", cid, source, x, y))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 27, True, False), \
            ooxcb.VoidCookie())

    def create_anim_cursor_checked(self, cid, cursors):
        cursors_len = len(cursors)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cid))
        for elt in cursors:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 31, True, True), \
            ooxcb.VoidCookie())

    def create_anim_cursor(self, cid, cursors):
        cursors_len = len(cursors)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cid))
        for elt in cursors:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 31, True, False), \
            ooxcb.VoidCookie())

    def create_solid_fill_checked(self, picture, color):
        picture = get_internal(picture)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        color.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 33, True, True), \
            ooxcb.VoidCookie())

    def create_solid_fill(self, picture, color):
        picture = get_internal(picture)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        color.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 33, True, False), \
            ooxcb.VoidCookie())

    def create_linear_gradient_checked(self, picture, p1, p2, num_stops, stops, colors):
        picture = get_internal(picture)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        for elt in p1:
            buf.write(pack("=ii", *elt))
        for elt in p2:
            buf.write(pack("=ii", *elt))
        buf.write(pack("=I", num_stops))
        buf.write(make_array(stops, "i"))
        for elt in colors:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 34, True, True), \
            ooxcb.VoidCookie())

    def create_linear_gradient(self, picture, p1, p2, num_stops, stops, colors):
        picture = get_internal(picture)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        for elt in p1:
            buf.write(pack("=ii", *elt))
        for elt in p2:
            buf.write(pack("=ii", *elt))
        buf.write(pack("=I", num_stops))
        buf.write(make_array(stops, "i"))
        for elt in colors:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 34, True, False), \
            ooxcb.VoidCookie())

    def create_radial_gradient_checked(self, picture, inner, outer, inner_radius, outer_radius, num_stops, stops, colors):
        picture = get_internal(picture)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        for elt in inner:
            buf.write(pack("=ii", *elt))
        for elt in outer:
            buf.write(pack("=ii", *elt))
        buf.write(pack("=iiI", inner_radius, outer_radius, num_stops))
        buf.write(make_array(stops, "i"))
        for elt in colors:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 35, True, True), \
            ooxcb.VoidCookie())

    def create_radial_gradient(self, picture, inner, outer, inner_radius, outer_radius, num_stops, stops, colors):
        picture = get_internal(picture)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        for elt in inner:
            buf.write(pack("=ii", *elt))
        for elt in outer:
            buf.write(pack("=ii", *elt))
        buf.write(pack("=iiI", inner_radius, outer_radius, num_stops))
        buf.write(make_array(stops, "i"))
        for elt in colors:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 35, True, False), \
            ooxcb.VoidCookie())

    def create_conical_gradient_checked(self, picture, center, angle, num_stops, stops, colors):
        picture = get_internal(picture)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        for elt in center:
            buf.write(pack("=ii", *elt))
        buf.write(pack("=iI", angle, num_stops))
        buf.write(make_array(stops, "i"))
        for elt in colors:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 36, True, True), \
            ooxcb.VoidCookie())

    def create_conical_gradient(self, picture, center, angle, num_stops, stops, colors):
        picture = get_internal(picture)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", picture))
        for elt in center:
            buf.write(pack("=ii", *elt))
        buf.write(pack("=iI", angle, num_stops))
        buf.write(make_array(stops, "i"))
        for elt in colors:
            elt.build(buf)
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 36, True, False), \
            ooxcb.VoidCookie())

class Pictforminfo(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.id = None
        self.type = None
        self.depth = None
        self.direct = None
        self.colormap = None

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=IBBxx", stream)
        self.id = self.conn.get_from_cache_fallback(_unpacked[0], Pictformat)
        self.type = _unpacked[1]
        self.depth = _unpacked[2]
        self.direct = Directformat.create_from_stream(self.conn, stream)
        stream.seek(ooxcb.type_pad(4, stream.tell() - root), 1)
        _unpacked = unpack_from_stream("=I", stream)
        self.colormap = _unpacked[0]

    def build(self, stream):
        count = 0
        stream.write(pack("=IBBxx", get_internal(self.id), self.type, self.depth))
        count += 8
        self.direct.build(stream)
        stream.write(pack("=I", self.colormap))

class BadGlyphSet(ooxcb.ProtocolException):
    pass

class Pointfix(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.x = None
        self.y = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=ii", stream)
        self.x = _unpacked[0]
        self.y = _unpacked[1]

    def build(self, stream):
        count = 0
        stream.write(pack("=ii", self.x, self.y))

class BadPictFormat(ooxcb.ProtocolException):
    pass

class Indexvalue(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.pixel = None
        self.red = None
        self.green = None
        self.blue = None
        self.alpha = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=IHHHH", stream)
        self.pixel = _unpacked[0]
        self.red = _unpacked[1]
        self.green = _unpacked[2]
        self.blue = _unpacked[3]
        self.alpha = _unpacked[4]

    def build(self, stream):
        count = 0
        stream.write(pack("=IHHHH", self.pixel, self.red, self.green, self.blue, self.alpha))

class Cursor(object):
    @classmethod
    def create(cls, conn, source, x=0, y=0):
        cid = conn.generate_id()
        cursor = cls(conn, cid)
        conn.render.create_cursor_checked(cursor, source, x, y).check()
        conn.add_to_cache(cid, cursor)
        return cursor

    @classmethod
    def create_anim(cls, cursors):
        cid = conn.generate_id()
        cursor = cls(conn, cid)
        conn.render.create_anim_cursor_checked(cursor, cursors).check()
        conn.add_to_cache(cid, cursor)
        return cursor

class QueryPictIndexValuesReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.num_values = None
        self.values = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxIxxxxxxxxxxxxxxxxxxxx", stream)
        self.num_values = _unpacked[0]
        self.values = ooxcb.List(self.conn, stream, self.num_values, Indexvalue, 12)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxIxxxxxxxxxxxxxxxxxxxx", self.num_values))
        count += 32
        build_list(self.conn, stream, self.values, Indexvalue)

class QueryFiltersReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.num_aliases = None
        self.num_filters = None
        self.aliases = []
        self.filters = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=xxxxxxxxIIxxxxxxxxxxxxxxxx", stream)
        self.num_aliases = _unpacked[0]
        self.num_filters = _unpacked[1]
        self.aliases = ooxcb.List(self.conn, stream, self.num_aliases, 'H', 2)
        stream.seek(ooxcb.type_pad(4, stream.tell() - root), 1)
        self.filters = ooxcb.List(self.conn, stream, self.num_filters, STR, -1)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxIIxxxxxxxxxxxxxxxx", self.num_aliases, self.num_filters))
        count += 32
        build_list(self.conn, stream, self.aliases, 'H')
        build_list(self.conn, stream, self.filters, STR)

class Linefix(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.p1 = None
        self.p2 = None

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        self.p1 = Pointfix.create_from_stream(self.conn, stream)
        stream.seek(ooxcb.type_pad(8, stream.tell() - root), 1)
        self.p2 = Pointfix.create_from_stream(self.conn, stream)

    def build(self, stream):
        count = 0
        self.p1.build(stream)
        self.p2.build(stream)

class Trapezoid(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=ii", stream)
        self.top = _unpacked[0]
        self.bottom = _unpacked[1]
        self.left = Linefix.create_from_stream(self.conn, stream)
        stream.seek(ooxcb.type_pad(16, stream.tell() - root), 1)
        self.right = Linefix.create_from_stream(self.conn, stream)

    def build(self, stream):
        count = 0
        stream.write(pack("=ii", self.top, self.bottom))
        count += 8
        self.left.build(stream)
        self.right.build(stream)

class Trap(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.top = None
        self.bot = None

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        self.top = Spanfix.create_from_stream(self.conn, stream)
        stream.seek(ooxcb.type_pad(12, stream.tell() - root), 1)
        self.bot = Spanfix.create_from_stream(self.conn, stream)

    def build(self, stream):
        count = 0
        self.top.build(stream)
        self.bot.build(stream)

class QueryPictIndexValuesCookie(ooxcb.Cookie):
    pass

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

class PictOpError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)

    def read(self, stream):
        self._address = stream.address

    def build(self, stream):
        count = 0

class Glyphinfo(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.width = None
        self.height = None
        self.x = None
        self.y = None
        self.x_off = None
        self.y_off = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=HHhhhh", stream)
        self.width = _unpacked[0]
        self.height = _unpacked[1]
        self.x = _unpacked[2]
        self.y = _unpacked[3]
        self.x_off = _unpacked[4]
        self.y_off = _unpacked[5]

    def build(self, stream):
        count = 0
        stream.write(pack("=HHhhhh", self.width, self.height, self.x, self.y, self.x_off, self.y_off))

class QueryPictFormatsCookie(ooxcb.Cookie):
    pass

class Color(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.red = None
        self.green = None
        self.blue = None
        self.alpha = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=HHHH", stream)
        self.red = _unpacked[0]
        self.green = _unpacked[1]
        self.blue = _unpacked[2]
        self.alpha = _unpacked[3]

    def build(self, stream):
        count = 0
        stream.write(pack("=HHHH", self.red, self.green, self.blue, self.alpha))

    @classmethod
    def create(cls, conn, red, green, blue, alpha):
        self = cls(conn)
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
        return self

class BadPictOp(ooxcb.ProtocolException):
    pass

class GlyphError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)

    def read(self, stream):
        self._address = stream.address

    def build(self, stream):
        count = 0

class Transform(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.matrix11 = None
        self.matrix12 = None
        self.matrix13 = None
        self.matrix21 = None
        self.matrix22 = None
        self.matrix23 = None
        self.matrix31 = None
        self.matrix32 = None
        self.matrix33 = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=iiiiiiiii", stream)
        self.matrix11 = _unpacked[0]
        self.matrix12 = _unpacked[1]
        self.matrix13 = _unpacked[2]
        self.matrix21 = _unpacked[3]
        self.matrix22 = _unpacked[4]
        self.matrix23 = _unpacked[5]
        self.matrix31 = _unpacked[6]
        self.matrix32 = _unpacked[7]
        self.matrix33 = _unpacked[8]

    def build(self, stream):
        count = 0
        stream.write(pack("=iiiiiiiii", self.matrix11, self.matrix12, self.matrix13, self.matrix21, self.matrix22, self.matrix23, self.matrix31, self.matrix32, self.matrix33))

class Pictformat(ooxcb.Resource):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def query_pict_index_values(self):
        format = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", format))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, False, True), \
            QueryPictIndexValuesCookie(),
            QueryPictIndexValuesReply)

    def query_pict_index_values_unchecked(self):
        format = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", format))
        return self.conn.render.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, False, False), \
            QueryPictIndexValuesCookie(),
            QueryPictIndexValuesReply)

class QueryFiltersCookie(ooxcb.Cookie):
    pass

class QueryPictFormatsReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.num_formats = None
        self.num_screens = None
        self.num_depths = None
        self.num_visuals = None
        self.num_subpixel = None
        self.formats = []
        self.screens = []
        self.subpixels = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=xxxxxxxxIIIIIxxxx", stream)
        self.num_formats = _unpacked[0]
        self.num_screens = _unpacked[1]
        self.num_depths = _unpacked[2]
        self.num_visuals = _unpacked[3]
        self.num_subpixel = _unpacked[4]
        self.formats = ooxcb.List(self.conn, stream, self.num_formats, Pictforminfo, 28)
        stream.seek(ooxcb.type_pad(4, stream.tell() - root), 1)
        self.screens = ooxcb.List(self.conn, stream, self.num_screens, Pictscreen, -1)
        stream.seek(ooxcb.type_pad(4, stream.tell() - root), 1)
        self.subpixels = ooxcb.List(self.conn, stream, self.num_subpixel, 'I', 4)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxIIIIIxxxx", self.num_formats, self.num_screens, self.num_depths, self.num_visuals, self.num_subpixel))
        count += 32
        build_list(self.conn, stream, self.formats, Pictforminfo)
        build_list(self.conn, stream, self.screens, Pictscreen)
        build_list(self.conn, stream, self.subpixels, 'I')

class Glyph(ooxcb.Resource):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

_events = {
}

_errors = {
    1: (PictureError, BadPicture),
    0: (PictFormatError, BadPictFormat),
    3: (GlyphSetError, BadGlyphSet),
    2: (PictOpError, BadPictOp),
    4: (GlyphError, BadGlyph),
}

for ev in _events.itervalues():
    if isinstance(ev.event_target_class, str):
        ev.event_target_class = globals()[ev.event_target_class]

ooxcb._add_ext(key, renderExtension, _events, _errors)
def mixin():
    DrawableMixin.mixin()
    ScreenMixin.mixin()


