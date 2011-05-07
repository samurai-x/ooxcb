# auto generated. yay.
import ooxcb
from ooxcb.resource import get_internal
from ooxcb.types import SIZES, make_array, build_list
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
from struct import pack, unpack, calcsize
from ooxcb.types import make_void_array
from ooxcb.util import cached_property

def unpack_from_stream(fmt, stream, offset=0):
    if offset:
        stream.seek(offset, 1)
    s = stream.read(calcsize(fmt))
    return unpack(fmt, s)

class Drawable(ooxcb.Resource):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def get_geometry(self):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", drawable))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 14, False, True), \
            GetGeometryCookie(),
            GetGeometryReply)

    def get_geometry_unchecked(self):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", drawable))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 14, False, False), \
            GetGeometryCookie(),
            GetGeometryReply)

    def get_image(self, format, x, y, width, height, plane_mask):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIhhHHI", format, drawable, x, y, width, height, plane_mask))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 73, False, True), \
            GetImageCookie(),
            GetImageReply)

    def get_image_unchecked(self, format, x, y, width, height, plane_mask):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIhhHHI", format, drawable, x, y, width, height, plane_mask))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 73, False, False), \
            GetImageCookie(),
            GetImageReply)

    def query_best_size(self, _class, width, height):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHH", _class, drawable, width, height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 97, False, True), \
            QueryBestSizeCookie(),
            QueryBestSizeReply)

    def query_best_size_unchecked(self, _class, width, height):
        drawable = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHH", _class, drawable, width, height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 97, False, False), \
            QueryBestSizeCookie(),
            QueryBestSizeReply)

class PropMode(object):
    Replace = 0
    Prepend = 1
    Append = 2

class HostMode(object):
    Insert = 0
    Delete = 1

class FontDraw(object):
    LeftToRight = 0
    RightToLeft = 1

class VisualClass(object):
    StaticGray = 0
    GrayScale = 1
    StaticColor = 2
    PseudoColor = 3
    TrueColor = 4
    DirectColor = 5

class Exposures(object):
    NotAllowed = 0
    Allowed = 1
    Default = 2

class ButtonIndex(object):
    Any = 0
    _1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5

class ConfigWindow(object):
    X = 1
    Y = 2
    Width = 4
    Height = 8
    BorderWidth = 16
    Sibling = 32
    StackMode = 64

class GetPropertyType(object):
    Any = 0

class AccessControl(object):
    Disable = 0
    Enable = 1

class Blanking(object):
    NotPreferred = 0
    Preferred = 1
    Default = 2

class QueryShapeOf(object):
    LargestCursor = 0
    FastestTile = 1
    FastestStipple = 2

class WindowClass(object):
    CopyFromParent = 0
    InputOutput = 1
    InputOnly = 2

class GX(object):
    clear = 0
    _and = 1
    andReverse = 2
    copy = 3
    andInverted = 4
    noop = 5
    xor = 6
    _or = 7
    nor = 8
    equiv = 9
    invert = 10
    orReverse = 11
    copyInverted = 12
    orInverted = 13
    nand = 14
    set = 15

class Motion(object):
    Normal = 0
    Hint = 1

class GC(object):
    Function = 1
    PlaneMask = 2
    Foreground = 4
    Background = 8
    LineWidth = 16
    LineStyle = 32
    CapStyle = 64
    JoinStyle = 128
    FillStyle = 256
    FillRule = 512
    Tile = 1024
    Stipple = 2048
    TileStippleOriginX = 4096
    TileStippleOriginY = 8192
    Font = 16384
    SubwindowMode = 32768
    GraphicsExposures = 65536
    ClipOriginX = 131072
    ClipOriginY = 262144
    ClipMask = 524288
    DashOffset = 1048576
    DashList = 2097152
    ArcMode = 4194304

class Kill(object):
    AllTemporary = 0

class CapStyle(object):
    NotLast = 0
    Butt = 1
    Round = 2
    Projecting = 3

class FillRule(object):
    EvenOdd = 0
    Winding = 1

class GrabMode(object):
    Sync = 0
    Async = 1

class ColormapAlloc(object):
    _None = 0
    All = 1

class ModMask(object):
    Shift = 1
    Lock = 2
    Control = 4
    _1 = 8
    _2 = 16
    _3 = 32
    _4 = 64
    _5 = 128
    Any = 32768

class Visibility(object):
    Unobscured = 0
    PartiallyObscured = 1
    FullyObscured = 2

class FillStyle(object):
    Solid = 0
    Tiled = 1
    Stippled = 2
    OpaqueStippled = 3

class LedMode(object):
    Off = 0
    On = 1

class SubwindowMode(object):
    ClipByChildren = 0
    IncludeInferiors = 1

class Circulate(object):
    RaiseLowest = 0
    LowerHighest = 1

class AutoRepeatMode(object):
    Off = 0
    On = 1
    Default = 2

class BackingStore(object):
    NotUseful = 0
    WhenMapped = 1
    Always = 2

class StackMode(object):
    Above = 0
    Below = 1
    TopIf = 2
    BottomIf = 3
    Opposite = 4

class ArcMode(object):
    Chord = 0
    PieSlice = 1

class BackPixmap(object):
    _None = 0
    ParentRelative = 1

class Place(object):
    OnTop = 0
    OnBottom = 1

class Grab(object):
    Any = 0

class Property(object):
    NewValue = 0
    Delete = 1

class MappingStatus(object):
    Success = 0
    Busy = 1
    Failure = 2

class KeyButMask(object):
    Shift = 1
    Lock = 2
    Control = 4
    Mod1 = 8
    Mod2 = 16
    Mod3 = 32
    Mod4 = 64
    Mod5 = 128
    Button1 = 256
    Button2 = 512
    Button3 = 1024
    Button4 = 2048
    Button5 = 4096

class ColormapState(object):
    Uninstalled = 0
    Installed = 1

class ColorFlag(object):
    Red = 1
    Green = 2
    Blue = 4

class Allow(object):
    AsyncPointer = 0
    SyncPointer = 1
    ReplayPointer = 2
    AsyncKeyboard = 3
    SyncKeyboard = 4
    ReplayKeyboard = 5
    AsyncBoth = 6
    SyncBoth = 7

class NotifyDetail(object):
    Ancestor = 0
    Virtual = 1
    Inferior = 2
    Nonlinear = 3
    NonlinearVirtual = 4
    Pointer = 5
    PointerRoot = 6
    _None = 7

class ClipOrdering(object):
    Unsorted = 0
    YSorted = 1
    YXSorted = 2
    YXBanded = 3

class ImageOrder(object):
    LSBFirst = 0
    MSBFirst = 1

class MapIndex(object):
    Shift = 0
    Lock = 1
    Control = 2
    _1 = 3
    _2 = 4
    _3 = 5
    _4 = 6
    _5 = 7

class JoinStyle(object):
    Miter = 0
    Round = 1
    Bevel = 2

class Gravity(object):
    BitForget = 0
    WinUnmap = 0
    NorthWest = 1
    North = 2
    NorthEast = 3
    West = 4
    Center = 5
    East = 6
    SouthWest = 7
    South = 8
    SouthEast = 9
    Static = 10

class Time(object):
    CurrentTime = 0

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

class KB(object):
    KeyClickPercent = 1
    BellPercent = 2
    BellPitch = 4
    BellDuration = 8
    Led = 16
    LedMode = 32
    Key = 64
    AutoRepeatMode = 128

class Family(object):
    Internet = 0
    DECnet = 1
    Chaos = 2
    ServerInterpreted = 5
    Internet6 = 6

class EventMask(object):
    NoEvent = 0
    KeyPress = 1
    KeyRelease = 2
    ButtonPress = 4
    ButtonRelease = 8
    EnterWindow = 16
    LeaveWindow = 32
    PointerMotion = 64
    PointerMotionHint = 128
    Button1Motion = 256
    Button2Motion = 512
    Button3Motion = 1024
    Button4Motion = 2048
    Button5Motion = 4096
    ButtonMotion = 8192
    KeymapState = 16384
    Exposure = 32768
    VisibilityChange = 65536
    StructureNotify = 131072
    ResizeRedirect = 262144
    SubstructureNotify = 524288
    SubstructureRedirect = 1048576
    FocusChange = 2097152
    PropertyChange = 4194304
    ColorMapChange = 8388608
    OwnerGrabButton = 16777216

class CoordMode(object):
    Origin = 0
    Previous = 1

class ImageFormat(object):
    XYBitmap = 0
    XYPixmap = 1
    ZPixmap = 2

class GrabStatus(object):
    Success = 0
    AlreadyGrabbed = 1
    InvalidTime = 2
    NotViewable = 3
    Frozen = 4

class LineStyle(object):
    Solid = 0
    OnOffDash = 1
    DoubleDash = 2

class InputFocus(object):
    _None = 0
    PointerRoot = 1
    Parent = 2

class SendEventDest(object):
    PointerWindow = 0
    ItemFocus = 1

class Mapping(object):
    Modifier = 0
    Keyboard = 1
    Pointer = 2

class ScreenSaver(object):
    Reset = 0
    Active = 1

class CloseDown(object):
    DestroyAll = 0
    RetainPermanent = 1
    RetainTemporary = 2

class MapState(object):
    Unmapped = 0
    Unviewable = 1
    Viewable = 2

class ButtonMask(object):
    _1 = 256
    _2 = 512
    _3 = 1024
    _4 = 2048
    _5 = 4096
    Any = 32768

class PolyShape(object):
    Complex = 0
    Nonconvex = 1
    Convex = 2

class SetMode(object):
    Insert = 0
    Delete = 1

class NotifyMode(object):
    Normal = 0
    Grab = 1
    Ungrab = 2
    WhileGrabbed = 3

class GetModifierMappingCookie(ooxcb.Cookie):
    pass

class TranslateCoordinatesReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.same_screen = None
        self.child = None
        self.dst_x = None
        self.dst_y = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxIHH", stream)
        self.same_screen = _unpacked[0]
        self.child = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.dst_x = _unpacked[2]
        self.dst_y = _unpacked[3]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxIHH", self.same_screen, get_internal(self.child), self.dst_x, self.dst_y))

class QueryBestSizeCookie(ooxcb.Cookie):
    pass

class GraphicsExposureEvent(ooxcb.Event):
    event_name = "on_graphics_exposure"
    opcode = 13
    event_target_class = "Drawable"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 13
        self.drawable = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.minor_opcode = None
        self.count = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIHHHHHHBxxx", stream)
        self.response_type = _unpacked[0]
        self.drawable = self.conn.get_from_cache_fallback(_unpacked[1], Drawable)
        self.x = _unpacked[2]
        self.y = _unpacked[3]
        self.width = _unpacked[4]
        self.height = _unpacked[5]
        self.minor_opcode = _unpacked[6]
        self.count = _unpacked[7]
        self.major_opcode = _unpacked[8]
        self.event_target = self.drawable

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIHHHHHHBxxx", self.response_type, get_internal(self.drawable), self.x, self.y, self.width, self.height, self.minor_opcode, self.count, self.major_opcode))
        stream.write("\0" * (32 - (stream.tell() - root)))

class ClientMessageData(ooxcb.Union):
    def __init__(self, conn):
        ooxcb.Union.__init__(self, conn)
        self.data8 = []
        self.data16 = []
        self.data32 = []

    def read(self, stream):
        count = 0
        root = stream.tell()
        self.data8 = ooxcb.List(self.conn, stream, 20, 'B', 1)
        count = max(count, self.data8.size)
        stream.seek(root)
        self.data16 = ooxcb.List(self.conn, stream, 10, 'H', 2)
        count = max(count, self.data16.size)
        stream.seek(root)
        self.data32 = ooxcb.List(self.conn, stream, 5, 'I', 4)
        count = max(count, self.data32.size)
        stream.seek(root)

    def build(self, stream):
        root = stream.tell()
        if self.data8:
            build_list(self.conn, stream, self.data8, 'B')
        elif self.data16:
            build_list(self.conn, stream, self.data16, 'H')
        elif self.data32:
            build_list(self.conn, stream, self.data32, 'I')
        else:
            raise ooxcb.XcbException("No value set in the union!")
        if stream.tell() - root < 20:
            stream.write(pack("=" + "x" * (20 - (stream.tell() - root))))

class QueryExtensionReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.present = None
        self.major_opcode = None
        self.first_event = None
        self.first_error = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxBBBB", stream)
        self.present = _unpacked[0]
        self.major_opcode = _unpacked[1]
        self.first_event = _unpacked[2]
        self.first_error = _unpacked[3]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxBBBB", self.present, self.major_opcode, self.first_event, self.first_error))

class QueryTreeReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.root = None
        self.parent = None
        self.children_len = None
        self.children = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxIIHxxxxxxxxxxxxxx", stream)
        self.root = self.conn.get_from_cache_fallback(_unpacked[0], Window)
        self.parent = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.children_len = _unpacked[2]
        self.children = [self.conn.get_from_cache_fallback(w, Window) for w in ooxcb.List(self.conn, stream, self.children_len, 'I', 4)]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxIIHxxxxxxxxxxxxxx", get_internal(self.root), get_internal(self.parent), self.children_len))
        count += 32
        build_list(self.conn, stream, self.children, 'I')

class ListInstalledColormapsReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.cmaps_len = None
        self.cmaps = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", stream)
        self.cmaps_len = _unpacked[0]
        self.cmaps = [self.conn.get_from_cache_fallback(w, Colormap) for w in ooxcb.List(self.conn, stream, self.cmaps_len, 'I', 4)]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", self.cmaps_len))
        count += 32
        build_list(self.conn, stream, self.cmaps, 'I')

class Rgb(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.red = None
        self.green = None
        self.blue = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=HHHxx", stream)
        self.red = _unpacked[0]
        self.green = _unpacked[1]
        self.blue = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=HHHxx", self.red, self.green, self.blue))

class QueryTreeCookie(ooxcb.Cookie):
    pass

class GetWindowAttributesReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.backing_store = None
        self.visual = None
        self._class = None
        self.bit_gravity = None
        self.win_gravity = None
        self.backing_planes = None
        self.backing_pixel = None
        self.save_under = None
        self.map_is_installed = None
        self.map_state = None
        self.override_redirect = None
        self.colormap = None
        self.all_event_masks = None
        self.your_event_mask = None
        self.do_not_propagate_mask = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxIHBBIIBBBBIIIHxx", stream)
        self.backing_store = _unpacked[0]
        self.visual = _unpacked[1]
        self._class = _unpacked[2]
        self.bit_gravity = _unpacked[3]
        self.win_gravity = _unpacked[4]
        self.backing_planes = _unpacked[5]
        self.backing_pixel = _unpacked[6]
        self.save_under = _unpacked[7]
        self.map_is_installed = _unpacked[8]
        self.map_state = _unpacked[9]
        self.override_redirect = _unpacked[10]
        self.colormap = self.conn.get_from_cache_fallback(_unpacked[11], Colormap)
        self.all_event_masks = _unpacked[12]
        self.your_event_mask = _unpacked[13]
        self.do_not_propagate_mask = _unpacked[14]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxIHBBIIBBBBIIIHxx", self.backing_store, self.visual, self._class, self.bit_gravity, self.win_gravity, self.backing_planes, self.backing_pixel, self.save_under, self.map_is_installed, self.map_state, self.override_redirect, get_internal(self.colormap), self.all_event_masks, self.your_event_mask, self.do_not_propagate_mask))

class AllocColorCookie(ooxcb.Cookie):
    pass

class AllocError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class Colormap(ooxcb.Resource):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def free_checked(self):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cmap))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 79, True, True), \
            ooxcb.VoidCookie())

    def free(self):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cmap))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 79, True, False), \
            ooxcb.VoidCookie())

    def copy_colormap_and_free_checked(self, mid):
        mid = get_internal(mid)
        src_cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", mid, src_cmap))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 80, True, True), \
            ooxcb.VoidCookie())

    def copy_colormap_and_free(self, mid):
        mid = get_internal(mid)
        src_cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", mid, src_cmap))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 80, True, False), \
            ooxcb.VoidCookie())

    def install_checked(self):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cmap))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 81, True, True), \
            ooxcb.VoidCookie())

    def install(self):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cmap))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 81, True, False), \
            ooxcb.VoidCookie())

    def uninstall_checked(self):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cmap))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 82, True, True), \
            ooxcb.VoidCookie())

    def uninstall(self):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cmap))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 82, True, False), \
            ooxcb.VoidCookie())

    def alloc_color(self, red, green, blue):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHHHxx", cmap, red, green, blue))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 84, False, True), \
            AllocColorCookie(),
            AllocColorReply)

    def alloc_color_unchecked(self, red, green, blue):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHHHxx", cmap, red, green, blue))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 84, False, False), \
            AllocColorCookie(),
            AllocColorReply)

    def alloc_named_color(self, name):
        name_len = len(name)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHxx", cmap, name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 85, False, True), \
            AllocNamedColorCookie(),
            AllocNamedColorReply)

    def alloc_named_color_unchecked(self, name):
        name_len = len(name)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHxx", cmap, name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 85, False, False), \
            AllocNamedColorCookie(),
            AllocNamedColorReply)

    def alloc_color_cells(self, contiguous, colors, planes):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHH", contiguous, cmap, colors, planes))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 86, False, True), \
            AllocColorCellsCookie(),
            AllocColorCellsReply)

    def alloc_color_cells_unchecked(self, contiguous, colors, planes):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHH", contiguous, cmap, colors, planes))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 86, False, False), \
            AllocColorCellsCookie(),
            AllocColorCellsReply)

    def alloc_color_planes(self, contiguous, colors, reds, greens, blues):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHHHH", contiguous, cmap, colors, reds, greens, blues))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 87, False, True), \
            AllocColorPlanesCookie(),
            AllocColorPlanesReply)

    def alloc_color_planes_unchecked(self, contiguous, colors, reds, greens, blues):
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHHHH", contiguous, cmap, colors, reds, greens, blues))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 87, False, False), \
            AllocColorPlanesCookie(),
            AllocColorPlanesReply)

    def free_colors_checked(self, pixels, plane_mask):
        pixels_len = len(pixels)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", cmap, plane_mask))
        buf.write(make_array(pixels, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 88, True, True), \
            ooxcb.VoidCookie())

    def free_colors(self, pixels, plane_mask):
        pixels_len = len(pixels)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", cmap, plane_mask))
        buf.write(make_array(pixels, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 88, True, False), \
            ooxcb.VoidCookie())

    def store_colors_checked(self, items):
        items_len = len(items)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cmap))
        for elt in items:
            elt.build(buf)
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 89, True, True), \
            ooxcb.VoidCookie())

    def store_colors(self, items):
        items_len = len(items)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cmap))
        for elt in items:
            elt.build(buf)
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 89, True, False), \
            ooxcb.VoidCookie())

    def store_named_color_checked(self, flags, pixel, name):
        name_len = len(name)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIHxx", flags, cmap, pixel, name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 90, True, True), \
            ooxcb.VoidCookie())

    def store_named_color(self, flags, pixel, name):
        name_len = len(name)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIHxx", flags, cmap, pixel, name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 90, True, False), \
            ooxcb.VoidCookie())

    def query_colors(self, pixels):
        pixels_len = len(pixels)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cmap))
        buf.write(make_array(pixels, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 91, False, True), \
            QueryColorsCookie(),
            QueryColorsReply)

    def query_colors_unchecked(self, pixels):
        pixels_len = len(pixels)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cmap))
        buf.write(make_array(pixels, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 91, False, False), \
            QueryColorsCookie(),
            QueryColorsReply)

    def lookup_color(self, name):
        name_len = len(name)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHxx", cmap, name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 92, False, True), \
            LookupColorCookie(),
            LookupColorReply)

    def lookup_color_unchecked(self, name):
        name_len = len(name)
        cmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHxx", cmap, name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 92, False, False), \
            LookupColorCookie(),
            LookupColorReply)

    def alloc_hex_color(self, color):
        color = color.strip('#')
        r, g, b = [65535 * int(v, base=16) // 255
                   for v in (color[:2], color[2:4], color[4:])]
        return self.alloc_color(r, g, b)

    @classmethod
    def create(cls, window, visual, alloc=0):
        mid = conn.generate_id()
        cmap = cls(conn, mid)
        if isinstance(visual, Visualtype):
            visual = visual.visual_id
        conn.core.create_colormap_checked(alloc, mid, window.get_internal(), visual).check()
        conn.add_to_cache(cmap, mid)
        return cmap

class SetModifierMappingReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.status = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxx", stream)
        self.status = _unpacked[0]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxx", self.status))

class GrabPointerReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.status = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxx", stream)
        self.status = _unpacked[0]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxx", self.status))

class NameError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class BadAtom(ooxcb.ProtocolException):
    pass

class BadCursor(ooxcb.ProtocolException):
    pass

class GContextError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class Coloritem(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.pixel = None
        self.red = None
        self.green = None
        self.blue = None
        self.flags = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=IHHHBx", stream)
        self.pixel = _unpacked[0]
        self.red = _unpacked[1]
        self.green = _unpacked[2]
        self.blue = _unpacked[3]
        self.flags = _unpacked[4]

    def build(self, stream):
        count = 0
        stream.write(pack("=IHHHBx", self.pixel, self.red, self.green, self.blue, self.flags))

class BadAccess(ooxcb.ProtocolException):
    pass

class RequestError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class Setupauthenticate(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.status = None
        self.length = None
        self.reason = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=BxxxxxH", stream)
        self.status = _unpacked[0]
        self.length = _unpacked[1]
        self.reason = ooxcb.List(self.conn, stream, (self.length * 4), 'B', 1).to_string()
        self.size = stream.tell() - root

    def build(self, stream):
        count = 0
        stream.write(pack("=BxxxxxH", self.status, self.length))
        count += 8
        build_list(self.conn, stream, self.reason, 'B')

class GetScreenSaverReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.timeout = None
        self.interval = None
        self.prefer_blanking = None
        self.allow_exposures = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHHBBxxxxxxxxxxxxxxxxxx", stream)
        self.timeout = _unpacked[0]
        self.interval = _unpacked[1]
        self.prefer_blanking = _unpacked[2]
        self.allow_exposures = _unpacked[3]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHHBBxxxxxxxxxxxxxxxxxx", self.timeout, self.interval, self.prefer_blanking, self.allow_exposures))

class LengthError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class ListFontsWithInfoCookie(ooxcb.Cookie):
    pass

class Fontable(ooxcb.Resource):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def query(self):
        font = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", font))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 47, False, True), \
            QueryFontCookie(),
            QueryFontReply)

    def query_unchecked(self):
        font = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", font))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 47, False, False), \
            QueryFontCookie(),
            QueryFontReply)

    def query_text_extents(self, string):
        string_len = len(string)
        font = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=x", ))
        buf.write(pack("=B", (string_len & 1)))
        buf.write(pack("=xxI", font))
        buf.write(string.encode("utf-16be"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 48, False, True), \
            QueryTextExtentsCookie(),
            QueryTextExtentsReply)

    def query_text_extents_unchecked(self, string):
        string_len = len(string)
        font = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=x", ))
        buf.write(pack("=B", (string_len & 1)))
        buf.write(pack("=xxI", font))
        buf.write(string.encode("utf-16be"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 48, False, False), \
            QueryTextExtentsCookie(),
            QueryTextExtentsReply)

class ConfigureNotifyEvent(ooxcb.Event):
    event_name = "on_configure_notify"
    opcode = 22
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 22
        self.event = None
        self.window = None
        self.above_sibling = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.border_width = None
        self.override_redirect = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIIhhHHHBx", stream)
        self.response_type = _unpacked[0]
        self.event = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.window = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.above_sibling = self.conn.get_from_cache_fallback(_unpacked[3], Window)
        self.x = _unpacked[4]
        self.y = _unpacked[5]
        self.width = _unpacked[6]
        self.height = _unpacked[7]
        self.border_width = _unpacked[8]
        self.override_redirect = _unpacked[9]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIIhhHHHBx", self.response_type, get_internal(self.event), get_internal(self.window), get_internal(self.above_sibling), self.x, self.y, self.width, self.height, self.border_width, self.override_redirect))
        stream.write("\0" * (32 - (stream.tell() - root)))

