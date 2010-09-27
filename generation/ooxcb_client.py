#!/usr/bin/env python

import sys
import re

import yaml

import wraplib
from wraplib.struct import Struct
from wraplib.names import prefix_if_needed
from wraplib.utils import pythonize_camelcase_name
from wraplib.codegen import Codegen, INDENT, DEDENT
from wraplib.pymember import PyMethod, PyClassMethod, PyAttribute, PyFunction
from wraplib.template import template
from wraplib.pyclass import PyClass

# setup yaml
def construct_indent(loader, node):
    return INDENT

def construct_dedent(loader, node):
    return DEDENT

def construct_xizer(loader, node):
    ident = loader.construct_scalar(node)
    return lambda ident=ident: XIZERS[ident]

yaml.add_constructor('!indent', construct_indent)
yaml.add_constructor('!dedent', construct_dedent)
yaml.add_constructor('!xizer', construct_xizer)

_pyname_except_re = re.compile('^Bad') # regular expression for Exceptions
CARDINAL_TYPES = {'CARD8':  'B', 'uint8_t': 'B',
                   'CARD16': 'H','uint16_t': 'H',
                   'CARD32': 'I','uint32_t': 'I',
                   'INT8':   'b', 'int8_t':  'b',
                   'INT16':  'h', 'int16_t': 'h',
                   'INT32':  'i', 'int32_t': 'i',
                   'BYTE': 'B',
                   'BOOL': 'B',
                   'char': 'B', # a char is a STRING8 is a LISTOFCARD8. (?)
#                   'void': 'B',
                   'float': 'f',
                   'double' : 'd'}
MODIFIERS = {'resource': 'self.conn.get_from_cache_fallback(%%s, %s)',
        'ATOM': 'self.conn.atoms.get_by_id(%s)'}

py = Codegen()

NAMESPACE = None
ALL = {} # contains classes, functions, globals ...
WRAPPERS = {}
TAIL = []

ERRORS = {} # {Opcode: (Blargh, Blargh)} - no idea what.
EVENTS = {} # {Opcode: classname}

def is_ignored(tup):
    if isinstance(tup, tuple):
        tup = strip_ns(tup)
    return tup in INTERFACE.get('Ignored', [])

def is_wrapped(name):
    return (name in WRAPPERS or name in INTERFACE.get('ExternallyWrapped', []))

def get_custom_classes():
    return INTERFACE.get('Classes', {})

def pythonize_classname(name):
    return INTERFACE.get('ClassAliases', {}).get(name, name.capitalize())

def pythonize_name(name):
    return INTERFACE.get('NameAliases', None) or pythonize_camelcase_name(name)

def get_request_info(name):
    return INTERFACE.get('Requests', {}).get(name, {})

def strip_ns(tup):
    """
        ('xcb', 'foo') -> 'foo'
    """
    return tup[-1]

def get_field_by_name(fields, name):
    for field in fields:
        if prefix_if_needed(field.field_name) == name:
            return field
    raise KeyError('No field named "%s" found!' % name)

def get_wrapped(name):
    if name in WRAPPERS:
        return WRAPPERS[name].name
    elif name in INTERFACE.get('CustomWrappers', ()):
        return INTERFACE['CustomWrappers'][name]
    else:
        return name

def get_modifier(field):
    if field.py_type in INTERFACE.get('ResourceClasses', []):
        return MODIFIERS['resource'] % get_wrapped(field.py_type)
    elif field.py_type in MODIFIERS:
        return MODIFIERS.get(field.py_type, None)
    elif field.py_type in WRAPPERS:
        if getattr(WRAPPERS[field.py_type], 'is_mixin', False):
            return '%s(self.conn, %%s)' % INTERFACE['Mixins'][field.py_type]
        else:
            return '%s(self.conn, %%s)' % WRAPPERS[field.py_type].name
    else:
        return '%s'

# --- xizers

def make_seq_xizer(seq_in='value', seq_out='value', length_out='value_len'):
    code = []
    code.append(template('$length_out = len($seq_in)', length_out=length_out, seq_in=seq_in))
    if seq_in != seq_out:
        code.append(template('$seq_out = $seq_in', seq_out=seq_out, seq_in=seq_in))
    return lambda code=code: code

def make_utf16_xizer(seq_in='value', seq_out='value', length_out='value_len'):
    code = []
    code.append(template('if not isinstance($seq_in, unicode):', seq_in=seq_in))
    code.extend([
        INDENT,
            template('raise XcbException("`$seq_in` has to be an unicode string")', seq_in=seq_in),
        DEDENT
        ])
    code.append(template('$seq_out = $seq_in.encode("utf-16be")', seq_out=seq_out, seq_in=seq_in))
    code.append(template('$length_out = len($seq_out) / 2 # should work',
        length_out=length_out,
        seq_out=seq_out))
    return lambda code=code: code

def make_objects_xizer(name, buf='buf'):
    code = ['for obj in %s:' % name,
            INDENT,
                'obj.build(%s)' % buf,
            DEDENT]
    return lambda code=code: code

