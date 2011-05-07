# Copyright (c) 2008-2011, samurai-x.org
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
    This module contains functions for putting and getting images using
    the gtk / gdk objects.
"""

import gtk.gdk

def get_icon_pixbufs(data):
    """
        Return a dictionary of all available icons in *icon_data*
        connecting size tuples to `gtk.gdk.Pixbuf` instances.
    """
    length = len(data)
    sizes = {}
    start = 0
    while start < length:
        width = data[start]
        height = data[start + 1]
        rgba_data = ''
        for argb in data[start + 2:start + 2 + width*height]:
            rgba = ((argb << 8) & 0xffffff00) | (argb >> 24)
            rgba_data += chr(rgba >> 24)
            rgba_data += chr((rgba >> 16) & 0xff)
            rgba_data += chr((rgba >> 8) & 0xff)
            rgba_data += chr(rgba & 0xff)
        start += 2 + width * height
        sizes[(width, height)] = gtk.gdk.pixbuf_new_from_data(
                rgba_data, gtk.gdk.COLORSPACE_RGB, True, 8, width, height, width * 4)
    return sizes

def choose_icon(pixbufs, desired_size):
    """
        Return a pixbuf scaled to *desired_size* or None.

        :param pixbufs: A dictionary connecting sizes to pixbufs as returned
                        by `get_icon_pixbufs`.
        :param desired_size: A 2-element (width, height) tuple describing the
                             desired icon size. If the return value is not None,
                             it is guaranteed to be scaled to *desired_size*.
    """
    best = None
    best_size = None

    def _diff(a, b):
        return (abs(a[0] - b[0]), abs(a[1] - b[1]))

    def _current_diff():
        return _diff(desired_size, best_size)

    for size, pixbuf in pixbufs.iteritems():
        if (best is None or _current_diff() > _diff(desired_size, size)):
            best = pixbuf
            best_size = size

    if(best is not None and best_size != desired_size):
        best = best.scale_simple(desired_size[0], desired_size[1], gtk.gdk.INTERP_HYPER)

    return best
