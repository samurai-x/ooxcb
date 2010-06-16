How to ...
==========

... get the title of the current window
---------------------------------------

There are several properties that can contain the title
of the current window. First, there is `_NET_WM_VISIBLE_NAME` (UTF-8 encoded).
If that property does not exist, there is `_NET_WM_NAME` (UTF-8).
If that property does not exist, there is `WM_NAME` (latin-1).
If that property does not exist, there is no title set.

For your convenience, there is the
:meth:`ewmh_get_window_title <ooxcb.contrib.ewmh.ewmh_get_window_title>` method
in the :mod:`ooxcb.contrib.ewmh` mixin module (see :ref:`mixins`).

... integrate it with your favourite gui toolkit
------------------------------------------------

pygtk
~~~~~

That's the minimal skeleton to integrate ooxcb into the gobject mainloop::

    import sys
    sys.path.append('..')

    import ooxcb
    from ooxcb import xproto

    import gtk
    import gobject

    def ooxcb_callback(source, cb_condition, connection):
        while connection.alive: # `if connection.conn:` for ooxcb 1.0
                break
            evt = connection.poll_for_event()
            if evt is None:
                break
            evt.dispatch()
        # return True so that the callback will be called again.
        return True

    conn = ooxcb.connect()
    # That's the important line. It makes gobject call `ooxcb_callback`
    # when data is available.
    gobject.io_add_watch(
            conn.get_file_descriptor(),
            gobject.IO_IN,
            ooxcb_callback,
            conn)

    gtk.main()


