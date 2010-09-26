ooxcb.protocol.damage
=====================

.. module:: ooxcb.protocol.damage

.. class:: ReportLevel

    .. data:: RawRectangles


    .. data:: DeltaRectangles


    .. data:: BoundingBox


    .. data:: NonEmpty


.. class:: damageExtension

    .. data:: header


    .. method:: query_version(self, client_major_version, client_minor_version)


    .. method:: query_version_unchecked(self, client_major_version, client_minor_version)


    .. method:: create_checked(self, damage, drawable, level)


    .. method:: create(self, damage, drawable, level)


.. class:: DrawableMixin

    .. data:: target_class


    .. method:: damage_add_checked(self, region)


    .. method:: damage_add(self, region)


.. class:: DamageNotifyEvent

    .. data:: event_name


    .. data:: opcode


    .. data:: event_target_class


    .. method:: __init__(self, conn)


    .. attribute:: area

    .. attribute:: geometry

    .. attribute:: timestamp

    .. attribute:: level

    .. attribute:: damage

    .. attribute:: response_type

    .. attribute:: drawable

.. class:: Damage

    .. method:: __init__(self, conn, xid)


    .. method:: destroy_checked(self)


    .. method:: destroy(self)


    .. method:: subtract_checked(self, repair, parts)


    .. method:: subtract(self, repair, parts)


    .. classmethod:: create(cls, conn, drawable, level)


.. class:: BadDamage

.. class:: QueryVersionCookie

.. class:: DamageError

    .. method:: __init__(self, conn)


.. class:: QueryVersionReply

    .. method:: __init__(self, conn)


    .. attribute:: major_version

    .. attribute:: minor_version

