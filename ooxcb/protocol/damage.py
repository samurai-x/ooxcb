# auto generated. yay.
import ooxcb
from ooxcb.resource import get_internal
from ooxcb.types import SIZES, make_array, build_list
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
from struct import pack, unpack, calcsize
from ooxcb.protocol.xproto import Drawable
from ooxcb.util import Mixin

def unpack_from_stream(fmt, stream, offset=0):
    if offset:
        stream.seek(offset, 1)
    s = stream.read(calcsize(fmt))
    return unpack(fmt, s)


MAJOR_VERSION = 1
MINOR_VERSION = 1
key = ooxcb.ExtensionKey("DAMAGE")

class ReportLevel(object):
    RawRectangles = 0
    DeltaRectangles = 1
    BoundingBox = 2
    NonEmpty = 3

class damageExtension(ooxcb.Extension):
    header = "damage"
    def query_version(self, client_major_version, client_minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", client_major_version, client_minor_version))
        return self.conn.damage.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, True), \
            QueryVersionCookie(),
            QueryVersionReply)

    def query_version_unchecked(self, client_major_version, client_minor_version):
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", client_major_version, client_minor_version))
        return self.conn.damage.send_request(ooxcb.Request(self.conn, buf.getvalue(), 0, False, False), \
            QueryVersionCookie(),
            QueryVersionReply)

    def create_checked(self, damage, drawable, level):
        damage = get_internal(damage)
        drawable = get_internal(drawable)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIBxxx", damage, drawable, level))
        return self.conn.damage.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, True, True), \
            ooxcb.VoidCookie())

    def create(self, damage, drawable, level):
        damage = get_internal(damage)
        drawable = get_internal(drawable)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIIBxxx", damage, drawable, level))
        return self.conn.damage.send_request(ooxcb.Request(self.conn, buf.getvalue(), 1, True, False), \
            ooxcb.VoidCookie())

class DrawableMixin(Mixin):
    target_class = Drawable
    def damage_add_checked(self, region):
        drawable = get_internal(self)
        region = get_internal(region)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", drawable, region))
        return self.conn.damage.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, True), \
            ooxcb.VoidCookie())

    def damage_add(self, region):
        drawable = get_internal(self)
        region = get_internal(region)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxII", drawable, region))
        return self.conn.damage.send_request(ooxcb.Request(self.conn, buf.getvalue(), 4, True, False), \
            ooxcb.VoidCookie())

class DamageNotifyEvent(ooxcb.Event):
    event_name = "on_damage_notify"
    opcode = 0
    event_target_class = "Drawable"
    def __init__(self, conn):
        ooxcb.Event.__init__(self, conn)
        self.response_type = 0
        self.level = None
        self.drawable = None
        self.damage = None
        self.timestamp = None
        self.area = None
        self.geometry = None

    def read(self, stream):
        self._address = stream.address
        root = stream.tell()
        _unpacked = unpack_from_stream("=BBxxIII", stream)
        self.response_type = _unpacked[0]
        self.level = _unpacked[1]
        self.drawable = Drawable(self.conn, _unpacked[2])
        self.damage = self.conn.get_from_cache_fallback(_unpacked[3], Damage)
        self.timestamp = _unpacked[4]
        self.area = RECTANGLE.create_from_stream(self.conn, stream)
        stream.seek(ooxcb.type_pad(8, stream.tell() - root), 1)
        self.geometry = RECTANGLE.create_from_stream(self.conn, stream)
        self.event_target = self.drawable

    def build(self, stream):
        count = 0
        root = stream.tell()
        stream.write(pack("=BBxxIII", self.response_type, self.level, get_internal(self.drawable), get_internal(self.damage), self.timestamp))
        count += 16
        self.area.build(stream)
        self.geometry.build(stream)
        stream.write("\0" * (32 - (stream.tell() - root)))

class Damage(ooxcb.Resource):
    def __init__(self, conn, xid):
        ooxcb.Resource.__init__(self, conn, xid)

    def destroy_checked(self):
        damage = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", damage))
        return self.conn.damage.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, True), \
            ooxcb.VoidCookie())

    def destroy(self):
        damage = get_internal(self)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxI", damage))
        return self.conn.damage.send_request(ooxcb.Request(self.conn, buf.getvalue(), 2, True, False), \
            ooxcb.VoidCookie())

    def subtract_checked(self, repair, parts):
        damage = get_internal(self)
        repair = get_internal(repair)
        parts = get_internal(parts)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", damage, repair, parts))
        return self.conn.damage.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, True), \
            ooxcb.VoidCookie())

    def subtract(self, repair, parts):
        damage = get_internal(self)
        repair = get_internal(repair)
        parts = get_internal(parts)
        buf = StringIO.StringIO()
        buf.write(pack("=xxxxIII", damage, repair, parts))
        return self.conn.damage.send_request(ooxcb.Request(self.conn, buf.getvalue(), 3, True, False), \
            ooxcb.VoidCookie())

    @classmethod
    def create(cls, conn, damage, level):
        did = conn.generate_id()
        damage = cls(conn, did)
        conn.damage.create_checked(damage, drawable, level).check()
        conn.add_to_cache(did, damage)
        return damage

class BadDamage(ooxcb.ProtocolException):
    pass

class QueryVersionCookie(ooxcb.Cookie):
    pass

class DamageError(ooxcb.Error):
    def __init__(self, conn):
        ooxcb.Error.__init__(self, conn)

    def read(self, stream):
        self._address = stream.address

    def build(self, stream):
        count = 0

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

_events = {
    0: NotifyEvent,
}

_errors = {
    0: (DamageError, BadDamage),
}

for ev in _events.itervalues():
    if isinstance(ev.event_target_class, str):
        ev.event_target_class = globals()[ev.event_target_class]

ooxcb._add_ext(key, damageExtension, _events, _errors)
def mixin():
    DrawableMixin.mixin()