def make_string_xizer(seq_in='value', seq_out='value', length_out='value_len'):
    code = []
    code.append(template('if isinstance($seq_in, unicode):', seq_in=seq_in))
    code.extend([
        INDENT,
            template('$seq_in = $seq_in.encode("utf-8")', seq_in=seq_in),
        DEDENT
        ])
    code.append(template('$length_out = len($seq_in)', length_out=length_out, seq_in=seq_in))
    code.append(template('$seq_out = map(ord, $seq_in)', seq_out=seq_out, seq_in=seq_in))
    return lambda code=code: code

def make_rectangles_xizer(list_in='rectangles', list_out='rectangles', length_out='rectangles_length'):
    code = []
    code.append(template("$list_out = []", list_out=list_out))
    code.append(template("for rect in $list_in:", list_in=list_in))
    code.append(INDENT)
    code.append(template("$list_out.extend([rect.x, rect.y, rect.width, rect.height])", list_out=list_out))
    code.append(DEDENT)
    code.append(template("$length_out = len($list_in)", length_out=length_out, list_in=list_in))
    return lambda code=code: code

def make_lazy_atom_xizer(name, conn='self.conn'):
    code = []
    code.append(template("if isinstance($name, basestring):", name=name))
    code.append(INDENT)
    code.append(template("$name = $conn.atoms[$name]", conn=conn, name=name))
    code.append(DEDENT)
    return lambda code=code: code

def make_values_xizer(enum_name, values_dict_name, mask_out='value_mask', list_out='value_list', xize=()):
    """
        make a simple values xizer code list and return it.
        A values xizer takes all values from the values dict
        and stores it in a values list and a values mask.
    """
    enum = ALL[enum_name]
    code = []
    pyvalues = []

    code.append(template("$mask_out, $list_out = 0, []",
        mask_out=mask_out,
        list_out=list_out
        ))
    for member in enum.members:#key, value in enum.values:
        if not isinstance(member, PyAttribute):
            continue

        key = pythonize_camelcase_name(member.name)
        value = member.value
        code.append(template('if "${key}" in ${values_dict_name}:',
                    key=key,
                    values_dict_name=values_dict_name))
        code.append(INDENT)
        code.append(template('$mask_out |= $value',
            mask_out=mask_out,
            value=value
            ))

        s = template('$values_dict_name["$key"]',
            values_dict_name=values_dict_name,
            key=key,
            )
        if key in xize:
            s = 'get_internal(%s)' % s

        code.append(template('$list_out.append($s)',
            list_out=list_out,
            s=s
            ))
        code.append(DEDENT)

    return lambda code=code: code

def make_mask_xizer(iterable_in, enum_name, mask_out):
    code = []
    enum = ALL[enum_name]
    code.append(template("$mask_out = 0", mask_out=mask_out))
    for member in enum.members:
        if not isinstance(member, PyAttribute):
            continue
        key = pythonize_camelcase_name(member.name)
        value = member.value
        code.extend([
            template('if "${key}" in ${iterable_in}:',
                key=key,
                iterable_in=iterable_in),
            INDENT,
            template('$mask_out |= $value',
                mask_out=mask_out,
                value=value),
            DEDENT])
    return lambda code=code: code

XIZER_MAKERS = {
        'values': make_values_xizer,
        'string': make_string_xizer,
        'utf16': make_utf16_xizer,
        'seq': make_seq_xizer,
        'objects': make_objects_xizer,
        'rectangles': make_rectangles_xizer,
        'mask': make_mask_xizer,
        'lazy_atom': make_lazy_atom_xizer,
        }
XIZERS = {}

def get_length_field(expr, use_self=True):
    '''
    Figures out what C code is needed to get a length field.
    For fields that follow a variable-length field, use the accessor.
    Otherwise, just reference the structure field directly.

    :param use_self: if True, use `self` for field access.
    '''
    if expr.lenfield_name != None:
        if use_self:
            return 'self.%s' % expr.lenfield_name
        else:
            return expr.lenfield_name
    else:
        return str(expr.nmemb)

def setup_type(self, name, postfix=''):
    '''
    Sets up all the C-related state by adding additional data fields to
    all Field and Type objects.  Here is where we figure out most of our
    variable and function names.

    Recurses into child fields and list member types.
    '''
    self.py_type = strip_ns(name) + postfix

    self.py_request_name = strip_ns(name)
    self.py_checked_name = strip_ns(name) + 'Checked'
    self.py_unchecked_name = strip_ns(name) + 'Unchecked'
    self.py_reply_name = strip_ns(name) + 'Reply'
    self.py_event_name = strip_ns(name) + 'Event'
    self.py_cookie_name = strip_ns(name) + 'Cookie'

    if _pyname_except_re.match(strip_ns(name)):
        self.py_error_name = strip_ns(name).replace('Bad', '') + 'Error'
        self.py_except_name = strip_ns(name)
    else:
        self.py_error_name = strip_ns(name) + 'Error'
        self.py_except_name = 'Bad' + strip_ns(name)

    if self.is_pad:
        self.py_format_str = 'x' * self.nmemb # TODO: not using struct's multipliers. ok?
        self.py_format_len = 0

    elif self.is_simple or self.is_expr:
        # so, it's simple. it may be a wrapped object. check.
        self.py_format_str = CARDINAL_TYPES[strip_ns(self.name)]
        self.py_format_len = 1
    elif self.is_list:
        if self.fixed_size():
            self.py_format_str = str(self.nmemb) + CARDINAL_TYPES[strip_ns(self.member.name)]
            self.py_format_len = self.nmemb
        else:
            self.py_format_str = None
            self.py_format_len = -1

    elif self.is_container:
        self.py_format_str = ''
        self.py_format_len = 0
        self.py_fixed_size = 0

        for field in self.fields:
            setup_type(field.type, field.field_type)
            field.py_type = strip_ns(field.field_type)

            if field.type.py_format_len < 0:
                self.py_format_str = None
                self.py_format_len = -1
            elif self.py_format_len >= 0:
                self.py_format_str += field.type.py_format_str
                self.py_format_len += field.type.py_format_len

            if field.type.is_list:
                setup_type(field.type.member, field.field_type)
                field.py_listtype = get_wrapped(strip_ns(field.type.member.name))
                if field.type.member.is_simple:
                    field.py_listtype = "'" + field.type.member.py_format_str + "'"

                field.py_listsize = -1
                if field.type.member.fixed_size():
                    field.py_listsize = field.type.member.size
            if field.type.fixed_size():
                self.py_fixed_size += field.type.size

