Getting Started
===============

The following tries to be something like a tutorial for ooxcb programming.
It requires a bit of knowledge of the X concept, but I tried to keep it
simple. Please contact us if you have any suggestions.

You can find the final version of this application in your source distribution
in `examples/gettingstarted.py` or online
`here <http://samurai-x.org/browser/ooxcb/examples/gettingstarted.py>`_.
Please don't forget the api documentation!

So, let's start:
If you want to use ooxcb in your application, you first have to import it.
You also need to import a module that provides with a core protocol
implementation. That's most likely the :mod:`ooxcb.protocol.xproto` module:

::

    import sys

    import ooxcb
    from ooxcb.protocol import xproto

The second import registers the xproto module as core module, so that import
is necessary.

Then, you will want to establish a connection to the X server. That is done
using the :func:`ooxcb.connect` method:

::

    conn = ooxcb.connect()

That connects to the default X display, specified by the `DISPLAY` environment
variable. You could also connect to another display:

::

    conn = ooxcb.connect(':1')

See the api documentation on :func:`ooxcb.connect` for more details.

At the end of the script, we do disconnect cleanly:

::

    conn.disconnect()

That's not really required, but recommended.

So, after you have established a connection, you will most likely want to get
some information about the available screens. You can get the connection setup
information by accessing the `setup` property of the connection:

::

    setup = conn.setup
    # That's equivalent to
    setup = conn.get_setup()

There's exactly no difference between the two calls, the setup information are
cached in any case. You can see all attributes of the setup here:
:class:`ooxcb.Setup` (not really documented, however).

You can access the screens (there is often only one) by the attribute `roots`.
And there is a `pref_screen` attribute on the connection that is the preferred
screen index:

::

    screen = conn.setup.roots[conn.pref_screen]

Yay. We have a screen.
Now, if we want to create a window on this screen, that looks complicated, but
it isn't (really!).

::

    window = xproto.Window.create(conn,
        screen.root,
        screen.root_depth,
        screen.root_visual
    )

That's the easiest call possible. It will create a window with the screen's
root window as parent, its root depth as depth and its root visual as visual.
Fortunately, there is a shortcut for this boilerplate code:

::

    window = xproto.Window.create_toplevel_on_screen(conn, screen)

Woah! So easy!

These two calls will create a new (unmapped: invisible) window with the root
window as parent: a top-level window. It will be 640x480 pixels huge, have no
border and be located at the top left edge of the screen (x=0, y=0).

Now ...

::

    window.map()
    print conn.wait_for_event()

Shouldn't this display a window? Why doesn't it do? It just does nothing and
doesn't even stop! `killall python` helps, but ... how to fix it?

As `Christophe Tronche <http://tronche.com>`_ explains in his awesome
`"Short Xlib Tutorial" <http://tronche.com/gui/x/xlib-tutorial/>`_
(worth reading!), we need to flush after we have done a bunch of requests.
They are cached until you check a request or call `flush`, then all cached
requests will be delivered. So, change the lines above to:

::

    window.map()
    conn.flush()
    print conn.wait_for_event()

As a convenience function, you can also use
:meth:`ooxcb.conn.Connection.bunch` in a `with` stament. After the execution
of the `with` block, the connection gets flushed.

::

    with conn.bunch():
        window.map()
    print conn.wait_for_event()

Of course, that makes more sense if you have more requests at a time.

And - the window appears, but with 'nothing in it'. We actually want to
see something, and so we'll set the background color of the window to
plain white. That is done by modifying the window creation line:

::

    window = xproto.Window.create_toplevel_on_screen(conn, screen,
                    back_pixel=screen.white_pixel)

And - it has a white background. Awesome!

Now, before we can start to draw anything here, we have to talk about events.
We are communiating with the X server, and the X server is communicating with
us. We send requests, he sends responses. And sometimes, he sends events.
It is possible to handle events in an Xlib style here:

::

    while 1:
        evt = conn.wait_for_event()
        if isinstance(evt, xproto.ExposeEvent):
            print 'Got an expose event!'
        elif ...

But ooxcb also comes with an event dispatching framework, and it is very
convenient to use because you don't have to figure out who has to handle
the event yourself.

::

    @window.event
    def on_expose(evt):
        print 'Got an expose event for %s!' % repr(window)

    while 1:
        conn.wait_for_event().dispatch()

So, `on_expose` is called only if `window` is exposed.

To draw in the window at the right time, we will register for the expose event
and draw if we receive one. We first have to register for the expose events to
receive any. Don't forget to register for events!

We can do that in the window creation line, too:

::

    window = xproto.Window.create_toplevel_on_screen(conn, screen,
                    back_pixel=screen.white_pixel,
                    event_mask=xproto.EventMask.Exposure
                    )

Now, let's listen to expose events. We have a new mainloop now:

::

    @window.event
    def on_expose(evt):
        " drawing here ... "

    # Our mainloop.
    while 1:
        conn.wait_for_event().dispatch()

Now, if we want to draw something in the window now, we need a graphics
context first. A graphics context is required for drawing anything on
a drawable. Fortunately, a window is a drawable, so it is rather easy
to start. Put the following in the beginning of the script:

::

    gc = xproto.GContext.create(conn, window)

We will draw a line from (0, 0) to (640, 480) now. A diagonal line through
the whole window. Put it in `on_expose`:

::

    @window.event
    def on_expose(evt):
        gc.poly_line(window, [(0, 0), (640, 480)])
        conn.flush()

You see, we are giving `poly_line` a list of tuples of (x, y) here. That's
useful if we want to draw multiple lines at once, e.g. a triangle:

::

    gc.poly_line(window, [(10, 10), (600, 400), (10, 400), (10, 10)])
    conn.flush()

Also note that we have to pass `window` to each drawing function again. Don't
forget that. And don't forget to flush.

Well, we have a very cool triangle now. But if we click on the tiny X to close
the window, we get a very bad "IOError: I/O error on X server connection."
exception. What can we do to avoid that?
Ah, we could close the window gracefully if the user presses a button!

That's easy. Just register for the ButtonPress events ...

::

    window = xproto.Window.create_toplevel_on_screen(conn, screen,
                    back_pixel=screen.white_pixel,
                    event_mask=xproto.EventMask.Exposure | xproto.EventMask.ButtonPress
                    )

:note: Multiple events to listen to are joined with the binary or operator \|, the pipe.

... and now create an event handler that disconnects and quits if invoked:

::

    @window.event
    def on_button_press(evt):
        conn.disconnect()
        sys.exit()


... and you're done.
