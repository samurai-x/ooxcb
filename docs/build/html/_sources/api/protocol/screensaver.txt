ooxcb.protocol.screensaver
==========================

.. module:: ooxcb.protocol.screensaver

.. class:: Kind

    .. data:: Blanked


    .. data:: Internal


    .. data:: External


.. class:: WindowMixin

    .. data:: target_class


.. class:: QueryVersionReply

    .. method:: __init__(self, conn)


    .. attribute:: server_minor_version

    .. attribute:: server_major_version

.. class:: screensaverExtension

    .. data:: header


    .. method:: query_version(self, client_major_version, client_minor_version)


    .. method:: query_version_unchecked(self, client_major_version, client_minor_version)


    .. method:: suspend_checked(self, suspend)


    .. method:: suspend(self, suspend)


.. class:: DrawableMixin

    .. data:: target_class


    .. method:: query_info(self)


    .. method:: query_info_unchecked(self)


    .. method:: select_input_checked(self, event_mask)


    .. method:: select_input(self, event_mask)


    .. method:: set_attributes_checked(self, x, y, width, height, border_width, _class, depth, visual, value_mask, value_list)


    .. method:: set_attributes(self, x, y, width, height, border_width, _class, depth, visual, value_mask, value_list)


    .. method:: unset_attributes_checked(self)


    .. method:: unset_attributes(self)


.. class:: NotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: forced

    .. attribute:: kind

    .. attribute:: code

    .. attribute:: window

    .. attribute:: state

    .. attribute:: response_type

    .. attribute:: time

    .. attribute:: root

    .. attribute:: sequence_number

.. class:: QueryVersionCookie

.. class:: State

    .. data:: Off


    .. data:: On


    .. data:: Cycle


    .. data:: Disabled


.. class:: QueryInfoCookie

.. class:: QueryInfoReply

    .. method:: __init__(self, conn)


    .. attribute:: saver_window

    .. attribute:: ms_since_user_input

    .. attribute:: event_mask

    .. attribute:: ms_until_server

    .. attribute:: kind

    .. attribute:: state

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


.. class:: Event

    .. data:: NotifyMask


    .. data:: CycleMask