def align_size(field):
    if field.type.is_list:
        return field.type.member.size if field.type.member.fixed_size() else 4 # .. pointer size??
    if field.type.is_container:
        return field.type.size if field.type.fixed_size() else 4
    return field.type.size

def get_expr(expr, use_self=True):
    '''
    Figures out what C code is needed to get the length of a list field.
    Recurses for math operations.
    Returns bitcount for value-mask fields.
    Otherwise, uses the value of the length field.

    :param use_self: if True: we are in a struct, so use `self` for field access.
    '''
    lenexp = get_length_field(expr, use_self)
    if expr.op != None:
        return '(' + get_expr(expr.lhs, use_self) + ' ' + expr.op + ' ' + get_expr(expr.rhs, use_self) + ')'
    elif expr.bitfield:
        return 'ooxcb.popcount(' + lenexp + ')'
    else:
        return lenexp

def py_complex(self, name, cls):
    m_init = cls.get_member_by_name('__init__')
    init_code = m_init.code

    m_read = cls.new_method('read')
    m_read.arguments.append('stream')
    read_code = m_read.code

    m_build = cls.new_method('build')
    m_build.arguments.append('stream')
    build_code = m_build.code

    def _add_fields(fields):
        read_code.append('_unpacked = unpack_from_stream("=%s", stream)' % fmt)
        build_fields = []
        for idx, field in enumerate(fields):
            # try if we can get a modifier
            modifier = get_modifier(field)
            value = modifier % ('_unpacked[%d]' % idx)
            read_code.append(template('self.$fieldname = $value',
                fieldname=prefix_if_needed(field.field_name),
                value=value
            ))

            if modifier != '%s':
                build_fields.append('get_internal(self.%s)' % prefix_if_needed(field.field_name))
            else:
                build_fields.append('self.%s' % prefix_if_needed(field.field_name))
            cls.add_instance_attribute(prefix_if_needed(field.field_name), '') # TODO: description
        build_code.append('stream.write(pack("=%s", %s))' %
                (fmt, ', '.join(build_fields)))

    need_alignment = False

    # because of that address storing, we'll only be able to read
    # from a MemStream. That's sad. But the address of the struct
    # seems to be needed by some replys, e.g. GetKeyboardMappingReply,
    # to access `self.length`.
    read_code.extend(['self._address = stream.address', 'root = stream.tell()'])
    # Here we store the index of the `root = stream.tell()` line to be able
    # to remove obsolete calls later.
    needs_root = False

    build_code.append('count = 0')
    # prework to pad to the correct size
    if cls.base == 'ooxcb.Event':
        build_code.append('root = stream.tell()')
    struct = Struct()
    for field in self.fields:
        # This hack is ugly, but it seems to be required for valid send_event stuff.
        # Normally, `response_type` is set automatically, but it isn't if the
        # event is part of a send_event request. We have to set it explicitly then
        # to avoid `BadValue` errors. I hope that doesn't have any side effects.
        if (field.field_name == 'response_type' and isinstance(self, xcbgen.xtypes.Event)):
            init_code.append('self.response_type = %s' % self.opcodes[name])
            struct.push_format(field)
            continue
        if field.auto:
            struct.push_pad(field.type.size)
            continue
        if field.type.is_simple:
            struct.push_format(field)
            # add a simple default value (needs to be changed by the user, of course)
            init_code.append('self.%s = None' % (prefix_if_needed(field.field_name)))
            cls.add_instance_attribute(prefix_if_needed(field.field_name), '') # TODO: description
            continue
        if field.type.is_pad:
            struct.push_pad(field.type.nmemb)
            continue
        fields, size, fmt = struct.flush()
        if fields:
            _add_fields(fields)
        if size > 0:
#            read_code.append(template('count += $size', size=size))
            build_code.append(template('count += $size', size=size))
        if need_alignment:
            read_code.append('stream.seek(ooxcb.type_pad(%d, stream.tell() - root), 1)' % align_size(field))
            needs_root = True
            # need to add pad for `build`?
