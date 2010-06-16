ooxcb.protocol.composite
========================

.. module:: ooxcb.protocol.composite

.. class:: Redirect

    .. data:: Automatic


    .. data:: Manual


.. class:: GetOverlayWindowReply

    .. method:: __init__(self, conn)


    .. attribute:: overlay_win

.. class:: WindowMixin

    .. data:: target_class


    .. method:: redirect_checked(self, update=Redirect.Automatic)


    .. method:: redirect(self, update=Redirect.Automatic)


    .. method:: redirect_subwindows_checked(self, update=Redirect.Automatic)


    .. method:: redirect_subwindows(self, update=Redirect.Automatic)


    .. method:: unredirect_checked(self, update=Redirect.Automatic)


    .. method:: unredirect(self, update=Redirect.Automatic)


    .. method:: unredirect_subwindows_checked(self, update=Redirect.Automatic)


    .. method:: unredirect_subwindows(self, update=Redirect.Automatic)


    .. method:: name_pixmap_checked(self, pixmap)


    .. method:: name_pixmap(self, pixmap)


    .. method:: get_overlay_window(self)


    .. method:: get_overlay_window_unchecked(self)


    .. method:: release_overlay_window_checked(self)


    .. method:: release_overlay_window(self)


.. class:: QueryVersionReply

    .. method:: __init__(self, conn)


    .. attribute:: major_version

    .. attribute:: minor_version

.. class:: QueryVersionCookie

.. class:: GetOverlayWindowCookie

.. class:: RegionMixin

    .. data:: target_class


    .. classmethod:: create_from_border_clip(cls, conn, window)


.. class:: compositeExtension

    .. data:: header


    .. method:: query_version(self, client_major_version, client_minor_version)


    .. method:: query_version_unchecked(self, client_major_version, client_minor_version)


    .. method:: create_region_from_border_clip_checked(self, region, window)


    .. method:: create_region_from_border_clip(self, region, window)


