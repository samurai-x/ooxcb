ooxcb.protocol.xfixes
=====================

.. module:: ooxcb.protocol.xfixes

.. class:: BadRegion

.. class:: SelectionEventMask

    .. data:: SetSelectionOwner


    .. data:: SelectionWindowDestroy


    .. data:: SelectionClientClose


.. class:: SaveSetMode

    .. data:: Insert


    .. data:: Delete


.. class:: CursorNotify

    .. data:: DisplayCursor


.. class:: CursorNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: cursor_serial

    .. attribute:: name

    .. attribute:: timestamp

    .. attribute:: subtype

    .. attribute:: window

    .. attribute:: response_type

.. class:: WindowMixin

    .. data:: target_class


    .. method:: change_save_set_checked(self, mode, target, map)


    .. method:: change_save_set(self, mode, target, map)


    .. method:: select_selection_input_checked(self, selection, event_mask)


    .. method:: select_selection_input(self, selection, event_mask)


    .. method:: select_cursor_input_checked(self, event_mask)


    .. method:: select_cursor_input(self, event_mask)


    .. method:: set_shape_region_checked(self, dest_kind, x_offset, y_offset, region)


    .. method:: set_shape_region(self, dest_kind, x_offset, y_offset, region)


    .. method:: hide_cursor_checked(self)


    .. method:: hide_cursor(self)


    .. method:: show_cursor_checked(self)


    .. method:: show_cursor(self)


.. class:: FetchRegionCookie

.. class:: FetchRegionReply

    .. method:: __init__(self, conn)


    .. attribute:: rectangles

    .. attribute:: extents

.. class:: RegionError

    .. method:: __init__(self, conn)


.. class:: SelectionEvent

    .. data:: SetSelectionOwner


    .. data:: SelectionWindowDestroy


    .. data:: SelectionClientClose


.. class:: xfixesExtension

    .. data:: header


    .. method:: query_version(self, client_major_version, client_minor_version)


    .. method:: query_version_unchecked(self, client_major_version, client_minor_version)


    .. method:: get_cursor_image(self)


    .. method:: get_cursor_image_unchecked(self)


    .. method:: create_region_checked(self, region, rectangles)


    .. method:: create_region(self, region, rectangles)


    .. method:: create_region_from_bitmap_checked(self, region, bitmap)


    .. method:: create_region_from_bitmap(self, region, bitmap)


    .. method:: create_region_from_window_checked(self, region, window, kind)


    .. method:: create_region_from_window(self, region, window, kind)


    .. method:: create_region_from_g_c_checked(self, region, gc)


    .. method:: create_region_from_g_c(self, region, gc)


    .. method:: create_region_from_picture_checked(self, region, picture)


    .. method:: create_region_from_picture(self, region, picture)


    .. method:: get_cursor_name(self, cursor)


    .. method:: get_cursor_name_unchecked(self, cursor)


    .. method:: get_cursor_image_and_name(self)


    .. method:: get_cursor_image_and_name_unchecked(self)


.. class:: GetCursorNameReply

    .. method:: __init__(self, conn)


    .. attribute:: nbytes

    .. attribute:: name

    .. attribute:: atom

.. class:: QueryVersionCookie

.. class:: Region

    .. method:: __init__(self, conn, xid)


    .. method:: destroy_checked(self)


    .. method:: destroy(self)


    .. method:: set_checked(self, rectangles)


    .. method:: set(self, rectangles)


    .. method:: copy_checked(self, destination)


    .. method:: copy(self, destination)


    .. method:: union_checked(self, source2, destination)


    .. method:: union(self, source2, destination)


    .. method:: intersect_checked(self, source2, destination)


    .. method:: intersect(self, source2, destination)


    .. method:: subtract_checked(self, source2, destination)


    .. method:: subtract(self, source2, destination)


    .. method:: invert_checked(self, bounds, destination)


    .. method:: invert(self, bounds, destination)


    .. method:: translate_checked(self, dx, dy)


    .. method:: translate(self, dx, dy)


    .. method:: extents_checked(self, destination)


    .. method:: extents(self, destination)


    .. method:: fetch(self)


    .. method:: fetch_unchecked(self)


    .. method:: expand_checked(self, destination, left, right, top, bottom)


    .. method:: expand(self, destination, left, right, top, bottom)


    .. classmethod:: create(cls, conn, rectangles)


    .. classmethod:: create_from_bitmap(cls, conn, bitmap)


    .. classmethod:: create_from_window(cls, conn, window, kind)


    .. classmethod:: create_from_gc(cls, conn, gc)


    .. classmethod:: create_from_picture(cls, conn, picture)


.. class:: SaveSetMapping

    .. data:: Map


    .. data:: Unmap


.. class:: PictureMixin

    .. data:: target_class


    .. method:: set_clip_region_checked(self, region, x_origin, y_origin)


    .. method:: set_clip_region(self, region, x_origin, y_origin)


.. class:: GetCursorImageReply

    .. method:: __init__(self, conn)


    .. attribute:: yhot

    .. attribute:: cursor_serial

    .. attribute:: cursor_image

    .. attribute:: height

    .. attribute:: width

    .. attribute:: y

    .. attribute:: x

    .. attribute:: xhot

.. class:: SaveSetTarget

    .. data:: Nearest


    .. data:: Root


.. class:: GContextMixin

    .. data:: target_class


    .. method:: set_clip_region_checked(self, region, x_origin, y_origin)


    .. method:: set_clip_region(self, region, x_origin, y_origin)


.. class:: QueryVersionReply

    .. method:: __init__(self, conn)


    .. attribute:: major_version

    .. attribute:: minor_version

.. class:: SelectionNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: selection

    .. attribute:: timestamp

    .. attribute:: subtype

    .. attribute:: window

    .. attribute:: selection_timestamp

    .. attribute:: response_type

    .. attribute:: owner

.. class:: GetCursorImageAndNameReply

    .. method:: __init__(self, conn)


    .. attribute:: cursor_atom

    .. attribute:: yhot

    .. attribute:: cursor_serial

    .. attribute:: name

    .. attribute:: cursor_image

    .. attribute:: height

    .. attribute:: width

    .. attribute:: nbytes

    .. attribute:: y

    .. attribute:: x

    .. attribute:: xhot

.. class:: GetCursorImageCookie

.. class:: GetCursorNameCookie

.. class:: GetCursorImageAndNameCookie

.. class:: CursorNotifyMask

    .. data:: DisplayCursor


.. class:: CursorMixin

    .. data:: target_class


    .. method:: set_name_checked(self, name)


    .. method:: set_name(self, name)


    .. method:: change_checked(self, destination)


    .. method:: change(self, destination)


    .. method:: change_by_name_checked(self, name)


    .. method:: change_by_name(self, name)


