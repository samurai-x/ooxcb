ooxcb.conn
==========

.. module:: ooxcb.conn

.. autoclass:: ooxcb.Connection
    :members:
    
    .. attribute:: synchronous_check

        If synchronous_check is True, all requests
        will be sent as checked (regardless if
        x() or x_checked() is called) and each requests
        will be checked automatically (and that's slow).
        Additionally, it also provokes lazy programming,
        because if a request is checked, it is immediately
        sent. If you are not careful, you will have a
        non-working program if you turn out the synchronous
        checks because you didn't care about calling
        `conn.flush()` at the correct places :)

    .. attribute:: keysyms

        A :class:`ooxcb.keysyms.Keysyms` helper instance.

    .. attribute:: atoms

        A :class:`ooxcb.atoms.AtomDict` helper instance.

    .. attribute:: conn

        The opaque libxcb connection pointer. You will most likely
        do not have to use that.