class Setup(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.status = None
        self.protocol_major_version = None
        self.protocol_minor_version = None
        self.length = None
        self.release_number = None
        self.resource_id_base = None
        self.resource_id_mask = None
        self.motion_buffer_size = None
        self.vendor_len = None
        self.maximum_request_length = None
        self.roots_len = None
        self.pixmap_formats_len = None
        self.image_byte_order = None
        self.bitmap_format_bit_order = None
        self.bitmap_format_scanline_unit = None
        self.bitmap_format_scanline_pad = None
        self.min_keycode = None
        self.max_keycode = None
        self.vendor = []
        self.pixmap_formats = []
        self.roots = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=BxHHHIIIIHHBBBBBBBBxxxx", stream)
        self.status = _unpacked[0]
        self.protocol_major_version = _unpacked[1]
        self.protocol_minor_version = _unpacked[2]
        self.length = _unpacked[3]
        self.release_number = _unpacked[4]
        self.resource_id_base = _unpacked[5]
        self.resource_id_mask = _unpacked[6]
        self.motion_buffer_size = _unpacked[7]
        self.vendor_len = _unpacked[8]
        self.maximum_request_length = _unpacked[9]
        self.roots_len = _unpacked[10]
        self.pixmap_formats_len = _unpacked[11]
        self.image_byte_order = _unpacked[12]
        self.bitmap_format_bit_order = _unpacked[13]
        self.bitmap_format_scanline_unit = _unpacked[14]
        self.bitmap_format_scanline_pad = _unpacked[15]
        self.min_keycode = _unpacked[16]
        self.max_keycode = _unpacked[17]
        self.vendor = ooxcb.List(self.conn, stream, self.vendor_len, 'B', 1).to_string()
        stream.seek(ooxcb.type_pad(8, stream.tell() - root), 1)
        self.pixmap_formats = ooxcb.List(self.conn, stream, self.pixmap_formats_len, Format, 8)
        stream.seek(ooxcb.type_pad(4, stream.tell() - root), 1)
        self.roots = ooxcb.List(self.conn, stream, self.roots_len, Screen, -1)
        self.size = stream.tell() - root

    def build(self, stream):
        count = 0
        stream.write(pack("=BxHHHIIIIHHBBBBBBBBxxxx", self.status, self.protocol_major_version, self.protocol_minor_version, self.length, self.release_number, self.resource_id_base, self.resource_id_mask, self.motion_buffer_size, self.vendor_len, self.maximum_request_length, self.roots_len, self.pixmap_formats_len, self.image_byte_order, self.bitmap_format_bit_order, self.bitmap_format_scanline_unit, self.bitmap_format_scanline_pad, self.min_keycode, self.max_keycode))
        count += 40
        build_list(self.conn, stream, self.vendor, 'B')
        build_list(self.conn, stream, self.pixmap_formats, Format)
        build_list(self.conn, stream, self.roots, Screen)

class SelectionClearEvent(ooxcb.Event):
    event_name = "on_selection_clear"
    opcode = 29
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 29
        self.time = None
        self.owner = None
        self.selection = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIII", stream)
        self.response_type = _unpacked[0]
        self.time = _unpacked[1]
        self.owner = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.selection = self.conn.atoms.get_by_id(_unpacked[3])
        self.event_target = self.owner

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIII", self.response_type, self.time, get_internal(self.owner), get_internal(self.selection)))
        stream.write("\0" * (32 - (stream.tell() - root)))

class GetSelectionOwnerCookie(ooxcb.Cookie):
    pass

class ImplementationError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class ListHostsReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.mode = None
        self.hosts_len = None
        self.hosts = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", stream)
        self.mode = _unpacked[0]
        self.hosts_len = _unpacked[1]
        self.hosts = ooxcb.List(self.conn, stream, self.hosts_len, Host, -1)

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", self.mode, self.hosts_len))
        count += 32
        build_list(self.conn, stream, self.hosts, Host)

class GetModifierMappingReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.keycodes_per_modifier = None
        self.keycodes = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", stream)
        self.keycodes_per_modifier = _unpacked[0]
        self.keycodes = ooxcb.List(self.conn, stream, (self.keycodes_per_modifier * 8), 'B', 1)

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", self.keycodes_per_modifier))
        count += 32
        build_list(self.conn, stream, self.keycodes, 'B')

class GetPointerMappingReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.map_len = None
        self.map = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", stream)
        self.map_len = _unpacked[0]
        self.map = ooxcb.List(self.conn, stream, self.map_len, 'B', 1)

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", self.map_len))
        count += 32
        build_list(self.conn, stream, self.map, 'B')

class DestroyNotifyEvent(ooxcb.Event):
    event_name = "on_destroy_notify"
    opcode = 17
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 17
        self.event = None
        self.window = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxII", stream)
        self.response_type = _unpacked[0]
        self.event = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.window = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxII", self.response_type, get_internal(self.event), get_internal(self.window)))
        stream.write("\0" * (32 - (stream.tell() - root)))

class QueryKeymapReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.keys = []

    def read(self, stream):
        self._address = stream.address
        stream.seek(8, 1)
        self.keys = ooxcb.List(self.conn, stream, 32, 'B', 1)

    def build(self, stream):
        count = 0
        count += 8
        build_list(self.conn, stream, self.keys, 'B')

class AllocColorReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.red = None
        self.green = None
        self.blue = None
        self.pixel = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHHHxxI", stream)
        self.red = _unpacked[0]
        self.green = _unpacked[1]
        self.blue = _unpacked[2]
        self.pixel = _unpacked[3]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHHHxxI", self.red, self.green, self.blue, self.pixel))

class BadName(ooxcb.ProtocolException):
    pass

class ListInstalledColormapsCookie(ooxcb.Cookie):
    pass

class GetScreenSaverCookie(ooxcb.Cookie):
    pass

class Arc(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.angle1 = None
        self.angle2 = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=hhHHhh", stream)
        self.x = _unpacked[0]
        self.y = _unpacked[1]
        self.width = _unpacked[2]
        self.height = _unpacked[3]
        self.angle1 = _unpacked[4]
        self.angle2 = _unpacked[5]

    def build(self, stream):
        count = 0
        stream.write(pack("=hhHHhh", self.x, self.y, self.width, self.height, self.angle1, self.angle2))

    @classmethod
    def create(cls, conn, x, y, width, height, angle1, angle2):
        arc = cls(conn)
        arc.x = x
        arc.y = y
        arc.width = width
        arc.height = height
        arc.angle1 = angle1
        arc.angle2 = angle2
        return arc

class QueryFontCookie(ooxcb.Cookie):
    pass

class Font(Fontable):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def close_checked(self):
        font = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", font))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 46, True, True), \
            ooxcb.VoidCookie())

    def close(self):
        font = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", font))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 46, True, False), \
            ooxcb.VoidCookie())

    @classmethod
    def open(cls, conn, name):
        fid = conn.generate_id()
        font = cls(conn, fid)
        conn.core.open_font_checked(font, name).check()
        conn.add_to_cache(fid, font)
        return font

class QueryKeymapCookie(ooxcb.Cookie):
    pass

class ExposeEvent(ooxcb.Event):
    event_name = "on_expose"
    opcode = 12
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 12
        self.window = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.count = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIHHHHHxx", stream)
        self.response_type = _unpacked[0]
        self.window = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.x = _unpacked[2]
        self.y = _unpacked[3]
        self.width = _unpacked[4]
        self.height = _unpacked[5]
        self.count = _unpacked[6]
        self.event_target = self.window

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIHHHHHxx", self.response_type, get_internal(self.window), self.x, self.y, self.width, self.height, self.count))
        stream.write("\0" * (32 - (stream.tell() - root)))

class GravityNotifyEvent(ooxcb.Event):
    event_name = "on_gravity_notify"
    opcode = 24
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 24
        self.event = None
        self.window = None
        self.x = None
        self.y = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIhh", stream)
        self.response_type = _unpacked[0]
        self.event = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.window = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.x = _unpacked[3]
        self.y = _unpacked[4]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIhh", self.response_type, get_internal(self.event), get_internal(self.window), self.x, self.y))
        stream.write("\0" * (32 - (stream.tell() - root)))

class GrabKeyboardReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.status = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxx", stream)
        self.status = _unpacked[0]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxx", self.status))

class ListPropertiesReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.atoms_len = None
        self.atoms = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", stream)
        self.atoms_len = _unpacked[0]
        self.atoms = map(self.conn.atoms.get_by_id, ooxcb.List(self.conn, stream, self.atoms_len, 'I', 4))

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", self.atoms_len))
        count += 32
        build_list(self.conn, stream, self.atoms, 'I')

class ListExtensionsReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.names_len = None
        self.names = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", stream)
        self.names_len = _unpacked[0]
        self.names = ooxcb.List(self.conn, stream, self.names_len, Str, -1)

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", self.names_len))
        count += 32
        build_list(self.conn, stream, self.names, Str)

class AllocNamedColorCookie(ooxcb.Cookie):
    pass

class MatchError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class UnmapNotifyEvent(ooxcb.Event):
    event_name = "on_unmap_notify"
    opcode = 18
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 18
        self.event = None
        self.window = None
        self.from_configure = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIBxxx", stream)
        self.response_type = _unpacked[0]
        self.event = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.window = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.from_configure = _unpacked[3]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIBxxx", self.response_type, get_internal(self.event), get_internal(self.window), self.from_configure))
        stream.write("\0" * (32 - (stream.tell() - root)))

class Setupfailed(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.status = None
        self.reason_len = None
        self.protocol_major_version = None
        self.protocol_minor_version = None
        self.length = None
        self.reason = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=BBHHH", stream)
        self.status = _unpacked[0]
        self.reason_len = _unpacked[1]
        self.protocol_major_version = _unpacked[2]
        self.protocol_minor_version = _unpacked[3]
        self.length = _unpacked[4]
        self.reason = ooxcb.List(self.conn, stream, self.reason_len, 'B', 1).to_string()
        self.size = stream.tell() - root

    def build(self, stream):
        count = 0
        stream.write(pack("=BBHHH", self.status, self.reason_len, self.protocol_major_version, self.protocol_minor_version, self.length))
        count += 8
        build_list(self.conn, stream, self.reason, 'B')

class IDChoiceError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class AllocColorCellsReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.pixels_len = None
        self.masks_len = None
        self.pixels = []
        self.masks = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=xxxxxxxxHHxxxxxxxxxxxxxxxxxxxx", stream)
        self.pixels_len = _unpacked[0]
        self.masks_len = _unpacked[1]
        self.pixels = ooxcb.List(self.conn, stream, self.pixels_len, 'I', 4)
        stream.seek(ooxcb.type_pad(4, stream.tell() - root), 1)
        self.masks = ooxcb.List(self.conn, stream, self.masks_len, 'I', 4)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHHxxxxxxxxxxxxxxxxxxxx", self.pixels_len, self.masks_len))
        count += 32
        build_list(self.conn, stream, self.pixels, 'I')
        build_list(self.conn, stream, self.masks, 'I')

class ConfigureRequestEvent(ooxcb.Event):
    event_name = "on_configure_request"
    opcode = 23
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 23
        self.stack_mode = None
        self.parent = None
        self.window = None
        self.sibling = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.border_width = None
        self.value_mask = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIIIhhHHHH", stream)
        self.response_type = _unpacked[0]
        self.stack_mode = _unpacked[1]
        self.parent = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.window = self.conn.get_from_cache_fallback(_unpacked[3], Window)
        self.sibling = self.conn.get_from_cache_fallback(_unpacked[4], Window)
        self.x = _unpacked[5]
        self.y = _unpacked[6]
        self.width = _unpacked[7]
        self.height = _unpacked[8]
        self.border_width = _unpacked[9]
        self.value_mask = _unpacked[10]
        self.event_target = self.parent

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIIIhhHHHH", self.response_type, self.stack_mode, get_internal(self.parent), get_internal(self.window), get_internal(self.sibling), self.x, self.y, self.width, self.height, self.border_width, self.value_mask))
        stream.write("\0" * (32 - (stream.tell() - root)))

class BadImplementation(ooxcb.ProtocolException):
    pass

class TranslateCoordinatesCookie(ooxcb.Cookie):
    pass

class BadRequest(ooxcb.ProtocolException):
    pass

class GetKeyboardControlCookie(ooxcb.Cookie):
    pass

class WMState(object):
    Withdrawn = 0
    Normal = 1
    Iconic = 3

class FontError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class Setuprequest(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.byte_order = None
        self.protocol_major_version = None
        self.protocol_minor_version = None
        self.authorization_protocol_name_len = None
        self.authorization_protocol_data_len = None
        self.authorization_protocol_name = []
        self.authorization_protocol_data = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=BxHHHHxx", stream)
        self.byte_order = _unpacked[0]
        self.protocol_major_version = _unpacked[1]
        self.protocol_minor_version = _unpacked[2]
        self.authorization_protocol_name_len = _unpacked[3]
        self.authorization_protocol_data_len = _unpacked[4]
        self.authorization_protocol_name = ooxcb.List(self.conn, stream, self.authorization_protocol_name_len, 'B', 1).to_string()
        stream.seek(ooxcb.type_pad(1, stream.tell() - root), 1)
        self.authorization_protocol_data = ooxcb.List(self.conn, stream, self.authorization_protocol_data_len, 'B', 1).to_string()
        self.size = stream.tell() - root

    def build(self, stream):
        count = 0
        stream.write(pack("=BxHHHHxx", self.byte_order, self.protocol_major_version, self.protocol_minor_version, self.authorization_protocol_name_len, self.authorization_protocol_data_len))
        count += 12
        build_list(self.conn, stream, self.authorization_protocol_name, 'B')
        build_list(self.conn, stream, self.authorization_protocol_data, 'B')

class KeymapNotifyEvent(ooxcb.Event):
    event_name = "on_keymap_notify"
    opcode = 11
    event_target_class = ooxcb.Connection
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 11
        self.keys = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=B", stream)
        self.response_type = _unpacked[0]
        self.keys = ooxcb.List(self.conn, stream, 31, 'B', 1)
        self.event_target = self.conn

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=B", self.response_type))
        count += 1
        build_list(self.conn, stream, self.keys, 'B')
        stream.write("\0" * (32 - (stream.tell() - root)))

class BadIDChoice(ooxcb.ProtocolException):
    pass

class GetKeyboardMappingCookie(ooxcb.Cookie):
    pass

class AllocColorPlanesCookie(ooxcb.Cookie):
    pass

class BadMatch(ooxcb.ProtocolException):
    pass

class Visualtype(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.visual_id = None
        self._class = None
        self.bits_per_rgb_value = None
        self.colormap_entries = None
        self.red_mask = None
        self.green_mask = None
        self.blue_mask = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=IBBHIIIxxxx", stream)
        self.visual_id = _unpacked[0]
        self._class = _unpacked[1]
        self.bits_per_rgb_value = _unpacked[2]
        self.colormap_entries = _unpacked[3]
        self.red_mask = _unpacked[4]
        self.green_mask = _unpacked[5]
        self.blue_mask = _unpacked[6]

    def build(self, stream):
        count = 0
        stream.write(pack("=IBBHIIIxxxx", self.visual_id, self._class, self.bits_per_rgb_value, self.colormap_entries, self.red_mask, self.green_mask, self.blue_mask))

class BadFont(ooxcb.ProtocolException):
    pass

class Cursor(ooxcb.Resource):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def free_checked(self):
        cursor = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cursor))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 95, True, True), \
            ooxcb.VoidCookie())

    def free(self):
        cursor = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", cursor))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 95, True, False), \
            ooxcb.VoidCookie())

    def recolor_checked(self, fore_red, fore_green, fore_blue, back_red, back_green, back_blue):
        cursor = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHHHHHH", cursor, fore_red, fore_green, fore_blue, back_red, back_green, back_blue))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 96, True, True), \
            ooxcb.VoidCookie())

    def recolor(self, fore_red, fore_green, fore_blue, back_red, back_green, back_blue):
        cursor = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHHHHHH", cursor, fore_red, fore_green, fore_blue, back_red, back_green, back_blue))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 96, True, False), \
            ooxcb.VoidCookie())

    @classmethod
    def create(cls, conn, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y):
        cid = conn.generate_id()
        cursor = cls(conn, cid)
        conn.core.create_cursor_checked(cursor, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y).check()
        conn.add_to_cache(cid, cursor)
        return cursor

    @classmethod
    def create_glyph(cls, conn, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue):
        cid = conn.generate_id()
        cursor = cls(conn, cid)
        conn.core.create_glyph_cursor_checked(cursor, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue).check()
        conn.add_to_cache(cid, cursor)
        return cursor

class GrabPointerCookie(ooxcb.Cookie):
    pass

class BadValue(ooxcb.ProtocolException):
    pass

class GetInputFocusCookie(ooxcb.Cookie):
    pass

class DrawableError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class AllocColorCellsCookie(ooxcb.Cookie):
    pass

class SetPointerMappingCookie(ooxcb.Cookie):
    pass

class Point(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.x = None
        self.y = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=hh", stream)
        self.x = _unpacked[0]
        self.y = _unpacked[1]

    def build(self, stream):
        count = 0
        stream.write(pack("=hh", self.x, self.y))

class BadColormap(ooxcb.ProtocolException):
    pass

class NoExposureEvent(ooxcb.Event):
    event_name = "on_no_exposure"
    opcode = 14
    event_target_class = "Drawable"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 14
        self.drawable = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIHBx", stream)
        self.response_type = _unpacked[0]
        self.drawable = self.conn.get_from_cache_fallback(_unpacked[1], Drawable)
        self.minor_opcode = _unpacked[2]
        self.major_opcode = _unpacked[3]
        self.event_target = self.drawable

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIHBx", self.response_type, get_internal(self.drawable), self.minor_opcode, self.major_opcode))
        stream.write("\0" * (32 - (stream.tell() - root)))

class BadPixmap(ooxcb.ProtocolException):
    pass

class ListPropertiesCookie(ooxcb.Cookie):
    pass

class BadGContext(ooxcb.ProtocolException):
    pass

class GetGeometryCookie(ooxcb.Cookie):
    pass

class BadDrawable(ooxcb.ProtocolException):
    pass

class AllocNamedColorReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.pixel = None
        self.exact_red = None
        self.exact_green = None
        self.exact_blue = None
        self.visual_red = None
        self.visual_green = None
        self.visual_blue = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxIHHHHHH", stream)
        self.pixel = _unpacked[0]
        self.exact_red = _unpacked[1]
        self.exact_green = _unpacked[2]
        self.exact_blue = _unpacked[3]
        self.visual_red = _unpacked[4]
        self.visual_green = _unpacked[5]
        self.visual_blue = _unpacked[6]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxIHHHHHH", self.pixel, self.exact_red, self.exact_green, self.exact_blue, self.visual_red, self.visual_green, self.visual_blue))

class GetImageCookie(ooxcb.Cookie):
    pass

class LookupColorCookie(ooxcb.Cookie):
    pass

class EnterNotifyEvent(ooxcb.Event):
    event_name = "on_enter_notify"
    opcode = 7
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 7
        self.detail = None
        self.time = None
        self.root = None
        self.event = None
        self.child = None
        self.root_x = None
        self.root_y = None
        self.event_x = None
        self.event_y = None
        self.state = None
        self.mode = None
        self.same_screen_focus = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIIIIhhhhHBB", stream)
        self.response_type = _unpacked[0]
        self.detail = _unpacked[1]
        self.time = _unpacked[2]
        self.root = self.conn.get_from_cache_fallback(_unpacked[3], Window)
        self.event = self.conn.get_from_cache_fallback(_unpacked[4], Window)
        self.child = self.conn.get_from_cache_fallback(_unpacked[5], Window)
        self.root_x = _unpacked[6]
        self.root_y = _unpacked[7]
        self.event_x = _unpacked[8]
        self.event_y = _unpacked[9]
        self.state = _unpacked[10]
        self.mode = _unpacked[11]
        self.same_screen_focus = _unpacked[12]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIIIIhhhhHBB", self.response_type, self.detail, self.time, get_internal(self.root), get_internal(self.event), get_internal(self.child), self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.mode, self.same_screen_focus))
        stream.write("\0" * (32 - (stream.tell() - root)))

class MapRequestEvent(ooxcb.Event):
    event_name = "on_map_request"
    opcode = 20
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 20
        self.parent = None
        self.window = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxII", stream)
        self.response_type = _unpacked[0]
        self.parent = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.window = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.event_target = self.parent

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxII", self.response_type, get_internal(self.parent), get_internal(self.window)))
        stream.write("\0" * (32 - (stream.tell() - root)))

class QueryPointerCookie(ooxcb.Cookie):
    pass

class ColormapError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class AccessError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class GrabKeyboardCookie(ooxcb.Cookie):
    pass

class KeyReleaseEvent(ooxcb.Event):
    event_name = "on_key_release"
    opcode = 3
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 3
        self.detail = None
        self.time = None
        self.root = None
        self.event = None
        self.child = None
        self.root_x = None
        self.root_y = None
        self.event_x = None
        self.event_y = None
        self.state = None
        self.same_screen = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIIIIhhhhHBx", stream)
        self.response_type = _unpacked[0]
        self.detail = _unpacked[1]
        self.time = _unpacked[2]
        self.root = self.conn.get_from_cache_fallback(_unpacked[3], Window)
        self.event = self.conn.get_from_cache_fallback(_unpacked[4], Window)
        self.child = self.conn.get_from_cache_fallback(_unpacked[5], Window)
        self.root_x = _unpacked[6]
        self.root_y = _unpacked[7]
        self.event_x = _unpacked[8]
        self.event_y = _unpacked[9]
        self.state = _unpacked[10]
        self.same_screen = _unpacked[11]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIIIIhhhhHBx", self.response_type, self.detail, self.time, get_internal(self.root), get_internal(self.event), get_internal(self.child), self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen))
        stream.write("\0" * (32 - (stream.tell() - root)))

class QueryTextExtentsCookie(ooxcb.Cookie):
    pass

class Rectangle(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.x = None
        self.y = None
        self.width = None
        self.height = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=hhHH", stream)
        self.x = _unpacked[0]
        self.y = _unpacked[1]
        self.width = _unpacked[2]
        self.height = _unpacked[3]

    def build(self, stream):
        count = 0
        stream.write(pack("=hhHH", self.x, self.y, self.width, self.height))

    @classmethod
    def create(cls, conn, x, y, width, height):
        rect = cls(conn)
        rect.x = x
        rect.y = y
        rect.width = width
        rect.height = height
        return rect

class ListFontsCookie(ooxcb.Cookie):
    pass

class GetPropertyReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.format = None
        self.type = None
        self.bytes_after = None
        self.value_len = None
        self.value = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxIIIxxxxxxxxxxxx", stream)
        self.format = _unpacked[0]
        self.type = self.conn.atoms.get_by_id(_unpacked[1])
        self.bytes_after = _unpacked[2]
        self.value_len = _unpacked[3]
        self.value = ooxcb.List(self.conn, stream, self.value_len, SIZES.get(self.format, "B"), self.format // 8)

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxIIIxxxxxxxxxxxx", self.format, get_internal(self.type), self.bytes_after, self.value_len))
        count += 32
        build_list(self.conn, stream, self.value, 'B')

    @property
    def exists(self):
        ''' is True if the queried property exists. (If a property does not exist, self.format is 0.) '''
        return self.format != 0

    @property
    def typed_value(self):
        ''' returns a Python object wrapping the value. See :mod:`autotypes`. '''
        from ooxcb.autotypes import autoconvert_value
        return autoconvert_value(self.conn, self.type, self.value)

class LookupColorReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.exact_red = None
        self.exact_green = None
        self.exact_blue = None
        self.visual_red = None
        self.visual_green = None
        self.visual_blue = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHHHHHH", stream)
        self.exact_red = _unpacked[0]
        self.exact_green = _unpacked[1]
        self.exact_blue = _unpacked[2]
        self.visual_red = _unpacked[3]
        self.visual_green = _unpacked[4]
        self.visual_blue = _unpacked[5]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHHHHHH", self.exact_red, self.exact_green, self.exact_blue, self.visual_red, self.visual_green, self.visual_blue))

class GetImageReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.depth = None
        self.visual = None
        self.data = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxIxxxxxxxxxxxxxxxxxxxx", stream)
        self.depth = _unpacked[0]
        self.visual = _unpacked[1]
        self.data = ooxcb.List(self.conn, stream, (self.length * 4), 'B', 1)

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxIxxxxxxxxxxxxxxxxxxxx", self.depth, self.visual))
        count += 32
        build_list(self.conn, stream, self.data, 'B')

class Screen(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.root = None
        self.default_colormap = None
        self.white_pixel = None
        self.black_pixel = None
        self.current_input_masks = None
        self.width_in_pixels = None
        self.height_in_pixels = None
        self.width_in_millimeters = None
        self.height_in_millimeters = None
        self.min_installed_maps = None
        self.max_installed_maps = None
        self.root_visual = None
        self.backing_stores = None
        self.save_unders = None
        self.root_depth = None
        self.allowed_depths_len = None
        self.allowed_depths = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=IIIIIHHHHHHIBBBB", stream)
        self.root = self.conn.get_from_cache_fallback(_unpacked[0], Window)
        self.default_colormap = self.conn.get_from_cache_fallback(_unpacked[1], Colormap)
        self.white_pixel = _unpacked[2]
        self.black_pixel = _unpacked[3]
        self.current_input_masks = _unpacked[4]
        self.width_in_pixels = _unpacked[5]
        self.height_in_pixels = _unpacked[6]
        self.width_in_millimeters = _unpacked[7]
        self.height_in_millimeters = _unpacked[8]
        self.min_installed_maps = _unpacked[9]
        self.max_installed_maps = _unpacked[10]
        self.root_visual = _unpacked[11]
        self.backing_stores = _unpacked[12]
        self.save_unders = _unpacked[13]
        self.root_depth = _unpacked[14]
        self.allowed_depths_len = _unpacked[15]
        self.allowed_depths = ooxcb.List(self.conn, stream, self.allowed_depths_len, Depth, -1)
        self.size = stream.tell() - root

    def build(self, stream):
        count = 0
        stream.write(pack("=IIIIIHHHHHHIBBBB", get_internal(self.root), get_internal(self.default_colormap), self.white_pixel, self.black_pixel, self.current_input_masks, self.width_in_pixels, self.height_in_pixels, self.width_in_millimeters, self.height_in_millimeters, self.min_installed_maps, self.max_installed_maps, self.root_visual, self.backing_stores, self.save_unders, self.root_depth, self.allowed_depths_len))
        count += 40
        build_list(self.conn, stream, self.allowed_depths, Depth)

    def get_active_window(self):
        return self.root.get_property('_NET_ACTIVE_WINDOW', 'WINDOW').reply().value.to_windows()[0]

    @cached_property
    def rgba_colormap(self):
        visual = self.get_root_visual_type()
        return Colormap.create(self.root, visual)

    def get_root_visual_type(self):
        for depth in self.allowed_depths:
            for vt in depth.visuals:
                if self.root_visual == vt.visual_id:
                    return vt
        return None

    def get_rgba_visual(self):
        for depth in self.allowed_depths:
            if depth.depth == 32:
                for visual in depth.visuals:
                    if (visual.red_mask == 0xff0000 and visual.green_mask == 0x00ff00 and visual.blue_mask == 0x0000ff):
                        return visual
        return None

class ReparentNotifyEvent(ooxcb.Event):
    event_name = "on_reparent_notify"
    opcode = 21
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 21
        self.event = None
        self.window = None
        self.parent = None
        self.x = None
        self.y = None
        self.override_redirect = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIIhhBxxx", stream)
        self.response_type = _unpacked[0]
        self.event = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.window = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.parent = self.conn.get_from_cache_fallback(_unpacked[3], Window)
        self.x = _unpacked[4]
        self.y = _unpacked[5]
        self.override_redirect = _unpacked[6]
        self.event_target = self.window

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIIhhBxxx", self.response_type, get_internal(self.event), get_internal(self.window), get_internal(self.parent), self.x, self.y, self.override_redirect))
        stream.write("\0" * (32 - (stream.tell() - root)))

class ClientMessageEvent(ooxcb.Event):
    event_name = "on_client_message"
    opcode = 33
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 33
        self.format = None
        self.window = None
        self.type = None
        self.data = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxII", stream)
        self.response_type = _unpacked[0]
        self.format = _unpacked[1]
        self.window = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.type = self.conn.atoms.get_by_id(_unpacked[3])
        self.data = ClientMessageData.create_from_stream(self.conn, stream)
        self.event_target = self.window

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxII", self.response_type, self.format, get_internal(self.window), get_internal(self.type)))
        count += 12
        self.data.build(stream)
        stream.write("\0" * (32 - (stream.tell() - root)))

    @classmethod
    def create(cls, conn, type, window, format, values):
        assert format in (8, 16, 32)
        evt = cls(conn)
        evt.type = type
        evt.window = window
        evt.format = format
        data = ClientMessageData(conn)
        setattr(data, "data%d" % format, values)
        evt.data = data
        return evt

class Host(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.family = None
        self.address_len = None
        self.address = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=BxH", stream)
        self.family = _unpacked[0]
        self.address_len = _unpacked[1]
        self.address = ooxcb.List(self.conn, stream, self.address_len, 'B', 1)
        self.size = stream.tell() - root

    def build(self, stream):
        count = 0
        stream.write(pack("=BxH", self.family, self.address_len))
        count += 4
        build_list(self.conn, stream, self.address, 'B')

class Char2b(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.byte1 = None
        self.byte2 = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BB", stream)
        self.byte1 = _unpacked[0]
        self.byte2 = _unpacked[1]

    def build(self, stream):
        count = 0
        stream.write(pack("=BB", self.byte1, self.byte2))

class InternAtomCookie(ooxcb.Cookie):
    pass

class ListFontsWithInfoReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.name_len = None
        self.min_bounds = None
        self.max_bounds = None
        self.min_char_or_byte2 = None
        self.max_char_or_byte2 = None
        self.default_char = None
        self.properties_len = None
        self.draw_direction = None
        self.min_byte1 = None
        self.max_byte1 = None
        self.all_chars_exist = None
        self.font_ascent = None
        self.font_descent = None
        self.replies_hint = None
        self.properties = []
        self.name = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=xBxxxxxx", stream)
        self.name_len = _unpacked[0]
        self.min_bounds = Charinfo.create_from_stream(self.conn, stream)
        stream.seek(4, 1)
        stream.seek(ooxcb.type_pad(12, stream.tell() - root), 1)
        self.max_bounds = Charinfo.create_from_stream(self.conn, stream)
        _unpacked = unpack_from_stream("=xxxxHHHHBBBBhhI", stream)
        self.min_char_or_byte2 = _unpacked[0]
        self.max_char_or_byte2 = _unpacked[1]
        self.default_char = _unpacked[2]
        self.properties_len = _unpacked[3]
        self.draw_direction = _unpacked[4]
        self.min_byte1 = _unpacked[5]
        self.max_byte1 = _unpacked[6]
        self.all_chars_exist = _unpacked[7]
        self.font_ascent = _unpacked[8]
        self.font_descent = _unpacked[9]
        self.replies_hint = _unpacked[10]
        stream.seek(ooxcb.type_pad(8, stream.tell() - root), 1)
        self.properties = ooxcb.List(self.conn, stream, self.properties_len, Fontprop, 8)
        stream.seek(ooxcb.type_pad(1, stream.tell() - root), 1)
        self.name = ooxcb.List(self.conn, stream, self.name_len, 'B', 1).to_string()

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxx", self.name_len))
        count += 8
        self.min_bounds.build(stream)
        count += 4
        self.max_bounds.build(stream)
        stream.write(pack("=xxxxHHHHBBBBhhI", self.min_char_or_byte2, self.max_char_or_byte2, self.default_char, self.properties_len, self.draw_direction, self.min_byte1, self.max_byte1, self.all_chars_exist, self.font_ascent, self.font_descent, self.replies_hint))
        count += 24
        build_list(self.conn, stream, self.properties, Fontprop)
        build_list(self.conn, stream, self.name, 'B')

class QueryTextExtentsReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.draw_direction = None
        self.font_ascent = None
        self.font_descent = None
        self.overall_ascent = None
        self.overall_descent = None
        self.overall_width = None
        self.overall_left = None
        self.overall_right = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxhhhhiii", stream)
        self.draw_direction = _unpacked[0]
        self.font_ascent = _unpacked[1]
        self.font_descent = _unpacked[2]
        self.overall_ascent = _unpacked[3]
        self.overall_descent = _unpacked[4]
        self.overall_width = _unpacked[5]
        self.overall_left = _unpacked[6]
        self.overall_right = _unpacked[7]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxhhhhiii", self.draw_direction, self.font_ascent, self.font_descent, self.overall_ascent, self.overall_descent, self.overall_width, self.overall_left, self.overall_right))

class ButtonReleaseEvent(ooxcb.Event):
    event_name = "on_button_release"
    opcode = 5
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 5
        self.detail = None
        self.time = None
        self.root = None
        self.event = None
        self.child = None
        self.root_x = None
        self.root_y = None
        self.event_x = None
        self.event_y = None
        self.state = None
        self.same_screen = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIIIIhhhhHBx", stream)
        self.response_type = _unpacked[0]
        self.detail = _unpacked[1]
        self.time = _unpacked[2]
        self.root = self.conn.get_from_cache_fallback(_unpacked[3], Window)
        self.event = self.conn.get_from_cache_fallback(_unpacked[4], Window)
        self.child = self.conn.get_from_cache_fallback(_unpacked[5], Window)
        self.root_x = _unpacked[6]
        self.root_y = _unpacked[7]
        self.event_x = _unpacked[8]
        self.event_y = _unpacked[9]
        self.state = _unpacked[10]
        self.same_screen = _unpacked[11]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIIIIhhhhHBx", self.response_type, self.detail, self.time, get_internal(self.root), get_internal(self.event), get_internal(self.child), self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen))
        stream.write("\0" * (32 - (stream.tell() - root)))

class Charinfo(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.left_side_bearing = None
        self.right_side_bearing = None
        self.character_width = None
        self.ascent = None
        self.descent = None
        self.attributes = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=hhhhhH", stream)
        self.left_side_bearing = _unpacked[0]
        self.right_side_bearing = _unpacked[1]
        self.character_width = _unpacked[2]
        self.ascent = _unpacked[3]
        self.descent = _unpacked[4]
        self.attributes = _unpacked[5]

    def build(self, stream):
        count = 0
        stream.write(pack("=hhhhhH", self.left_side_bearing, self.right_side_bearing, self.character_width, self.ascent, self.descent, self.attributes))

class BadLength(ooxcb.ProtocolException):
    pass

class xprotoExtension(ooxcb.Extension):
    header = "xproto"
    def create_window_checked(self, depth, wid, parent, x, y, width, height, border_width, _class, visual, value_mask, value_list):
        wid = get_internal(wid)
        parent = get_internal(parent)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIhhHHHHII", depth, wid, parent, x, y, width, height, border_width, _class, visual, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, True, True), \
            ooxcb.VoidCookie())

    def create_window(self, depth, wid, parent, x, y, width, height, border_width, _class, visual, value_mask, value_list):
        wid = get_internal(wid)
        parent = get_internal(parent)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIhhHHHHII", depth, wid, parent, x, y, width, height, border_width, _class, visual, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, True, False), \
            ooxcb.VoidCookie())

    def intern_atom(self, name, only_if_exists=False):
        name_len = len(name)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxHxx", only_if_exists, name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 16, False, True), \
            InternAtomCookie(),
            InternAtomReply)

    def intern_atom_unchecked(self, name, only_if_exists=False):
        name_len = len(name)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxHxx", only_if_exists, name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 16, False, False), \
            InternAtomCookie(),
            InternAtomReply)

    def ungrab_pointer_checked(self, time=Time.CurrentTime):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 27, True, True), \
            ooxcb.VoidCookie())

    def ungrab_pointer(self, time=Time.CurrentTime):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 27, True, False), \
            ooxcb.VoidCookie())

    def change_active_pointer_grab_checked(self, cursor, time, event_mask):
        cursor = get_internal(cursor)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIHxx", cursor, time, event_mask))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 30, True, True), \
            ooxcb.VoidCookie())

    def change_active_pointer_grab(self, cursor, time, event_mask):
        cursor = get_internal(cursor)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIHxx", cursor, time, event_mask))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 30, True, False), \
            ooxcb.VoidCookie())

    def ungrab_keyboard_checked(self, time=0):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 32, True, True), \
            ooxcb.VoidCookie())

    def ungrab_keyboard(self, time=0):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 32, True, False), \
            ooxcb.VoidCookie())

    def allow_events_checked(self, mode, time=0):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxI", mode, time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 35, True, True), \
            ooxcb.VoidCookie())

    def allow_events(self, mode, time=0):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxI", mode, time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 35, True, False), \
            ooxcb.VoidCookie())

    def grab_server_checked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 36, True, True), \
            ooxcb.VoidCookie())

    def grab_server(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 36, True, False), \
            ooxcb.VoidCookie())

    def ungrab_server_checked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 37, True, True), \
            ooxcb.VoidCookie())

    def ungrab_server(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 37, True, False), \
            ooxcb.VoidCookie())

    def warp_pointer_checked(self, src_window, dst_window, src_x, src_y, src_width, src_height, dst_x, dst_y):
        src_window = get_internal(src_window)
        dst_window = get_internal(dst_window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhhHHhh", src_window, dst_window, src_x, src_y, src_width, src_height, dst_x, dst_y))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 41, True, True), \
            ooxcb.VoidCookie())

    def warp_pointer(self, src_window, dst_window, src_x, src_y, src_width, src_height, dst_x, dst_y):
        src_window = get_internal(src_window)
        dst_window = get_internal(dst_window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhhHHhh", src_window, dst_window, src_x, src_y, src_width, src_height, dst_x, dst_y))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 41, True, False), \
            ooxcb.VoidCookie())

    def get_input_focus(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 43, False, True), \
            GetInputFocusCookie(),
            GetInputFocusReply)

    def get_input_focus_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 43, False, False), \
            GetInputFocusCookie(),
            GetInputFocusReply)

    def query_keymap(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 44, False, True), \
            QueryKeymapCookie(),
            QueryKeymapReply)

    def query_keymap_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 44, False, False), \
            QueryKeymapCookie(),
            QueryKeymapReply)

    def open_font_checked(self, fid, name):
        name_len = len(name)
        fid = get_internal(fid)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHxx", fid, name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 45, True, True), \
            ooxcb.VoidCookie())

    def open_font(self, fid, name):
        name_len = len(name)
        fid = get_internal(fid)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHxx", fid, name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 45, True, False), \
            ooxcb.VoidCookie())

    def list_fonts(self, max_names, pattern):
        pattern_len = len(pattern)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxHH", max_names, pattern_len))
        buf.write(make_array(pattern, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 49, False, True), \
            ListFontsCookie(),
            ListFontsReply)

    def list_fonts_unchecked(self, max_names, pattern):
        pattern_len = len(pattern)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxHH", max_names, pattern_len))
        buf.write(make_array(pattern, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 49, False, False), \
            ListFontsCookie(),
            ListFontsReply)

    def list_fonts_with_info(self, max_names, pattern):
        pattern_len = len(pattern)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxHH", max_names, pattern_len))
        buf.write(make_array(pattern, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 50, False, True), \
            ListFontsWithInfoCookie(),
            ListFontsWithInfoReply)

    def list_fonts_with_info_unchecked(self, max_names, pattern):
        pattern_len = len(pattern)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxHH", max_names, pattern_len))
        buf.write(make_array(pattern, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 50, False, False), \
            ListFontsWithInfoCookie(),
            ListFontsWithInfoReply)

    def set_font_path_checked(self, path):
        font_qty = len(path)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxHxx", font_qty))
        for item in path:
            buf.write(make_array(item, "B") + "\x00")
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 51, True, True), \
            ooxcb.VoidCookie())

    def set_font_path(self, path):
        font_qty = len(path)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxHxx", font_qty))
        for item in path:
            buf.write(make_array(item, "B") + "\x00")
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 51, True, False), \
            ooxcb.VoidCookie())

    def get_font_path(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 52, False, True), \
            GetFontPathCookie(),
            GetFontPathReply)

    def get_font_path_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 52, False, False), \
            GetFontPathCookie(),
            GetFontPathReply)

    def create_pixmap_checked(self, depth, pid, drawable, width, height):
        pid = get_internal(pid)
        drawable = get_internal(drawable)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIHH", depth, pid, drawable, width, height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 53, True, True), \
            ooxcb.VoidCookie())

    def create_pixmap(self, depth, pid, drawable, width, height):
        pid = get_internal(pid)
        drawable = get_internal(drawable)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIHH", depth, pid, drawable, width, height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 53, True, False), \
            ooxcb.VoidCookie())

    def create_g_c_checked(self, cid, drawable, value_mask, value_list):
        cid = get_internal(cid)
        drawable = get_internal(drawable)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", cid, drawable, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 55, True, True), \
            ooxcb.VoidCookie())

    def create_g_c(self, cid, drawable, value_mask, value_list):
        cid = get_internal(cid)
        drawable = get_internal(drawable)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", cid, drawable, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 55, True, False), \
            ooxcb.VoidCookie())

    def create_colormap_checked(self, alloc, mid, window, visual):
        mid = get_internal(mid)
        window = get_internal(window)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIII", alloc, mid, window, visual))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 78, True, True), \
            ooxcb.VoidCookie())

    def create_colormap(self, alloc, mid, window, visual):
        mid = get_internal(mid)
        window = get_internal(window)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIII", alloc, mid, window, visual))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 78, True, False), \
            ooxcb.VoidCookie())

    def create_cursor_checked(self, cid, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y):
        cid = get_internal(cid)
        source = get_internal(source)
        mask = get_internal(mask)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIIHHHHHHHH", cid, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 93, True, True), \
            ooxcb.VoidCookie())

    def create_cursor(self, cid, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y):
        cid = get_internal(cid)
        source = get_internal(source)
        mask = get_internal(mask)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIIHHHHHHHH", cid, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 93, True, False), \
            ooxcb.VoidCookie())

    def create_glyph_cursor_checked(self, cid, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue):
        cid = get_internal(cid)
        source_font = get_internal(source_font)
        mask_font = get_internal(mask_font)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIIHHHHHHHH", cid, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 94, True, True), \
            ooxcb.VoidCookie())

    def create_glyph_cursor(self, cid, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue):
        cid = get_internal(cid)
        source_font = get_internal(source_font)
        mask_font = get_internal(mask_font)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIIHHHHHHHH", cid, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 94, True, False), \
            ooxcb.VoidCookie())

    def query_extension(self, name):
        name_len = len(name)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxHxx", name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 98, False, True), \
            QueryExtensionCookie(),
            QueryExtensionReply)

    def query_extension_unchecked(self, name):
        name_len = len(name)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxHxx", name_len))
        buf.write(make_array(name, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 98, False, False), \
            QueryExtensionCookie(),
            QueryExtensionReply)

    def list_extensions(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 99, False, True), \
            ListExtensionsCookie(),
            ListExtensionsReply)

    def list_extensions_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 99, False, False), \
            ListExtensionsCookie(),
            ListExtensionsReply)

    def change_keyboard_mapping_checked(self, keycode_count, first_keycode, keysyms_per_keycode, keysyms):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxBB", keycode_count, first_keycode, keysyms_per_keycode))
        buf.write(make_array(keysyms, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 100, True, True), \
            ooxcb.VoidCookie())

    def change_keyboard_mapping(self, keycode_count, first_keycode, keysyms_per_keycode, keysyms):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxBB", keycode_count, first_keycode, keysyms_per_keycode))
        buf.write(make_array(keysyms, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 100, True, False), \
            ooxcb.VoidCookie())

    def get_keyboard_mapping(self, first_keycode, count):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBB", first_keycode, count))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 101, False, True), \
            GetKeyboardMappingCookie(),
            GetKeyboardMappingReply)

    def get_keyboard_mapping_unchecked(self, first_keycode, count):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxBB", first_keycode, count))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 101, False, False), \
            GetKeyboardMappingCookie(),
            GetKeyboardMappingReply)

    def change_keyboard_control_checked(self, **values):
        value_mask, value_list = 0, []
        if "key_click_percent" in values:
            value_mask |= 1
            value_list.append(values["key_click_percent"])
        if "bell_percent" in values:
            value_mask |= 2
            value_list.append(values["bell_percent"])
        if "bell_pitch" in values:
            value_mask |= 4
            value_list.append(values["bell_pitch"])
        if "bell_duration" in values:
            value_mask |= 8
            value_list.append(values["bell_duration"])
        if "led" in values:
            value_mask |= 16
            value_list.append(values["led"])
        if "led_mode" in values:
            value_mask |= 32
            value_list.append(values["led_mode"])
        if "key" in values:
            value_mask |= 64
            value_list.append(values["key"])
        if "auto_repeat_mode" in values:
            value_mask |= 128
            value_list.append(values["auto_repeat_mode"])
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 102, True, True), \
            ooxcb.VoidCookie())

    def change_keyboard_control(self, **values):
        value_mask, value_list = 0, []
        if "key_click_percent" in values:
            value_mask |= 1
            value_list.append(values["key_click_percent"])
        if "bell_percent" in values:
            value_mask |= 2
            value_list.append(values["bell_percent"])
        if "bell_pitch" in values:
            value_mask |= 4
            value_list.append(values["bell_pitch"])
        if "bell_duration" in values:
            value_mask |= 8
            value_list.append(values["bell_duration"])
        if "led" in values:
            value_mask |= 16
            value_list.append(values["led"])
        if "led_mode" in values:
            value_mask |= 32
            value_list.append(values["led_mode"])
        if "key" in values:
            value_mask |= 64
            value_list.append(values["key"])
        if "auto_repeat_mode" in values:
            value_mask |= 128
            value_list.append(values["auto_repeat_mode"])
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 102, True, False), \
            ooxcb.VoidCookie())

    def get_keyboard_control(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 103, False, True), \
            GetKeyboardControlCookie(),
            GetKeyboardControlReply)

    def get_keyboard_control_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 103, False, False), \
            GetKeyboardControlCookie(),
            GetKeyboardControlReply)

    def bell_checked(self, percent=0):
        buf = StringIO.StringIO()
        buf.write(pack("=xbxx", percent))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 104, True, True), \
            ooxcb.VoidCookie())

    def bell(self, percent=0):
        buf = StringIO.StringIO()
        buf.write(pack("=xbxx", percent))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 104, True, False), \
            ooxcb.VoidCookie())

    def change_pointer_control_checked(self, acceleration_numerator, acceleration_denominator, threshold, do_acceleration, do_threshold):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxhhhBB", acceleration_numerator, acceleration_denominator, threshold, do_acceleration, do_threshold))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 105, True, True), \
            ooxcb.VoidCookie())

    def change_pointer_control(self, acceleration_numerator, acceleration_denominator, threshold, do_acceleration, do_threshold):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxhhhBB", acceleration_numerator, acceleration_denominator, threshold, do_acceleration, do_threshold))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 105, True, False), \
            ooxcb.VoidCookie())

    def get_pointer_control(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 106, False, True), \
            GetPointerControlCookie(),
            GetPointerControlReply)

    def get_pointer_control_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 106, False, False), \
            GetPointerControlCookie(),
            GetPointerControlReply)

    def set_screen_saver_checked(self, timeout, interval, prefer_blanking, allow_exposures):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxhhBB", timeout, interval, prefer_blanking, allow_exposures))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 107, True, True), \
            ooxcb.VoidCookie())

    def set_screen_saver(self, timeout, interval, prefer_blanking, allow_exposures):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxhhBB", timeout, interval, prefer_blanking, allow_exposures))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 107, True, False), \
            ooxcb.VoidCookie())

    def get_screen_saver(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 108, False, True), \
            GetScreenSaverCookie(),
            GetScreenSaverReply)

    def get_screen_saver_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 108, False, False), \
            GetScreenSaverCookie(),
            GetScreenSaverReply)

    def change_hosts_checked(self, mode, family, address):
        address_len = len(address)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxBxH", mode, family, address_len))
        buf.write(make_array(address, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 109, True, True), \
            ooxcb.VoidCookie())

    def change_hosts(self, mode, family, address):
        address_len = len(address)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxBxH", mode, family, address_len))
        buf.write(make_array(address, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 109, True, False), \
            ooxcb.VoidCookie())

    def list_hosts(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 110, False, True), \
            ListHostsCookie(),
            ListHostsReply)

    def list_hosts_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 110, False, False), \
            ListHostsCookie(),
            ListHostsReply)

    def set_access_control_checked(self, mode):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxx", mode))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 111, True, True), \
            ooxcb.VoidCookie())

    def set_access_control(self, mode):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxx", mode))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 111, True, False), \
            ooxcb.VoidCookie())

    def set_close_down_mode_checked(self, mode):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxx", mode))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 112, True, True), \
            ooxcb.VoidCookie())

    def set_close_down_mode(self, mode):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxx", mode))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 112, True, False), \
            ooxcb.VoidCookie())

    def kill_client_checked(self, resource):
        resource = resource.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", resource))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 113, True, True), \
            ooxcb.VoidCookie())

    def kill_client(self, resource):
        resource = resource.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", resource))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 113, True, False), \
            ooxcb.VoidCookie())

    def force_screen_saver_checked(self, mode):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxx", mode))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 115, True, True), \
            ooxcb.VoidCookie())

    def force_screen_saver(self, mode):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxx", mode))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 115, True, False), \
            ooxcb.VoidCookie())

    def set_pointer_mapping(self, map):
        map_len = len(map)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxx", map_len))
        buf.write(make_array(map, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 116, False, True), \
            SetPointerMappingCookie(),
            SetPointerMappingReply)

    def set_pointer_mapping_unchecked(self, map):
        map_len = len(map)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxx", map_len))
        buf.write(make_array(map, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 116, False, False), \
            SetPointerMappingCookie(),
            SetPointerMappingReply)

    def get_pointer_mapping(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 117, False, True), \
            GetPointerMappingCookie(),
            GetPointerMappingReply)

    def get_pointer_mapping_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 117, False, False), \
            GetPointerMappingCookie(),
            GetPointerMappingReply)

    def set_modifier_mapping(self, keycodes_per_modifier, keycodes):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxx", keycodes_per_modifier))
        buf.write(make_array(keycodes, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 118, False, True), \
            SetModifierMappingCookie(),
            SetModifierMappingReply)

    def set_modifier_mapping_unchecked(self, keycodes_per_modifier, keycodes):
        buf = StringIO.StringIO()
        buf.write(pack("=xBxx", keycodes_per_modifier))
        buf.write(make_array(keycodes, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 118, False, False), \
            SetModifierMappingCookie(),
            SetModifierMappingReply)

    def get_modifier_mapping(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 119, False, True), \
            GetModifierMappingCookie(),
            GetModifierMappingReply)

    def get_modifier_mapping_unchecked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 119, False, False), \
            GetModifierMappingCookie(),
            GetModifierMappingReply)

    def no_operation_checked(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 127, True, True), \
            ooxcb.VoidCookie())

    def no_operation(self):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxx", ))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 127, True, False), \
            ooxcb.VoidCookie())

    def list_all_fonts_with_info(self, max_names, pattern):
        cookie = self.list_fonts_with_info(max_names, pattern)
        ret = []
        while True:
            try:
                reply = cookie.reply()
            except BadAtom:
                break
            if reply.name_len == 0:
                break
            ret.append(reply)
        return ret

