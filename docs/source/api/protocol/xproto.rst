ooxcb.protocol.xproto
=====================

.. module:: ooxcb.protocol.xproto

.. class:: GetModifierMappingCookie

.. class:: TranslateCoordinatesReply

    .. method:: __init__(self, conn)


    .. attribute:: dst_y

    .. attribute:: dst_x

    .. attribute:: same_screen

    .. attribute:: child

.. class:: PropMode

    .. data:: Replace


    .. data:: Prepend


    .. data:: Append


.. class:: HostMode

    .. data:: Insert


    .. data:: Delete


.. class:: QueryBestSizeCookie

.. class:: GraphicsExposureEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: count

    .. attribute:: width

    .. attribute:: major_opcode

    .. attribute:: height

    .. attribute:: minor_opcode

    .. attribute:: response_type

    .. attribute:: y

    .. attribute:: x

    .. attribute:: drawable

.. class:: FontDraw

    .. data:: LeftToRight


    .. data:: RightToLeft


.. class:: ClientMessageData

    .. method:: __init__(self, conn)


.. class:: QueryExtensionReply

    .. method:: __init__(self, conn)


    .. attribute:: first_event

    .. attribute:: first_error

    .. attribute:: major_opcode

    .. attribute:: present

.. class:: QueryTreeReply

    .. method:: __init__(self, conn)


    .. attribute:: children_len

    .. attribute:: root

    .. attribute:: children

    .. attribute:: parent

.. class:: ListInstalledColormapsReply

    .. method:: __init__(self, conn)


    .. attribute:: cmaps_len

    .. attribute:: cmaps

.. class:: Rgb

    .. method:: __init__(self, conn)


    .. attribute:: blue

    .. attribute:: green

    .. attribute:: red

.. class:: QueryTreeCookie

.. class:: VisualClass

    .. data:: StaticGray


    .. data:: GrayScale


    .. data:: StaticColor


    .. data:: PseudoColor


    .. data:: TrueColor


    .. data:: DirectColor


.. class:: GetWindowAttributesReply

    .. method:: __init__(self, conn)


    .. attribute:: your_event_mask

    .. attribute:: override_redirect

    .. attribute:: backing_pixel

    .. attribute:: bit_gravity

    .. attribute:: all_event_masks

    .. attribute:: save_under

    .. attribute:: visual

    .. attribute:: do_not_propagate_mask

    .. attribute:: map_state

    .. attribute:: backing_store

    .. attribute:: win_gravity

    .. attribute:: backing_planes

    .. attribute:: map_is_installed

    .. attribute:: _class

    .. attribute:: colormap

.. class:: AllocColorCookie

.. class:: Exposures

    .. data:: NotAllowed


    .. data:: Allowed


    .. data:: Default


.. class:: AllocError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: ButtonIndex

    .. data:: Any


    .. data:: _1


    .. data:: _2


    .. data:: _3


    .. data:: _4


    .. data:: _5


.. class:: Colormap

    .. method:: __init__(self, conn, xid)


    .. method:: free_checked(self)


    .. method:: free(self)


    .. method:: copy_colormap_and_free_checked(self, mid)


    .. method:: copy_colormap_and_free(self, mid)


    .. method:: install_checked(self)


    .. method:: install(self)


    .. method:: uninstall_checked(self)


    .. method:: uninstall(self)


    .. method:: alloc_color(self, red, green, blue)


    .. method:: alloc_color_unchecked(self, red, green, blue)


    .. method:: alloc_named_color(self, name)


    .. method:: alloc_named_color_unchecked(self, name)


    .. method:: alloc_color_cells(self, contiguous, colors, planes)


    .. method:: alloc_color_cells_unchecked(self, contiguous, colors, planes)


    .. method:: alloc_color_planes(self, contiguous, colors, reds, greens, blues)


    .. method:: alloc_color_planes_unchecked(self, contiguous, colors, reds, greens, blues)


    .. method:: free_colors_checked(self, pixels, plane_mask)


    .. method:: free_colors(self, pixels, plane_mask)


    .. method:: store_colors_checked(self, items)


    .. method:: store_colors(self, items)


    .. method:: store_named_color_checked(self, flags, pixel, name)


    .. method:: store_named_color(self, flags, pixel, name)


    .. method:: query_colors(self, pixels)


    .. method:: query_colors_unchecked(self, pixels)


    .. method:: lookup_color(self, name)


    .. method:: lookup_color_unchecked(self, name)


    .. method:: alloc_hex_color(self, color)


    .. classmethod:: create(cls, window, visual, alloc=0)


.. class:: SetModifierMappingReply

    .. method:: __init__(self, conn)


    .. attribute:: status

.. class:: ConfigWindow

    .. data:: X


    .. data:: Y


    .. data:: Width


    .. data:: Height


    .. data:: BorderWidth


    .. data:: Sibling


    .. data:: StackMode


.. class:: GrabPointerReply

    .. method:: __init__(self, conn)


    .. attribute:: status

.. class:: NameError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: BadAtom

.. class:: BadCursor

.. class:: GContextError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: GetPropertyType

    .. data:: Any


.. class:: Coloritem

    .. method:: __init__(self, conn)


    .. attribute:: blue

    .. attribute:: flags

    .. attribute:: green

    .. attribute:: pixel

    .. attribute:: red

.. class:: BadAccess

.. class:: RequestError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: Setupauthenticate

    .. method:: __init__(self, conn)


    .. attribute:: status

    .. attribute:: length

    .. attribute:: reason

.. class:: GetScreenSaverReply

    .. method:: __init__(self, conn)


    .. attribute:: interval

    .. attribute:: prefer_blanking

    .. attribute:: timeout

    .. attribute:: allow_exposures

.. class:: LengthError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: AccessControl

    .. data:: Disable


    .. data:: Enable


.. class:: ListFontsWithInfoCookie

.. class:: Blanking

    .. data:: NotPreferred


    .. data:: Preferred


    .. data:: Default


.. class:: Fontable

    .. method:: __init__(self, conn, xid)


    .. method:: query(self)


    .. method:: query_unchecked(self)


    .. method:: query_text_extents(self, string)


    .. method:: query_text_extents_unchecked(self, string)


.. class:: QueryShapeOf

    .. data:: LargestCursor


    .. data:: FastestTile


    .. data:: FastestStipple


