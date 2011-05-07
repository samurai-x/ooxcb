ooxcb.protocol.record
=====================

.. module:: ooxcb.protocol.record

.. class:: Category

    .. data:: FromServer


    .. data:: FromClient


    .. data:: ClientStarted


    .. data:: ClientDied


    .. data:: StartOfData


    .. data:: EndOfData


.. class:: recordExtension

    .. data:: header


    .. method:: query_version(self, major_version, minor_version)


    .. method:: query_version_unchecked(self, major_version, minor_version)


    .. method:: create_context_checked(self, context, element_header, client_specs, ranges)


    .. method:: create_context(self, context, element_header, client_specs, ranges)


.. class:: ElementHeader

    .. method:: __init__(self, conn, xid)


.. class:: ClientInfo

    .. method:: __init__(self, conn)


    .. attribute:: ranges

    .. attribute:: num_ranges

    .. attribute:: client_resource

.. class:: BadContext

.. class:: ContextError

    .. method:: __init__(self, conn)


    .. attribute:: invalid_record

.. class:: EnableContextCookie

.. class:: QueryVersionCookie

.. class:: GetContextCookie

.. class:: GetContextReply

    .. method:: __init__(self, conn)


    .. attribute:: enabled

    .. attribute:: num_intercepted_clients

    .. attribute:: element_header

    .. attribute:: intercepted_clients

.. class:: Range16

    .. method:: __init__(self, conn)


    .. classmethod:: create(cls, conn, first, last)


    .. attribute:: last

    .. attribute:: first

.. class:: ExtRange

    .. method:: __init__(self, conn)


    .. classmethod:: create(cls, conn, major_first, major_last, minor_first, minor_last)


    .. attribute:: major

    .. attribute:: minor

.. class:: Range

    .. method:: __init__(self, conn)


    .. classmethod:: create(cls, conn, core_requests, core_replies, ext_requests, ext_replies, delivered_events, device_events, errors, client_started, client_died)


    .. attribute:: client_started

    .. attribute:: ext_requests

    .. attribute:: device_events

    .. attribute:: core_replies

    .. attribute:: core_requests

    .. attribute:: client_died

    .. attribute:: errors

    .. attribute:: ext_replies

    .. attribute:: delivered_events

.. class:: HType

    .. data:: FromServerTime


    .. data:: FromClientTime


    .. data:: FromClientSequence


.. class:: Context

    .. method:: __init__(self, conn, xid)


    .. method:: register_clients_checked(self, element_header, client_specs, ranges)


    .. method:: register_clients(self, element_header, client_specs, ranges)


    .. method:: unregister_clients_checked(self, client_specs)


    .. method:: unregister_clients(self, client_specs)


    .. method:: get(self)


    .. method:: get_unchecked(self)


    .. method:: enable(self)


    .. method:: enable_unchecked(self)


    .. method:: disable_checked(self)


    .. method:: disable(self)


    .. method:: free_checked(self)


    .. method:: free(self)


    .. classmethod:: create(cls, conn, element_header, client_specs, ranges)


.. class:: Clientspec

    .. method:: __init__(self, conn, xid)


.. class:: CS

    .. data:: CurrentClients


    .. data:: FutureClients


    .. data:: AllClients


.. class:: Range8

    .. method:: __init__(self, conn)


    .. classmethod:: create(cls, conn, first, last)


    .. attribute:: last

    .. attribute:: first

.. class:: EnableContextReply

    .. method:: __init__(self, conn)


    .. attribute:: category

    .. attribute:: server_time

    .. attribute:: xid_base

    .. attribute:: client_swapped

    .. attribute:: element_header

    .. attribute:: rec_sequence_num

    .. attribute:: data

.. class:: QueryVersionReply

    .. method:: __init__(self, conn)


    .. attribute:: major_version

    .. attribute:: minor_version

