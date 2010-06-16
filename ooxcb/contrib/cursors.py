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

from ooxcb.protocol.xproto import Font, Cursor

# See http://tronche.com/gui/x/xlib/appendix/b/ for values
XUTIL_CURSOR_FLEUR = 52
XUTIL_CURSOR_LEFT_PTR = 68
XUTIL_CURSOR_SIZING = 120
XUTIL_CURSOR_BOTTOM_LEFT_CORNER = 12
XUTIL_CURSOR_BOTTOM_RIGHT_CORNER = 14
XUTIL_CURSOR_TOP_LEFT_CORNER = 134
XUTIL_CURSOR_TOP_RIGHT_CORNER = 136
XUTIL_CURSOR_DOUBLE_ARROW_HORIZ = 108
XUTIL_CURSOR_DOUBLE_ARROW_VERT = 116

CURSORS = (
    ('Normal',    XUTIL_CURSOR_LEFT_PTR),
    ('Resize',    XUTIL_CURSOR_SIZING),
    ('ResizeH',   XUTIL_CURSOR_DOUBLE_ARROW_HORIZ),
    ('ResizeV',   XUTIL_CURSOR_DOUBLE_ARROW_VERT),
    ('Move',      XUTIL_CURSOR_FLEUR),
    ('TopRight',  XUTIL_CURSOR_TOP_RIGHT_CORNER),
    ('TopLeft',   XUTIL_CURSOR_TOP_LEFT_CORNER),
    ('BotRight',  XUTIL_CURSOR_BOTTOM_RIGHT_CORNER),
    ('BotLeft',   XUTIL_CURSOR_BOTTOM_LEFT_CORNER),
)

class Cursors(dict):
    """
        A dictionary holding some `Cursor` instances,
        generated from the 'cursor' font.

        Currently it has the following items (each cursor
        listed with its corresponding cursor
        on http://tronche.com/gui/x/xlib/appendix/b/):

        'Normal'
            XC_left_ptr
        'Resize'
            XC_sizing
        'ResizeH'
            XC_sb_h_double_arrow
        'ResizeV'
            XC_sb_v_double_arrow
        'Move'
            XC_fleur
        'TopRight'
            XC_top_right_corner
        'TopLeft'
            XC_top_left_corner
        'BotRight'
            XC_bottom_right_corner
        'BotLeft'
            XC_bottom_left_corner

        Example:

        ::

            cursors = Cursors(my_connection)
            print cursors['Resize']

    """
    def __init__(self, connection):
        self.connection = connection
        self.font = Font.open(self.connection, "cursor")

        for name, cursor_font in CURSORS:
            self._load_cursor(name, cursor_font)

    def _load_cursor(self, name, cursor_font):
        """
            load the cursor named *name* from the font object
            *cursor_font*, and add it to the dictionary.
        """
        self[name] = Cursor.create_glyph(self.connection,
                self.font, self.font,
                cursor_font, cursor_font + 1,
                0, 0, 0,
                65535, 65535, 65535)