class ButtonPressEvent(ooxcb.Event):
    event_name = "on_button_press"
    opcode = 4
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 4
        self.detail = None
        self.time = None
        self.root = None
        self.event = None
        self.child = None
        self.root_x = None
        self.root_y = None
        self.event_x = None
        self.event_y = None
        self.state = None
        self.same_screen = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIIIIhhhhHBx", stream)
        self.response_type = _unpacked[0]
        self.detail = _unpacked[1]
        self.time = _unpacked[2]
        self.root = self.conn.get_from_cache_fallback(_unpacked[3], Window)
        self.event = self.conn.get_from_cache_fallback(_unpacked[4], Window)
        self.child = self.conn.get_from_cache_fallback(_unpacked[5], Window)
        self.root_x = _unpacked[6]
        self.root_y = _unpacked[7]
        self.event_x = _unpacked[8]
        self.event_y = _unpacked[9]
        self.state = _unpacked[10]
        self.same_screen = _unpacked[11]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIIIIhhhhHBx", self.response_type, self.detail, self.time, get_internal(self.root), get_internal(self.event), get_internal(self.child), self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen))
        stream.write("\0" * (32 - (stream.tell() - root)))

class GetKeyboardControlReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.global_auto_repeat = None
        self.led_mask = None
        self.key_click_percent = None
        self.bell_percent = None
        self.bell_pitch = None
        self.bell_duration = None
        self.auto_repeats = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxIBBHHxx", stream)
        self.global_auto_repeat = _unpacked[0]
        self.led_mask = _unpacked[1]
        self.key_click_percent = _unpacked[2]
        self.bell_percent = _unpacked[3]
        self.bell_pitch = _unpacked[4]
        self.bell_duration = _unpacked[5]
        self.auto_repeats = ooxcb.List(self.conn, stream, 32, 'B', 1)

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxIBBHHxx", self.global_auto_repeat, self.led_mask, self.key_click_percent, self.bell_percent, self.bell_pitch, self.bell_duration))
        count += 20
        build_list(self.conn, stream, self.auto_repeats, 'B')