.. class:: ConfigureNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: override_redirect

    .. attribute:: above_sibling

    .. attribute:: height

    .. attribute:: width

    .. attribute:: window

    .. attribute:: response_type

    .. attribute:: y

    .. attribute:: x

    .. attribute:: border_width

    .. attribute:: event

.. class:: Setup

    .. method:: __init__(self, conn)


    .. attribute:: status

    .. attribute:: protocol_major_version

    .. attribute:: roots_len

    .. attribute:: bitmap_format_bit_order

    .. attribute:: resource_id_base

    .. attribute:: max_keycode

    .. attribute:: bitmap_format_scanline_pad

    .. attribute:: min_keycode

    .. attribute:: protocol_minor_version

    .. attribute:: release_number

    .. attribute:: vendor

    .. attribute:: length

    .. attribute:: vendor_len

    .. attribute:: bitmap_format_scanline_unit

    .. attribute:: pixmap_formats

    .. attribute:: pixmap_formats_len

    .. attribute:: image_byte_order

    .. attribute:: motion_buffer_size

    .. attribute:: maximum_request_length

    .. attribute:: roots

    .. attribute:: resource_id_mask

.. class:: WindowClass

    .. data:: CopyFromParent


    .. data:: InputOutput


    .. data:: InputOnly


.. class:: SelectionClearEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: owner

    .. attribute:: selection

    .. attribute:: response_type

    .. attribute:: time

.. class:: GX

    .. data:: clear


    .. data:: _and


    .. data:: andReverse


    .. data:: copy


    .. data:: andInverted


    .. data:: noop


    .. data:: xor


    .. data:: _or


    .. data:: nor


    .. data:: equiv


    .. data:: invert


    .. data:: orReverse


    .. data:: copyInverted


    .. data:: orInverted


    .. data:: nand


    .. data:: set


.. class:: Motion

    .. data:: Normal


    .. data:: Hint


.. class:: GC

    .. data:: Function


    .. data:: PlaneMask


    .. data:: Foreground


    .. data:: Background


    .. data:: LineWidth


    .. data:: LineStyle


    .. data:: CapStyle


    .. data:: JoinStyle


    .. data:: FillStyle


    .. data:: FillRule


    .. data:: Tile


    .. data:: Stipple


    .. data:: TileStippleOriginX


    .. data:: TileStippleOriginY


    .. data:: Font


    .. data:: SubwindowMode


    .. data:: GraphicsExposures


    .. data:: ClipOriginX


    .. data:: ClipOriginY


    .. data:: ClipMask


    .. data:: DashOffset


    .. data:: DashList


    .. data:: ArcMode


.. class:: GetSelectionOwnerCookie

.. class:: ImplementationError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: ListHostsReply

    .. method:: __init__(self, conn)


    .. attribute:: hosts_len

    .. attribute:: hosts

    .. attribute:: mode

.. class:: GetModifierMappingReply

    .. method:: __init__(self, conn)


    .. attribute:: keycodes

    .. attribute:: keycodes_per_modifier

.. class:: GetPointerMappingReply

    .. method:: __init__(self, conn)


    .. attribute:: map_len

    .. attribute:: map

.. class:: DestroyNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: window

    .. attribute:: event

    .. attribute:: response_type

.. class:: QueryKeymapReply

    .. method:: __init__(self, conn)


    .. attribute:: keys

.. class:: AllocColorReply

    .. method:: __init__(self, conn)


    .. attribute:: blue

    .. attribute:: green

    .. attribute:: pixel

    .. attribute:: red

.. class:: BadName

.. class:: ListInstalledColormapsCookie

.. class:: GetScreenSaverCookie

.. class:: Arc

    .. method:: __init__(self, conn)


    .. classmethod:: create(cls, conn, x, y, width, height, angle1, angle2)


    .. attribute:: height

    .. attribute:: width

    .. attribute:: angle1

    .. attribute:: angle2

    .. attribute:: y

    .. attribute:: x

.. class:: Kill

    .. data:: AllTemporary


.. class:: QueryFontCookie

.. class:: Font

    .. method:: __init__(self, conn, xid)


    .. method:: close_checked(self)


    .. method:: close(self)


    .. classmethod:: open(cls, conn, name)


.. class:: QueryKeymapCookie

.. class:: ExposeEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: count

    .. attribute:: height

    .. attribute:: width

    .. attribute:: window

    .. attribute:: response_type

    .. attribute:: y

    .. attribute:: x

.. class:: GravityNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: y

    .. attribute:: x

    .. attribute:: window

    .. attribute:: event

    .. attribute:: response_type

.. class:: GrabKeyboardReply

    .. method:: __init__(self, conn)


    .. attribute:: status

.. class:: ListPropertiesReply

    .. method:: __init__(self, conn)


    .. attribute:: atoms

    .. attribute:: atoms_len

.. class:: ListExtensionsReply

    .. method:: __init__(self, conn)


    .. attribute:: names_len

    .. attribute:: names

.. class:: CapStyle

    .. data:: NotLast


    .. data:: Butt


    .. data:: Round


    .. data:: Projecting


.. class:: AllocNamedColorCookie

.. class:: MatchError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: UnmapNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: window

    .. attribute:: response_type

    .. attribute:: event

    .. attribute:: from_configure

.. class:: Setupfailed

    .. method:: __init__(self, conn)


    .. attribute:: status

    .. attribute:: protocol_major_version

    .. attribute:: length

    .. attribute:: protocol_minor_version

    .. attribute:: reason

    .. attribute:: reason_len

.. class:: IDChoiceError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: AllocColorCellsReply

    .. method:: __init__(self, conn)


    .. attribute:: pixels_len

    .. attribute:: masks_len

    .. attribute:: pixels

    .. attribute:: masks

.. class:: ConfigureRequestEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: parent

    .. attribute:: width

    .. attribute:: stack_mode

    .. attribute:: height

    .. attribute:: sibling

    .. attribute:: window

    .. attribute:: response_type

    .. attribute:: y

    .. attribute:: x

    .. attribute:: border_width

    .. attribute:: value_mask

.. class:: BadImplementation

.. class:: TranslateCoordinatesCookie

.. class:: BadRequest

.. class:: FillRule

    .. data:: EvenOdd


    .. data:: Winding


.. class:: GrabMode

    .. data:: Sync


    .. data:: Async