#            build_code.append(r'stream.write("\0" * ooxcb.type_pad(%d, count)' % align_size(field))
        need_alignment = True

        if field.type.is_list:
            if field.type.member.py_type == 'void':
                # It is a void list. The problem about void lists is:
                # we don't exactly know if it's 8, 16 or 32 bit per item.
                # Fortunately, there seems to be an complex type
                # attribute called `self.format` present which has the
                # value 8, 16 or 32. So, we'll use this value
                # to get the type of the list members.
                # That should work for the GetPropertyReply in xproto,
                # but it might not work for other stuff. TODO? It's not nice.
                #
                # If `self.format` is 0 (happens for GetPropertyReply
                # if we try to access a non-existent property),
                # we use "B" (which is an unsigned byte) as a fallback.
                lread_code = ('ooxcb.List(self.conn, stream, %s, SIZES.get(self.format, "B"), self.format // 8)' % \
                        (get_expr(field.type.expr)))
            else:
                lread_code = ('ooxcb.List(self.conn, stream, %s, %s, %d)' % \
                        (get_expr(field.type.expr),
                            field.py_listtype,
                            field.py_listsize))
                if field.py_type == 'char':
                    # convert a list of chars to strings
                    lread_code = '%s.to_string()' % lread_code
                elif field.py_type in INTERFACE.get('ResourceClasses', []):
                    # is a resource. wrap them.
                    lread_code = '[%s for w in %s]' % (get_modifier(field) % 'w', lread_code)
                elif field.py_type == 'ATOM': # TODO: hey, to have this hardcoded is not cool!
                    lread_code = 'map(self.conn.atoms.get_by_id, %s)' % lread_code
            read_code.append('self.%s = %s' % (prefix_if_needed(field.field_name), lread_code))
            cls.add_instance_attribute(prefix_if_needed(field.field_name), '') # TODO: description

            # TODO: add the lazy length property setter ...
            # e.g. `self.cmaps_length` is set to `len(self.colormaps)`.
            # The problem is: the field type expr isn't always a simple
            # expression, it also can be "(self.keycodes_per_modifier * 5)" -
            # how should we solve that?
            build_code.append('build_list(self.conn, stream, self.%s, %s)' % (
                prefix_if_needed(field.field_name), field.py_listtype))

            init_code.append('self.%s = []' % (prefix_if_needed(field.field_name)))
        elif field.type.is_container and field.type.fixed_size():
            read_code.append('self.%s = %s.create_from_stream(self.conn, stream)' % (prefix_if_needed(field.field_name),
                    get_wrapped(field.py_type)))
            cls.add_instance_attribute(prefix_if_needed(field.field_name), '') # TODO: description

            build_code.append('self.%s.build(stream)' % prefix_if_needed(field.field_name))
            init_code.append('self.%s = None' % (prefix_if_needed(field.field_name)))
        else:
            read_code.append('self.%s = %s.create_from_stream(self.conn, stream)' % (prefix_if_needed(field.field_name),
                    get_wrapped(field.py_type)))
            cls.add_instance_attribute(prefix_if_needed(field.field_name), '') # TODO: description
            build_code.append('self.%s.build(stream)' % prefix_if_needed(field.field_name))
            init_code.append('self.%s = None' % (prefix_if_needed(field.field_name)))

    fields, size, fmt = struct.flush()
    if fields:
        if need_alignment:
            read_code.append('stream.seek(ooxcb.type_pad(4, stream.tell() - root), 1)')
            needs_root = True
        _add_fields(fields)
    if (not self.fixed_size() and cls.base == 'ooxcb.Struct'):
        # only do that for variable-length structs.
        # However, the check above is very nasty.
        needs_root = True
    # Events have a fixed size of 32 bytes. Here we pad them to the correct size
    # in the build code.TODO: this solution is nasty, but at least it works.
    if cls.base == 'ooxcb.Event':
        build_code.append(r'stream.write("\0" * (32 - (stream.tell() - root)))')
    if not needs_root:
        read_code.remove('root = stream.tell()')

def py_open(self):
    global NAMESPACE
    NAMESPACE = self.namespace

    py('# auto generated. yay.') \
      ('import ooxcb') \
      ('from ooxcb.resource import get_internal') \
      ('from ooxcb.types import SIZES, make_array, build_list') \
      ('try:').indent() \
                ('import cStringIO as StringIO') \
                .dedent() \
      ('except ImportError:').indent() \
                ('import StringIO') \
                .dedent() \
      ('from struct import pack, unpack, calcsize') \

    if 'ImportCode' in INTERFACE:
        py(INTERFACE['ImportCode'])
    if 'Mixins' in INTERFACE:
        py('from ooxcb.util import Mixin')

    py() \
      ('def unpack_from_stream(fmt, stream, offset=0):') \
      .indent() \
                ('if offset:').indent()('stream.seek(offset, 1)').dedent() \
                ('s = stream.read(calcsize(fmt))') \
                ('return unpack(fmt, s)') \
                .dedent() \
      ()

    if self.namespace.is_ext:
        py() \
                ('MAJOR_VERSION = %s' % self.namespace.major_version) \
                ('MINOR_VERSION = %s' % self.namespace.minor_version) \
                ('key = ooxcb.ExtensionKey("%s")' % self.namespace.ext_xname) \
                ()

def py_close(self):
    pass

def py_enum(self, name):
    '''
    Exported function that handles enum declarations.
    '''
    if is_ignored(name):
        return

    cls = PyClass(strip_ns(name))

    count = 0

    for (enam, evalue) in self.values:
        cls.new_attribute(prefix_if_needed(enam), evalue if evalue != '' else count)
        count += 1

    ALL[cls.name] = cls
    cls.is_enum = True

