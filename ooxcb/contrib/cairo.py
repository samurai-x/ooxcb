import ctypes
from ctypes import util
from ctypes import *

from ooxcb.libxcb import xcb_connection_t

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

def load_lib(name):
    libname = util.find_library(name)
    if not libname:
        raise OSError("Could not find library '%s'" % name)
    else:
        return CDLL(libname)

_lib = load_lib('cairo')

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]



CAIRO_VERSION = 10806 	# /usr/include/cairo/cairo.h:68
# /usr/include/cairo/cairo.h:86
cairo_version = _lib.cairo_version
cairo_version.restype = c_int
cairo_version.argtypes = []

# /usr/include/cairo/cairo.h:88
cairo_version_string = _lib.cairo_version_string
cairo_version_string.restype = c_char_p
cairo_version_string.argtypes = []

cairo_bool_t = c_int 	# /usr/include/cairo/cairo.h:105
class struct__cairo(Structure):
    __slots__ = [
    ]
struct__cairo._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo(Structure):
    __slots__ = [
    ]
struct__cairo._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_t = struct__cairo 	# /usr/include/cairo/cairo.h:120
class struct__cairo_surface(Structure):
    __slots__ = [
    ]
struct__cairo_surface._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_surface(Structure):
    __slots__ = [
    ]
struct__cairo_surface._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_surface_t = struct__cairo_surface 	# /usr/include/cairo/cairo.h:138
class struct__cairo_matrix(Structure):
    __slots__ = [
        'xx',
        'yx',
        'xy',
        'yy',
        'x0',
        'y0',
    ]
struct__cairo_matrix._fields_ = [
    ('xx', c_double),
    ('yx', c_double),
    ('xy', c_double),
    ('yy', c_double),
    ('x0', c_double),
    ('y0', c_double),
]

cairo_matrix_t = struct__cairo_matrix 	# /usr/include/cairo/cairo.h:161
class struct__cairo_pattern(Structure):
    __slots__ = [
    ]
struct__cairo_pattern._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_pattern(Structure):
    __slots__ = [
    ]
struct__cairo_pattern._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_pattern_t = struct__cairo_pattern 	# /usr/include/cairo/cairo.h:182
cairo_destroy_func_t = CFUNCTYPE(None, POINTER(None)) 	# /usr/include/cairo/cairo.h:192
class struct__cairo_user_data_key(Structure):
    __slots__ = [
        'unused',
    ]
struct__cairo_user_data_key._fields_ = [
    ('unused', c_int),
]

cairo_user_data_key_t = struct__cairo_user_data_key 	# /usr/include/cairo/cairo.h:206
enum__cairo_status = c_int
CAIRO_STATUS_SUCCESS = 0
CAIRO_STATUS_NO_MEMORY = 1
CAIRO_STATUS_INVALID_RESTORE = 2
CAIRO_STATUS_INVALID_POP_GROUP = 3
CAIRO_STATUS_NO_CURRENT_POINT = 4
CAIRO_STATUS_INVALID_MATRIX = 5
CAIRO_STATUS_INVALID_STATUS = 6
CAIRO_STATUS_NULL_POINTER = 7
CAIRO_STATUS_INVALID_STRING = 8
CAIRO_STATUS_INVALID_PATH_DATA = 9
CAIRO_STATUS_READ_ERROR = 10
CAIRO_STATUS_WRITE_ERROR = 11
CAIRO_STATUS_SURFACE_FINISHED = 12
CAIRO_STATUS_SURFACE_TYPE_MISMATCH = 13
CAIRO_STATUS_PATTERN_TYPE_MISMATCH = 14
CAIRO_STATUS_INVALID_CONTENT = 15
CAIRO_STATUS_INVALID_FORMAT = 16
CAIRO_STATUS_INVALID_VISUAL = 17
CAIRO_STATUS_FILE_NOT_FOUND = 18
CAIRO_STATUS_INVALID_DASH = 19
CAIRO_STATUS_INVALID_DSC_COMMENT = 20
CAIRO_STATUS_INVALID_INDEX = 21
CAIRO_STATUS_CLIP_NOT_REPRESENTABLE = 22
CAIRO_STATUS_TEMP_FILE_ERROR = 23
CAIRO_STATUS_INVALID_STRIDE = 24
CAIRO_STATUS_FONT_TYPE_MISMATCH = 25
CAIRO_STATUS_USER_FONT_IMMUTABLE = 26
CAIRO_STATUS_USER_FONT_ERROR = 27
CAIRO_STATUS_NEGATIVE_COUNT = 28
CAIRO_STATUS_INVALID_CLUSTERS = 29
CAIRO_STATUS_INVALID_SLANT = 30
CAIRO_STATUS_INVALID_WEIGHT = 31
cairo_status_t = enum__cairo_status 	# /usr/include/cairo/cairo.h:285
enum__cairo_content = c_int
CAIRO_CONTENT_COLOR = 4096
CAIRO_CONTENT_ALPHA = 8192
CAIRO_CONTENT_COLOR_ALPHA = 12288
cairo_content_t = enum__cairo_content 	# /usr/include/cairo/cairo.h:305
cairo_write_func_t = CFUNCTYPE(cairo_status_t, POINTER(None), POINTER(c_ubyte), c_uint) 	# /usr/include/cairo/cairo.h:323
cairo_read_func_t = CFUNCTYPE(cairo_status_t, POINTER(None), POINTER(c_ubyte), c_uint) 	# /usr/include/cairo/cairo.h:343
# /usr/include/cairo/cairo.h:348
cairo_create = _lib.cairo_create
cairo_create.restype = POINTER(cairo_t)
cairo_create.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:351
cairo_reference = _lib.cairo_reference
cairo_reference.restype = POINTER(cairo_t)
cairo_reference.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:355
cairo_destroy = _lib.cairo_destroy
cairo_destroy.restype = None
cairo_destroy.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:358
cairo_get_reference_count = _lib.cairo_get_reference_count
cairo_get_reference_count.restype = c_uint
cairo_get_reference_count.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:360
cairo_get_user_data = _lib.cairo_get_user_data
cairo_get_user_data.restype = POINTER(c_void)
cairo_get_user_data.argtypes = [POINTER(cairo_t), POINTER(cairo_user_data_key_t)]

# /usr/include/cairo/cairo.h:365
cairo_set_user_data = _lib.cairo_set_user_data
cairo_set_user_data.restype = cairo_status_t
cairo_set_user_data.argtypes = [POINTER(cairo_t), POINTER(cairo_user_data_key_t), POINTER(None), cairo_destroy_func_t]

# /usr/include/cairo/cairo.h:371
cairo_save = _lib.cairo_save
cairo_save.restype = None
cairo_save.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:374
cairo_restore = _lib.cairo_restore
cairo_restore.restype = None
cairo_restore.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:377
cairo_push_group = _lib.cairo_push_group
cairo_push_group.restype = None
cairo_push_group.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:380
cairo_push_group_with_content = _lib.cairo_push_group_with_content
cairo_push_group_with_content.restype = None
cairo_push_group_with_content.argtypes = [POINTER(cairo_t), cairo_content_t]

# /usr/include/cairo/cairo.h:382
cairo_pop_group = _lib.cairo_pop_group
cairo_pop_group.restype = POINTER(cairo_pattern_t)
cairo_pop_group.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:386
cairo_pop_group_to_source = _lib.cairo_pop_group_to_source
cairo_pop_group_to_source.restype = None
cairo_pop_group_to_source.argtypes = [POINTER(cairo_t)]

enum__cairo_operator = c_int
CAIRO_OPERATOR_CLEAR = 0
CAIRO_OPERATOR_SOURCE = 1
CAIRO_OPERATOR_OVER = 2
CAIRO_OPERATOR_IN = 3
CAIRO_OPERATOR_OUT = 4
CAIRO_OPERATOR_ATOP = 5
CAIRO_OPERATOR_DEST = 6
CAIRO_OPERATOR_DEST_OVER = 7
CAIRO_OPERATOR_DEST_IN = 8
CAIRO_OPERATOR_DEST_OUT = 9
CAIRO_OPERATOR_DEST_ATOP = 10
CAIRO_OPERATOR_XOR = 11
CAIRO_OPERATOR_ADD = 12
CAIRO_OPERATOR_SATURATE = 13
cairo_operator_t = enum__cairo_operator 	# /usr/include/cairo/cairo.h:452
# /usr/include/cairo/cairo.h:455
cairo_set_operator = _lib.cairo_set_operator
cairo_set_operator.restype = None
cairo_set_operator.argtypes = [POINTER(cairo_t), cairo_operator_t]