.. class:: GetKeyboardControlCookie

.. class:: WMState

    .. data:: Withdrawn


    .. data:: Normal


    .. data:: Iconic


.. class:: ColormapAlloc

    .. data:: _None


    .. data:: All


.. class:: FontError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: ModMask

    .. data:: Shift


    .. data:: Lock


    .. data:: Control


    .. data:: _1


    .. data:: _2


    .. data:: _3


    .. data:: _4


    .. data:: _5


    .. data:: Any


.. class:: Setuprequest

    .. method:: __init__(self, conn)


    .. attribute:: byte_order

    .. attribute:: authorization_protocol_name

    .. attribute:: protocol_minor_version

    .. attribute:: authorization_protocol_data

    .. attribute:: authorization_protocol_data_len

    .. attribute:: protocol_major_version

    .. attribute:: authorization_protocol_name_len

.. class:: Visibility

    .. data:: Unobscured


    .. data:: PartiallyObscured


    .. data:: FullyObscured


.. class:: FillStyle

    .. data:: Solid


    .. data:: Tiled


    .. data:: Stippled


    .. data:: OpaqueStippled


.. class:: LedMode

    .. data:: Off


    .. data:: On


.. class:: KeymapNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: keys

    .. attribute:: response_type

.. class:: BadIDChoice

.. class:: GetKeyboardMappingCookie

.. class:: SubwindowMode

    .. data:: ClipByChildren


    .. data:: IncludeInferiors


.. class:: Circulate

    .. data:: RaiseLowest


    .. data:: LowerHighest


.. class:: AutoRepeatMode

    .. data:: Off


    .. data:: On


    .. data:: Default


.. class:: BackingStore

    .. data:: NotUseful


    .. data:: WhenMapped


    .. data:: Always


.. class:: StackMode

    .. data:: Above


    .. data:: Below


    .. data:: TopIf


    .. data:: BottomIf


    .. data:: Opposite


.. class:: AllocColorPlanesCookie

.. class:: BadMatch

.. class:: Visualtype

    .. method:: __init__(self, conn)


    .. attribute:: colormap_entries

    .. attribute:: visual_id

    .. attribute:: blue_mask

    .. attribute:: green_mask

    .. attribute:: red_mask

    .. attribute:: _class

    .. attribute:: bits_per_rgb_value

.. class:: ArcMode

    .. data:: Chord


    .. data:: PieSlice


.. class:: BackPixmap

    .. data:: _None


    .. data:: ParentRelative


.. class:: BadFont

.. class:: Cursor

    .. method:: __init__(self, conn, xid)


    .. method:: free_checked(self)


    .. method:: free(self)


    .. method:: recolor_checked(self, fore_red, fore_green, fore_blue, back_red, back_green, back_blue)


    .. method:: recolor(self, fore_red, fore_green, fore_blue, back_red, back_green, back_blue)


    .. classmethod:: create(cls, conn, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y)


    .. classmethod:: create_glyph(cls, conn, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue)


.. class:: Place

    .. data:: OnTop


    .. data:: OnBottom


.. class:: GrabPointerCookie

.. class:: BadValue

.. class:: GetInputFocusCookie

.. class:: Grab

    .. data:: Any


.. class:: Property

    .. data:: NewValue


    .. data:: Delete


.. class:: DrawableError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: AllocColorCellsCookie

.. class:: MappingStatus

    .. data:: Success


    .. data:: Busy


    .. data:: Failure


.. class:: SetPointerMappingCookie

.. class:: Point

    .. method:: __init__(self, conn)


    .. attribute:: y

    .. attribute:: x

.. class:: KeyButMask

    .. data:: Shift


    .. data:: Lock


    .. data:: Control


    .. data:: Mod1


    .. data:: Mod2


    .. data:: Mod3


    .. data:: Mod4


    .. data:: Mod5


    .. data:: Button1


    .. data:: Button2


    .. data:: Button3


    .. data:: Button4


    .. data:: Button5


.. class:: BadColormap

.. class:: NoExposureEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: drawable

    .. attribute:: major_opcode

    .. attribute:: response_type

.. class:: BadPixmap

.. class:: ColormapState

    .. data:: Uninstalled


    .. data:: Installed


.. class:: ListPropertiesCookie

.. class:: ColorFlag

    .. data:: Red


    .. data:: Green


    .. data:: Blue


.. class:: BadGContext

.. class:: GetGeometryCookie

.. class:: BadDrawable

.. class:: Allow

    .. data:: AsyncPointer


    .. data:: SyncPointer


    .. data:: ReplayPointer


    .. data:: AsyncKeyboard


    .. data:: SyncKeyboard


    .. data:: ReplayKeyboard


    .. data:: AsyncBoth


    .. data:: SyncBoth


.. class:: AllocNamedColorReply

    .. method:: __init__(self, conn)


    .. attribute:: exact_red

    .. attribute:: visual_green

    .. attribute:: exact_green

    .. attribute:: exact_blue

    .. attribute:: visual_red

    .. attribute:: visual_blue

    .. attribute:: pixel

.. class:: GetImageCookie

.. class:: LookupColorCookie

.. class:: EnterNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: event_y

    .. attribute:: time

    .. attribute:: detail

    .. attribute:: same_screen_focus

    .. attribute:: state

    .. attribute:: mode

    .. attribute:: child

    .. attribute:: event_x

    .. attribute:: root_y

    .. attribute:: root_x

    .. attribute:: root

    .. attribute:: event

    .. attribute:: response_type

.. class:: MapRequestEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: window

    .. attribute:: response_type

    .. attribute:: parent

.. class:: QueryPointerCookie

.. class:: ColormapError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: NotifyDetail

    .. data:: Ancestor


    .. data:: Virtual


    .. data:: Inferior


    .. data:: Nonlinear


    .. data:: NonlinearVirtual


    .. data:: Pointer


    .. data:: PointerRoot


    .. data:: _None


.. class:: AccessError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: GrabKeyboardCookie

.. class:: KeyReleaseEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: event_y

    .. attribute:: time

    .. attribute:: detail

    .. attribute:: state

    .. attribute:: response_type

    .. attribute:: child

    .. attribute:: event_x

    .. attribute:: root_y

    .. attribute:: root_x

    .. attribute:: root

    .. attribute:: event

    .. attribute:: same_screen

.. class:: QueryTextExtentsCookie

