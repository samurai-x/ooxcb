# Copyright (c) 2008-2010, samurai-x.org
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the samurai-x.org nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY SAMURAI-X.ORG ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL SAMURAI-X.ORG  BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
    This module contains some helper functions for the icccm standard.
"""

from ooxcb.protocol.xproto import Window, Pixmap

class WMState(object):
    """
        container class for the WM_STATE property.

        .. attribute:: state

            one member of :class:`ooxcb.xproto.WMState`

        .. attribute:: icon

            The icon window, either a :class:`ooxcb.xproto.Window` instance
            or None.
    """
    def __init__(self, state, icon):
        self.state = state
        self.icon = icon

def icccm_get_wm_state(window):
    """
        return a :class:`WMState` instance or None if
        there is no `WM_STATE` property.
    """
    prop = window.get_property('WM_STATE', 'WM_STATE').reply()
    if not prop.exists:
        return None
    else:
        icon = None
        if prop.value[1]:
            prop = window.conn.get_from_cache_fallback(prop.value[1], Window)
        return WMState(prop.value[0], icon)

class WMHints(object):
    """
        a container class for the `WM_HINTS` property.

        .. attribute:: flags

            a mask of the :class:`WMHintsFlags` values

        .. attribute:: input

            The client's input model (True/False)

        .. attribute:: initial_state

            The state when first mapped

        .. attribute:: icon_pixmap

            The pixmap for the icon image

        .. attribute:: icon_window

            The window for the icon image

        .. attribute:: icon_x

            X coordinate of the icon location

        .. attribute:: icon_y

            Y coordinate of the icon location

        .. attribute:: icon_mask

            The mask for the icon shape

    """
    def __init__(self, flags, input, initial_state, icon_pixmap,
            icon_window, icon_x, icon_y, icon_mask):
        self.flags = flags
        self.input = input
        self.initial_state = initial_state
        self.icon_pixmap = icon_pixmap
        self.icon_window = icon_window
        self.icon_x = icon_x
        self.icon_y = icon_y
        self.icon_mask = icon_mask

def icccm_get_wm_hints(window):
    """
        return a :class:`WMHints` instance or None if there is no
        `WM_HINTS` property or the value is invalid.
    """
    prop = window.get_property('WM_HINTS', 'CARDINAL').reply()
    if (not prop.exists or not prop.value):
        return None
    else:
        value = prop.value
        return WMHints(
                value[0],
                value[1],
                value[2],
                window.conn.get_from_cache_fallback(value[3], Pixmap),
                window.conn.get_from_cache_fallback(value[4], Window),
                value[5],
                value[6],
                window.conn.get_from_cache_fallback(value[7], Pixmap)
                )

def mixin():
    from ooxcb.util import mixin_functions
    mixin_functions((
        icccm_get_wm_state,
        icccm_get_wm_hints,
        ), Window)

