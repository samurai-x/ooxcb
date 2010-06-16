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
    This module contains some helper functions and methods
    dealing with the `ewmh standard`_.
    They can also mixed into their corresponding classes.

    .. _ewmh standard: http://standards.freedesktop.org/wm-spec/wm-spec-latest.html
"""

from ooxcb.list import List

def ewmh_get_client_list(screen):
    """
        return a list of :class:`ooxcb.protocol.xproto.Window` instances, or
        None if the _NET_CLIENT_LIST property is not set.
    """
    reply = screen.root.get_property('_NET_CLIENT_LIST', 'WINDOW').reply()
    if not reply.exists:
        return None
    else:
        return reply.value.to_windows()

def ewmh_get_client_list_stacking(screen):
    """
        return a list of :class:`ooxcb.protocol.xproto.Window` instances, or
        None if the _NET_CLIENT_LIST_STACKING property is not set.
    """
    reply = screen.root.get_property('_NET_CLIENT_LIST_STACKING', 'WINDOW').reply()
    if not reply.exists:
        return None
    else:
        return reply.value.to_windows()

def ewmh_get_number_of_desktops(screen):
    """
        return the number of desktops, or None if the property
        _NET_NUMBER_OF_DESKTOPS is not set.
    """
    reply = screen.root.get_property('_NET_NUMBER_OF_DESKTOPS', 'CARDINAL').reply()
    if not reply.exists:
        return None
    else:
        return reply.value[0]

def ewmh_get_current_desktop(screen):
    """
        return the current desktop index (starting at 0),
        or None if the _NET_CURRENT_DESKTOP property is not set.
    """
    reply = screen.root.get_property('_NET_CURRENT_DESKTOP', 'CARDINAL').reply()
    if not reply.exists:
        return None
    else:
        return reply.value[0]

def ewmh_get_desktop(window):
    """
        return the desktop of the window or None
        if the _NET_WM_DESKTOP property is not set.
        0xffffffff is returned if the window wants to be
        visible on all desktops (according to the ewmh spec)
    """
    reply = window.get_property('_NET_WM_DESKTOP', 'CARDINAL').reply()
    if not reply.exists:
        return None
    else:
        return reply.value[0]

# TODO emwh_get_visible_window_name/get_window_name
def ewmh_get_window_name(window):
    """
        returns the window title you should use.
        Since it respects the icccm and the ewmh standard,
        it will use:

         * _NET_WM_VISIBLE_NAME if available. if not,
         * _NET_WM_NAME if available. if not,
         * WM_NAME

        If `WM_NAME` is not available, it will return an empty string.

        .. note:: WM_NAME's encoding is latin-1, _NET_WM_NAME and
                _NET_WM_VISIBLE_NAME are utf-8-encoded.
    """
    # try _NET_WM_VISIBLE_NAME
    encoding = 'utf-8'
    reply = window.get_property(
            '_NET_WM_VISIBLE_NAME', 'UTF8_STRING').reply()
    if not reply.exists:
        # try _NET_WM_NAME
        reply = window.get_property(
                '_NET_WM_NAME', 'UTF8_STRING').reply()
        if not reply.exists:
            # use WM_NAME ( has ... to ... exist! )
            reply = window.get_property(
                    'WM_NAME', 'STRING').reply()
            encoding = 'latin-1'
            if not reply.exists:
                return ''
    return reply.value.to_string().decode(encoding)


def ewmh_set_window_name(window, name):
    if type(name) is not unicode:
        name = unicode(name, 'utf8', 'replace')
    window.change_property('WM_NAME', 'STRING', 8, List.from_string(name.encode('latin-1', 'replace')))
    window.change_property('_NET_WM_NAME', 'UTF8_STRING', 8, List.from_string(name.encode('utf8', 'replace')))


def mixin():
    """
        mix em all
    """
    from ooxcb.util import mixin_functions
    from ooxcb.protocol.xproto import Screen, Window
    
    mixin_functions((
        ewmh_get_client_list,
        ewmh_get_client_list_stacking,
        ewmh_get_number_of_desktops,
        ewmh_get_current_desktop,
        ), Screen)
    mixin_functions((
        ewmh_get_desktop,
        ewmh_get_window_name,
        ewmh_set_window_name,
        ), Window)