.. class:: ClipOrdering

    .. data:: Unsorted


    .. data:: YSorted


    .. data:: YXSorted


    .. data:: YXBanded


.. class:: Rectangle

    .. method:: __init__(self, conn)


    .. classmethod:: create(cls, conn, x, y, width, height)


    .. attribute:: y

    .. attribute:: x

    .. attribute:: height

    .. attribute:: width

.. class:: ImageOrder

    .. data:: LSBFirst


    .. data:: MSBFirst


.. class:: ListFontsCookie

.. class:: GetPropertyReply

    .. method:: __init__(self, conn)


    .. method:: exists(self)


    .. method:: typed_value(self)


    .. attribute:: bytes_after

    .. attribute:: value_len

    .. attribute:: type

    .. attribute:: value

    .. attribute:: format

.. class:: LookupColorReply

    .. method:: __init__(self, conn)


    .. attribute:: exact_red

    .. attribute:: visual_green

    .. attribute:: exact_green

    .. attribute:: exact_blue

    .. attribute:: visual_red

    .. attribute:: visual_blue

.. class:: GetImageReply

    .. method:: __init__(self, conn)


    .. attribute:: depth

    .. attribute:: data

    .. attribute:: visual

.. class:: Screen

    .. method:: __init__(self, conn)


    .. method:: get_active_window(self)


    .. method:: rgba_colormap(self)


    .. method:: get_root_visual_type(self)


    .. method:: get_rgba_visual(self)


    .. attribute:: min_installed_maps

    .. attribute:: max_installed_maps

    .. attribute:: default_colormap

    .. attribute:: width_in_pixels

    .. attribute:: backing_stores

    .. attribute:: height_in_pixels

    .. attribute:: white_pixel

    .. attribute:: save_unders

    .. attribute:: width_in_millimeters

    .. attribute:: current_input_masks

    .. attribute:: root_depth

    .. attribute:: black_pixel

    .. attribute:: root_visual

    .. attribute:: height_in_millimeters

    .. attribute:: root

    .. attribute:: allowed_depths

    .. attribute:: allowed_depths_len

.. class:: ReparentNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: override_redirect

    .. attribute:: parent

    .. attribute:: window

    .. attribute:: response_type

    .. attribute:: y

    .. attribute:: x

    .. attribute:: event

.. class:: ClientMessageEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. classmethod:: create(cls, conn, type, window, format, values)


    .. attribute:: data

    .. attribute:: window

    .. attribute:: type

    .. attribute:: response_type

    .. attribute:: format

.. class:: Host

    .. method:: __init__(self, conn)


    .. attribute:: address

    .. attribute:: family

    .. attribute:: address_len

.. class:: Char2b

    .. method:: __init__(self, conn)


    .. attribute:: byte2

    .. attribute:: byte1

.. class:: InternAtomCookie

.. class:: ListFontsWithInfoReply

    .. method:: __init__(self, conn)


    .. attribute:: max_bounds

    .. attribute:: name_len

    .. attribute:: font_ascent

    .. attribute:: name

    .. attribute:: properties_len

    .. attribute:: replies_hint

    .. attribute:: font_descent

    .. attribute:: draw_direction

    .. attribute:: min_char_or_byte2

    .. attribute:: default_char

    .. attribute:: max_char_or_byte2

    .. attribute:: max_byte1

    .. attribute:: min_byte1

    .. attribute:: all_chars_exist

    .. attribute:: properties

    .. attribute:: min_bounds

.. class:: QueryTextExtentsReply

    .. method:: __init__(self, conn)


    .. attribute:: font_descent

    .. attribute:: overall_left

    .. attribute:: overall_right

    .. attribute:: overall_descent

    .. attribute:: overall_ascent

    .. attribute:: draw_direction

    .. attribute:: font_ascent

    .. attribute:: overall_width

.. class:: ButtonReleaseEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: event_y

    .. attribute:: time

    .. attribute:: detail

    .. attribute:: state

    .. attribute:: response_type

    .. attribute:: child

    .. attribute:: event_x

    .. attribute:: root_y

    .. attribute:: root_x

    .. attribute:: root

    .. attribute:: event

    .. attribute:: same_screen

.. class:: MapIndex

    .. data:: Shift


    .. data:: Lock


    .. data:: Control


    .. data:: _1


    .. data:: _2


    .. data:: _3


    .. data:: _4


    .. data:: _5


.. class:: Charinfo

    .. method:: __init__(self, conn)


    .. attribute:: descent

    .. attribute:: right_side_bearing

    .. attribute:: character_width

    .. attribute:: left_side_bearing

    .. attribute:: attributes

    .. attribute:: ascent

.. class:: BadLength