def py_simple(self, name):
    '''
    Exported function that handles cardinal declarations.
    These are types which are typedef'd to one of the CARDx's char, float, etc.
    '''
    setup_type(self, name, '')
    if not is_ignored(name): # create a class ...
        clsname = pythonize_classname(strip_ns(name))
        cls = PyClass(clsname)
        cls.base = 'ooxcb.Resource'
        init = cls.new_method('__init__')
        init.arguments.extend(['conn', 'xid'])
        init.code.append('ooxcb.Resource.__init__(self, conn, xid)')
        WRAPPERS[strip_ns(name)] = cls
        ALL[clsname] = cls

def py_struct(self, oldname):
    name = (oldname[-2], pythonize_classname(oldname[-1]))
    setup_type(self, name)

    cls = PyClass(self.py_type)
    cls.base = 'ooxcb.Struct'
    init = cls.new_method('__init__')

    if self.fixed_size():
        init.arguments += ['conn']
        init.code.append('ooxcb.Struct.__init__(self, conn)')
    else:
        init.arguments += ['conn']
        init.code.append('ooxcb.Struct.__init__(self, conn)')

    py_complex(self, name, cls)

    if not self.fixed_size():
        cls.get_member_by_name('read').code.append('self.size = stream.tell() - root')

    ALL[strip_ns(name)] = cls
    WRAPPERS[strip_ns(oldname)] = cls

def py_union(self, name):
    '''
    Exported function that handles union declarations.
    '''
    setup_type(self, name)

    cls = PyClass(self.py_type)
    cls.base = 'ooxcb.Union'

    init = cls.new_method('__init__')

    if self.fixed_size():
        init.arguments += ['conn']
        init.code.append('ooxcb.Union.__init__(self, conn)')
    else:
        init.arguments += ['conn']
        init.code.append('ooxcb.Union.__init__(self, conn)')

    read = cls.new_method('read')
    read.arguments.append('stream')

    build = cls.new_method('build')
    build.arguments.append('stream')

    read.code.append('count = 0')
    read.code.append('root = stream.tell()')

    build.code.append('root = stream.tell()')

    kw = 'if' # the first iteration has an if!
    for field in self.fields:
        # TODO: is it possible to have wrapped objects in unions? if yes, what to do?
        # TODO: we should check against None. What if we send the int 0 in an union?
        build.code.append('%s self.%s:' % (kw, prefix_if_needed(field.field_name)))
        build.code.append(INDENT)
        if field.type.is_simple:
            read.code.append('self.%s = unpack_from_stream("=%s", stream)' % \
                    (prefix_if_needed(field.field_name),
                    field.type.py_format_str))
            read.code.append('count = max(count, %s)', field.type.size)
            read.code.append('stream.seek(root)')

            build.code.append(
                    'stream.write(pack("=%s", %s))' % (field.py_format_str, prefix_if_needed(field.field_name))
                    )

            # add a simple default value.
            init.code.append('self.%s = None' % (prefix_if_needed(field.field_name)))
        elif field.type.is_list:
            read.code.append('self.%s = ooxcb.List(self.conn, stream, %s, %s, %s)' % \
                    (prefix_if_needed(field.field_name),
                    get_expr(field.type.expr),
                    field.py_listtype,
                    field.py_listsize))
            read.code.append('count = max(count, self.%s.size)' % prefix_if_needed(field.field_name))
            read.code.append('stream.seek(root)')

            build.code.append(
                    'build_list(self.conn, stream, self.%s, %s)' %
                    (prefix_if_needed(field.field_name), field.py_listtype)
                    )
            init.code.append('self.%s = []' % (prefix_if_needed(field.field_name)))
        elif field.type.is_container and field.type.fixed_size():
            read.code.append('self.%s = %s.create_from_stream(self.conn, stream)' % (prefix_if_needed(field.field_name),
                    field.py_type,
                    field.type.size))
            read.code.append('count = max(count, %s)' % field.type.size)
            read.code.append('stream.seek(root)')

            build.code.append('self.%s.build(stream)' % prefix_if_needed(field.field_name))
            init.code.append('self.%s = None' % (prefix_if_needed(field.field_name)))
        else:
            read.code.append('self.%s = %s.create_from_stream(self.conn, stream)' % (prefix_if_needed(field.field_name), field.py_type))
            read.code.append('count = max(count, self.%s.size)' % prefix_if_needed(field.field_name))
            read.code.append('stream.seek(root)')

            build.code.append('self.%s.build(stream)' % prefix_if_needed(field.field_name))
            init.code.append('self.%s = None' % (prefix_if_needed(field.field_name)))

        kw = 'elif' # all further iterations have an elif.
        build.code.append(DEDENT)

    # using this dirty stuff to get the total length
    # of the union. TODO: what for not-fixed-size unions?
    assert self.fixed_size()
    size = self.fields[0].type.py_format_len
    build.code.extend(['else:',
        INDENT,
            'raise ooxcb.XcbException("No value set in the union!")',
        DEDENT,
        # check if the union has the correct size. if not, append dummy bytes.
        'if stream.tell() - root < %d:' % size,
        INDENT,
            'stream.write(pack("=" + "x" * (%d - (stream.tell() - root))))' % size,
        DEDENT,
        ])

    if not self.fixed_size():
        read.code.append('ooxcb._resize_obj(self, count)')

    ALL[cls.name] = cls
    WRAPPERS[strip_ns(name)] = cls