class GetPointerControlCookie(ooxcb.Cookie):
    pass

class GetPropertyCookie(ooxcb.Cookie):
    pass

class GetAtomNameCookie(ooxcb.Cookie):
    pass

class Str(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.name_len = None
        self.name = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=B", stream)
        self.name_len = _unpacked[0]
        self.name = ooxcb.List(self.conn, stream, self.name_len, 'B', 1).to_string()
        self.size = stream.tell() - root

    def build(self, stream):
        count = 0
        stream.write(pack("=B", self.name_len))
        count += 1
        build_list(self.conn, stream, self.name, 'B')

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<ooxcb.protocol.xproto.Str %s>' % repr(self.name)

    def pythonize_lazy(self):
        return self.name

    @classmethod
    def create_lazy(cls, conn, string):
        struct = Str(conn)
        struct.name = string
        struct.name_len = len(string)
        return struct

class AllocColorPlanesReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.pixels_len = None
        self.red_mask = None
        self.green_mask = None
        self.blue_mask = None
        self.pixels = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHxxIIIxxxxxxxx", stream)
        self.pixels_len = _unpacked[0]
        self.red_mask = _unpacked[1]
        self.green_mask = _unpacked[2]
        self.blue_mask = _unpacked[3]
        self.pixels = ooxcb.List(self.conn, stream, self.pixels_len, 'I', 4)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHxxIIIxxxxxxxx", self.pixels_len, self.red_mask, self.green_mask, self.blue_mask))
        count += 32
        build_list(self.conn, stream, self.pixels, 'I')

class CirculateNotifyEvent(ooxcb.Event):
    event_name = "on_circulate_notify"
    opcode = 26
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 26
        self.event = None
        self.window = None
        self.place = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIxxxxBxxx", stream)
        self.response_type = _unpacked[0]
        self.event = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.window = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.place = _unpacked[3]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIxxxxBxxx", self.response_type, get_internal(self.event), get_internal(self.window), self.place))
        stream.write("\0" * (32 - (stream.tell() - root)))

class QueryExtensionCookie(ooxcb.Cookie):
    pass

class GetWindowAttributesCookie(ooxcb.Cookie):
    pass

class GetMotionEventsReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.events_len = None
        self.events = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxIxxxxxxxxxxxxxxxxxxxx", stream)
        self.events_len = _unpacked[0]
        self.events = ooxcb.List(self.conn, stream, self.events_len, Timecoord, 8)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxIxxxxxxxxxxxxxxxxxxxx", self.events_len))
        count += 32
        build_list(self.conn, stream, self.events, Timecoord)

class ListFontsReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.names_len = None
        self.names = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", stream)
        self.names_len = _unpacked[0]
        self.names = ooxcb.List(self.conn, stream, self.names_len, Str, -1)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", self.names_len))
        count += 32
        build_list(self.conn, stream, self.names, Str)

class InternAtomReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.atom = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxI", stream)
        self.atom = self.conn.atoms.get_by_id(_unpacked[0])

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxI", get_internal(self.atom)))

class KeyPressEvent(ooxcb.Event):
    event_name = "on_key_press"
    opcode = 2
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 2
        self.detail = None
        self.time = None
        self.root = None
        self.event = None
        self.child = None
        self.root_x = None
        self.root_y = None
        self.event_x = None
        self.event_y = None
        self.state = None
        self.same_screen = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIIIIhhhhHBx", stream)
        self.response_type = _unpacked[0]
        self.detail = _unpacked[1]
        self.time = _unpacked[2]
        self.root = self.conn.get_from_cache_fallback(_unpacked[3], Window)
        self.event = self.conn.get_from_cache_fallback(_unpacked[4], Window)
        self.child = self.conn.get_from_cache_fallback(_unpacked[5], Window)
        self.root_x = _unpacked[6]
        self.root_y = _unpacked[7]
        self.event_x = _unpacked[8]
        self.event_y = _unpacked[9]
        self.state = _unpacked[10]
        self.same_screen = _unpacked[11]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIIIIhhhhHBx", self.response_type, self.detail, self.time, get_internal(self.root), get_internal(self.event), get_internal(self.child), self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen))
        stream.write("\0" * (32 - (stream.tell() - root)))

class GetPointerControlReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.acceleration_numerator = None
        self.acceleration_denominator = None
        self.threshold = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHHHxxxxxxxxxxxxxxxxxx", stream)
        self.acceleration_numerator = _unpacked[0]
        self.acceleration_denominator = _unpacked[1]
        self.threshold = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHHHxxxxxxxxxxxxxxxxxx", self.acceleration_numerator, self.acceleration_denominator, self.threshold))

class GetFontPathCookie(ooxcb.Cookie):
    pass

class LeaveNotifyEvent(ooxcb.Event):
    event_name = "on_leave_notify"
    opcode = 8
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 8
        self.detail = None
        self.time = None
        self.root = None
        self.event = None
        self.child = None
        self.root_x = None
        self.root_y = None
        self.event_x = None
        self.event_y = None
        self.state = None
        self.mode = None
        self.same_screen_focus = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIIIIhhhhHBB", stream)
        self.response_type = _unpacked[0]
        self.detail = _unpacked[1]
        self.time = _unpacked[2]
        self.root = self.conn.get_from_cache_fallback(_unpacked[3], Window)
        self.event = self.conn.get_from_cache_fallback(_unpacked[4], Window)
        self.child = self.conn.get_from_cache_fallback(_unpacked[5], Window)
        self.root_x = _unpacked[6]
        self.root_y = _unpacked[7]
        self.event_x = _unpacked[8]
        self.event_y = _unpacked[9]
        self.state = _unpacked[10]
        self.mode = _unpacked[11]
        self.same_screen_focus = _unpacked[12]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIIIIhhhhHBB", self.response_type, self.detail, self.time, get_internal(self.root), get_internal(self.event), get_internal(self.child), self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.mode, self.same_screen_focus))
        stream.write("\0" * (32 - (stream.tell() - root)))

class QueryColorsCookie(ooxcb.Cookie):
    pass

class AtomError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class ListHostsCookie(ooxcb.Cookie):
    pass

class GetMotionEventsCookie(ooxcb.Cookie):
    pass

class Pixmap(Drawable):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def free_checked(self):
        pixmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", pixmap))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 54, True, True), \
            ooxcb.VoidCookie())

    def free(self):
        pixmap = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", pixmap))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 54, True, False), \
            ooxcb.VoidCookie())

    @classmethod
    def create(cls, conn, drawable, width, height, depth):
        pid = conn.generate_id()
        pixmap = cls(conn, pid)
        conn.core.create_pixmap_checked(depth, pixmap, drawable, width, height).check()
        return pixmap

class MapNotifyEvent(ooxcb.Event):
    event_name = "on_map_notify"
    opcode = 19
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 19
        self.event = None
        self.window = None
        self.override_redirect = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIBxxx", stream)
        self.response_type = _unpacked[0]
        self.event = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.window = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.override_redirect = _unpacked[3]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIBxxx", self.response_type, get_internal(self.event), get_internal(self.window), self.override_redirect))
        stream.write("\0" * (32 - (stream.tell() - root)))

class GetAtomNameReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.name_len = None
        self.name = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", stream)
        self.name_len = _unpacked[0]
        self.name = ooxcb.List(self.conn, stream, self.name_len, 'B', 1).to_string()

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", self.name_len))
        count += 32
        build_list(self.conn, stream, self.name, 'B')

class Fontprop(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.name = None
        self.value = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=II", stream)
        self.name = self.conn.atoms.get_by_id(_unpacked[0])
        self.value = _unpacked[1]

    def build(self, stream):
        count = 0
        stream.write(pack("=II", get_internal(self.name), self.value))

class Window(Drawable):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def change_attributes_checked(self, **values):
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
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", window, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, True), \
            ooxcb.VoidCookie())

    def change_attributes(self, **values):
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
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", window, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, False), \
            ooxcb.VoidCookie())

    def get_attributes(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, False, True), \
            GetWindowAttributesCookie(),
            GetWindowAttributesReply)

    def get_attributes_unchecked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, False, False), \
            GetWindowAttributesCookie(),
            GetWindowAttributesReply)

    def destroy_checked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, True), \
            ooxcb.VoidCookie())

    def destroy(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, False), \
            ooxcb.VoidCookie())

    def destroy_subwindows_checked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, True, True), \
            ooxcb.VoidCookie())

    def destroy_subwindows(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 5, True, False), \
            ooxcb.VoidCookie())

    def change_save_set_checked(self, mode):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxI", mode, window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 6, True, True), \
            ooxcb.VoidCookie())

    def change_save_set(self, mode):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxI", mode, window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 6, True, False), \
            ooxcb.VoidCookie())

    def reparent_checked(self, parent, x=0, y=0):
        window = get_internal(self)
        parent = get_internal(parent)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", window, parent, x, y))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 7, True, True), \
            ooxcb.VoidCookie())

    def reparent(self, parent, x=0, y=0):
        window = get_internal(self)
        parent = get_internal(parent)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", window, parent, x, y))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 7, True, False), \
            ooxcb.VoidCookie())

    def map_checked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 8, True, True), \
            ooxcb.VoidCookie())

    def map(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 8, True, False), \
            ooxcb.VoidCookie())

    def map_subwindows_checked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 9, True, True), \
            ooxcb.VoidCookie())

    def map_subwindows(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 9, True, False), \
            ooxcb.VoidCookie())

    def unmap_checked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 10, True, True), \
            ooxcb.VoidCookie())

    def unmap(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 10, True, False), \
            ooxcb.VoidCookie())

    def unmap_subwindows_checked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 11, True, True), \
            ooxcb.VoidCookie())

    def unmap_subwindows(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 11, True, False), \
            ooxcb.VoidCookie())

    def configure_checked(self, **values):
        value_mask, value_list = 0, []
        if "x" in values:
            value_mask |= 1
            value_list.append(values["x"])
        if "y" in values:
            value_mask |= 2
            value_list.append(values["y"])
        if "width" in values:
            value_mask |= 4
            value_list.append(values["width"])
        if "height" in values:
            value_mask |= 8
            value_list.append(values["height"])
        if "border_width" in values:
            value_mask |= 16
            value_list.append(values["border_width"])
        if "sibling" in values:
            value_mask |= 32
            value_list.append(get_internal(values["sibling"]))
        if "stack_mode" in values:
            value_mask |= 64
            value_list.append(values["stack_mode"])
        window = self.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIH", window, value_mask))
        buf.write(pack("=xx"))
        if value_mask & ConfigWindow.X:
            buf.write(pack("=i", value_list[0]))
            del value_list[0]
        if value_mask & ConfigWindow.Y:
            buf.write(pack("=i", value_list[0]))
            del value_list[0]
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 12, True, True), \
            ooxcb.VoidCookie())

    def configure(self, **values):
        value_mask, value_list = 0, []
        if "x" in values:
            value_mask |= 1
            value_list.append(values["x"])
        if "y" in values:
            value_mask |= 2
            value_list.append(values["y"])
        if "width" in values:
            value_mask |= 4
            value_list.append(values["width"])
        if "height" in values:
            value_mask |= 8
            value_list.append(values["height"])
        if "border_width" in values:
            value_mask |= 16
            value_list.append(values["border_width"])
        if "sibling" in values:
            value_mask |= 32
            value_list.append(get_internal(values["sibling"]))
        if "stack_mode" in values:
            value_mask |= 64
            value_list.append(values["stack_mode"])
        window = self.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIH", window, value_mask))
        buf.write(pack("=xx"))
        if value_mask & ConfigWindow.X:
            buf.write(pack("=i", value_list[0]))
            del value_list[0]
        if value_mask & ConfigWindow.Y:
            buf.write(pack("=i", value_list[0]))
            del value_list[0]
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 12, True, False), \
            ooxcb.VoidCookie())

    def circulate_window_checked(self, direction):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxI", direction, window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 13, True, True), \
            ooxcb.VoidCookie())

    def circulate_window(self, direction):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxI", direction, window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 13, True, False), \
            ooxcb.VoidCookie())

    def query_tree(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 15, False, True), \
            QueryTreeCookie(),
            QueryTreeReply)

    def query_tree_unchecked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 15, False, False), \
            QueryTreeCookie(),
            QueryTreeReply)

    def change_property_checked(self, property, type, format, data, mode=PropMode.Replace):
        data_len = len(data)
        if isinstance(property, basestring):
            property = self.conn.atoms[property]
        if isinstance(type, basestring):
            type = self.conn.atoms[type]
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIIBxxxI", mode, self.get_internal(), property.get_internal(), type.get_internal(), format, data_len))
        buf.write(make_void_array(data, format))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 18, True, True), \
            ooxcb.VoidCookie())

    def change_property(self, property, type, format, data, mode=PropMode.Replace):
        data_len = len(data)
        if isinstance(property, basestring):
            property = self.conn.atoms[property]
        if isinstance(type, basestring):
            type = self.conn.atoms[type]
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIIBxxxI", mode, self.get_internal(), property.get_internal(), type.get_internal(), format, data_len))
        buf.write(make_void_array(data, format))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 18, True, False), \
            ooxcb.VoidCookie())

    def delete_property_checked(self, property):
        if isinstance(property, basestring):
            property = self.conn.atoms[property]
        window = get_internal(self)
        property = get_internal(property)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", window, property))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 19, True, True), \
            ooxcb.VoidCookie())

    def delete_property(self, property):
        if isinstance(property, basestring):
            property = self.conn.atoms[property]
        window = get_internal(self)
        property = get_internal(property)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", window, property))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 19, True, False), \
            ooxcb.VoidCookie())

    def get_property(self, property, type, delete=False, long_offset=0, long_length=2**32-1):
        if isinstance(property, basestring):
            property = self.conn.atoms[property]
        if isinstance(type, basestring):
            type = self.conn.atoms[type]
        window = get_internal(self)
        property = get_internal(property)
        type = get_internal(type)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIIII", delete, window, property, type, long_offset, long_length))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 20, False, True), \
            GetPropertyCookie(),
            GetPropertyReply)

    def get_property_unchecked(self, property, type, delete=False, long_offset=0, long_length=2**32-1):
        if isinstance(property, basestring):
            property = self.conn.atoms[property]
        if isinstance(type, basestring):
            type = self.conn.atoms[type]
        window = get_internal(self)
        property = get_internal(property)
        type = get_internal(type)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIIII", delete, window, property, type, long_offset, long_length))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 20, False, False), \
            GetPropertyCookie(),
            GetPropertyReply)

    def list_properties(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 21, False, True), \
            ListPropertiesCookie(),
            ListPropertiesReply)

    def list_properties_unchecked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 21, False, False), \
            ListPropertiesCookie(),
            ListPropertiesReply)

    def send_event_checked(self, event_mask, event, propagate=False):
        destination = self.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxII", propagate, destination, event_mask))
        event.build(buf)
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 25, True, True), \
            ooxcb.VoidCookie())

    def send_event(self, event_mask, event, propagate=False):
        destination = self.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxII", propagate, destination, event_mask))
        event.build(buf)
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 25, True, False), \
            ooxcb.VoidCookie())

    def grab_pointer(self, event_mask, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async, confine_to=None, cursor=None, time=Time.CurrentTime):
        grab_window = get_internal(self)
        confine_to = get_internal(confine_to)
        cursor = get_internal(cursor)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHBBIII", owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 26, False, True), \
            GrabPointerCookie(),
            GrabPointerReply)

    def grab_pointer_unchecked(self, event_mask, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async, confine_to=None, cursor=None, time=Time.CurrentTime):
        grab_window = get_internal(self)
        confine_to = get_internal(confine_to)
        cursor = get_internal(cursor)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHBBIII", owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 26, False, False), \
            GrabPointerCookie(),
            GrabPointerReply)

    def grab_button_checked(self, event_mask, button, modifiers, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async, confine_to=None, cursor=None):
        grab_window = get_internal(self)
        confine_to = get_internal(confine_to)
        cursor = get_internal(cursor)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHBBIIBxH", owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, button, modifiers))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 28, True, True), \
            ooxcb.VoidCookie())

    def grab_button(self, event_mask, button, modifiers, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async, confine_to=None, cursor=None):
        grab_window = get_internal(self)
        confine_to = get_internal(confine_to)
        cursor = get_internal(cursor)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHBBIIBxH", owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, button, modifiers))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 28, True, False), \
            ooxcb.VoidCookie())

    def ungrab_button_checked(self, button, modifiers):
        grab_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHxx", button, grab_window, modifiers))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 29, True, True), \
            ooxcb.VoidCookie())

    def ungrab_button(self, button, modifiers):
        grab_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHxx", button, grab_window, modifiers))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 29, True, False), \
            ooxcb.VoidCookie())

    def grab_keyboard(self, owner_events=True, time=Time.CurrentTime, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async):
        grab_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIBBxx", owner_events, grab_window, time, pointer_mode, keyboard_mode))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 31, False, True), \
            GrabKeyboardCookie(),
            GrabKeyboardReply)

    def grab_keyboard_unchecked(self, owner_events=True, time=Time.CurrentTime, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async):
        grab_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIBBxx", owner_events, grab_window, time, pointer_mode, keyboard_mode))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 31, False, False), \
            GrabKeyboardCookie(),
            GrabKeyboardReply)

    def grab_key_checked(self, key, modifiers, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async):
        grab_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHBBBxxx", owner_events, grab_window, modifiers, key, pointer_mode, keyboard_mode))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 33, True, True), \
            ooxcb.VoidCookie())

    def grab_key(self, key, modifiers, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async):
        grab_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHBBBxxx", owner_events, grab_window, modifiers, key, pointer_mode, keyboard_mode))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 33, True, False), \
            ooxcb.VoidCookie())

    def ungrab_key_checked(self, key, modifiers):
        grab_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHxx", key, grab_window, modifiers))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 34, True, True), \
            ooxcb.VoidCookie())

    def ungrab_key(self, key, modifiers):
        grab_window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIHxx", key, grab_window, modifiers))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 34, True, False), \
            ooxcb.VoidCookie())

    def query_pointer(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 38, False, True), \
            QueryPointerCookie(),
            QueryPointerReply)

    def query_pointer_unchecked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 38, False, False), \
            QueryPointerCookie(),
            QueryPointerReply)

    def get_motion_events(self, start, stop):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", window, start, stop))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 39, False, True), \
            GetMotionEventsCookie(),
            GetMotionEventsReply)

    def get_motion_events_unchecked(self, start, stop):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", window, start, stop))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 39, False, False), \
            GetMotionEventsCookie(),
            GetMotionEventsReply)

    def translate_coordinates(self, dst_window, src_x, src_y):
        src_window = get_internal(self)
        dst_window = get_internal(dst_window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", src_window, dst_window, src_x, src_y))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 40, False, True), \
            TranslateCoordinatesCookie(),
            TranslateCoordinatesReply)

    def translate_coordinates_unchecked(self, dst_window, src_x, src_y):
        src_window = get_internal(self)
        dst_window = get_internal(dst_window)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", src_window, dst_window, src_x, src_y))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 40, False, False), \
            TranslateCoordinatesCookie(),
            TranslateCoordinatesReply)

    def set_input_focus_checked(self, revert_to=InputFocus.PointerRoot, time=Time.CurrentTime):
        focus = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxII", revert_to, focus, time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 42, True, True), \
            ooxcb.VoidCookie())

    def set_input_focus(self, revert_to=InputFocus.PointerRoot, time=Time.CurrentTime):
        focus = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxII", revert_to, focus, time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 42, True, False), \
            ooxcb.VoidCookie())

    def clear_area_checked(self, x, y, width, height, exposures=False):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIhhHH", exposures, window, x, y, width, height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 61, True, True), \
            ooxcb.VoidCookie())

    def clear_area(self, x, y, width, height, exposures=False):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIhhHH", exposures, window, x, y, width, height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 61, True, False), \
            ooxcb.VoidCookie())

    def list_installed_colormaps(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 83, False, True), \
            ListInstalledColormapsCookie(),
            ListInstalledColormapsReply)

    def list_installed_colormaps_unchecked(self):
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", window))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 83, False, False), \
            ListInstalledColormapsCookie(),
            ListInstalledColormapsReply)

    def rotate_properties_checked(self, atoms, delta):
        atoms_ = []
        for atom in atoms_:
            atoms.append(atom.get_internal())
        atoms_len = len(atoms_)
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHh", window, atoms_len, delta))
        buf.write(make_array(atoms, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 114, True, True), \
            ooxcb.VoidCookie())

    def rotate_properties(self, atoms, delta):
        atoms_ = []
        for atom in atoms_:
            atoms.append(atom.get_internal())
        atoms_len = len(atoms_)
        window = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHh", window, atoms_len, delta))
        buf.write(make_array(atoms, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 114, True, False), \
            ooxcb.VoidCookie())

    @classmethod
    def create(cls, conn, parent, depth, visual, x=0, y=0, width=640, height=480, border_width=0, _class=WindowClass.InputOutput, **values):
        wid = conn.generate_id()
        win = cls(conn, wid)
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
        conn.core.create_window_checked(depth, win, parent, x, y, width, height, border_width, _class, visual, value_mask, value_list).check()
        conn.add_to_cache(wid, win)
        return win

    @classmethod
    def create_toplevel_on_screen(cls, conn, screen, *args, **kwargs):
        return cls.create(conn, screen.root, screen.root_depth, screen.root_visual, *args, **kwargs)

    def add_to_save_set(self):
        self.change_save_set_checked(SetMode.Insert).check()

    def remove_from_save_set(self):
        self.change_save_set_checked(SetMode.Delete).check()