.. class:: xprotoExtension

    .. data:: header


    .. method:: create_window_checked(self, depth, wid, parent, x, y, width, height, border_width, _class, visual, value_mask, value_list)


    .. method:: create_window(self, depth, wid, parent, x, y, width, height, border_width, _class, visual, value_mask, value_list)


    .. method:: intern_atom(self, name, only_if_exists=False)


    .. method:: intern_atom_unchecked(self, name, only_if_exists=False)


    .. method:: ungrab_pointer_checked(self, time=Time.CurrentTime)


    .. method:: ungrab_pointer(self, time=Time.CurrentTime)


    .. method:: change_active_pointer_grab_checked(self, cursor, time, event_mask)


    .. method:: change_active_pointer_grab(self, cursor, time, event_mask)


    .. method:: ungrab_keyboard_checked(self, time=0)


    .. method:: ungrab_keyboard(self, time=0)


    .. method:: allow_events_checked(self, mode, time=0)


    .. method:: allow_events(self, mode, time=0)


    .. method:: grab_server_checked(self)


    .. method:: grab_server(self)


    .. method:: ungrab_server_checked(self)


    .. method:: ungrab_server(self)


    .. method:: warp_pointer_checked(self, src_window, dst_window, src_x, src_y, src_width, src_height, dst_x, dst_y)


    .. method:: warp_pointer(self, src_window, dst_window, src_x, src_y, src_width, src_height, dst_x, dst_y)


    .. method:: get_input_focus(self)


    .. method:: get_input_focus_unchecked(self)


    .. method:: query_keymap(self)


    .. method:: query_keymap_unchecked(self)


    .. method:: open_font_checked(self, fid, name)


    .. method:: open_font(self, fid, name)


    .. method:: list_fonts(self, max_names, pattern)


    .. method:: list_fonts_unchecked(self, max_names, pattern)


    .. method:: list_fonts_with_info(self, max_names, pattern)


    .. method:: list_fonts_with_info_unchecked(self, max_names, pattern)


    .. method:: set_font_path_checked(self, path)


    .. method:: set_font_path(self, path)


    .. method:: get_font_path(self)


    .. method:: get_font_path_unchecked(self)


    .. method:: create_pixmap_checked(self, depth, pid, drawable, width, height)


    .. method:: create_pixmap(self, depth, pid, drawable, width, height)


    .. method:: create_g_c_checked(self, cid, drawable, value_mask, value_list)


    .. method:: create_g_c(self, cid, drawable, value_mask, value_list)


    .. method:: create_colormap_checked(self, alloc, mid, window, visual)


    .. method:: create_colormap(self, alloc, mid, window, visual)


    .. method:: create_cursor_checked(self, cid, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y)


    .. method:: create_cursor(self, cid, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y)


    .. method:: create_glyph_cursor_checked(self, cid, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue)


    .. method:: create_glyph_cursor(self, cid, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue)


    .. method:: query_extension(self, name)


    .. method:: query_extension_unchecked(self, name)


    .. method:: list_extensions(self)


    .. method:: list_extensions_unchecked(self)


    .. method:: change_keyboard_mapping_checked(self, keycode_count, first_keycode, keysyms_per_keycode, keysyms)


    .. method:: change_keyboard_mapping(self, keycode_count, first_keycode, keysyms_per_keycode, keysyms)


    .. method:: get_keyboard_mapping(self, first_keycode, count)


    .. method:: get_keyboard_mapping_unchecked(self, first_keycode, count)


    .. method:: change_keyboard_control_checked(self, **values)


    .. method:: change_keyboard_control(self, **values)


    .. method:: get_keyboard_control(self)


    .. method:: get_keyboard_control_unchecked(self)


    .. method:: bell_checked(self, percent=0)


    .. method:: bell(self, percent=0)


    .. method:: change_pointer_control_checked(self, acceleration_numerator, acceleration_denominator, threshold, do_acceleration, do_threshold)


    .. method:: change_pointer_control(self, acceleration_numerator, acceleration_denominator, threshold, do_acceleration, do_threshold)


    .. method:: get_pointer_control(self)


    .. method:: get_pointer_control_unchecked(self)


    .. method:: set_screen_saver_checked(self, timeout, interval, prefer_blanking, allow_exposures)


    .. method:: set_screen_saver(self, timeout, interval, prefer_blanking, allow_exposures)


    .. method:: get_screen_saver(self)


    .. method:: get_screen_saver_unchecked(self)


    .. method:: change_hosts_checked(self, mode, family, address)


    .. method:: change_hosts(self, mode, family, address)


    .. method:: list_hosts(self)


    .. method:: list_hosts_unchecked(self)


    .. method:: set_access_control_checked(self, mode)


    .. method:: set_access_control(self, mode)


    .. method:: set_close_down_mode_checked(self, mode)


    .. method:: set_close_down_mode(self, mode)


    .. method:: kill_client_checked(self, resource)


    .. method:: kill_client(self, resource)


    .. method:: force_screen_saver_checked(self, mode)


    .. method:: force_screen_saver(self, mode)


    .. method:: set_pointer_mapping(self, map)


    .. method:: set_pointer_mapping_unchecked(self, map)


    .. method:: get_pointer_mapping(self)


    .. method:: get_pointer_mapping_unchecked(self)


    .. method:: set_modifier_mapping(self, keycodes_per_modifier, keycodes)


    .. method:: set_modifier_mapping_unchecked(self, keycodes_per_modifier, keycodes)


    .. method:: get_modifier_mapping(self)


    .. method:: get_modifier_mapping_unchecked(self)


    .. method:: no_operation_checked(self)


    .. method:: no_operation(self)


    .. method:: list_all_fonts_with_info(self, max_names, pattern)


.. class:: ButtonPressEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: event_y

    .. attribute:: time

    .. attribute:: detail

    .. attribute:: state

    .. attribute:: response_type

    .. attribute:: child

    .. attribute:: event_x

    .. attribute:: root_y

    .. attribute:: root_x

    .. attribute:: root

    .. attribute:: event

    .. attribute:: same_screen

.. class:: GetKeyboardControlReply

    .. method:: __init__(self, conn)


    .. attribute:: auto_repeats

    .. attribute:: bell_pitch

    .. attribute:: global_auto_repeat

    .. attribute:: bell_percent

    .. attribute:: key_click_percent

    .. attribute:: led_mask

    .. attribute:: bell_duration

.. class:: GetPointerControlCookie

.. class:: GetPropertyCookie

.. class:: JoinStyle

    .. data:: Miter


    .. data:: Round


    .. data:: Bevel


.. class:: Gravity

    .. data:: BitForget


    .. data:: WinUnmap


    .. data:: NorthWest


    .. data:: North


    .. data:: NorthEast


    .. data:: West


    .. data:: Center


    .. data:: East


    .. data:: SouthWest


    .. data:: South


    .. data:: SouthEast


    .. data:: Static


.. class:: GetAtomNameCookie

.. class:: Str

    .. method:: __init__(self, conn)


    .. method:: __str__(self)


    .. method:: __repr__(self)


    .. method:: pythonize_lazy(self)


    .. classmethod:: create_lazy(cls, conn, string)


    .. attribute:: name_len

    .. attribute:: name

.. class:: Time

    .. data:: CurrentTime


.. class:: AllocColorPlanesReply

    .. method:: __init__(self, conn)


    .. attribute:: red_mask

    .. attribute:: pixels_len

    .. attribute:: blue_mask

    .. attribute:: green_mask

    .. attribute:: pixels

.. class:: CirculateNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: window

    .. attribute:: place

    .. attribute:: event

    .. attribute:: response_type

.. class:: CW

    .. data:: BackPixmap


    .. data:: BackPixel


    .. data:: BorderPixmap


    .. data:: BorderPixel


    .. data:: BitGravity


    .. data:: WinGravity


    .. data:: BackingStore


    .. data:: BackingPlanes


    .. data:: BackingPixel


    .. data:: OverrideRedirect


    .. data:: SaveUnder


    .. data:: EventMask


    .. data:: DontPropagate


    .. data:: Colormap


    .. data:: Cursor