def request_helper(self, name, void, regular):
    '''
    Declares a request function.
    '''

    # Four stunningly confusing possibilities here:
    #
    #   Void            Non-void
    # ------------------------------
    # "req"            "req"
    # 0 flag           CHECKED flag   Normal Mode
    # void_cookie      req_cookie
    # ------------------------------
    # "req_checked"    "req_unchecked"
    # CHECKED flag     0 flag         Abnormal Mode
    # void_cookie      req_cookie
    # ------------------------------
    reqinfo = get_request_info(strip_ns(name))
    defaults = reqinfo.get('defaults', {})

    # Whether we are _checked or _unchecked
    checked = void and not regular
    unchecked = not void and not regular

    # What kind of cookie we return
    func_cookie = 'ooxcb.VoidCookie' if void else self.py_cookie_name

    # What flag is passed to xcb_request
    func_flags = checked or (not void and regular)

    # What our function name is
    func_name = self.py_request_name
    if checked:
        func_name = self.py_checked_name
    if unchecked:
        func_name = self.py_unchecked_name

    # now pythonize the name ...
    if not 'name' in reqinfo:
        func_name = pythonize_name(func_name)
    else:
        func_name = reqinfo['name']
        if checked:
            func_name += '_checked'
        if unchecked:
            func_name += '_unchecked'

    param_fields = []
    wire_fields = []
    optional_param_fields = []

    meth = PyMethod(func_name)
    # now decide to which class that stuff belongs to, and
    # determinate the `self` parameter
    subject_field = None
    # Check for a subject parameter, use extension class as fallback
    if 'subject' in reqinfo:
        # yep, there's a subject. so, try to get the py class of the
        # subject. or, maybe it's givin explicitly!
        subject_field = get_field_by_name(self.fields, reqinfo['subject'])
        clsname = reqinfo.get('class', None)
        if not clsname:
            cls = WRAPPERS[subject_field.py_type]
        else:
            cls = ALL[clsname]
    else:
        clsname = reqinfo.get('class', None)
        if clsname is None:
            cls = EXTCLS
        else:
            cls = ALL[clsname]
    cls.add_member(meth)

    # get the argument / field names. Only needed for the length field shortcut.
    all_field_names = [prefix_if_needed(field.field_name) for field in self.fields]
    if 'arguments' in reqinfo:
        all_field_names = reqinfo

    for field in self.fields:
        if field.wire:
            wire_fields.append(field)

        if field is subject_field:
            # It's `self`. skippit.
            continue

        if field.visible:
            # The field should appear as a call parameter
            f = prefix_if_needed(field.field_name)
            if f in defaults: # interface provides with a default value
                f += '=' + str(defaults[f])
                optional_param_fields.append(f)
            else:
                if (f.endswith('_len') and
                        f[:-len('_len')] in all_field_names):
                    # It's most likely a length field. We don't have
                    # to include those in the arguments list, the length
                    # can be got from the list itself.
                    meth.code.append('%s = len(%s)' % (f, f[:-len('_len')]))
                else:
                    param_fields.append(f)

    if 'arguments' in reqinfo:
        param_fields = reqinfo['arguments']
        optional_param_fields = []

    meth.arguments.extend(param_fields)
    meth.arguments.extend(optional_param_fields)

    if 'precode' in reqinfo:
        meth.code.extend(reqinfo['precode'])

    if 'initcode' in reqinfo:
        meth.code.extend(reqinfo['initcode'])
    else:
        # Check if we have to add some `get_internal()` somewhere
        for field in self.fields:
            if (is_wrapped(field.py_type) and
                field is not subject_field and
                field.field_name not in reqinfo.get('do_not_xize', []) and
                field.type.is_simple) :
                    meth.code.append('%s = get_internal(%s)' % (field.field_name, field.field_name))
            if field is subject_field:
                # Well, that's not really necessary, because `self` will never
                # be None or an int instance.
                meth.code.append('%s = get_internal(self)' % field.field_name)

        meth.code.append('buf = StringIO.StringIO()')

        struct = Struct()
        for field in wire_fields:
            if field.auto:
                struct.push_pad(field.type.size)
                continue
            if field.type.is_simple:
                struct.push_format(field)
                continue
            if field.type.is_pad:
                struct.push_pad(field.type.nmemb)
                continue

            fields, size, format = struct.flush()

            if size > 0:
                meth.code.append('buf.write(pack("=%s", %s))' % (format, \
                        ', '.join([prefix_if_needed(f.field_name) for f in fields])))

            if field.type.is_expr:
                #_py('        buf.write(pack(\'%s\', %s))', field.type.py_format_str, _py_get_expr(field.type.expr))
                meth.code.append('buf.write(pack("=%s", %s))' % (field.type.py_format_str,
                    get_expr(field.type.expr, False)))

            elif field.type.is_pad:
                meth.code.append('buf.write(pack("=%sx"))' % field.type.nmemb)
            elif field.type.is_container:
                if is_ignored(strip_ns(field.type.name)):
                    meth.code.append('for elt in %s:' % prefix_if_needed(field.field_name))
                    meth.code.append(INDENT)
                    meth.code.append('buf.write(pack("=%s", *elt))' % field.type.py_format_str)
                    meth.code.append(DEDENT)
                else:
                    meth.code.append('%s.build(buf)' % prefix_if_needed(field.field_name))

            elif field.type.is_list and field.type.member.is_simple:
                meth.code.append('buf.write(make_array(%s, "%s"))' % \
                        (prefix_if_needed(field.field_name),
                        field.type.member.py_format_str))
            else:
# TODO: should we really add that? hmmm ...
                if field.field_type[-1] == 'CHAR2B':
                    # we don't need a struct for CHAR2B. We'll just `.encode`.
                    meth.code.append('buf.write(%s.encode("utf-16be"))' % \
                            prefix_if_needed(field.field_name))
                else:
                    if is_ignored(strip_ns(field.type.name)):
                        meth.code.append('for elt in %s:' % (prefix_if_needed(field.field_name)))
                        meth.code.append(INDENT)
                        meth.code.append('buf.write(pack("=%s", *elt))' % field.type.member.py_format_str)
                        meth.code.append(DEDENT)
                    elif is_wrapped(strip_ns(field.type.name)):
                        meth.code.extend([
                            'for elt in %s:' % prefix_if_needed(field.field_name),
                            INDENT,
                            'elt.build(buf)',
                            DEDENT])
                    else:
                        meth.code.append('%s.build(buf)' % prefix_if_needed(field.field_name))

        fields, size, format = struct.flush()
        if size > 0:
            meth.code.append('buf.write(pack("=%s", %s))' % (format, ', '.join(
                [prefix_if_needed(f.field_name) for f in fields])))

    meth.code.append('return self.conn.%s.send_request(ooxcb.Request(self.conn, buf.getvalue(), %s, %s, %s), \\' % \
            (NAMESPACE.header, self.opcode, void, func_flags))
    meth.code.append(INDENT)
    meth.code.append('%s()%s' % (func_cookie, ')' if void else ','))
    if not void:
        meth.code.append('%s)' % self.py_reply_name)
    meth.code.append(DEDENT)

def py_request(self, name):
    '''
    Exported function that handles request declarations.
    '''
    setup_type(self, name, 'Request')

    if self.reply:
        # Cookie class declaration
        cookiecls = PyClass(self.py_cookie_name)
        cookiecls.base = 'ooxcb.Cookie'
        ALL[self.py_cookie_name] = cookiecls

    if self.reply:
        # Reply class definition
        py_reply(self.reply, name)
        # Request prototypes
        request_helper(self, name, False, True)
        request_helper(self, name, False, False)
    else:
        # Request prototypes
        request_helper(self, name, True, False)
        request_helper(self, name, True, True)

def py_reply(self, name):
    '''
    Handles reply declarations.
    '''
    setup_type(self, name, 'Reply')

    cls = PyClass(self.py_reply_name)
    cls.base = 'ooxcb.Reply'
    init = cls.new_method('__init__')
    init.arguments.extend(['conn'])
    init.code.append('ooxcb.Reply.__init__(self, conn)')
    py_complex(self, name, cls)

    ALL[cls.name] = cls # TODO: to WRAPPERS, too?

def py_error(self, name):
    setup_type(self, name, 'Error')

    struct = PyClass(self.py_error_name)
    struct.base = 'ooxcb.Error'
    init = struct.new_method('__init__')
    init.arguments.extend(['conn'])
    init.code.append('ooxcb.Error.__init__(self, conn)')
    ALL[self.py_error_name] = WRAPPERS[self.py_error_name] = struct

    py_complex(self, name, struct)

    # Exception definition
    exc = PyClass(self.py_except_name)
    exc.base = 'ooxcb.ProtocolException'
    ALL[self.py_except_name] = exc

    # Opcode define
    ERRORS[self.opcodes[name]] = '(%s, %s)' % (self.py_error_name, self.py_except_name)

def py_event(self, name):
    setup_type(self, name, 'Event')

    entry = INTERFACE.get('Events', {}).get(strip_ns(name), {})

    clsname = entry.get('classname', self.py_event_name)

    # Opcode define
    EVENTS[self.opcodes[name]] = clsname

    eventname = ('"%s"' % entry.get('eventname',
            'on_%s' % pythonize_camelcase_name(strip_ns(name))))
    struct = PyClass(clsname)
    struct.base = 'ooxcb.Event'
    struct.new_attribute('event_name', eventname)
    # each event class has an `opcode` attribute
    struct.new_attribute('opcode', self.opcodes[name])

    if not entry:
        clsname, membername = ('ooxcb.Connection', 'conn')
    else:
        membername = entry['member']
        # here we want to register the events to the original class.
        # TODO: The way I am doing that here is dirty.
        clsname = '"%s"' % entry.get('class',
                get_wrapped(get_field_by_name(self.fields, membername).py_type).replace('Mixin', ''))
        # the classnames are resolved later. see generate_all.

    struct.new_attribute('event_target_class', clsname)

    init = struct.new_method('__init__')
    init.arguments.extend(['conn'])
    init.code.append('ooxcb.Event.__init__(self, conn)')
    ALL[self.py_event_name] = WRAPPERS[self.py_event_name] = struct

    py_complex(self, name, struct)

    struct.get_member_by_name('read').code.append('self.event_target = self.%s' % membername)