class Timecoord(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.time = None
        self.x = None
        self.y = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=Ihh", stream)
        self.time = _unpacked[0]
        self.x = _unpacked[1]
        self.y = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=Ihh", self.time, self.x, self.y))

class QueryBestSizeReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.width = None
        self.height = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHH", stream)
        self.width = _unpacked[0]
        self.height = _unpacked[1]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHH", self.width, self.height))

class VisibilityNotifyEvent(ooxcb.Event):
    event_name = "on_visibility_notify"
    opcode = 15
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 15
        self.window = None
        self.state = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIBxxx", stream)
        self.response_type = _unpacked[0]
        self.window = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.state = _unpacked[2]
        self.event_target = self.window

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIBxxx", self.response_type, get_internal(self.window), self.state))
        stream.write("\0" * (32 - (stream.tell() - root)))

class FocusOutEvent(ooxcb.Event):
    event_name = "on_focus_out"
    opcode = 10
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 10
        self.detail = None
        self.event = None
        self.mode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIBxxx", stream)
        self.response_type = _unpacked[0]
        self.detail = _unpacked[1]
        self.event = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.mode = _unpacked[3]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIBxxx", self.response_type, self.detail, get_internal(self.event), self.mode))
        stream.write("\0" * (32 - (stream.tell() - root)))

class Format(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.depth = None
        self.bits_per_pixel = None
        self.scanline_pad = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBBxxxxx", stream)
        self.depth = _unpacked[0]
        self.bits_per_pixel = _unpacked[1]
        self.scanline_pad = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=BBBxxxxx", self.depth, self.bits_per_pixel, self.scanline_pad))

class ColormapNotifyEvent(ooxcb.Event):
    event_name = "on_colormap_notify"
    opcode = 32
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 32
        self.window = None
        self.colormap = None
        self.new = None
        self.state = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIBBxx", stream)
        self.response_type = _unpacked[0]
        self.window = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.colormap = self.conn.get_from_cache_fallback(_unpacked[2], Colormap)
        self.new = _unpacked[3]
        self.state = _unpacked[4]
        self.event_target = self.window

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIBBxx", self.response_type, get_internal(self.window), get_internal(self.colormap), self.new, self.state))
        stream.write("\0" * (32 - (stream.tell() - root)))

class CirculateRequestEvent(ooxcb.Event):
    event_name = "on_circulate_request"
    opcode = 27
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 27
        self.event = None
        self.window = None
        self.place = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIxxxxBxxx", stream)
        self.response_type = _unpacked[0]
        self.event = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.window = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.place = _unpacked[3]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIxxxxBxxx", self.response_type, get_internal(self.event), get_internal(self.window), self.place))
        stream.write("\0" * (32 - (stream.tell() - root)))

class QueryFontReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.min_bounds = None
        self.max_bounds = None
        self.min_char_or_byte2 = None
        self.max_char_or_byte2 = None
        self.default_char = None
        self.properties_len = None
        self.draw_direction = None
        self.min_byte1 = None
        self.max_byte1 = None
        self.all_chars_exist = None
        self.font_ascent = None
        self.font_descent = None
        self.char_infos_len = None
        self.properties = []
        self.char_infos = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        stream.seek(8, 1)
        self.min_bounds = Charinfo.create_from_stream(self.conn, stream)
        stream.seek(4, 1)
        stream.seek(ooxcb.type_pad(12, stream.tell() - root), 1)
        self.max_bounds = Charinfo.create_from_stream(self.conn, stream)
        _unpacked = unpack_from_stream("=xxxxHHHHBBBBhhI", stream)
        self.min_char_or_byte2 = _unpacked[0]
        self.max_char_or_byte2 = _unpacked[1]
        self.default_char = _unpacked[2]
        self.properties_len = _unpacked[3]
        self.draw_direction = _unpacked[4]
        self.min_byte1 = _unpacked[5]
        self.max_byte1 = _unpacked[6]
        self.all_chars_exist = _unpacked[7]
        self.font_ascent = _unpacked[8]
        self.font_descent = _unpacked[9]
        self.char_infos_len = _unpacked[10]
        stream.seek(ooxcb.type_pad(8, stream.tell() - root), 1)
        self.properties = ooxcb.List(self.conn, stream, self.properties_len, Fontprop, 8)
        stream.seek(ooxcb.type_pad(12, stream.tell() - root), 1)
        self.char_infos = ooxcb.List(self.conn, stream, self.char_infos_len, Charinfo, 12)

    def build(self, stream):
        count = 0
        count += 8
        self.min_bounds.build(stream)
        count += 4
        self.max_bounds.build(stream)
        stream.write(pack("=xxxxHHHHBBBBhhI", self.min_char_or_byte2, self.max_char_or_byte2, self.default_char, self.properties_len, self.draw_direction, self.min_byte1, self.max_byte1, self.all_chars_exist, self.font_ascent, self.font_descent, self.char_infos_len))
        count += 24
        build_list(self.conn, stream, self.properties, Fontprop)
        build_list(self.conn, stream, self.char_infos, Charinfo)

class CreateNotifyEvent(ooxcb.Event):
    event_name = "on_create_notify"
    opcode = 16
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 16
        self.parent = None
        self.window = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.border_width = None
        self.override_redirect = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIhhHHHBx", stream)
        self.response_type = _unpacked[0]
        self.parent = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.window = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.x = _unpacked[3]
        self.y = _unpacked[4]
        self.width = _unpacked[5]
        self.height = _unpacked[6]
        self.border_width = _unpacked[7]
        self.override_redirect = _unpacked[8]
        self.event_target = self.parent

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIhhHHHBx", self.response_type, get_internal(self.parent), get_internal(self.window), self.x, self.y, self.width, self.height, self.border_width, self.override_redirect))
        stream.write("\0" * (32 - (stream.tell() - root)))

class ResizeRequestEvent(ooxcb.Event):
    event_name = "on_resize_request"
    opcode = 25
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 25
        self.window = None
        self.width = None
        self.height = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIHH", stream)
        self.response_type = _unpacked[0]
        self.window = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.width = _unpacked[2]
        self.height = _unpacked[3]
        self.event_target = self.window

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIHH", self.response_type, get_internal(self.window), self.width, self.height))
        stream.write("\0" * (32 - (stream.tell() - root)))

class QueryColorsReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.colors_len = None
        self.colors = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", stream)
        self.colors_len = _unpacked[0]
        self.colors = ooxcb.List(self.conn, stream, self.colors_len, Rgb, 8)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", self.colors_len))
        count += 32
        build_list(self.conn, stream, self.colors, Rgb)

class MotionNotifyEvent(ooxcb.Event):
    event_name = "on_motion_notify"
    opcode = 6
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 6
        self.detail = None
        self.time = None
        self.root = None
        self.event = None
        self.child = None
        self.root_x = None
        self.root_y = None
        self.event_x = None
        self.event_y = None
        self.state = None
        self.same_screen = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIIIIhhhhHBx", stream)
        self.response_type = _unpacked[0]
        self.detail = _unpacked[1]
        self.time = _unpacked[2]
        self.root = self.conn.get_from_cache_fallback(_unpacked[3], Window)
        self.event = self.conn.get_from_cache_fallback(_unpacked[4], Window)
        self.child = self.conn.get_from_cache_fallback(_unpacked[5], Window)
        self.root_x = _unpacked[6]
        self.root_y = _unpacked[7]
        self.event_x = _unpacked[8]
        self.event_y = _unpacked[9]
        self.state = _unpacked[10]
        self.same_screen = _unpacked[11]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIIIIhhhhHBx", self.response_type, self.detail, self.time, get_internal(self.root), get_internal(self.event), get_internal(self.child), self.root_x, self.root_y, self.event_x, self.event_y, self.state, self.same_screen))
        stream.write("\0" * (32 - (stream.tell() - root)))

class Atom(ooxcb.Resource):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def get_name(self):
        atom = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", atom))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 17, False, True), \
            GetAtomNameCookie(),
            GetAtomNameReply)

    def get_name_unchecked(self):
        atom = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", atom))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 17, False, False), \
            GetAtomNameCookie(),
            GetAtomNameReply)

    def set_selection_owner_checked(self, owner=None, time=0):
        owner = get_internal(owner)
        selection = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", owner, selection, time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 22, True, True), \
            ooxcb.VoidCookie())

    def set_selection_owner(self, owner=None, time=0):
        owner = get_internal(owner)
        selection = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", owner, selection, time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 22, True, False), \
            ooxcb.VoidCookie())

    def get_selection_owner(self):
        selection = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", selection))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 23, False, True), \
            GetSelectionOwnerCookie(),
            GetSelectionOwnerReply)

    def get_selection_owner_unchecked(self):
        selection = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", selection))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 23, False, False), \
            GetSelectionOwnerCookie(),
            GetSelectionOwnerReply)

    def convert_selection_checked(self, requestor, target, property=None, time=0):
        requestor = get_internal(requestor)
        selection = get_internal(self)
        target = get_internal(target)
        property = get_internal(property)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIIII", requestor, selection, target, property, time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 24, True, True), \
            ooxcb.VoidCookie())

    def convert_selection(self, requestor, target, property=None, time=0):
        requestor = get_internal(requestor)
        selection = get_internal(self)
        target = get_internal(target)
        property = get_internal(property)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIIII", requestor, selection, target, property, time))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 24, True, False), \
            ooxcb.VoidCookie())

    def __repr__(self):
        if self.has_cached_name:
            return '<Atom ID=%d (0x%x) name=%s>' % (self.xid, id(self), self.name)
        else:
            return '<Atom ID=%d (0x%x)>' % (self.xid, id(self))

    @property
    def name(self):
        if not self.has_cached_name:
            self._cache_name(self.get_name().reply().name)
        return self._cached_name

    def _cache_name(self, name):
        self._cached_name = name

    @property
    def has_cached_name(self):
        return hasattr(self, '_cached_name')

class SetPointerMappingReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.status = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxx", stream)
        self.status = _unpacked[0]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxx", self.status))

class Segment(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=hhhh", stream)
        self.x1 = _unpacked[0]
        self.y1 = _unpacked[1]
        self.x2 = _unpacked[2]
        self.y2 = _unpacked[3]

    def build(self, stream):
        count = 0
        stream.write(pack("=hhhh", self.x1, self.y1, self.x2, self.y2))

class ValueError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class GetInputFocusReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.revert_to = None
        self.focus = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxI", stream)
        self.revert_to = _unpacked[0]
        self.focus = self.conn.get_from_cache_fallback(_unpacked[1], Window)

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxI", self.revert_to, get_internal(self.focus)))

class MappingNotifyEvent(ooxcb.Event):
    event_name = "on_mapping_notify"
    opcode = 34
    event_target_class = ooxcb.Connection
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 34
        self.request = None
        self.first_keycode = None
        self.count = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxBBBx", stream)
        self.response_type = _unpacked[0]
        self.request = _unpacked[1]
        self.first_keycode = _unpacked[2]
        self.count = _unpacked[3]
        self.event_target = self.conn

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxBBBx", self.response_type, self.request, self.first_keycode, self.count))
        stream.write("\0" * (32 - (stream.tell() - root)))

class GetGeometryReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.depth = None
        self.root = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.border_width = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxIhhHHHxx", stream)
        self.depth = _unpacked[0]
        self.root = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.x = _unpacked[2]
        self.y = _unpacked[3]
        self.width = _unpacked[4]
        self.height = _unpacked[5]
        self.border_width = _unpacked[6]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxIhhHHHxx", self.depth, get_internal(self.root), self.x, self.y, self.width, self.height, self.border_width))

class SelectionRequestEvent(ooxcb.Event):
    event_name = "on_selection_request"
    opcode = 30
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 30
        self.time = None
        self.owner = None
        self.requestor = None
        self.selection = None
        self.target = None
        self.property = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIIIII", stream)
        self.response_type = _unpacked[0]
        self.time = _unpacked[1]
        self.owner = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.requestor = self.conn.get_from_cache_fallback(_unpacked[3], Window)
        self.selection = self.conn.atoms.get_by_id(_unpacked[4])
        self.target = self.conn.atoms.get_by_id(_unpacked[5])
        self.property = self.conn.atoms.get_by_id(_unpacked[6])
        self.event_target = self.owner

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIIIII", self.response_type, self.time, get_internal(self.owner), get_internal(self.requestor), get_internal(self.selection), get_internal(self.target), get_internal(self.property)))
        stream.write("\0" * (32 - (stream.tell() - root)))

class BadWindow(ooxcb.ProtocolException):
    pass

class Depth(ooxcb.Struct):
    def __init__(self, conn):
        ooxcb.Struct.__init__(self, conn)
        self.depth = None
        self.visuals_len = None
        self.visuals = []

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=BxHxxxx", stream)
        self.depth = _unpacked[0]
        self.visuals_len = _unpacked[1]
        self.visuals = ooxcb.List(self.conn, stream, self.visuals_len, Visualtype, 24)
        self.size = stream.tell() - root

    def build(self, stream):
        count = 0
        stream.write(pack("=BxHxxxx", self.depth, self.visuals_len))
        count += 8
        build_list(self.conn, stream, self.visuals, Visualtype)

class ListExtensionsCookie(ooxcb.Cookie):
    pass

class CursorError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class FocusInEvent(ooxcb.Event):
    event_name = "on_focus_in"
    opcode = 9
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 9
        self.detail = None
        self.event = None
        self.mode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BBxxIBxxx", stream)
        self.response_type = _unpacked[0]
        self.detail = _unpacked[1]
        self.event = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.mode = _unpacked[3]
        self.event_target = self.event

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIBxxx", self.response_type, self.detail, get_internal(self.event), self.mode))
        stream.write("\0" * (32 - (stream.tell() - root)))

class GContext(Fontable):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def change_checked(self, **values):
        value_mask, value_list = 0, []
        if "function" in values:
            value_mask |= 1
            value_list.append(values["function"])
        if "plane_mask" in values:
            value_mask |= 2
            value_list.append(values["plane_mask"])
        if "foreground" in values:
            value_mask |= 4
            value_list.append(values["foreground"])
        if "background" in values:
            value_mask |= 8
            value_list.append(values["background"])
        if "line_width" in values:
            value_mask |= 16
            value_list.append(values["line_width"])
        if "line_style" in values:
            value_mask |= 32
            value_list.append(values["line_style"])
        if "cap_style" in values:
            value_mask |= 64
            value_list.append(values["cap_style"])
        if "join_style" in values:
            value_mask |= 128
            value_list.append(values["join_style"])
        if "fill_style" in values:
            value_mask |= 256
            value_list.append(values["fill_style"])
        if "fill_rule" in values:
            value_mask |= 512
            value_list.append(values["fill_rule"])
        if "tile" in values:
            value_mask |= 1024
            value_list.append(values["tile"])
        if "stipple" in values:
            value_mask |= 2048
            value_list.append(values["stipple"])
        if "tile_stipple_origin_x" in values:
            value_mask |= 4096
            value_list.append(values["tile_stipple_origin_x"])
        if "tile_stipple_origin_y" in values:
            value_mask |= 8192
            value_list.append(values["tile_stipple_origin_y"])
        if "font" in values:
            value_mask |= 16384
            value_list.append(get_internal(values["font"]))
        if "subwindow_mode" in values:
            value_mask |= 32768
            value_list.append(values["subwindow_mode"])
        if "graphics_exposures" in values:
            value_mask |= 65536
            value_list.append(values["graphics_exposures"])
        if "clip_origin_x" in values:
            value_mask |= 131072
            value_list.append(values["clip_origin_x"])
        if "clip_origin_y" in values:
            value_mask |= 262144
            value_list.append(values["clip_origin_y"])
        if "clip_mask" in values:
            value_mask |= 524288
            value_list.append(values["clip_mask"])
        if "dash_offset" in values:
            value_mask |= 1048576
            value_list.append(values["dash_offset"])
        if "dash_list" in values:
            value_mask |= 2097152
            value_list.append(values["dash_list"])
        if "arc_mode" in values:
            value_mask |= 4194304
            value_list.append(values["arc_mode"])
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", gc, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 56, True, True), \
            ooxcb.VoidCookie())

    def change(self, **values):
        value_mask, value_list = 0, []
        if "function" in values:
            value_mask |= 1
            value_list.append(values["function"])
        if "plane_mask" in values:
            value_mask |= 2
            value_list.append(values["plane_mask"])
        if "foreground" in values:
            value_mask |= 4
            value_list.append(values["foreground"])
        if "background" in values:
            value_mask |= 8
            value_list.append(values["background"])
        if "line_width" in values:
            value_mask |= 16
            value_list.append(values["line_width"])
        if "line_style" in values:
            value_mask |= 32
            value_list.append(values["line_style"])
        if "cap_style" in values:
            value_mask |= 64
            value_list.append(values["cap_style"])
        if "join_style" in values:
            value_mask |= 128
            value_list.append(values["join_style"])
        if "fill_style" in values:
            value_mask |= 256
            value_list.append(values["fill_style"])
        if "fill_rule" in values:
            value_mask |= 512
            value_list.append(values["fill_rule"])
        if "tile" in values:
            value_mask |= 1024
            value_list.append(values["tile"])
        if "stipple" in values:
            value_mask |= 2048
            value_list.append(values["stipple"])
        if "tile_stipple_origin_x" in values:
            value_mask |= 4096
            value_list.append(values["tile_stipple_origin_x"])
        if "tile_stipple_origin_y" in values:
            value_mask |= 8192
            value_list.append(values["tile_stipple_origin_y"])
        if "font" in values:
            value_mask |= 16384
            value_list.append(get_internal(values["font"]))
        if "subwindow_mode" in values:
            value_mask |= 32768
            value_list.append(values["subwindow_mode"])
        if "graphics_exposures" in values:
            value_mask |= 65536
            value_list.append(values["graphics_exposures"])
        if "clip_origin_x" in values:
            value_mask |= 131072
            value_list.append(values["clip_origin_x"])
        if "clip_origin_y" in values:
            value_mask |= 262144
            value_list.append(values["clip_origin_y"])
        if "clip_mask" in values:
            value_mask |= 524288
            value_list.append(values["clip_mask"])
        if "dash_offset" in values:
            value_mask |= 1048576
            value_list.append(values["dash_offset"])
        if "dash_list" in values:
            value_mask |= 2097152
            value_list.append(values["dash_list"])
        if "arc_mode" in values:
            value_mask |= 4194304
            value_list.append(values["arc_mode"])
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", gc, value_mask))
        buf.write(make_array(value_list, "I"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 56, True, False), \
            ooxcb.VoidCookie())

    def copy_checked(self, values=()):
        value_mask = 0
        if "function" in values:
            value_mask |= 1
        if "plane_mask" in values:
            value_mask |= 2
        if "foreground" in values:
            value_mask |= 4
        if "background" in values:
            value_mask |= 8
        if "line_width" in values:
            value_mask |= 16
        if "line_style" in values:
            value_mask |= 32
        if "cap_style" in values:
            value_mask |= 64
        if "join_style" in values:
            value_mask |= 128
        if "fill_style" in values:
            value_mask |= 256
        if "fill_rule" in values:
            value_mask |= 512
        if "tile" in values:
            value_mask |= 1024
        if "stipple" in values:
            value_mask |= 2048
        if "tile_stipple_origin_x" in values:
            value_mask |= 4096
        if "tile_stipple_origin_y" in values:
            value_mask |= 8192
        if "font" in values:
            value_mask |= 16384
        if "subwindow_mode" in values:
            value_mask |= 32768
        if "graphics_exposures" in values:
            value_mask |= 65536
        if "clip_origin_x" in values:
            value_mask |= 131072
        if "clip_origin_y" in values:
            value_mask |= 262144
        if "clip_mask" in values:
            value_mask |= 524288
        if "dash_offset" in values:
            value_mask |= 1048576
        if "dash_list" in values:
            value_mask |= 2097152
        if "arc_mode" in values:
            value_mask |= 4194304
        src_gc = get_internal(self)
        dst_gc = get_internal(dst_gc)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", src_gc, dst_gc, value_mask))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 57, True, True), \
            ooxcb.VoidCookie())

    def copy(self, values=()):
        value_mask = 0
        if "function" in values:
            value_mask |= 1
        if "plane_mask" in values:
            value_mask |= 2
        if "foreground" in values:
            value_mask |= 4
        if "background" in values:
            value_mask |= 8
        if "line_width" in values:
            value_mask |= 16
        if "line_style" in values:
            value_mask |= 32
        if "cap_style" in values:
            value_mask |= 64
        if "join_style" in values:
            value_mask |= 128
        if "fill_style" in values:
            value_mask |= 256
        if "fill_rule" in values:
            value_mask |= 512
        if "tile" in values:
            value_mask |= 1024
        if "stipple" in values:
            value_mask |= 2048
        if "tile_stipple_origin_x" in values:
            value_mask |= 4096
        if "tile_stipple_origin_y" in values:
            value_mask |= 8192
        if "font" in values:
            value_mask |= 16384
        if "subwindow_mode" in values:
            value_mask |= 32768
        if "graphics_exposures" in values:
            value_mask |= 65536
        if "clip_origin_x" in values:
            value_mask |= 131072
        if "clip_origin_y" in values:
            value_mask |= 262144
        if "clip_mask" in values:
            value_mask |= 524288
        if "dash_offset" in values:
            value_mask |= 1048576
        if "dash_list" in values:
            value_mask |= 2097152
        if "arc_mode" in values:
            value_mask |= 4194304
        src_gc = get_internal(self)
        dst_gc = get_internal(dst_gc)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", src_gc, dst_gc, value_mask))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 57, True, False), \
            ooxcb.VoidCookie())

    def set_dashes_checked(self, dash_offset, dashes):
        dashes_len = len(dashes)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHH", gc, dash_offset, dashes_len))
        buf.write(make_array(dashes, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 58, True, True), \
            ooxcb.VoidCookie())

    def set_dashes(self, dash_offset, dashes):
        dashes_len = len(dashes)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIHH", gc, dash_offset, dashes_len))
        buf.write(make_array(dashes, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 58, True, False), \
            ooxcb.VoidCookie())

    def set_clip_rectangles_checked(self, clip_x_origin, clip_y_origin, ordering, rectangles):
        rectangles_len = len(rectangles)
        gc = self.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIhh", ordering, gc, clip_x_origin, clip_y_origin))
        for obj in rectangles:
            obj.build(buf)
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 59, True, True), \
            ooxcb.VoidCookie())

    def set_clip_rectangles(self, clip_x_origin, clip_y_origin, ordering, rectangles):
        rectangles_len = len(rectangles)
        gc = self.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIhh", ordering, gc, clip_x_origin, clip_y_origin))
        for obj in rectangles:
            obj.build(buf)
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 59, True, False), \
            ooxcb.VoidCookie())

    def free_checked(self):
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", gc))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 60, True, True), \
            ooxcb.VoidCookie())

    def free(self):
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", gc))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 60, True, False), \
            ooxcb.VoidCookie())

    def copy_area_checked(self, src_drawable, dst_drawable, src_x, src_y, dst_x, dst_y, width, height):
        src_drawable = get_internal(src_drawable)
        dst_drawable = get_internal(dst_drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIIhhhhHH", src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 62, True, True), \
            ooxcb.VoidCookie())

    def copy_area(self, src_drawable, dst_drawable, src_x, src_y, dst_x, dst_y, width, height):
        src_drawable = get_internal(src_drawable)
        dst_drawable = get_internal(dst_drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIIhhhhHH", src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 62, True, False), \
            ooxcb.VoidCookie())

    def copy_plane_checked(self, src_drawable, dst_drawable, src_x, src_y, dst_x, dst_y, width, height, bit_plane):
        src_drawable = get_internal(src_drawable)
        dst_drawable = get_internal(dst_drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIIhhhhHHI", src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height, bit_plane))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 63, True, True), \
            ooxcb.VoidCookie())

    def copy_plane(self, src_drawable, dst_drawable, src_x, src_y, dst_x, dst_y, width, height, bit_plane):
        src_drawable = get_internal(src_drawable)
        dst_drawable = get_internal(dst_drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIIhhhhHHI", src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height, bit_plane))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 63, True, False), \
            ooxcb.VoidCookie())

    def poly_point_checked(self, drawable, points, coordinate_mode=0):
        points_len = len(points)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxII", coordinate_mode, drawable, gc))
        for elt in points:
            buf.write(pack("=hh", *elt))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 64, True, True), \
            ooxcb.VoidCookie())

    def poly_point(self, drawable, points, coordinate_mode=0):
        points_len = len(points)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxII", coordinate_mode, drawable, gc))
        for elt in points:
            buf.write(pack("=hh", *elt))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 64, True, False), \
            ooxcb.VoidCookie())

    def poly_line_checked(self, drawable, points, coordinate_mode=0):
        points_len = len(points)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxII", coordinate_mode, drawable, gc))
        for elt in points:
            buf.write(pack("=hh", *elt))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 65, True, True), \
            ooxcb.VoidCookie())

    def poly_line(self, drawable, points, coordinate_mode=0):
        points_len = len(points)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxII", coordinate_mode, drawable, gc))
        for elt in points:
            buf.write(pack("=hh", *elt))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 65, True, False), \
            ooxcb.VoidCookie())

    def poly_segment_checked(self, drawable, segments):
        segments_len = len(segments)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", drawable, gc))
        for elt in segments:
            buf.write(pack("=hhhh", *elt))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 66, True, True), \
            ooxcb.VoidCookie())

    def poly_segment(self, drawable, segments):
        segments_len = len(segments)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", drawable, gc))
        for elt in segments:
            buf.write(pack("=hhhh", *elt))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 66, True, False), \
            ooxcb.VoidCookie())

    def poly_rectangle_checked(self, drawable, rectangles):
        gc = self.get_internal()
        drawable = drawable.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", drawable, gc))
        for rect in rectangles:
            buf.write(pack("=hhHH", rect.x, rect.y, rect.width, rect.height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 67, True, True), \
            ooxcb.VoidCookie())

    def poly_rectangle(self, drawable, rectangles):
        gc = self.get_internal()
        drawable = drawable.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", drawable, gc))
        for rect in rectangles:
            buf.write(pack("=hhHH", rect.x, rect.y, rect.width, rect.height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 67, True, False), \
            ooxcb.VoidCookie())

    def poly_arc_checked(self, drawable, arcs):
        arcs_length = len(arcs)
        drawable = drawable.get_internal()
        gc = self.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack('xxxxII', drawable, gc))
        for obj in arcs:
            obj.build(buf)
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 68, True, True), \
            ooxcb.VoidCookie())

    def poly_arc(self, drawable, arcs):
        arcs_length = len(arcs)
        drawable = drawable.get_internal()
        gc = self.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack('xxxxII', drawable, gc))
        for obj in arcs:
            obj.build(buf)
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 68, True, False), \
            ooxcb.VoidCookie())

    def fill_poly_checked(self, drawable, points, shape=0, coordinate_mode=0):
        points_len = len(points)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIBBxx", drawable, gc, shape, coordinate_mode))
        for elt in points:
            buf.write(pack("=hh", *elt))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 69, True, True), \
            ooxcb.VoidCookie())

    def fill_poly(self, drawable, points, shape=0, coordinate_mode=0):
        points_len = len(points)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIBBxx", drawable, gc, shape, coordinate_mode))
        for elt in points:
            buf.write(pack("=hh", *elt))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 69, True, False), \
            ooxcb.VoidCookie())

    def poly_fill_rectangle_checked(self, drawable, rectangles):
        gc = self.get_internal()
        drawable = drawable.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", drawable, gc))
        for rect in rectangles:
            buf.write(pack("=hhHH", rect.x, rect.y, rect.width, rect.height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 70, True, True), \
            ooxcb.VoidCookie())

    def poly_fill_rectangle(self, drawable, rectangles):
        gc = self.get_internal()
        drawable = drawable.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", drawable, gc))
        for rect in rectangles:
            buf.write(pack("=hhHH", rect.x, rect.y, rect.width, rect.height))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 70, True, False), \
            ooxcb.VoidCookie())

    def poly_fill_arc_checked(self, drawable, arcs):
        arcs_length = len(arcs)
        drawable = drawable.get_internal()
        gc = self.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack('xxxxII', drawable, gc))
        for obj in arcs:
            obj.build(buf)
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 71, True, True), \
            ooxcb.VoidCookie())

    def poly_fill_arc(self, drawable, arcs):
        arcs_length = len(arcs)
        drawable = drawable.get_internal()
        gc = self.get_internal()
        buf = StringIO.StringIO()
        buf.write(pack('xxxxII', drawable, gc))
        for obj in arcs:
            obj.build(buf)
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 71, True, False), \
            ooxcb.VoidCookie())

    def put_image_checked(self, drawable, format, width, height, dst_x, dst_y, depth, left_pad, data):
        data_len = len(data)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIHHhhBBxx", format, drawable, gc, width, height, dst_x, dst_y, left_pad, depth))
        buf.write(make_array(data, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 72, True, True), \
            ooxcb.VoidCookie())

    def put_image(self, drawable, format, width, height, dst_x, dst_y, depth, left_pad, data):
        data_len = len(data)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIHHhhBBxx", format, drawable, gc, width, height, dst_x, dst_y, left_pad, depth))
        buf.write(make_array(data, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 72, True, False), \
            ooxcb.VoidCookie())

    def poly_text8_checked(self, drawable, x, y, string):
        if isinstance(string, unicode):
            string = string.encode("utf-8")
        items_len = len(string)
        items = map(ord, string)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", drawable, gc, x, y))
        buf.write(make_array(items, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 74, True, True), \
            ooxcb.VoidCookie())

    def poly_text8(self, drawable, x, y, string):
        if isinstance(string, unicode):
            string = string.encode("utf-8")
        items_len = len(string)
        items = map(ord, string)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", drawable, gc, x, y))
        buf.write(make_array(items, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 74, True, False), \
            ooxcb.VoidCookie())

    def poly_text16_checked(self, drawable, x, y, string):
        if not isinstance(string, unicode):
            raise XcbException("`string` has to be an unicode string")
        items = string.encode("utf-16be")
        items_len = len(items) / 2 # should work
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", drawable, gc, x, y))
        buf.write(make_array(items, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 75, True, True), \
            ooxcb.VoidCookie())

    def poly_text16(self, drawable, x, y, string):
        if not isinstance(string, unicode):
            raise XcbException("`string` has to be an unicode string")
        items = string.encode("utf-16be")
        items_len = len(items) / 2 # should work
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIhh", drawable, gc, x, y))
        buf.write(make_array(items, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 75, True, False), \
            ooxcb.VoidCookie())

    def image_text8_checked(self, drawable, x, y, string):
        if isinstance(string, unicode):
            string = string.encode("utf-8")
        string_len = len(string)
        string = map(ord, string)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIhh", string_len, drawable, gc, x, y))
        buf.write(make_array(string, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 76, True, True), \
            ooxcb.VoidCookie())

    def image_text8(self, drawable, x, y, string):
        if isinstance(string, unicode):
            string = string.encode("utf-8")
        string_len = len(string)
        string = map(ord, string)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIhh", string_len, drawable, gc, x, y))
        buf.write(make_array(string, "B"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 76, True, False), \
            ooxcb.VoidCookie())

    def image_text16_checked(self, drawable, x, y, string):
        string_len = len(string)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIhh", string_len, drawable, gc, x, y))
        buf.write(string.encode("utf-16be"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 77, True, True), \
            ooxcb.VoidCookie())

    def image_text16(self, drawable, x, y, string):
        string_len = len(string)
        drawable = get_internal(drawable)
        gc = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xBxxIIhh", string_len, drawable, gc, x, y))
        buf.write(string.encode("utf-16be"))
        return self.conn.xproto.send_request(ooxcb.Request(self.conn, buf.getvalue(), 77, True, False), \
            ooxcb.VoidCookie())

    @classmethod
    def create(cls, conn, drawable, **values):
        cid = conn.generate_id()
        gc = cls(conn, cid)
        value_mask, value_list = 0, []
        if "function" in values:
            value_mask |= 1
            value_list.append(values["function"])
        if "plane_mask" in values:
            value_mask |= 2
            value_list.append(values["plane_mask"])
        if "foreground" in values:
            value_mask |= 4
            value_list.append(values["foreground"])
        if "background" in values:
            value_mask |= 8
            value_list.append(values["background"])
        if "line_width" in values:
            value_mask |= 16
            value_list.append(values["line_width"])
        if "line_style" in values:
            value_mask |= 32
            value_list.append(values["line_style"])
        if "cap_style" in values:
            value_mask |= 64
            value_list.append(values["cap_style"])
        if "join_style" in values:
            value_mask |= 128
            value_list.append(values["join_style"])
        if "fill_style" in values:
            value_mask |= 256
            value_list.append(values["fill_style"])
        if "fill_rule" in values:
            value_mask |= 512
            value_list.append(values["fill_rule"])
        if "tile" in values:
            value_mask |= 1024
            value_list.append(values["tile"])
        if "stipple" in values:
            value_mask |= 2048
            value_list.append(values["stipple"])
        if "tile_stipple_origin_x" in values:
            value_mask |= 4096
            value_list.append(values["tile_stipple_origin_x"])
        if "tile_stipple_origin_y" in values:
            value_mask |= 8192
            value_list.append(values["tile_stipple_origin_y"])
        if "font" in values:
            value_mask |= 16384
            value_list.append(get_internal(values["font"]))
        if "subwindow_mode" in values:
            value_mask |= 32768
            value_list.append(values["subwindow_mode"])
        if "graphics_exposures" in values:
            value_mask |= 65536
            value_list.append(values["graphics_exposures"])
        if "clip_origin_x" in values:
            value_mask |= 131072
            value_list.append(values["clip_origin_x"])
        if "clip_origin_y" in values:
            value_mask |= 262144
            value_list.append(values["clip_origin_y"])
        if "clip_mask" in values:
            value_mask |= 524288
            value_list.append(values["clip_mask"])
        if "dash_offset" in values:
            value_mask |= 1048576
            value_list.append(values["dash_offset"])
        if "dash_list" in values:
            value_mask |= 2097152
            value_list.append(values["dash_list"])
        if "arc_mode" in values:
            value_mask |= 4194304
            value_list.append(values["arc_mode"])
        conn.core.create_g_c_checked(gc, drawable, value_mask, value_list).check()
        conn.add_to_cache(cid, gc)
        return gc