.. class:: QueryExtensionCookie

.. class:: GetWindowAttributesCookie

.. class:: KB

    .. data:: KeyClickPercent


    .. data:: BellPercent


    .. data:: BellPitch


    .. data:: BellDuration


    .. data:: Led


    .. data:: LedMode


    .. data:: Key


    .. data:: AutoRepeatMode


.. class:: GetMotionEventsReply

    .. method:: __init__(self, conn)


    .. attribute:: events_len

    .. attribute:: events

.. class:: ListFontsReply

    .. method:: __init__(self, conn)


    .. attribute:: names_len

    .. attribute:: names

.. class:: Family

    .. data:: Internet


    .. data:: DECnet


    .. data:: Chaos


    .. data:: ServerInterpreted


    .. data:: Internet6


.. class:: EventMask

    .. data:: NoEvent


    .. data:: KeyPress


    .. data:: KeyRelease


    .. data:: ButtonPress


    .. data:: ButtonRelease


    .. data:: EnterWindow


    .. data:: LeaveWindow


    .. data:: PointerMotion


    .. data:: PointerMotionHint


    .. data:: Button1Motion


    .. data:: Button2Motion


    .. data:: Button3Motion


    .. data:: Button4Motion


    .. data:: Button5Motion


    .. data:: ButtonMotion


    .. data:: KeymapState


    .. data:: Exposure


    .. data:: VisibilityChange


    .. data:: StructureNotify


    .. data:: ResizeRedirect


    .. data:: SubstructureNotify


    .. data:: SubstructureRedirect


    .. data:: FocusChange


    .. data:: PropertyChange


    .. data:: ColorMapChange


    .. data:: OwnerGrabButton


.. class:: InternAtomReply

    .. method:: __init__(self, conn)


    .. attribute:: atom

.. class:: KeyPressEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: event_y

    .. attribute:: time

    .. attribute:: detail

    .. attribute:: state

    .. attribute:: response_type

    .. attribute:: child

    .. attribute:: event_x

    .. attribute:: root_y

    .. attribute:: root_x

    .. attribute:: root

    .. attribute:: event

    .. attribute:: same_screen

.. class:: GetPointerControlReply

    .. method:: __init__(self, conn)


    .. attribute:: threshold

    .. attribute:: acceleration_denominator

    .. attribute:: acceleration_numerator

.. class:: GetFontPathCookie

.. class:: LeaveNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: event_y

    .. attribute:: time

    .. attribute:: detail

    .. attribute:: same_screen_focus

    .. attribute:: state

    .. attribute:: mode

    .. attribute:: child

    .. attribute:: event_x

    .. attribute:: root_y

    .. attribute:: root_x

    .. attribute:: root

    .. attribute:: event

    .. attribute:: response_type

.. class:: QueryColorsCookie

.. class:: AtomError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: ListHostsCookie

.. class:: GetMotionEventsCookie

.. class:: Pixmap

    .. method:: __init__(self, conn, xid)


    .. method:: free_checked(self)


    .. method:: free(self)


    .. classmethod:: create(cls, conn, drawable, width, height, depth)


.. class:: MapNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: window

    .. attribute:: response_type

    .. attribute:: event

    .. attribute:: override_redirect

.. class:: GetAtomNameReply

    .. method:: __init__(self, conn)


    .. attribute:: name_len

    .. attribute:: name

.. class:: Fontprop

    .. method:: __init__(self, conn)


    .. attribute:: name

    .. attribute:: value

.. class:: Window

    .. method:: __init__(self, conn, xid)


    .. method:: change_attributes_checked(self, **values)


    .. method:: change_attributes(self, **values)


    .. method:: get_attributes(self)


    .. method:: get_attributes_unchecked(self)


    .. method:: destroy_checked(self)


    .. method:: destroy(self)


    .. method:: destroy_subwindows_checked(self)


    .. method:: destroy_subwindows(self)


    .. method:: change_save_set_checked(self, mode)


    .. method:: change_save_set(self, mode)


    .. method:: reparent_checked(self, parent, x=0, y=0)


    .. method:: reparent(self, parent, x=0, y=0)


    .. method:: map_checked(self)


    .. method:: map(self)


    .. method:: map_subwindows_checked(self)


    .. method:: map_subwindows(self)


    .. method:: unmap_checked(self)


    .. method:: unmap(self)


    .. method:: unmap_subwindows_checked(self)


    .. method:: unmap_subwindows(self)


    .. method:: configure_checked(self, **values)


    .. method:: configure(self, **values)


    .. method:: circulate_window_checked(self, direction)


    .. method:: circulate_window(self, direction)


    .. method:: query_tree(self)


    .. method:: query_tree_unchecked(self)


    .. method:: change_property_checked(self, property, type, format, data, mode=PropMode.Replace)


    .. method:: change_property(self, property, type, format, data, mode=PropMode.Replace)


    .. method:: delete_property_checked(self, property)


    .. method:: delete_property(self, property)


    .. method:: get_property(self, property, type, delete=False, long_offset=0, long_length=2**32-1)


    .. method:: get_property_unchecked(self, property, type, delete=False, long_offset=0, long_length=2**32-1)


    .. method:: list_properties(self)


    .. method:: list_properties_unchecked(self)


    .. method:: send_event_checked(self, event_mask, event, propagate=False)


    .. method:: send_event(self, event_mask, event, propagate=False)


    .. method:: grab_pointer(self, event_mask, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async, confine_to=None, cursor=None, time=Time.CurrentTime)


    .. method:: grab_pointer_unchecked(self, event_mask, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async, confine_to=None, cursor=None, time=Time.CurrentTime)


    .. method:: grab_button_checked(self, event_mask, button, modifiers, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async, confine_to=None, cursor=None)


    .. method:: grab_button(self, event_mask, button, modifiers, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async, confine_to=None, cursor=None)


    .. method:: ungrab_button_checked(self, button, modifiers)


    .. method:: ungrab_button(self, button, modifiers)


    .. method:: grab_keyboard(self, owner_events=True, time=Time.CurrentTime, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async)


    .. method:: grab_keyboard_unchecked(self, owner_events=True, time=Time.CurrentTime, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async)


    .. method:: grab_key_checked(self, key, modifiers, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async)


    .. method:: grab_key(self, key, modifiers, owner_events=True, pointer_mode=GrabMode.Async, keyboard_mode=GrabMode.Async)


    .. method:: ungrab_key_checked(self, key, modifiers)


    .. method:: ungrab_key(self, key, modifiers)


    .. method:: query_pointer(self)


    .. method:: query_pointer_unchecked(self)


    .. method:: get_motion_events(self, start, stop)


    .. method:: get_motion_events_unchecked(self, start, stop)


    .. method:: translate_coordinates(self, dst_window, src_x, src_y)


    .. method:: translate_coordinates_unchecked(self, dst_window, src_x, src_y)


    .. method:: set_input_focus_checked(self, revert_to=InputFocus.PointerRoot, time=Time.CurrentTime)


    .. method:: set_input_focus(self, revert_to=InputFocus.PointerRoot, time=Time.CurrentTime)


    .. method:: clear_area_checked(self, x, y, width, height, exposures=False)


    .. method:: clear_area(self, x, y, width, height, exposures=False)


    .. method:: list_installed_colormaps(self)


    .. method:: list_installed_colormaps_unchecked(self)


    .. method:: rotate_properties_checked(self, atoms, delta)


    .. method:: rotate_properties(self, atoms, delta)


    .. classmethod:: create(cls, conn, parent, depth, visual, x=0, y=0, width=640, height=480, border_width=0, _class=WindowClass.InputOutput, **values)


    .. classmethod:: create_toplevel_on_screen(cls, conn, screen, *args, **kwargs)


    .. method:: add_to_save_set(self)


    .. method:: remove_from_save_set(self)