def add_custom_member(cls, mtype, minfo):
    def _handle_method(meth):
        meth.code.extend(minfo['code'])
        meth.arguments.extend(minfo.get('arguments', []))
        meth.decorators.extend(minfo.get('decorators', []))

    def _add_method():
        meth = cls.new_method(minfo['name'])
        _handle_method(meth)

    def _add_classmethod():
        meth = PyClassMethod(minfo['name'])
        cls.add_member(meth)
        _handle_method(meth)

    def _add_attribute():
        cls.new_attribute(minfo['name'], str(minfo['value']))

    def _set_base():
        cls.base = minfo

    def _set_order():
        cls.order = int(minfo)

    types = {
        'method': _add_method,
        'classmethod': _add_classmethod,
        'attribute': _add_attribute,
        'base': _set_base,
        'order': _set_order,
        }
    return types[mtype]()

def process_custom_classes(classes):
    for clsname, members in classes.iteritems():
        if clsname in ALL:
            cls = ALL.get(clsname)
        else:
            cls = PyClass(clsname)
            ALL[clsname] = cls
        for dct in members:
            assert len(dct) == 1, "strange syntax ... %s" % dct
            mtype, minfo = dct.items()[0]
            add_custom_member(cls, mtype, minfo)

def make_mixins():
    m = PyFunction('mixin')
    for name, into in INTERFACE.get('Mixins', {}).iteritems():
        clsname = into + 'Mixin'
        WRAPPERS[name] = ALL[clsname] = cls = PyClass(clsname)
        cls.new_attribute('target_class', into)
        cls.base = 'Mixin'
        cls.is_mixin = True
        m.code.append('%s.mixin()' % clsname)
    TAIL.append(m.generate_code())

def make_xizers():
    for name, info in INTERFACE.get('Xizers', {}).iteritems():
        typ = info['type']
        del info['type']
        XIZERS[name] = XIZER_MAKERS[typ](**info)

def generate_docs():
    gen = Codegen()
    mod = 'ooxcb.protocol.%s' % MODNAME
    heading = mod
    gen(heading)
    gen('=' * len(heading))()
    gen('.. module:: %s' % mod)()
    for name, obj in ALL.iteritems():
        gen(obj.generate_docs())
    with open('%s.rst' % MODNAME, 'w') as f:
        f.write(gen.buf)

def generate_all():
    # print all items, sorted ascending by their `order` attribute.
    # default is 100. but enums come first!
    enum_sorted = sorted(ALL.itervalues(), key=lambda item: int(not hasattr(item, 'is_enum')))
    for item in sorted(enum_sorted, key=lambda item: getattr(item, 'order', 100)):
        map(py, item.generate_code())
    # and last but not least: the events, errors, and registring!
    py('_events = {')
    py.indent()
    map(py, ['%s: %s,' % (key, value) for key, value in EVENTS.iteritems()]) # TODO: sort
    py.dedent()
    py('}')()
    py('_errors = {')
    py.indent()
    map(py, ['%s: %s,' % (key, value) for key, value in ERRORS.iteritems()]) # TODO: sort
    py.dedent()
    py('}')()

    py('for ev in _events.itervalues():').indent()\
            ('if isinstance(ev.event_target_class, str):').indent() \
                ('ev.event_target_class = globals()[ev.event_target_class]') \
                .dedent() \
            .dedent() \
            ()

    if NAMESPACE.is_ext:
        py('ooxcb._add_ext(key, %sExtension, _events, _errors)' % MODNAME)
    else:
        py('ooxcb._add_core(%sExtension, Setup, _events, _errors)' % MODNAME)

    py(TAIL)

# Must create an "output" dictionary before any xcbgen imports.
output = {'open'    : py_open,
          'close'   : py_close,
          'simple'  : py_simple,
          'enum'    : py_enum,
          'struct'  : py_struct,
          'union'   : py_union,
          'request' : py_request,
          'event'   : py_event,
          'error'   : py_error
          }


# Check for the argument that specifies path to the xcbgen python package.
# Import the module class

try:
    from xcbgen.state import Module
except ImportError:
    print ''
    print 'Failed to load the xcbgen Python package!'
    print 'Make sure that xcb/proto installed it on your Python path.'
    print 'If not, you will need to create a .pth file or define $PYTHONPATH'
    print 'to extend the path.'
    print 'Refer to the README file in xcb/proto for more info.'
    print ''
    raise

import xcbgen

if len(sys.argv) > 1: # provided with a module name
    MODNAME = sys.argv[1]
else:
    MODNAME = 'xproto'

print >>sys.stderr, 'Wrapping %s ...' % MODNAME

EXTCLS = PyClass('%sExtension' % MODNAME)

EXTCLS.new_attribute('header', '"%s"' % MODNAME)

EXTCLS.base = 'ooxcb.Extension'
ALL['%sExtension' % MODNAME] = EXTCLS

try:
    ifile = open('%s.i' % MODNAME, 'r')
    INTERFACE = yaml.load(ifile.read())
finally:
    ifile.close()


module = Module('%s.xml' % MODNAME, output)

module.register()
module.resolve()
make_mixins()

module.generate()
make_xizers()
process_custom_classes(get_custom_classes())
generate_all()
generate_docs()
print py.buf