class PixmapError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class BadAlloc(ooxcb.ProtocolException):
    pass

class QueryPointerReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.same_screen = None
        self.root = None
        self.child = None
        self.root_x = None
        self.root_y = None
        self.win_x = None
        self.win_y = None
        self.mask = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxIIhhhhHxx", stream)
        self.same_screen = _unpacked[0]
        self.root = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.child = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.root_x = _unpacked[3]
        self.root_y = _unpacked[4]
        self.win_x = _unpacked[5]
        self.win_y = _unpacked[6]
        self.mask = _unpacked[7]

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxIIhhhhHxx", self.same_screen, get_internal(self.root), get_internal(self.child), self.root_x, self.root_y, self.win_x, self.win_y, self.mask))

class SelectionNotifyEvent(ooxcb.Event):
    event_name = "on_selection_notify"
    opcode = 31
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 31
        self.time = None
        self.requestor = None
        self.selection = None
        self.target = None
        self.property = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIIII", stream)
        self.response_type = _unpacked[0]
        self.time = _unpacked[1]
        self.requestor = self.conn.get_from_cache_fallback(_unpacked[2], Window)
        self.selection = self.conn.atoms.get_by_id(_unpacked[3])
        self.target = self.conn.atoms.get_by_id(_unpacked[4])
        self.property = self.conn.atoms.get_by_id(_unpacked[5])
        self.event_target = self.requestor

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIIII", self.response_type, self.time, get_internal(self.requestor), get_internal(self.selection), get_internal(self.target), get_internal(self.property)))
        stream.write("\0" * (32 - (stream.tell() - root)))

class SetModifierMappingCookie(ooxcb.Cookie):
    pass

class GetPointerMappingCookie(ooxcb.Cookie):
    pass

class GetSelectionOwnerReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.owner = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxI", stream)
        self.owner = self.conn.get_from_cache_fallback(_unpacked[0], Window)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxI", get_internal(self.owner)))

class WindowError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)
        self.bad_value = None
        self.minor_opcode = None
        self.major_opcode = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxIHBx", stream)
        self.bad_value = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxIHBx", self.bad_value, self.minor_opcode, self.major_opcode))

class PropertyNotifyEvent(ooxcb.Event):
    event_name = "on_property_notify"
    opcode = 28
    event_target_class = "Window"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 28
        self.window = None
        self.atom = None
        self.time = None
        self.state = None

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=BxxxIIIBxxx", stream)
        self.response_type = _unpacked[0]
        self.window = self.conn.get_from_cache_fallback(_unpacked[1], Window)
        self.atom = self.conn.atoms.get_by_id(_unpacked[2])
        self.time = _unpacked[3]
        self.state = _unpacked[4]
        self.event_target = self.window

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BxxxIIIBxxx", self.response_type, get_internal(self.window), get_internal(self.atom), self.time, self.state))
        stream.write("\0" * (32 - (stream.tell() - root)))

class GetFontPathReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.path_len = None
        self.path = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", stream)
        self.path_len = _unpacked[0]
        self.path = ooxcb.List(self.conn, stream, self.path_len, Str, -1)

    def build(self, stream):
        count = 0
        stream.write(pack("=xxxxxxxxHxxxxxxxxxxxxxxxxxxxxxx", self.path_len))
        count += 32
        build_list(self.conn, stream, self.path, Str)

class GetKeyboardMappingReply(ooxcb.Reply):
    def __init__(self, conn):
        ooxcb.Reply.__init__(self, conn)
        self.keysyms_per_keycode = None
        self.keysyms = []

    def read(self, stream):
        self._address = stream.address
        _unpacked = unpack_from_stream("=xBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", stream)
        self.keysyms_per_keycode = _unpacked[0]
        self.keysyms = ooxcb.List(self.conn, stream, self.length, 'I', 4)

    def build(self, stream):
        count = 0
        stream.write(pack("=xBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", self.keysyms_per_keycode))
        count += 32
        build_list(self.conn, stream, self.keysyms, 'I')

_events = {
    24: GravityNotifyEvent,
    25: ResizeRequestEvent,
    26: CirculateNotifyEvent,
    27: CirculateRequestEvent,
    20: MapRequestEvent,
    21: ReparentNotifyEvent,
    22: ConfigureNotifyEvent,
    23: ConfigureRequestEvent,
    28: PropertyNotifyEvent,
    29: SelectionClearEvent,
    3: KeyReleaseEvent,
    2: KeyPressEvent,
    5: ButtonReleaseEvent,
    4: ButtonPressEvent,
    7: EnterNotifyEvent,
    6: MotionNotifyEvent,
    9: FocusInEvent,
    8: LeaveNotifyEvent,
    11: KeymapNotifyEvent,
    10: FocusOutEvent,
    13: GraphicsExposureEvent,
    12: ExposeEvent,
    15: VisibilityNotifyEvent,
    14: NoExposureEvent,
    17: DestroyNotifyEvent,
    16: CreateNotifyEvent,
    19: MapNotifyEvent,
    18: UnmapNotifyEvent,
    31: SelectionNotifyEvent,
    30: SelectionRequestEvent,
    34: MappingNotifyEvent,
    33: ClientMessageEvent,
    32: ColormapNotifyEvent,
}

_errors = {
    11: (AllocError, BadAlloc),
    10: (AccessError, BadAccess),
    13: (GContextError, BadGContext),
    12: (ColormapError, BadColormap),
    15: (NameError, BadName),
    14: (IDChoiceError, BadIDChoice),
    17: (ImplementationError, BadImplementation),
    16: (LengthError, BadLength),
    1: (RequestError, BadRequest),
    3: (WindowError, BadWindow),
    2: (ValueError, BadValue),
    5: (AtomError, BadAtom),
    4: (PixmapError, BadPixmap),
    7: (FontError, BadFont),
    6: (CursorError, BadCursor),
    9: (DrawableError, BadDrawable),
    8: (MatchError, BadMatch),
}

for ev in _events.itervalues():
    if isinstance(ev.event_target_class, str):
        ev.event_target_class = globals()[ev.event_target_class]

ooxcb._add_core(xprotoExtension, Setup, _events, _errors)
def mixin():
    pass