.. class:: CoordMode

    .. data:: Origin


    .. data:: Previous


.. class:: ImageFormat

    .. data:: XYBitmap


    .. data:: XYPixmap


    .. data:: ZPixmap


.. class:: GrabStatus

    .. data:: Success


    .. data:: AlreadyGrabbed


    .. data:: InvalidTime


    .. data:: NotViewable


    .. data:: Frozen


.. class:: Timecoord

    .. method:: __init__(self, conn)


    .. attribute:: y

    .. attribute:: x

    .. attribute:: time

.. class:: LineStyle

    .. data:: Solid


    .. data:: OnOffDash


    .. data:: DoubleDash


.. class:: QueryBestSizeReply

    .. method:: __init__(self, conn)


    .. attribute:: width

    .. attribute:: height

.. class:: InputFocus

    .. data:: _None


    .. data:: PointerRoot


    .. data:: Parent


.. class:: VisibilityNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: window

    .. attribute:: state

    .. attribute:: response_type

.. class:: FocusOutEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: mode

    .. attribute:: response_type

    .. attribute:: detail

    .. attribute:: event

.. class:: SendEventDest

    .. data:: PointerWindow


    .. data:: ItemFocus


.. class:: Format

    .. method:: __init__(self, conn)


    .. attribute:: depth

    .. attribute:: scanline_pad

    .. attribute:: bits_per_pixel

.. class:: ColormapNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: new

    .. attribute:: window

    .. attribute:: response_type

    .. attribute:: colormap

    .. attribute:: state

.. class:: CirculateRequestEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: window

    .. attribute:: place

    .. attribute:: event

    .. attribute:: response_type

.. class:: QueryFontReply

    .. method:: __init__(self, conn)


    .. attribute:: max_bounds

    .. attribute:: all_chars_exist

    .. attribute:: font_ascent

    .. attribute:: char_infos_len

    .. attribute:: properties_len

    .. attribute:: font_descent

    .. attribute:: draw_direction

    .. attribute:: min_char_or_byte2

    .. attribute:: default_char

    .. attribute:: max_char_or_byte2

    .. attribute:: char_infos

    .. attribute:: max_byte1

    .. attribute:: min_byte1

    .. attribute:: properties

    .. attribute:: min_bounds

.. class:: CreateNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: override_redirect

    .. attribute:: parent

    .. attribute:: height

    .. attribute:: width

    .. attribute:: window

    .. attribute:: response_type

    .. attribute:: y

    .. attribute:: x

    .. attribute:: border_width

.. class:: Mapping

    .. data:: Modifier


    .. data:: Keyboard


    .. data:: Pointer


.. class:: ResizeRequestEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: width

    .. attribute:: window

    .. attribute:: response_type

    .. attribute:: height

.. class:: QueryColorsReply

    .. method:: __init__(self, conn)


    .. attribute:: colors_len

    .. attribute:: colors

.. class:: MotionNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: event_y

    .. attribute:: time

    .. attribute:: detail

    .. attribute:: state

    .. attribute:: response_type

    .. attribute:: child

    .. attribute:: event_x

    .. attribute:: root_y

    .. attribute:: root_x

    .. attribute:: root

    .. attribute:: event

    .. attribute:: same_screen

.. class:: Atom

    .. method:: __init__(self, conn, xid)


    .. method:: get_name(self)


    .. method:: get_name_unchecked(self)


    .. method:: set_selection_owner_checked(self, owner=None, time=0)


    .. method:: set_selection_owner(self, owner=None, time=0)


    .. method:: get_selection_owner(self)


    .. method:: get_selection_owner_unchecked(self)


    .. method:: convert_selection_checked(self, requestor, target, property=None, time=0)


    .. method:: convert_selection(self, requestor, target, property=None, time=0)


    .. method:: __repr__(self)


    .. method:: name(self)


    .. method:: _cache_name(self, name)


    .. method:: has_cached_name(self)


.. class:: ScreenSaver

    .. data:: Reset


    .. data:: Active


.. class:: CloseDown

    .. data:: DestroyAll


    .. data:: RetainPermanent


    .. data:: RetainTemporary


.. class:: SetPointerMappingReply

    .. method:: __init__(self, conn)


    .. attribute:: status

.. class:: Segment

    .. method:: __init__(self, conn)


    .. attribute:: y1

    .. attribute:: x2

    .. attribute:: x1

    .. attribute:: y2

.. class:: ValueError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: GetInputFocusReply

    .. method:: __init__(self, conn)


    .. attribute:: revert_to

    .. attribute:: focus

.. class:: MappingNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: first_keycode

    .. attribute:: count

    .. attribute:: request

    .. attribute:: response_type