# /usr/include/cairo/cairo.h:458
cairo_set_source = _lib.cairo_set_source
cairo_set_source.restype = None
cairo_set_source.argtypes = [POINTER(cairo_t), POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:461
cairo_set_source_rgb = _lib.cairo_set_source_rgb
cairo_set_source_rgb.restype = None
cairo_set_source_rgb.argtypes = [POINTER(cairo_t), c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:464
cairo_set_source_rgba = _lib.cairo_set_source_rgba
cairo_set_source_rgba.restype = None
cairo_set_source_rgba.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:469
cairo_set_source_surface = _lib.cairo_set_source_surface
cairo_set_source_surface.restype = None
cairo_set_source_surface.argtypes = [POINTER(cairo_t), POINTER(cairo_surface_t), c_double, c_double]

# /usr/include/cairo/cairo.h:475
cairo_set_tolerance = _lib.cairo_set_tolerance
cairo_set_tolerance.restype = None
cairo_set_tolerance.argtypes = [POINTER(cairo_t), c_double]

enum__cairo_antialias = c_int
CAIRO_ANTIALIAS_DEFAULT = 0
CAIRO_ANTIALIAS_NONE = 1
CAIRO_ANTIALIAS_GRAY = 2
CAIRO_ANTIALIAS_SUBPIXEL = 3
cairo_antialias_t = enum__cairo_antialias 	# /usr/include/cairo/cairo.h:495
# /usr/include/cairo/cairo.h:498
cairo_set_antialias = _lib.cairo_set_antialias
cairo_set_antialias.restype = None
cairo_set_antialias.argtypes = [POINTER(cairo_t), cairo_antialias_t]

enum__cairo_fill_rule = c_int
CAIRO_FILL_RULE_WINDING = 0
CAIRO_FILL_RULE_EVEN_ODD = 1
cairo_fill_rule_t = enum__cairo_fill_rule 	# /usr/include/cairo/cairo.h:528
# /usr/include/cairo/cairo.h:531
cairo_set_fill_rule = _lib.cairo_set_fill_rule
cairo_set_fill_rule.restype = None
cairo_set_fill_rule.argtypes = [POINTER(cairo_t), cairo_fill_rule_t]

# /usr/include/cairo/cairo.h:534
cairo_set_line_width = _lib.cairo_set_line_width
cairo_set_line_width.restype = None
cairo_set_line_width.argtypes = [POINTER(cairo_t), c_double]

enum__cairo_line_cap = c_int
CAIRO_LINE_CAP_BUTT = 0
CAIRO_LINE_CAP_ROUND = 1
CAIRO_LINE_CAP_SQUARE = 2
cairo_line_cap_t = enum__cairo_line_cap 	# /usr/include/cairo/cairo.h:550
# /usr/include/cairo/cairo.h:553
cairo_set_line_cap = _lib.cairo_set_line_cap
cairo_set_line_cap.restype = None
cairo_set_line_cap.argtypes = [POINTER(cairo_t), cairo_line_cap_t]

enum__cairo_line_join = c_int
CAIRO_LINE_JOIN_MITER = 0
CAIRO_LINE_JOIN_ROUND = 1
CAIRO_LINE_JOIN_BEVEL = 2
cairo_line_join_t = enum__cairo_line_join 	# /usr/include/cairo/cairo.h:572
# /usr/include/cairo/cairo.h:575
cairo_set_line_join = _lib.cairo_set_line_join
cairo_set_line_join.restype = None
cairo_set_line_join.argtypes = [POINTER(cairo_t), cairo_line_join_t]

# /usr/include/cairo/cairo.h:578
cairo_set_dash = _lib.cairo_set_dash
cairo_set_dash.restype = None
cairo_set_dash.argtypes = [POINTER(cairo_t), POINTER(c_double), c_int, c_double]

# /usr/include/cairo/cairo.h:584
cairo_set_miter_limit = _lib.cairo_set_miter_limit
cairo_set_miter_limit.restype = None
cairo_set_miter_limit.argtypes = [POINTER(cairo_t), c_double]

# /usr/include/cairo/cairo.h:587
cairo_translate = _lib.cairo_translate
cairo_translate.restype = None
cairo_translate.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:590
cairo_scale = _lib.cairo_scale
cairo_scale.restype = None
cairo_scale.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:593
cairo_rotate = _lib.cairo_rotate
cairo_rotate.restype = None
cairo_rotate.argtypes = [POINTER(cairo_t), c_double]

# /usr/include/cairo/cairo.h:596
cairo_transform = _lib.cairo_transform
cairo_transform.restype = None
cairo_transform.argtypes = [POINTER(cairo_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:600
cairo_set_matrix = _lib.cairo_set_matrix
cairo_set_matrix.restype = None
cairo_set_matrix.argtypes = [POINTER(cairo_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:604
cairo_identity_matrix = _lib.cairo_identity_matrix
cairo_identity_matrix.restype = None
cairo_identity_matrix.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:607
cairo_user_to_device = _lib.cairo_user_to_device
cairo_user_to_device.restype = None
cairo_user_to_device.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:610
cairo_user_to_device_distance = _lib.cairo_user_to_device_distance
cairo_user_to_device_distance.restype = None
cairo_user_to_device_distance.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:613
cairo_device_to_user = _lib.cairo_device_to_user
cairo_device_to_user.restype = None
cairo_device_to_user.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:616
cairo_device_to_user_distance = _lib.cairo_device_to_user_distance
cairo_device_to_user_distance.restype = None
cairo_device_to_user_distance.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:620
cairo_new_path = _lib.cairo_new_path
cairo_new_path.restype = None
cairo_new_path.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:623
cairo_move_to = _lib.cairo_move_to
cairo_move_to.restype = None
cairo_move_to.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:626
cairo_new_sub_path = _lib.cairo_new_sub_path
cairo_new_sub_path.restype = None
cairo_new_sub_path.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:629
cairo_line_to = _lib.cairo_line_to
cairo_line_to.restype = None
cairo_line_to.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:632
cairo_curve_to = _lib.cairo_curve_to
cairo_curve_to.restype = None
cairo_curve_to.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:638
cairo_arc = _lib.cairo_arc
cairo_arc.restype = None
cairo_arc.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:644
cairo_arc_negative = _lib.cairo_arc_negative
cairo_arc_negative.restype = None
cairo_arc_negative.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:658
cairo_rel_move_to = _lib.cairo_rel_move_to
cairo_rel_move_to.restype = None
cairo_rel_move_to.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:661
cairo_rel_line_to = _lib.cairo_rel_line_to
cairo_rel_line_to.restype = None
cairo_rel_line_to.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:664
cairo_rel_curve_to = _lib.cairo_rel_curve_to
cairo_rel_curve_to.restype = None
cairo_rel_curve_to.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:670
cairo_rectangle = _lib.cairo_rectangle
cairo_rectangle.restype = None
cairo_rectangle.argtypes = [POINTER(cairo_t), c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:680
cairo_close_path = _lib.cairo_close_path
cairo_close_path.restype = None
cairo_close_path.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:683
cairo_path_extents = _lib.cairo_path_extents
cairo_path_extents.restype = None
cairo_path_extents.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:689
cairo_paint = _lib.cairo_paint
cairo_paint.restype = None
cairo_paint.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:692
cairo_paint_with_alpha = _lib.cairo_paint_with_alpha
cairo_paint_with_alpha.restype = None
cairo_paint_with_alpha.argtypes = [POINTER(cairo_t), c_double]

# /usr/include/cairo/cairo.h:696
cairo_mask = _lib.cairo_mask
cairo_mask.restype = None
cairo_mask.argtypes = [POINTER(cairo_t), POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:700
cairo_mask_surface = _lib.cairo_mask_surface
cairo_mask_surface.restype = None
cairo_mask_surface.argtypes = [POINTER(cairo_t), POINTER(cairo_surface_t), c_double, c_double]

# /usr/include/cairo/cairo.h:706
cairo_stroke = _lib.cairo_stroke
cairo_stroke.restype = None
cairo_stroke.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:709
cairo_stroke_preserve = _lib.cairo_stroke_preserve
cairo_stroke_preserve.restype = None
cairo_stroke_preserve.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:712
cairo_fill = _lib.cairo_fill
cairo_fill.restype = None
cairo_fill.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:715
cairo_fill_preserve = _lib.cairo_fill_preserve
cairo_fill_preserve.restype = None
cairo_fill_preserve.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:718
cairo_copy_page = _lib.cairo_copy_page
cairo_copy_page.restype = None
cairo_copy_page.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:721
cairo_show_page = _lib.cairo_show_page
cairo_show_page.restype = None
cairo_show_page.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:725
cairo_in_stroke = _lib.cairo_in_stroke
cairo_in_stroke.restype = cairo_bool_t
cairo_in_stroke.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:728
cairo_in_fill = _lib.cairo_in_fill
cairo_in_fill.restype = cairo_bool_t
cairo_in_fill.argtypes = [POINTER(cairo_t), c_double, c_double]

# /usr/include/cairo/cairo.h:732
cairo_stroke_extents = _lib.cairo_stroke_extents
cairo_stroke_extents.restype = None
cairo_stroke_extents.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:737
cairo_fill_extents = _lib.cairo_fill_extents
cairo_fill_extents.restype = None
cairo_fill_extents.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:743
cairo_reset_clip = _lib.cairo_reset_clip
cairo_reset_clip.restype = None
cairo_reset_clip.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:746
cairo_clip = _lib.cairo_clip
cairo_clip.restype = None
cairo_clip.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:749
cairo_clip_preserve = _lib.cairo_clip_preserve
cairo_clip_preserve.restype = None
cairo_clip_preserve.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:752
cairo_clip_extents = _lib.cairo_clip_extents
cairo_clip_extents.restype = None
cairo_clip_extents.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

class struct__cairo_rectangle(Structure):
    __slots__ = [
        'x',
        'y',
        'width',
        'height',
    ]
struct__cairo_rectangle._fields_ = [
    ('x', c_double),
    ('y', c_double),
    ('width', c_double),
    ('height', c_double),
]

cairo_rectangle_t = struct__cairo_rectangle 	# /usr/include/cairo/cairo.h:769
class struct__cairo_rectangle_list(Structure):
    __slots__ = [
        'status',
        'rectangles',
        'num_rectangles',
    ]
struct__cairo_rectangle_list._fields_ = [
    ('status', cairo_status_t),
    ('rectangles', POINTER(cairo_rectangle_t)),
    ('num_rectangles', c_int),
]

cairo_rectangle_list_t = struct__cairo_rectangle_list 	# /usr/include/cairo/cairo.h:786
# /usr/include/cairo/cairo.h:788
cairo_copy_clip_rectangle_list = _lib.cairo_copy_clip_rectangle_list
cairo_copy_clip_rectangle_list.restype = POINTER(cairo_rectangle_list_t)
cairo_copy_clip_rectangle_list.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:792
cairo_rectangle_list_destroy = _lib.cairo_rectangle_list_destroy
cairo_rectangle_list_destroy.restype = None
cairo_rectangle_list_destroy.argtypes = [POINTER(cairo_rectangle_list_t)]

class struct__cairo_scaled_font(Structure):
    __slots__ = [
    ]
struct__cairo_scaled_font._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_scaled_font(Structure):
    __slots__ = [
    ]
struct__cairo_scaled_font._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_scaled_font_t = struct__cairo_scaled_font 	# /usr/include/cairo/cairo.h:811
class struct__cairo_font_face(Structure):
    __slots__ = [
    ]
struct__cairo_font_face._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_font_face(Structure):
    __slots__ = [
    ]
struct__cairo_font_face._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_font_face_t = struct__cairo_font_face 	# /usr/include/cairo/cairo.h:830
class struct_anon_1(Structure):
    __slots__ = [
        'index',
        'x',
        'y',
    ]
struct_anon_1._fields_ = [
    ('index', c_ulong),
    ('x', c_double),
    ('y', c_double),
]

cairo_glyph_t = struct_anon_1 	# /usr/include/cairo/cairo.h:860
# /usr/include/cairo/cairo.h:862
cairo_glyph_allocate = _lib.cairo_glyph_allocate
cairo_glyph_allocate.restype = POINTER(cairo_glyph_t)
cairo_glyph_allocate.argtypes = [c_int]

# /usr/include/cairo/cairo.h:866
cairo_glyph_free = _lib.cairo_glyph_free
cairo_glyph_free.restype = None
cairo_glyph_free.argtypes = [POINTER(cairo_glyph_t)]

class struct_anon_2(Structure):
    __slots__ = [
        'num_bytes',
        'num_glyphs',
    ]
struct_anon_2._fields_ = [
    ('num_bytes', c_int),
    ('num_glyphs', c_int),
]

cairo_text_cluster_t = struct_anon_2 	# /usr/include/cairo/cairo.h:891
# /usr/include/cairo/cairo.h:893
cairo_text_cluster_allocate = _lib.cairo_text_cluster_allocate
cairo_text_cluster_allocate.restype = POINTER(cairo_text_cluster_t)
cairo_text_cluster_allocate.argtypes = [c_int]

# /usr/include/cairo/cairo.h:897
cairo_text_cluster_free = _lib.cairo_text_cluster_free
cairo_text_cluster_free.restype = None
cairo_text_cluster_free.argtypes = [POINTER(cairo_text_cluster_t)]

enum__cairo_text_cluster_flags = c_int
CAIRO_TEXT_CLUSTER_FLAG_BACKWARD = 1
cairo_text_cluster_flags_t = enum__cairo_text_cluster_flags 	# /usr/include/cairo/cairo.h:910
class struct_anon_3(Structure):
    __slots__ = [
        'x_bearing',
        'y_bearing',
        'width',
        'height',
        'x_advance',
        'y_advance',
    ]
struct_anon_3._fields_ = [
    ('x_bearing', c_double),
    ('y_bearing', c_double),
    ('width', c_double),
    ('height', c_double),
    ('x_advance', c_double),
    ('y_advance', c_double),
]

cairo_text_extents_t = struct_anon_3 	# /usr/include/cairo/cairo.h:946
class struct_anon_4(Structure):
    __slots__ = [
        'ascent',
        'descent',
        'height',
        'max_x_advance',
        'max_y_advance',
    ]
struct_anon_4._fields_ = [
    ('ascent', c_double),
    ('descent', c_double),
    ('height', c_double),
    ('max_x_advance', c_double),
    ('max_y_advance', c_double),
]

cairo_font_extents_t = struct_anon_4 	# /usr/include/cairo/cairo.h:995
enum__cairo_font_slant = c_int
CAIRO_FONT_SLANT_NORMAL = 0
CAIRO_FONT_SLANT_ITALIC = 1
CAIRO_FONT_SLANT_OBLIQUE = 2
cairo_font_slant_t = enum__cairo_font_slant 	# /usr/include/cairo/cairo.h:1009
enum__cairo_font_weight = c_int
CAIRO_FONT_WEIGHT_NORMAL = 0
CAIRO_FONT_WEIGHT_BOLD = 1
cairo_font_weight_t = enum__cairo_font_weight 	# /usr/include/cairo/cairo.h:1021
enum__cairo_subpixel_order = c_int
CAIRO_SUBPIXEL_ORDER_DEFAULT = 0
CAIRO_SUBPIXEL_ORDER_RGB = 1
CAIRO_SUBPIXEL_ORDER_BGR = 2
CAIRO_SUBPIXEL_ORDER_VRGB = 3
CAIRO_SUBPIXEL_ORDER_VBGR = 4
cairo_subpixel_order_t = enum__cairo_subpixel_order 	# /usr/include/cairo/cairo.h:1046
enum__cairo_hint_style = c_int
CAIRO_HINT_STYLE_DEFAULT = 0
CAIRO_HINT_STYLE_NONE = 1
CAIRO_HINT_STYLE_SLIGHT = 2
CAIRO_HINT_STYLE_MEDIUM = 3
CAIRO_HINT_STYLE_FULL = 4
cairo_hint_style_t = enum__cairo_hint_style 	# /usr/include/cairo/cairo.h:1076
enum__cairo_hint_metrics = c_int
CAIRO_HINT_METRICS_DEFAULT = 0
CAIRO_HINT_METRICS_OFF = 1
CAIRO_HINT_METRICS_ON = 2
cairo_hint_metrics_t = enum__cairo_hint_metrics 	# /usr/include/cairo/cairo.h:1095
class struct__cairo_font_options(Structure):
    __slots__ = [
    ]
struct__cairo_font_options._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_font_options(Structure):
    __slots__ = [
    ]
struct__cairo_font_options._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_font_options_t = struct__cairo_font_options 	# /usr/include/cairo/cairo.h:1117
# /usr/include/cairo/cairo.h:1119
cairo_font_options_create = _lib.cairo_font_options_create
cairo_font_options_create.restype = POINTER(cairo_font_options_t)
cairo_font_options_create.argtypes = []

# /usr/include/cairo/cairo.h:1122
cairo_font_options_copy = _lib.cairo_font_options_copy
cairo_font_options_copy.restype = POINTER(cairo_font_options_t)
cairo_font_options_copy.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1126
cairo_font_options_destroy = _lib.cairo_font_options_destroy
cairo_font_options_destroy.restype = None
cairo_font_options_destroy.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1129
cairo_font_options_status = _lib.cairo_font_options_status
cairo_font_options_status.restype = cairo_status_t
cairo_font_options_status.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1132
cairo_font_options_merge = _lib.cairo_font_options_merge
cairo_font_options_merge.restype = None
cairo_font_options_merge.argtypes = [POINTER(cairo_font_options_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1135
cairo_font_options_equal = _lib.cairo_font_options_equal
cairo_font_options_equal.restype = cairo_bool_t
cairo_font_options_equal.argtypes = [POINTER(cairo_font_options_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1139
cairo_font_options_hash = _lib.cairo_font_options_hash
cairo_font_options_hash.restype = c_ulong
cairo_font_options_hash.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1142
cairo_font_options_set_antialias = _lib.cairo_font_options_set_antialias
cairo_font_options_set_antialias.restype = None
cairo_font_options_set_antialias.argtypes = [POINTER(cairo_font_options_t), cairo_antialias_t]

# /usr/include/cairo/cairo.h:1145
cairo_font_options_get_antialias = _lib.cairo_font_options_get_antialias
cairo_font_options_get_antialias.restype = cairo_antialias_t
cairo_font_options_get_antialias.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1148
cairo_font_options_set_subpixel_order = _lib.cairo_font_options_set_subpixel_order
cairo_font_options_set_subpixel_order.restype = None
cairo_font_options_set_subpixel_order.argtypes = [POINTER(cairo_font_options_t), cairo_subpixel_order_t]

# /usr/include/cairo/cairo.h:1151
cairo_font_options_get_subpixel_order = _lib.cairo_font_options_get_subpixel_order
cairo_font_options_get_subpixel_order.restype = cairo_subpixel_order_t
cairo_font_options_get_subpixel_order.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1154
cairo_font_options_set_hint_style = _lib.cairo_font_options_set_hint_style
cairo_font_options_set_hint_style.restype = None
cairo_font_options_set_hint_style.argtypes = [POINTER(cairo_font_options_t), cairo_hint_style_t]

# /usr/include/cairo/cairo.h:1157
cairo_font_options_get_hint_style = _lib.cairo_font_options_get_hint_style
cairo_font_options_get_hint_style.restype = cairo_hint_style_t
cairo_font_options_get_hint_style.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1160
cairo_font_options_set_hint_metrics = _lib.cairo_font_options_set_hint_metrics
cairo_font_options_set_hint_metrics.restype = None
cairo_font_options_set_hint_metrics.argtypes = [POINTER(cairo_font_options_t), cairo_hint_metrics_t]

# /usr/include/cairo/cairo.h:1163
cairo_font_options_get_hint_metrics = _lib.cairo_font_options_get_hint_metrics
cairo_font_options_get_hint_metrics.restype = cairo_hint_metrics_t
cairo_font_options_get_hint_metrics.argtypes = [POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1169
cairo_select_font_face = _lib.cairo_select_font_face
cairo_select_font_face.restype = None
cairo_select_font_face.argtypes = [POINTER(cairo_t), c_char_p, cairo_font_slant_t, cairo_font_weight_t]

# /usr/include/cairo/cairo.h:1175
cairo_set_font_size = _lib.cairo_set_font_size
cairo_set_font_size.restype = None
cairo_set_font_size.argtypes = [POINTER(cairo_t), c_double]

# /usr/include/cairo/cairo.h:1178
cairo_set_font_matrix = _lib.cairo_set_font_matrix
cairo_set_font_matrix.restype = None
cairo_set_font_matrix.argtypes = [POINTER(cairo_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1182
cairo_get_font_matrix = _lib.cairo_get_font_matrix
cairo_get_font_matrix.restype = None
cairo_get_font_matrix.argtypes = [POINTER(cairo_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1186
cairo_set_font_options = _lib.cairo_set_font_options
cairo_set_font_options.restype = None
cairo_set_font_options.argtypes = [POINTER(cairo_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1190
cairo_get_font_options = _lib.cairo_get_font_options
cairo_get_font_options.restype = None
cairo_get_font_options.argtypes = [POINTER(cairo_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1194
cairo_set_font_face = _lib.cairo_set_font_face
cairo_set_font_face.restype = None
cairo_set_font_face.argtypes = [POINTER(cairo_t), POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1196
cairo_get_font_face = _lib.cairo_get_font_face
cairo_get_font_face.restype = POINTER(cairo_font_face_t)
cairo_get_font_face.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1200
cairo_set_scaled_font = _lib.cairo_set_scaled_font
cairo_set_scaled_font.restype = None
cairo_set_scaled_font.argtypes = [POINTER(cairo_t), POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1203
cairo_get_scaled_font = _lib.cairo_get_scaled_font
cairo_get_scaled_font.restype = POINTER(cairo_scaled_font_t)
cairo_get_scaled_font.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1207
cairo_show_text = _lib.cairo_show_text
cairo_show_text.restype = None
cairo_show_text.argtypes = [POINTER(cairo_t), c_char_p]

# /usr/include/cairo/cairo.h:1210
cairo_show_glyphs = _lib.cairo_show_glyphs
cairo_show_glyphs.restype = None
cairo_show_glyphs.argtypes = [POINTER(cairo_t), POINTER(cairo_glyph_t), c_int]

# /usr/include/cairo/cairo.h:1213
cairo_show_text_glyphs = _lib.cairo_show_text_glyphs
cairo_show_text_glyphs.restype = None
cairo_show_text_glyphs.argtypes = [POINTER(cairo_t), c_char_p, c_int, POINTER(cairo_glyph_t), c_int, POINTER(cairo_text_cluster_t), c_int, cairo_text_cluster_flags_t]

# /usr/include/cairo/cairo.h:1223
cairo_text_path = _lib.cairo_text_path
cairo_text_path.restype = None
cairo_text_path.argtypes = [POINTER(cairo_t), c_char_p]

# /usr/include/cairo/cairo.h:1226
cairo_glyph_path = _lib.cairo_glyph_path
cairo_glyph_path.restype = None
cairo_glyph_path.argtypes = [POINTER(cairo_t), POINTER(cairo_glyph_t), c_int]

# /usr/include/cairo/cairo.h:1229
cairo_text_extents = _lib.cairo_text_extents
cairo_text_extents.restype = None
cairo_text_extents.argtypes = [POINTER(cairo_t), c_char_p, POINTER(cairo_text_extents_t)]

# /usr/include/cairo/cairo.h:1234
cairo_glyph_extents = _lib.cairo_glyph_extents
cairo_glyph_extents.restype = None
cairo_glyph_extents.argtypes = [POINTER(cairo_t), POINTER(cairo_glyph_t), c_int, POINTER(cairo_text_extents_t)]

# /usr/include/cairo/cairo.h:1240
cairo_font_extents = _lib.cairo_font_extents
cairo_font_extents.restype = None
cairo_font_extents.argtypes = [POINTER(cairo_t), POINTER(cairo_font_extents_t)]

# /usr/include/cairo/cairo.h:1245
cairo_font_face_reference = _lib.cairo_font_face_reference
cairo_font_face_reference.restype = POINTER(cairo_font_face_t)
cairo_font_face_reference.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1249
cairo_font_face_destroy = _lib.cairo_font_face_destroy
cairo_font_face_destroy.restype = None
cairo_font_face_destroy.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1252
cairo_font_face_get_reference_count = _lib.cairo_font_face_get_reference_count
cairo_font_face_get_reference_count.restype = c_uint
cairo_font_face_get_reference_count.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1255
cairo_font_face_status = _lib.cairo_font_face_status
cairo_font_face_status.restype = cairo_status_t
cairo_font_face_status.argtypes = [POINTER(cairo_font_face_t)]

enum__cairo_font_type = c_int
CAIRO_FONT_TYPE_TOY = 0
CAIRO_FONT_TYPE_FT = 1
CAIRO_FONT_TYPE_WIN32 = 2
CAIRO_FONT_TYPE_QUARTZ = 3
CAIRO_FONT_TYPE_USER = 4
cairo_font_type_t = enum__cairo_font_type 	# /usr/include/cairo/cairo.h:1301
# /usr/include/cairo/cairo.h:1304
cairo_font_face_get_type = _lib.cairo_font_face_get_type
cairo_font_face_get_type.restype = cairo_font_type_t
cairo_font_face_get_type.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1306
cairo_font_face_get_user_data = _lib.cairo_font_face_get_user_data
cairo_font_face_get_user_data.restype = POINTER(c_void)
cairo_font_face_get_user_data.argtypes = [POINTER(cairo_font_face_t), POINTER(cairo_user_data_key_t)]

# /usr/include/cairo/cairo.h:1311
cairo_font_face_set_user_data = _lib.cairo_font_face_set_user_data
cairo_font_face_set_user_data.restype = cairo_status_t
cairo_font_face_set_user_data.argtypes = [POINTER(cairo_font_face_t), POINTER(cairo_user_data_key_t), POINTER(None), cairo_destroy_func_t]

# /usr/include/cairo/cairo.h:1318
cairo_scaled_font_create = _lib.cairo_scaled_font_create
cairo_scaled_font_create.restype = POINTER(cairo_scaled_font_t)
cairo_scaled_font_create.argtypes = [POINTER(cairo_font_face_t), POINTER(cairo_matrix_t), POINTER(cairo_matrix_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1324
cairo_scaled_font_reference = _lib.cairo_scaled_font_reference
cairo_scaled_font_reference.restype = POINTER(cairo_scaled_font_t)
cairo_scaled_font_reference.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1328
cairo_scaled_font_destroy = _lib.cairo_scaled_font_destroy
cairo_scaled_font_destroy.restype = None
cairo_scaled_font_destroy.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1331
cairo_scaled_font_get_reference_count = _lib.cairo_scaled_font_get_reference_count
cairo_scaled_font_get_reference_count.restype = c_uint
cairo_scaled_font_get_reference_count.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1334
cairo_scaled_font_status = _lib.cairo_scaled_font_status
cairo_scaled_font_status.restype = cairo_status_t
cairo_scaled_font_status.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1337
cairo_scaled_font_get_type = _lib.cairo_scaled_font_get_type
cairo_scaled_font_get_type.restype = cairo_font_type_t
cairo_scaled_font_get_type.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1339
cairo_scaled_font_get_user_data = _lib.cairo_scaled_font_get_user_data
cairo_scaled_font_get_user_data.restype = POINTER(c_void)
cairo_scaled_font_get_user_data.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_user_data_key_t)]

# /usr/include/cairo/cairo.h:1344
cairo_scaled_font_set_user_data = _lib.cairo_scaled_font_set_user_data
cairo_scaled_font_set_user_data.restype = cairo_status_t
cairo_scaled_font_set_user_data.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_user_data_key_t), POINTER(None), cairo_destroy_func_t]

# /usr/include/cairo/cairo.h:1350
cairo_scaled_font_extents = _lib.cairo_scaled_font_extents
cairo_scaled_font_extents.restype = None
cairo_scaled_font_extents.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_font_extents_t)]

# /usr/include/cairo/cairo.h:1354
cairo_scaled_font_text_extents = _lib.cairo_scaled_font_text_extents
cairo_scaled_font_text_extents.restype = None
cairo_scaled_font_text_extents.argtypes = [POINTER(cairo_scaled_font_t), c_char_p, POINTER(cairo_text_extents_t)]

# /usr/include/cairo/cairo.h:1359
cairo_scaled_font_glyph_extents = _lib.cairo_scaled_font_glyph_extents
cairo_scaled_font_glyph_extents.restype = None
cairo_scaled_font_glyph_extents.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_glyph_t), c_int, POINTER(cairo_text_extents_t)]

# /usr/include/cairo/cairo.h:1365
cairo_scaled_font_text_to_glyphs = _lib.cairo_scaled_font_text_to_glyphs
cairo_scaled_font_text_to_glyphs.restype = cairo_status_t
cairo_scaled_font_text_to_glyphs.argtypes = [POINTER(cairo_scaled_font_t), c_double, c_double, c_char_p, c_int, POINTER(POINTER(cairo_glyph_t)), POINTER(c_int), POINTER(POINTER(cairo_text_cluster_t)), POINTER(c_int), POINTER(cairo_text_cluster_flags_t)]

# /usr/include/cairo/cairo.h:1376
cairo_scaled_font_get_font_face = _lib.cairo_scaled_font_get_font_face
cairo_scaled_font_get_font_face.restype = POINTER(cairo_font_face_t)
cairo_scaled_font_get_font_face.argtypes = [POINTER(cairo_scaled_font_t)]

# /usr/include/cairo/cairo.h:1380
cairo_scaled_font_get_font_matrix = _lib.cairo_scaled_font_get_font_matrix
cairo_scaled_font_get_font_matrix.restype = None
cairo_scaled_font_get_font_matrix.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1384
cairo_scaled_font_get_ctm = _lib.cairo_scaled_font_get_ctm
cairo_scaled_font_get_ctm.restype = None
cairo_scaled_font_get_ctm.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1388
cairo_scaled_font_get_scale_matrix = _lib.cairo_scaled_font_get_scale_matrix
cairo_scaled_font_get_scale_matrix.restype = None
cairo_scaled_font_get_scale_matrix.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1392
cairo_scaled_font_get_font_options = _lib.cairo_scaled_font_get_font_options
cairo_scaled_font_get_font_options.restype = None
cairo_scaled_font_get_font_options.argtypes = [POINTER(cairo_scaled_font_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1398
cairo_toy_font_face_create = _lib.cairo_toy_font_face_create
cairo_toy_font_face_create.restype = POINTER(cairo_font_face_t)
cairo_toy_font_face_create.argtypes = [c_char_p, cairo_font_slant_t, cairo_font_weight_t]

# /usr/include/cairo/cairo.h:1403
cairo_toy_font_face_get_family = _lib.cairo_toy_font_face_get_family
cairo_toy_font_face_get_family.restype = c_char_p
cairo_toy_font_face_get_family.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1407
cairo_toy_font_face_get_slant = _lib.cairo_toy_font_face_get_slant
cairo_toy_font_face_get_slant.restype = cairo_font_slant_t
cairo_toy_font_face_get_slant.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1410
cairo_toy_font_face_get_weight = _lib.cairo_toy_font_face_get_weight
cairo_toy_font_face_get_weight.restype = cairo_font_weight_t
cairo_toy_font_face_get_weight.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1415
cairo_user_font_face_create = _lib.cairo_user_font_face_create
cairo_user_font_face_create.restype = POINTER(cairo_font_face_t)
cairo_user_font_face_create.argtypes = []

cairo_user_scaled_font_init_func_t = CFUNCTYPE(cairo_status_t, POINTER(cairo_scaled_font_t), POINTER(cairo_t), POINTER(cairo_font_extents_t)) 	# /usr/include/cairo/cairo.h:1453
cairo_user_scaled_font_render_glyph_func_t = CFUNCTYPE(cairo_status_t, POINTER(cairo_scaled_font_t), c_ulong, POINTER(cairo_t), POINTER(cairo_text_extents_t)) 	# /usr/include/cairo/cairo.h:1500
cairo_user_scaled_font_text_to_glyphs_func_t = CFUNCTYPE(cairo_status_t, POINTER(cairo_scaled_font_t), c_char_p, c_int, POINTER(POINTER(cairo_glyph_t)), POINTER(c_int), POINTER(POINTER(cairo_text_cluster_t)), POINTER(c_int), POINTER(cairo_text_cluster_flags_t)) 	# /usr/include/cairo/cairo.h:1566
cairo_user_scaled_font_unicode_to_glyph_func_t = CFUNCTYPE(cairo_status_t, POINTER(cairo_scaled_font_t), c_ulong, POINTER(c_ulong)) 	# /usr/include/cairo/cairo.h:1611
# /usr/include/cairo/cairo.h:1618
cairo_user_font_face_set_init_func = _lib.cairo_user_font_face_set_init_func
cairo_user_font_face_set_init_func.restype = None
cairo_user_font_face_set_init_func.argtypes = [POINTER(cairo_font_face_t), cairo_user_scaled_font_init_func_t]

# /usr/include/cairo/cairo.h:1622
cairo_user_font_face_set_render_glyph_func = _lib.cairo_user_font_face_set_render_glyph_func
cairo_user_font_face_set_render_glyph_func.restype = None
cairo_user_font_face_set_render_glyph_func.argtypes = [POINTER(cairo_font_face_t), cairo_user_scaled_font_render_glyph_func_t]

# /usr/include/cairo/cairo.h:1626
cairo_user_font_face_set_text_to_glyphs_func = _lib.cairo_user_font_face_set_text_to_glyphs_func
cairo_user_font_face_set_text_to_glyphs_func.restype = None
cairo_user_font_face_set_text_to_glyphs_func.argtypes = [POINTER(cairo_font_face_t), cairo_user_scaled_font_text_to_glyphs_func_t]

# /usr/include/cairo/cairo.h:1630
cairo_user_font_face_set_unicode_to_glyph_func = _lib.cairo_user_font_face_set_unicode_to_glyph_func
cairo_user_font_face_set_unicode_to_glyph_func.restype = None
cairo_user_font_face_set_unicode_to_glyph_func.argtypes = [POINTER(cairo_font_face_t), cairo_user_scaled_font_unicode_to_glyph_func_t]

# /usr/include/cairo/cairo.h:1636
cairo_user_font_face_get_init_func = _lib.cairo_user_font_face_get_init_func
cairo_user_font_face_get_init_func.restype = cairo_user_scaled_font_init_func_t
cairo_user_font_face_get_init_func.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1639
cairo_user_font_face_get_render_glyph_func = _lib.cairo_user_font_face_get_render_glyph_func
cairo_user_font_face_get_render_glyph_func.restype = cairo_user_scaled_font_render_glyph_func_t
cairo_user_font_face_get_render_glyph_func.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1642
cairo_user_font_face_get_text_to_glyphs_func = _lib.cairo_user_font_face_get_text_to_glyphs_func
cairo_user_font_face_get_text_to_glyphs_func.restype = cairo_user_scaled_font_text_to_glyphs_func_t
cairo_user_font_face_get_text_to_glyphs_func.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1645
cairo_user_font_face_get_unicode_to_glyph_func = _lib.cairo_user_font_face_get_unicode_to_glyph_func
cairo_user_font_face_get_unicode_to_glyph_func.restype = cairo_user_scaled_font_unicode_to_glyph_func_t
cairo_user_font_face_get_unicode_to_glyph_func.argtypes = [POINTER(cairo_font_face_t)]

# /usr/include/cairo/cairo.h:1651
cairo_get_operator = _lib.cairo_get_operator
cairo_get_operator.restype = cairo_operator_t
cairo_get_operator.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1653
cairo_get_source = _lib.cairo_get_source
cairo_get_source.restype = POINTER(cairo_pattern_t)
cairo_get_source.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1657
cairo_get_tolerance = _lib.cairo_get_tolerance
cairo_get_tolerance.restype = c_double
cairo_get_tolerance.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1660
cairo_get_antialias = _lib.cairo_get_antialias
cairo_get_antialias.restype = cairo_antialias_t
cairo_get_antialias.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1663
cairo_has_current_point = _lib.cairo_has_current_point
cairo_has_current_point.restype = cairo_bool_t
cairo_has_current_point.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1666
cairo_get_current_point = _lib.cairo_get_current_point
cairo_get_current_point.restype = None
cairo_get_current_point.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:1669
cairo_get_fill_rule = _lib.cairo_get_fill_rule
cairo_get_fill_rule.restype = cairo_fill_rule_t
cairo_get_fill_rule.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1672
cairo_get_line_width = _lib.cairo_get_line_width
cairo_get_line_width.restype = c_double
cairo_get_line_width.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1675
cairo_get_line_cap = _lib.cairo_get_line_cap
cairo_get_line_cap.restype = cairo_line_cap_t
cairo_get_line_cap.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1678
cairo_get_line_join = _lib.cairo_get_line_join
cairo_get_line_join.restype = cairo_line_join_t
cairo_get_line_join.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1681
cairo_get_miter_limit = _lib.cairo_get_miter_limit
cairo_get_miter_limit.restype = c_double
cairo_get_miter_limit.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1684
cairo_get_dash_count = _lib.cairo_get_dash_count
cairo_get_dash_count.restype = c_int
cairo_get_dash_count.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1687
cairo_get_dash = _lib.cairo_get_dash
cairo_get_dash.restype = None
cairo_get_dash.argtypes = [POINTER(cairo_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:1690
cairo_get_matrix = _lib.cairo_get_matrix
cairo_get_matrix.restype = None
cairo_get_matrix.argtypes = [POINTER(cairo_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:1692
cairo_get_target = _lib.cairo_get_target
cairo_get_target.restype = POINTER(cairo_surface_t)
cairo_get_target.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1695
cairo_get_group_target = _lib.cairo_get_group_target
cairo_get_group_target.restype = POINTER(cairo_surface_t)
cairo_get_group_target.argtypes = [POINTER(cairo_t)]

enum__cairo_path_data_type = c_int
CAIRO_PATH_MOVE_TO = 0
CAIRO_PATH_LINE_TO = 1
CAIRO_PATH_CURVE_TO = 2
CAIRO_PATH_CLOSE_PATH = 3
cairo_path_data_type_t = enum__cairo_path_data_type 	# /usr/include/cairo/cairo.h:1714
class struct__cairo_path_data_t(Union):
    __slots__ = [
    ]
struct__cairo_path_data_t._fields_ = [
    ('_opaque_struct', c_int)
]

class struct__cairo_path_data_t(Union):
    __slots__ = [
    ]
struct__cairo_path_data_t._fields_ = [
    ('_opaque_struct', c_int)
]

cairo_path_data_t = struct__cairo_path_data_t 	# /usr/include/cairo/cairo.h:1782
class struct_cairo_path(Structure):
    __slots__ = [
        'status',
        'data',
        'num_data',
    ]
struct_cairo_path._fields_ = [
    ('status', cairo_status_t),
    ('data', POINTER(cairo_path_data_t)),
    ('num_data', c_int),
]

cairo_path_t = struct_cairo_path 	# /usr/include/cairo/cairo.h:1816
# /usr/include/cairo/cairo.h:1818
cairo_copy_path = _lib.cairo_copy_path
cairo_copy_path.restype = POINTER(cairo_path_t)
cairo_copy_path.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1821
cairo_copy_path_flat = _lib.cairo_copy_path_flat
cairo_copy_path_flat.restype = POINTER(cairo_path_t)
cairo_copy_path_flat.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1825
cairo_append_path = _lib.cairo_append_path
cairo_append_path.restype = None
cairo_append_path.argtypes = [POINTER(cairo_t), POINTER(cairo_path_t)]

# /usr/include/cairo/cairo.h:1829
cairo_path_destroy = _lib.cairo_path_destroy
cairo_path_destroy.restype = None
cairo_path_destroy.argtypes = [POINTER(cairo_path_t)]

# /usr/include/cairo/cairo.h:1834
cairo_status = _lib.cairo_status
cairo_status.restype = cairo_status_t
cairo_status.argtypes = [POINTER(cairo_t)]

# /usr/include/cairo/cairo.h:1836
cairo_status_to_string = _lib.cairo_status_to_string
cairo_status_to_string.restype = c_char_p
cairo_status_to_string.argtypes = [cairo_status_t]

# /usr/include/cairo/cairo.h:1841
cairo_surface_create_similar = _lib.cairo_surface_create_similar
cairo_surface_create_similar.restype = POINTER(cairo_surface_t)
cairo_surface_create_similar.argtypes = [POINTER(cairo_surface_t), cairo_content_t, c_int, c_int]

# /usr/include/cairo/cairo.h:1847
cairo_surface_reference = _lib.cairo_surface_reference
cairo_surface_reference.restype = POINTER(cairo_surface_t)
cairo_surface_reference.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1851
cairo_surface_finish = _lib.cairo_surface_finish
cairo_surface_finish.restype = None
cairo_surface_finish.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1854
cairo_surface_destroy = _lib.cairo_surface_destroy
cairo_surface_destroy.restype = None
cairo_surface_destroy.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1857
cairo_surface_get_reference_count = _lib.cairo_surface_get_reference_count
cairo_surface_get_reference_count.restype = c_uint
cairo_surface_get_reference_count.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1860
cairo_surface_status = _lib.cairo_surface_status
cairo_surface_status.restype = cairo_status_t
cairo_surface_status.argtypes = [POINTER(cairo_surface_t)]

enum__cairo_surface_type = c_int
CAIRO_SURFACE_TYPE_IMAGE = 0
CAIRO_SURFACE_TYPE_PDF = 1
CAIRO_SURFACE_TYPE_PS = 2
CAIRO_SURFACE_TYPE_XLIB = 3
CAIRO_SURFACE_TYPE_XCB = 4
CAIRO_SURFACE_TYPE_GLITZ = 5
CAIRO_SURFACE_TYPE_QUARTZ = 6
CAIRO_SURFACE_TYPE_WIN32 = 7
CAIRO_SURFACE_TYPE_BEOS = 8
CAIRO_SURFACE_TYPE_DIRECTFB = 9
CAIRO_SURFACE_TYPE_SVG = 10
CAIRO_SURFACE_TYPE_OS2 = 11
CAIRO_SURFACE_TYPE_WIN32_PRINTING = 12
CAIRO_SURFACE_TYPE_QUARTZ_IMAGE = 13
cairo_surface_type_t = enum__cairo_surface_type 	# /usr/include/cairo/cairo.h:1917
# /usr/include/cairo/cairo.h:1920
cairo_surface_get_type = _lib.cairo_surface_get_type
cairo_surface_get_type.restype = cairo_surface_type_t
cairo_surface_get_type.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1923
cairo_surface_get_content = _lib.cairo_surface_get_content
cairo_surface_get_content.restype = cairo_content_t
cairo_surface_get_content.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1928
cairo_surface_write_to_png = _lib.cairo_surface_write_to_png
cairo_surface_write_to_png.restype = cairo_status_t
cairo_surface_write_to_png.argtypes = [POINTER(cairo_surface_t), c_char_p]

# /usr/include/cairo/cairo.h:1932
cairo_surface_write_to_png_stream = _lib.cairo_surface_write_to_png_stream
cairo_surface_write_to_png_stream.restype = cairo_status_t
cairo_surface_write_to_png_stream.argtypes = [POINTER(cairo_surface_t), cairo_write_func_t, POINTER(None)]

# /usr/include/cairo/cairo.h:1938
cairo_surface_get_user_data = _lib.cairo_surface_get_user_data
cairo_surface_get_user_data.restype = POINTER(c_void)
cairo_surface_get_user_data.argtypes = [POINTER(cairo_surface_t), POINTER(cairo_user_data_key_t)]

# /usr/include/cairo/cairo.h:1943
cairo_surface_set_user_data = _lib.cairo_surface_set_user_data
cairo_surface_set_user_data.restype = cairo_status_t
cairo_surface_set_user_data.argtypes = [POINTER(cairo_surface_t), POINTER(cairo_user_data_key_t), POINTER(None), cairo_destroy_func_t]

# /usr/include/cairo/cairo.h:1949
cairo_surface_get_font_options = _lib.cairo_surface_get_font_options
cairo_surface_get_font_options.restype = None
cairo_surface_get_font_options.argtypes = [POINTER(cairo_surface_t), POINTER(cairo_font_options_t)]

# /usr/include/cairo/cairo.h:1953
cairo_surface_flush = _lib.cairo_surface_flush
cairo_surface_flush.restype = None
cairo_surface_flush.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1956
cairo_surface_mark_dirty = _lib.cairo_surface_mark_dirty
cairo_surface_mark_dirty.restype = None
cairo_surface_mark_dirty.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1959
cairo_surface_mark_dirty_rectangle = _lib.cairo_surface_mark_dirty_rectangle
cairo_surface_mark_dirty_rectangle.restype = None
cairo_surface_mark_dirty_rectangle.argtypes = [POINTER(cairo_surface_t), c_int, c_int, c_int, c_int]

# /usr/include/cairo/cairo.h:1966
cairo_surface_set_device_offset = _lib.cairo_surface_set_device_offset
cairo_surface_set_device_offset.restype = None
cairo_surface_set_device_offset.argtypes = [POINTER(cairo_surface_t), c_double, c_double]

# /usr/include/cairo/cairo.h:1971
cairo_surface_get_device_offset = _lib.cairo_surface_get_device_offset
cairo_surface_get_device_offset.restype = None
cairo_surface_get_device_offset.argtypes = [POINTER(cairo_surface_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:1976
cairo_surface_set_fallback_resolution = _lib.cairo_surface_set_fallback_resolution
cairo_surface_set_fallback_resolution.restype = None
cairo_surface_set_fallback_resolution.argtypes = [POINTER(cairo_surface_t), c_double, c_double]

# /usr/include/cairo/cairo.h:1981
cairo_surface_get_fallback_resolution = _lib.cairo_surface_get_fallback_resolution
cairo_surface_get_fallback_resolution.restype = None
cairo_surface_get_fallback_resolution.argtypes = [POINTER(cairo_surface_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:1986
cairo_surface_copy_page = _lib.cairo_surface_copy_page
cairo_surface_copy_page.restype = None
cairo_surface_copy_page.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1989
cairo_surface_show_page = _lib.cairo_surface_show_page
cairo_surface_show_page.restype = None
cairo_surface_show_page.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:1992
cairo_surface_has_show_text_glyphs = _lib.cairo_surface_has_show_text_glyphs
cairo_surface_has_show_text_glyphs.restype = cairo_bool_t
cairo_surface_has_show_text_glyphs.argtypes = [POINTER(cairo_surface_t)]

enum__cairo_format = c_int
CAIRO_FORMAT_ARGB32 = 0
CAIRO_FORMAT_RGB24 = 1
CAIRO_FORMAT_A8 = 2
CAIRO_FORMAT_A1 = 3
cairo_format_t = enum__cairo_format 	# /usr/include/cairo/cairo.h:2032
# /usr/include/cairo/cairo.h:2034
cairo_image_surface_create = _lib.cairo_image_surface_create
cairo_image_surface_create.restype = POINTER(cairo_surface_t)
cairo_image_surface_create.argtypes = [cairo_format_t, c_int, c_int]

# /usr/include/cairo/cairo.h:2040
cairo_format_stride_for_width = _lib.cairo_format_stride_for_width
cairo_format_stride_for_width.restype = c_int
cairo_format_stride_for_width.argtypes = [cairo_format_t, c_int]

# /usr/include/cairo/cairo.h:2043
cairo_image_surface_create_for_data = _lib.cairo_image_surface_create_for_data
cairo_image_surface_create_for_data.restype = POINTER(cairo_surface_t)
cairo_image_surface_create_for_data.argtypes = [POINTER(c_ubyte), cairo_format_t, c_int, c_int, c_int]

# /usr/include/cairo/cairo.h:2050
cairo_image_surface_get_data = _lib.cairo_image_surface_get_data
cairo_image_surface_get_data.restype = POINTER(c_ubyte)
cairo_image_surface_get_data.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:2054
cairo_image_surface_get_format = _lib.cairo_image_surface_get_format
cairo_image_surface_get_format.restype = cairo_format_t
cairo_image_surface_get_format.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:2057
cairo_image_surface_get_width = _lib.cairo_image_surface_get_width
cairo_image_surface_get_width.restype = c_int
cairo_image_surface_get_width.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:2060
cairo_image_surface_get_height = _lib.cairo_image_surface_get_height
cairo_image_surface_get_height.restype = c_int
cairo_image_surface_get_height.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:2063
cairo_image_surface_get_stride = _lib.cairo_image_surface_get_stride
cairo_image_surface_get_stride.restype = c_int
cairo_image_surface_get_stride.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:2067
cairo_image_surface_create_from_png = _lib.cairo_image_surface_create_from_png
cairo_image_surface_create_from_png.restype = POINTER(cairo_surface_t)
cairo_image_surface_create_from_png.argtypes = [c_char_p]

# /usr/include/cairo/cairo.h:2070
cairo_image_surface_create_from_png_stream = _lib.cairo_image_surface_create_from_png_stream
cairo_image_surface_create_from_png_stream.restype = POINTER(cairo_surface_t)
cairo_image_surface_create_from_png_stream.argtypes = [cairo_read_func_t, POINTER(None)]

# /usr/include/cairo/cairo.h:2078
cairo_pattern_create_rgb = _lib.cairo_pattern_create_rgb
cairo_pattern_create_rgb.restype = POINTER(cairo_pattern_t)
cairo_pattern_create_rgb.argtypes = [c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:2081
cairo_pattern_create_rgba = _lib.cairo_pattern_create_rgba
cairo_pattern_create_rgba.restype = POINTER(cairo_pattern_t)
cairo_pattern_create_rgba.argtypes = [c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:2085
cairo_pattern_create_for_surface = _lib.cairo_pattern_create_for_surface
cairo_pattern_create_for_surface.restype = POINTER(cairo_pattern_t)
cairo_pattern_create_for_surface.argtypes = [POINTER(cairo_surface_t)]

# /usr/include/cairo/cairo.h:2088
cairo_pattern_create_linear = _lib.cairo_pattern_create_linear
cairo_pattern_create_linear.restype = POINTER(cairo_pattern_t)
cairo_pattern_create_linear.argtypes = [c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:2092
cairo_pattern_create_radial = _lib.cairo_pattern_create_radial
cairo_pattern_create_radial.restype = POINTER(cairo_pattern_t)
cairo_pattern_create_radial.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:2096
cairo_pattern_reference = _lib.cairo_pattern_reference
cairo_pattern_reference.restype = POINTER(cairo_pattern_t)
cairo_pattern_reference.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:2100
cairo_pattern_destroy = _lib.cairo_pattern_destroy
cairo_pattern_destroy.restype = None
cairo_pattern_destroy.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:2103
cairo_pattern_get_reference_count = _lib.cairo_pattern_get_reference_count
cairo_pattern_get_reference_count.restype = c_uint
cairo_pattern_get_reference_count.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:2106
cairo_pattern_status = _lib.cairo_pattern_status
cairo_pattern_status.restype = cairo_status_t
cairo_pattern_status.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:2108
cairo_pattern_get_user_data = _lib.cairo_pattern_get_user_data
cairo_pattern_get_user_data.restype = POINTER(c_void)
cairo_pattern_get_user_data.argtypes = [POINTER(cairo_pattern_t), POINTER(cairo_user_data_key_t)]

# /usr/include/cairo/cairo.h:2113
cairo_pattern_set_user_data = _lib.cairo_pattern_set_user_data
cairo_pattern_set_user_data.restype = cairo_status_t
cairo_pattern_set_user_data.argtypes = [POINTER(cairo_pattern_t), POINTER(cairo_user_data_key_t), POINTER(None), cairo_destroy_func_t]

enum__cairo_pattern_type = c_int
CAIRO_PATTERN_TYPE_SOLID = 0
CAIRO_PATTERN_TYPE_SURFACE = 1
CAIRO_PATTERN_TYPE_LINEAR = 2
CAIRO_PATTERN_TYPE_RADIAL = 3
cairo_pattern_type_t = enum__cairo_pattern_type 	# /usr/include/cairo/cairo.h:2153
# /usr/include/cairo/cairo.h:2156
cairo_pattern_get_type = _lib.cairo_pattern_get_type
cairo_pattern_get_type.restype = cairo_pattern_type_t
cairo_pattern_get_type.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:2159
cairo_pattern_add_color_stop_rgb = _lib.cairo_pattern_add_color_stop_rgb
cairo_pattern_add_color_stop_rgb.restype = None
cairo_pattern_add_color_stop_rgb.argtypes = [POINTER(cairo_pattern_t), c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:2164
cairo_pattern_add_color_stop_rgba = _lib.cairo_pattern_add_color_stop_rgba
cairo_pattern_add_color_stop_rgba.restype = None
cairo_pattern_add_color_stop_rgba.argtypes = [POINTER(cairo_pattern_t), c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:2170
cairo_pattern_set_matrix = _lib.cairo_pattern_set_matrix
cairo_pattern_set_matrix.restype = None
cairo_pattern_set_matrix.argtypes = [POINTER(cairo_pattern_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:2174
cairo_pattern_get_matrix = _lib.cairo_pattern_get_matrix
cairo_pattern_get_matrix.restype = None
cairo_pattern_get_matrix.argtypes = [POINTER(cairo_pattern_t), POINTER(cairo_matrix_t)]

enum__cairo_extend = c_int
CAIRO_EXTEND_NONE = 0
CAIRO_EXTEND_REPEAT = 1
CAIRO_EXTEND_REFLECT = 2
CAIRO_EXTEND_PAD = 3
cairo_extend_t = enum__cairo_extend 	# /usr/include/cairo/cairo.h:2203
# /usr/include/cairo/cairo.h:2206
cairo_pattern_set_extend = _lib.cairo_pattern_set_extend
cairo_pattern_set_extend.restype = None
cairo_pattern_set_extend.argtypes = [POINTER(cairo_pattern_t), cairo_extend_t]

# /usr/include/cairo/cairo.h:2209
cairo_pattern_get_extend = _lib.cairo_pattern_get_extend
cairo_pattern_get_extend.restype = cairo_extend_t
cairo_pattern_get_extend.argtypes = [POINTER(cairo_pattern_t)]

enum__cairo_filter = c_int
CAIRO_FILTER_FAST = 0
CAIRO_FILTER_GOOD = 1
CAIRO_FILTER_BEST = 2
CAIRO_FILTER_NEAREST = 3
CAIRO_FILTER_BILINEAR = 4
CAIRO_FILTER_GAUSSIAN = 5
cairo_filter_t = enum__cairo_filter 	# /usr/include/cairo/cairo.h:2236
# /usr/include/cairo/cairo.h:2239
cairo_pattern_set_filter = _lib.cairo_pattern_set_filter
cairo_pattern_set_filter.restype = None
cairo_pattern_set_filter.argtypes = [POINTER(cairo_pattern_t), cairo_filter_t]

# /usr/include/cairo/cairo.h:2242
cairo_pattern_get_filter = _lib.cairo_pattern_get_filter
cairo_pattern_get_filter.restype = cairo_filter_t
cairo_pattern_get_filter.argtypes = [POINTER(cairo_pattern_t)]

# /usr/include/cairo/cairo.h:2245
cairo_pattern_get_rgba = _lib.cairo_pattern_get_rgba
cairo_pattern_get_rgba.restype = cairo_status_t
cairo_pattern_get_rgba.argtypes = [POINTER(cairo_pattern_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2250
cairo_pattern_get_surface = _lib.cairo_pattern_get_surface
cairo_pattern_get_surface.restype = cairo_status_t
cairo_pattern_get_surface.argtypes = [POINTER(cairo_pattern_t), POINTER(POINTER(cairo_surface_t))]

# /usr/include/cairo/cairo.h:2255
cairo_pattern_get_color_stop_rgba = _lib.cairo_pattern_get_color_stop_rgba
cairo_pattern_get_color_stop_rgba.restype = cairo_status_t
cairo_pattern_get_color_stop_rgba.argtypes = [POINTER(cairo_pattern_t), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2261
cairo_pattern_get_color_stop_count = _lib.cairo_pattern_get_color_stop_count
cairo_pattern_get_color_stop_count.restype = cairo_status_t
cairo_pattern_get_color_stop_count.argtypes = [POINTER(cairo_pattern_t), POINTER(c_int)]

# /usr/include/cairo/cairo.h:2265
cairo_pattern_get_linear_points = _lib.cairo_pattern_get_linear_points
cairo_pattern_get_linear_points.restype = cairo_status_t
cairo_pattern_get_linear_points.argtypes = [POINTER(cairo_pattern_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2270
cairo_pattern_get_radial_circles = _lib.cairo_pattern_get_radial_circles
cairo_pattern_get_radial_circles.restype = cairo_status_t
cairo_pattern_get_radial_circles.argtypes = [POINTER(cairo_pattern_t), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2277
cairo_matrix_init = _lib.cairo_matrix_init
cairo_matrix_init.restype = None
cairo_matrix_init.argtypes = [POINTER(cairo_matrix_t), c_double, c_double, c_double, c_double, c_double, c_double]

# /usr/include/cairo/cairo.h:2283
cairo_matrix_init_identity = _lib.cairo_matrix_init_identity
cairo_matrix_init_identity.restype = None
cairo_matrix_init_identity.argtypes = [POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:2286
cairo_matrix_init_translate = _lib.cairo_matrix_init_translate
cairo_matrix_init_translate.restype = None
cairo_matrix_init_translate.argtypes = [POINTER(cairo_matrix_t), c_double, c_double]

# /usr/include/cairo/cairo.h:2290
cairo_matrix_init_scale = _lib.cairo_matrix_init_scale
cairo_matrix_init_scale.restype = None
cairo_matrix_init_scale.argtypes = [POINTER(cairo_matrix_t), c_double, c_double]

# /usr/include/cairo/cairo.h:2294
cairo_matrix_init_rotate = _lib.cairo_matrix_init_rotate
cairo_matrix_init_rotate.restype = None
cairo_matrix_init_rotate.argtypes = [POINTER(cairo_matrix_t), c_double]

# /usr/include/cairo/cairo.h:2298
cairo_matrix_translate = _lib.cairo_matrix_translate
cairo_matrix_translate.restype = None
cairo_matrix_translate.argtypes = [POINTER(cairo_matrix_t), c_double, c_double]

# /usr/include/cairo/cairo.h:2301
cairo_matrix_scale = _lib.cairo_matrix_scale
cairo_matrix_scale.restype = None
cairo_matrix_scale.argtypes = [POINTER(cairo_matrix_t), c_double, c_double]

# /usr/include/cairo/cairo.h:2304
cairo_matrix_rotate = _lib.cairo_matrix_rotate
cairo_matrix_rotate.restype = None
cairo_matrix_rotate.argtypes = [POINTER(cairo_matrix_t), c_double]

# /usr/include/cairo/cairo.h:2307
cairo_matrix_invert = _lib.cairo_matrix_invert
cairo_matrix_invert.restype = cairo_status_t
cairo_matrix_invert.argtypes = [POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:2310
cairo_matrix_multiply = _lib.cairo_matrix_multiply
cairo_matrix_multiply.restype = None
cairo_matrix_multiply.argtypes = [POINTER(cairo_matrix_t), POINTER(cairo_matrix_t), POINTER(cairo_matrix_t)]

# /usr/include/cairo/cairo.h:2315
cairo_matrix_transform_distance = _lib.cairo_matrix_transform_distance
cairo_matrix_transform_distance.restype = None
cairo_matrix_transform_distance.argtypes = [POINTER(cairo_matrix_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2319
cairo_matrix_transform_point = _lib.cairo_matrix_transform_point
cairo_matrix_transform_point.restype = None
cairo_matrix_transform_point.argtypes = [POINTER(cairo_matrix_t), POINTER(c_double), POINTER(c_double)]

# /usr/include/cairo/cairo.h:2324
cairo_debug_reset_static_data = _lib.cairo_debug_reset_static_data
cairo_debug_reset_static_data.restype = None
cairo_debug_reset_static_data.argtypes = []


__all__ = ['CAIRO_VERSION', 'cairo_version', 'cairo_version_string',
'cairo_bool_t', 'cairo_t', 'cairo_surface_t', 'cairo_matrix_t',
'cairo_pattern_t', 'cairo_destroy_func_t', 'cairo_user_data_key_t',
'cairo_status_t', 'CAIRO_STATUS_SUCCESS', 'CAIRO_STATUS_NO_MEMORY',
'CAIRO_STATUS_INVALID_RESTORE', 'CAIRO_STATUS_INVALID_POP_GROUP',
'CAIRO_STATUS_NO_CURRENT_POINT', 'CAIRO_STATUS_INVALID_MATRIX',
'CAIRO_STATUS_INVALID_STATUS', 'CAIRO_STATUS_NULL_POINTER',
'CAIRO_STATUS_INVALID_STRING', 'CAIRO_STATUS_INVALID_PATH_DATA',
'CAIRO_STATUS_READ_ERROR', 'CAIRO_STATUS_WRITE_ERROR',
'CAIRO_STATUS_SURFACE_FINISHED', 'CAIRO_STATUS_SURFACE_TYPE_MISMATCH',
'CAIRO_STATUS_PATTERN_TYPE_MISMATCH', 'CAIRO_STATUS_INVALID_CONTENT',
'CAIRO_STATUS_INVALID_FORMAT', 'CAIRO_STATUS_INVALID_VISUAL',
'CAIRO_STATUS_FILE_NOT_FOUND', 'CAIRO_STATUS_INVALID_DASH',
'CAIRO_STATUS_INVALID_DSC_COMMENT', 'CAIRO_STATUS_INVALID_INDEX',
'CAIRO_STATUS_CLIP_NOT_REPRESENTABLE', 'CAIRO_STATUS_TEMP_FILE_ERROR',
'CAIRO_STATUS_INVALID_STRIDE', 'CAIRO_STATUS_FONT_TYPE_MISMATCH',
'CAIRO_STATUS_USER_FONT_IMMUTABLE', 'CAIRO_STATUS_USER_FONT_ERROR',
'CAIRO_STATUS_NEGATIVE_COUNT', 'CAIRO_STATUS_INVALID_CLUSTERS',
'CAIRO_STATUS_INVALID_SLANT', 'CAIRO_STATUS_INVALID_WEIGHT',
'cairo_content_t', 'CAIRO_CONTENT_COLOR', 'CAIRO_CONTENT_ALPHA',
'CAIRO_CONTENT_COLOR_ALPHA', 'cairo_write_func_t', 'cairo_read_func_t',
'cairo_create', 'cairo_reference', 'cairo_destroy',
'cairo_get_reference_count', 'cairo_get_user_data', 'cairo_set_user_data',
'cairo_save', 'cairo_restore', 'cairo_push_group',
'cairo_push_group_with_content', 'cairo_pop_group',
'cairo_pop_group_to_source', 'cairo_operator_t', 'CAIRO_OPERATOR_CLEAR',
'CAIRO_OPERATOR_SOURCE', 'CAIRO_OPERATOR_OVER', 'CAIRO_OPERATOR_IN',
'CAIRO_OPERATOR_OUT', 'CAIRO_OPERATOR_ATOP', 'CAIRO_OPERATOR_DEST',
'CAIRO_OPERATOR_DEST_OVER', 'CAIRO_OPERATOR_DEST_IN',
'CAIRO_OPERATOR_DEST_OUT', 'CAIRO_OPERATOR_DEST_ATOP', 'CAIRO_OPERATOR_XOR',
'CAIRO_OPERATOR_ADD', 'CAIRO_OPERATOR_SATURATE', 'cairo_set_operator',
'cairo_set_source', 'cairo_set_source_rgb', 'cairo_set_source_rgba',
'cairo_set_source_surface', 'cairo_set_tolerance', 'cairo_antialias_t',
'CAIRO_ANTIALIAS_DEFAULT', 'CAIRO_ANTIALIAS_NONE', 'CAIRO_ANTIALIAS_GRAY',
'CAIRO_ANTIALIAS_SUBPIXEL', 'cairo_set_antialias', 'cairo_fill_rule_t',
'CAIRO_FILL_RULE_WINDING', 'CAIRO_FILL_RULE_EVEN_ODD', 'cairo_set_fill_rule',
'cairo_set_line_width', 'cairo_line_cap_t', 'CAIRO_LINE_CAP_BUTT',
'CAIRO_LINE_CAP_ROUND', 'CAIRO_LINE_CAP_SQUARE', 'cairo_set_line_cap',
'cairo_line_join_t', 'CAIRO_LINE_JOIN_MITER', 'CAIRO_LINE_JOIN_ROUND',
'CAIRO_LINE_JOIN_BEVEL', 'cairo_set_line_join', 'cairo_set_dash',
'cairo_set_miter_limit', 'cairo_translate', 'cairo_scale', 'cairo_rotate',
'cairo_transform', 'cairo_set_matrix', 'cairo_identity_matrix',
'cairo_user_to_device', 'cairo_user_to_device_distance',
'cairo_device_to_user', 'cairo_device_to_user_distance', 'cairo_new_path',
'cairo_move_to', 'cairo_new_sub_path', 'cairo_line_to', 'cairo_curve_to',
'cairo_arc', 'cairo_arc_negative', 'cairo_rel_move_to', 'cairo_rel_line_to',
'cairo_rel_curve_to', 'cairo_rectangle', 'cairo_close_path',
'cairo_path_extents', 'cairo_paint', 'cairo_paint_with_alpha', 'cairo_mask',
'cairo_mask_surface', 'cairo_stroke', 'cairo_stroke_preserve', 'cairo_fill',
'cairo_fill_preserve', 'cairo_copy_page', 'cairo_show_page',
'cairo_in_stroke', 'cairo_in_fill', 'cairo_stroke_extents',
'cairo_fill_extents', 'cairo_reset_clip', 'cairo_clip', 'cairo_clip_preserve',
'cairo_clip_extents', 'cairo_rectangle_t', 'cairo_rectangle_list_t',
'cairo_copy_clip_rectangle_list', 'cairo_rectangle_list_destroy',
'cairo_scaled_font_t', 'cairo_font_face_t', 'cairo_glyph_t',
'cairo_glyph_allocate', 'cairo_glyph_free', 'cairo_text_cluster_t',
'cairo_text_cluster_allocate', 'cairo_text_cluster_free',
'cairo_text_cluster_flags_t', 'CAIRO_TEXT_CLUSTER_FLAG_BACKWARD',
'cairo_text_extents_t', 'cairo_font_extents_t', 'cairo_font_slant_t',
'CAIRO_FONT_SLANT_NORMAL', 'CAIRO_FONT_SLANT_ITALIC',
'CAIRO_FONT_SLANT_OBLIQUE', 'cairo_font_weight_t', 'CAIRO_FONT_WEIGHT_NORMAL',
'CAIRO_FONT_WEIGHT_BOLD', 'cairo_subpixel_order_t',
'CAIRO_SUBPIXEL_ORDER_DEFAULT', 'CAIRO_SUBPIXEL_ORDER_RGB',
'CAIRO_SUBPIXEL_ORDER_BGR', 'CAIRO_SUBPIXEL_ORDER_VRGB',
'CAIRO_SUBPIXEL_ORDER_VBGR', 'cairo_hint_style_t', 'CAIRO_HINT_STYLE_DEFAULT',
'CAIRO_HINT_STYLE_NONE', 'CAIRO_HINT_STYLE_SLIGHT', 'CAIRO_HINT_STYLE_MEDIUM',
'CAIRO_HINT_STYLE_FULL', 'cairo_hint_metrics_t', 'CAIRO_HINT_METRICS_DEFAULT',
'CAIRO_HINT_METRICS_OFF', 'CAIRO_HINT_METRICS_ON', 'cairo_font_options_t',
'cairo_font_options_create', 'cairo_font_options_copy',
'cairo_font_options_destroy', 'cairo_font_options_status',
'cairo_font_options_merge', 'cairo_font_options_equal',
'cairo_font_options_hash', 'cairo_font_options_set_antialias',
'cairo_font_options_get_antialias', 'cairo_font_options_set_subpixel_order',
'cairo_font_options_get_subpixel_order', 'cairo_font_options_set_hint_style',
'cairo_font_options_get_hint_style', 'cairo_font_options_set_hint_metrics',
'cairo_font_options_get_hint_metrics', 'cairo_select_font_face',
'cairo_set_font_size', 'cairo_set_font_matrix', 'cairo_get_font_matrix',
'cairo_set_font_options', 'cairo_get_font_options', 'cairo_set_font_face',
'cairo_get_font_face', 'cairo_set_scaled_font', 'cairo_get_scaled_font',
'cairo_show_text', 'cairo_show_glyphs', 'cairo_show_text_glyphs',
'cairo_text_path', 'cairo_glyph_path', 'cairo_text_extents',
'cairo_glyph_extents', 'cairo_font_extents', 'cairo_font_face_reference',
'cairo_font_face_destroy', 'cairo_font_face_get_reference_count',
'cairo_font_face_status', 'cairo_font_type_t', 'CAIRO_FONT_TYPE_TOY',
'CAIRO_FONT_TYPE_FT', 'CAIRO_FONT_TYPE_WIN32', 'CAIRO_FONT_TYPE_QUARTZ',
'CAIRO_FONT_TYPE_USER', 'cairo_font_face_get_type',
'cairo_font_face_get_user_data', 'cairo_font_face_set_user_data',
'cairo_scaled_font_create', 'cairo_scaled_font_reference',
'cairo_scaled_font_destroy', 'cairo_scaled_font_get_reference_count',
'cairo_scaled_font_status', 'cairo_scaled_font_get_type',
'cairo_scaled_font_get_user_data', 'cairo_scaled_font_set_user_data',
'cairo_scaled_font_extents', 'cairo_scaled_font_text_extents',
'cairo_scaled_font_glyph_extents', 'cairo_scaled_font_text_to_glyphs',
'cairo_scaled_font_get_font_face', 'cairo_scaled_font_get_font_matrix',
'cairo_scaled_font_get_ctm', 'cairo_scaled_font_get_scale_matrix',
'cairo_scaled_font_get_font_options', 'cairo_toy_font_face_create',
'cairo_toy_font_face_get_family', 'cairo_toy_font_face_get_slant',
'cairo_toy_font_face_get_weight', 'cairo_user_font_face_create',
'cairo_user_scaled_font_init_func_t',
'cairo_user_scaled_font_render_glyph_func_t',
'cairo_user_scaled_font_text_to_glyphs_func_t',
'cairo_user_scaled_font_unicode_to_glyph_func_t',
'cairo_user_font_face_set_init_func',
'cairo_user_font_face_set_render_glyph_func',
'cairo_user_font_face_set_text_to_glyphs_func',
'cairo_user_font_face_set_unicode_to_glyph_func',
'cairo_user_font_face_get_init_func',
'cairo_user_font_face_get_render_glyph_func',
'cairo_user_font_face_get_text_to_glyphs_func',
'cairo_user_font_face_get_unicode_to_glyph_func', 'cairo_get_operator',
'cairo_get_source', 'cairo_get_tolerance', 'cairo_get_antialias',
'cairo_has_current_point', 'cairo_get_current_point', 'cairo_get_fill_rule',
'cairo_get_line_width', 'cairo_get_line_cap', 'cairo_get_line_join',
'cairo_get_miter_limit', 'cairo_get_dash_count', 'cairo_get_dash',
'cairo_get_matrix', 'cairo_get_target', 'cairo_get_group_target',
'cairo_path_data_type_t', 'CAIRO_PATH_MOVE_TO', 'CAIRO_PATH_LINE_TO',
'CAIRO_PATH_CURVE_TO', 'CAIRO_PATH_CLOSE_PATH', 'cairo_path_data_t',
'cairo_path_t', 'cairo_copy_path', 'cairo_copy_path_flat',
'cairo_append_path', 'cairo_path_destroy', 'cairo_status',
'cairo_status_to_string', 'cairo_surface_create_similar',
'cairo_surface_reference', 'cairo_surface_finish', 'cairo_surface_destroy',
'cairo_surface_get_reference_count', 'cairo_surface_status',
'cairo_surface_type_t', 'CAIRO_SURFACE_TYPE_IMAGE', 'CAIRO_SURFACE_TYPE_PDF',
'CAIRO_SURFACE_TYPE_PS', 'CAIRO_SURFACE_TYPE_XLIB', 'CAIRO_SURFACE_TYPE_XCB',
'CAIRO_SURFACE_TYPE_GLITZ', 'CAIRO_SURFACE_TYPE_QUARTZ',
'CAIRO_SURFACE_TYPE_WIN32', 'CAIRO_SURFACE_TYPE_BEOS',
'CAIRO_SURFACE_TYPE_DIRECTFB', 'CAIRO_SURFACE_TYPE_SVG',
'CAIRO_SURFACE_TYPE_OS2', 'CAIRO_SURFACE_TYPE_WIN32_PRINTING',
'CAIRO_SURFACE_TYPE_QUARTZ_IMAGE', 'cairo_surface_get_type',
'cairo_surface_get_content', 'cairo_surface_write_to_png',
'cairo_surface_write_to_png_stream', 'cairo_surface_get_user_data',
'cairo_surface_set_user_data', 'cairo_surface_get_font_options',
'cairo_surface_flush', 'cairo_surface_mark_dirty',
'cairo_surface_mark_dirty_rectangle', 'cairo_surface_set_device_offset',
'cairo_surface_get_device_offset', 'cairo_surface_set_fallback_resolution',
'cairo_surface_get_fallback_resolution', 'cairo_surface_copy_page',
'cairo_surface_show_page', 'cairo_surface_has_show_text_glyphs',
'cairo_format_t', 'CAIRO_FORMAT_ARGB32', 'CAIRO_FORMAT_RGB24',
'CAIRO_FORMAT_A8', 'CAIRO_FORMAT_A1', 'cairo_image_surface_create',
'cairo_format_stride_for_width', 'cairo_image_surface_create_for_data',
'cairo_image_surface_get_data', 'cairo_image_surface_get_format',
'cairo_image_surface_get_width', 'cairo_image_surface_get_height',
'cairo_image_surface_get_stride', 'cairo_image_surface_create_from_png',
'cairo_image_surface_create_from_png_stream', 'cairo_pattern_create_rgb',
'cairo_pattern_create_rgba', 'cairo_pattern_create_for_surface',
'cairo_pattern_create_linear', 'cairo_pattern_create_radial',
'cairo_pattern_reference', 'cairo_pattern_destroy',
'cairo_pattern_get_reference_count', 'cairo_pattern_status',
'cairo_pattern_get_user_data', 'cairo_pattern_set_user_data',
'cairo_pattern_type_t', 'CAIRO_PATTERN_TYPE_SOLID',
'CAIRO_PATTERN_TYPE_SURFACE', 'CAIRO_PATTERN_TYPE_LINEAR',
'CAIRO_PATTERN_TYPE_RADIAL', 'cairo_pattern_get_type',
'cairo_pattern_add_color_stop_rgb', 'cairo_pattern_add_color_stop_rgba',
'cairo_pattern_set_matrix', 'cairo_pattern_get_matrix', 'cairo_extend_t',
'CAIRO_EXTEND_NONE', 'CAIRO_EXTEND_REPEAT', 'CAIRO_EXTEND_REFLECT',
'CAIRO_EXTEND_PAD', 'cairo_pattern_set_extend', 'cairo_pattern_get_extend',
'cairo_filter_t', 'CAIRO_FILTER_FAST', 'CAIRO_FILTER_GOOD',
'CAIRO_FILTER_BEST', 'CAIRO_FILTER_NEAREST', 'CAIRO_FILTER_BILINEAR',
'CAIRO_FILTER_GAUSSIAN', 'cairo_pattern_set_filter',
'cairo_pattern_get_filter', 'cairo_pattern_get_rgba',
'cairo_pattern_get_surface', 'cairo_pattern_get_color_stop_rgba',
'cairo_pattern_get_color_stop_count', 'cairo_pattern_get_linear_points',
'cairo_pattern_get_radial_circles', 'cairo_matrix_init',
'cairo_matrix_init_identity', 'cairo_matrix_init_translate',
'cairo_matrix_init_scale', 'cairo_matrix_init_rotate',
'cairo_matrix_translate', 'cairo_matrix_scale', 'cairo_matrix_rotate',
'cairo_matrix_invert', 'cairo_matrix_multiply',
'cairo_matrix_transform_distance', 'cairo_matrix_transform_point',
'cairo_debug_reset_static_data']

xcb_drawable_t = c_uint32 	# /usr/include/xcb/xproto.h:115
xcb_visualid_t = c_uint32 	# /usr/include/xcb/xproto.h:137
# /usr/include/cairo/cairo-xcb.h:48
_cairo_xcb_surface_create = _lib.cairo_xcb_surface_create
_cairo_xcb_surface_create.restype = POINTER(cairo_surface_t)
_cairo_xcb_surface_create.argtypes = [POINTER(xcb_connection_t), xcb_drawable_t, c_void_p, c_int, c_int]

def cairo_xcb_surface_create(conn, drawable, visualtype, width, height):
    stream = StringIO()
    visualtype.build(stream)
    buffer = stream.getvalue()
    visualtype_data = cast(create_string_buffer(buffer, len(buffer)), c_void_p)
    return _cairo_xcb_surface_create(
            conn.conn,
            drawable.get_internal(),
            visualtype_data,
            width,
            height)

xcb_pixmap_t = c_uint32 	# /usr/include/xcb/xproto.h:49
xcb_window_t = c_uint32 	# /usr/include/xcb/xproto.h:38
xcb_colormap_t = c_uint32 	# /usr/include/xcb/xproto.h:93

# /usr/include/cairo/cairo-xcb.h:55
_cairo_xcb_surface_create_for_bitmap = _lib.cairo_xcb_surface_create_for_bitmap
_cairo_xcb_surface_create_for_bitmap.restype = POINTER(cairo_surface_t)
_cairo_xcb_surface_create_for_bitmap.argtypes = [POINTER(xcb_connection_t), xcb_pixmap_t, c_void_p, c_int, c_int]

def cairo_xcb_surface_create_for_bitmap(conn, pixmap, screen, width, height):
    stream = StringIO()
    screen.build(stream)
    buffer = stream.getvalue()
    screen_data = cast(create_string_buffer(buffer, len(buffer)), c_void_p)
    return _cairo_xcb_surface_create_for_bitmap(
            conn.conn,
            pixmap.get_internal(),
            screen_data,
            width,
            height)

# /usr/include/cairo/cairo-xcb.h:63
cairo_xcb_surface_set_size = _lib.cairo_xcb_surface_set_size
cairo_xcb_surface_set_size.restype = None
cairo_xcb_surface_set_size.argtypes = [POINTER(cairo_surface_t), c_int, c_int]


__all__ += ['cairo_xcb_surface_create', 'cairo_xcb_surface_create_for_bitmap',
'cairo_xcb_surface_set_size']