.. class:: GetGeometryReply

    .. method:: __init__(self, conn)


    .. attribute:: height

    .. attribute:: width

    .. attribute:: depth

    .. attribute:: y

    .. attribute:: x

    .. attribute:: border_width

    .. attribute:: root

.. class:: SelectionRequestEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: selection

    .. attribute:: target

    .. attribute:: requestor

    .. attribute:: response_type

    .. attribute:: time

    .. attribute:: owner

    .. attribute:: property

.. class:: BadWindow

.. class:: MapState

    .. data:: Unmapped


    .. data:: Unviewable


    .. data:: Viewable


.. class:: Depth

    .. method:: __init__(self, conn)


    .. attribute:: visuals

    .. attribute:: depth

    .. attribute:: visuals_len

.. class:: ListExtensionsCookie

.. class:: ButtonMask

    .. data:: _1


    .. data:: _2


    .. data:: _3


    .. data:: _4


    .. data:: _5


    .. data:: Any


.. class:: CursorError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: Drawable

    .. method:: __init__(self, conn, xid)


    .. method:: get_geometry(self)


    .. method:: get_geometry_unchecked(self)


    .. method:: get_image(self, format, x, y, width, height, plane_mask)


    .. method:: get_image_unchecked(self, format, x, y, width, height, plane_mask)


    .. method:: query_best_size(self, _class, width, height)


    .. method:: query_best_size_unchecked(self, _class, width, height)


.. class:: FocusInEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: mode

    .. attribute:: response_type

    .. attribute:: detail

    .. attribute:: event

.. class:: GContext

    .. method:: __init__(self, conn, xid)


    .. method:: change_checked(self, **values)


    .. method:: change(self, **values)


    .. method:: copy_checked(self, values=())


    .. method:: copy(self, values=())


    .. method:: set_dashes_checked(self, dash_offset, dashes)


    .. method:: set_dashes(self, dash_offset, dashes)


    .. method:: set_clip_rectangles_checked(self, clip_x_origin, clip_y_origin, ordering, rectangles)


    .. method:: set_clip_rectangles(self, clip_x_origin, clip_y_origin, ordering, rectangles)


    .. method:: free_checked(self)


    .. method:: free(self)


    .. method:: copy_area_checked(self, src_drawable, dst_drawable, src_x, src_y, dst_x, dst_y, width, height)


    .. method:: copy_area(self, src_drawable, dst_drawable, src_x, src_y, dst_x, dst_y, width, height)


    .. method:: copy_plane_checked(self, src_drawable, dst_drawable, src_x, src_y, dst_x, dst_y, width, height, bit_plane)


    .. method:: copy_plane(self, src_drawable, dst_drawable, src_x, src_y, dst_x, dst_y, width, height, bit_plane)


    .. method:: poly_point_checked(self, drawable, points, coordinate_mode=0)


    .. method:: poly_point(self, drawable, points, coordinate_mode=0)


    .. method:: poly_line_checked(self, drawable, points, coordinate_mode=0)


    .. method:: poly_line(self, drawable, points, coordinate_mode=0)


    .. method:: poly_segment_checked(self, drawable, segments)


    .. method:: poly_segment(self, drawable, segments)


    .. method:: poly_rectangle_checked(self, drawable, rectangles)


    .. method:: poly_rectangle(self, drawable, rectangles)


    .. method:: poly_arc_checked(self, drawable, arcs)


    .. method:: poly_arc(self, drawable, arcs)


    .. method:: fill_poly_checked(self, drawable, points, shape=0, coordinate_mode=0)


    .. method:: fill_poly(self, drawable, points, shape=0, coordinate_mode=0)


    .. method:: poly_fill_rectangle_checked(self, drawable, rectangles)


    .. method:: poly_fill_rectangle(self, drawable, rectangles)


    .. method:: poly_fill_arc_checked(self, drawable, arcs)


    .. method:: poly_fill_arc(self, drawable, arcs)


    .. method:: put_image_checked(self, drawable, format, width, height, dst_x, dst_y, depth, left_pad, data)


    .. method:: put_image(self, drawable, format, width, height, dst_x, dst_y, depth, left_pad, data)


    .. method:: poly_text8_checked(self, drawable, x, y, string)


    .. method:: poly_text8(self, drawable, x, y, string)


    .. method:: poly_text16_checked(self, drawable, x, y, string)


    .. method:: poly_text16(self, drawable, x, y, string)


    .. method:: image_text8_checked(self, drawable, x, y, string)


    .. method:: image_text8(self, drawable, x, y, string)


    .. method:: image_text16_checked(self, drawable, x, y, string)


    .. method:: image_text16(self, drawable, x, y, string)


    .. classmethod:: create(cls, conn, drawable, **values)


.. class:: PixmapError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: BadAlloc

.. class:: QueryPointerReply

    .. method:: __init__(self, conn)


    .. attribute:: mask

    .. attribute:: same_screen

    .. attribute:: child

    .. attribute:: root_y

    .. attribute:: root_x

    .. attribute:: root

    .. attribute:: win_x

    .. attribute:: win_y

.. class:: SelectionNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: selection

    .. attribute:: target

    .. attribute:: requestor

    .. attribute:: response_type

    .. attribute:: time

    .. attribute:: property

.. class:: PolyShape

    .. data:: Complex


    .. data:: Nonconvex


    .. data:: Convex


.. class:: SetModifierMappingCookie

.. class:: GetPointerMappingCookie

.. class:: GetSelectionOwnerReply

    .. method:: __init__(self, conn)


    .. attribute:: owner

.. class:: WindowError

    .. method:: __init__(self, conn)


    .. attribute:: minor_opcode

    .. attribute:: major_opcode

    .. attribute:: bad_value

.. class:: SetMode

    .. data:: Insert


    .. data:: Delete


.. class:: NotifyMode

    .. data:: Normal


    .. data:: Grab


    .. data:: Ungrab


    .. data:: WhileGrabbed


.. class:: PropertyNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: window

    .. attribute:: time

    .. attribute:: response_type

    .. attribute:: state

    .. attribute:: atom

.. class:: GetFontPathReply

    .. method:: __init__(self, conn)


    .. attribute:: path

    .. attribute:: path_len

.. class:: GetKeyboardMappingReply

    .. method:: __init__(self, conn)


    .. attribute:: keysyms_per_keycode

    .. attribute:: keysyms

