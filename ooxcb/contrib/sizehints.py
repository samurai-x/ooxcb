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

from __future__ import division

US_POSITION = 1 << 0
US_SIZE = 1 << 1
P_POSITION = 1 << 2
P_SIZE = 1 << 3
P_MINSIZE = 1 << 4
P_MAXSIZE = 1 << 5
P_RESIZEINC = 1 << 6
P_ASPECT = 1 << 7
P_BASESIZE = 1 << 8
P_WINGRAVITY = 1 << 9

class SizeHints(object):
    """
        :class:`SizeHints` is a convenience class for parsing the
        `WM_NORMAL_HINTS` property (as defined in the icccm)

        .. data:: properties

            The tuple of allowed property values.
            
            :: 

                ('flags', 'x', 'y', 'width', 'height', 'min_width', 
                  'min_height', 'max_width', 'max_height', 'width_inc',
                  'height_inc', 'min_aspect_num', 'min_aspect_den',
                  'max_aspect_num', 'max_aspect_den', 'base_width', 
                  'base_height', 'win_gravity')

    """
    properties = ('flags', 'x', 'y', 'width', 'height', 'min_width',
              'min_height', 'max_width', 'max_height', 'width_inc',
              'height_inc', 'min_aspect_num', 'min_aspect_den',
              'max_aspect_num', 'max_aspect_den', 'base_width', 'base_height',
              'win_gravity')
 
    def __init__(self, **kwargs):
        """
            :param \*\*kwargs: Provided information, keys from 
                               :data:`SizeHints.properties`
        """
        flags = kwargs['flags']
        valid = False

        try:
            if flags & P_SIZE:
                self.base_width = kwargs['base_width']
                self.base_height = kwargs['base_height']
                valid = True
            elif flags & P_MINSIZE:
                self.base_width = kwargs['min_width']
                self.base_height = kwargs['min_height']
                valid = True
            else:
                self.base_width, self.base_height = 0, 0
            if flags & P_RESIZEINC:
                self.width_inc = kwargs['width_inc']
                self.height_inc = kwargs['height_inc']
                valid = True
            else:
                self.width_inc, self.height_inc = 0, 0
            if flags & P_MAXSIZE:
                self.max_width = kwargs['max_width']
                self.max_height = kwargs['height_inc']
                valid = True
            else:
                self.max_width, self.max_height = 0, 0
            if flags & P_MINSIZE:
                self.min_width = kwargs['min_width']
                self.min_height = kwargs['min_height']
                valid = True
            elif flags & P_BASESIZE:
                self.min_width = kwargs['base_width']
                self.min_height = kwargs['base_height']
                valid = True
            else:
                self.min_width, self.min_height = 0, 0
            if flags & P_ASPECT:
                self.min_aspect_num = kwargs['min_aspect_num']
                self.min_aspect_den = kwargs['min_aspect_den']
                self.max_aspect_num = kwargs['max_aspect_num']
                self.max_aspect_den = kwargs['max_aspect_den']
                valid = True
            else:
                self.min_aspect_num = 0
                self.min_aspect_den = 0
                self.max_aspect_num = 0
                self.max_aspect_den = 0
        except KeyError:
            valid = False

        self.valid = valid

    @classmethod
    def from_values(cls, values):
        """
            create a SizeHints instance from a list of integers,
            e.g. from a GetPropertyReply
        """
        return cls(**dict(zip(cls.properties, values)))

    def compute(self, geom):
        """
            compute *geom* in-place. If *self* is not valid,
            nothing is changed.
        """
        if not self.valid:
            # don't compute if not valid
            return

        if self.min_aspect_den > 0 and self.max_aspect_den > 0 and \
                (geom.width - self.base_width) > 0 and \
                (geom.height - self.base_height) > 0:
            dx = geom.width - self.base_width
            dy = geom.height - self.base_height
            min_ = self.min_aspect_num / self.min_aspect_den # float division
            max_ = self.max_aspect_num / self.max_aspect_den

            ratio = dx / dy
            if max_ > 0 and min_ > 0 and ratio > 0:
                if ratio < min:
                    dy = (dx * min_ + dy) / (min_ * min_ + 1)
                    dx = dy * min_
                    geom.width = int(dx + self.base_width)
                    geom.height = int(dy + self.base_height)
                elif ratio > max:
                    dy = (dx * min_ + dy) / (max_ * max_ + 1)
                    dx = dy * min_
                    geom.width = int(dx + self.base_width)
                    geom.height = int(dy + self.base_height)
        if self.min_width:
            geom.width = max(self.min_width, geom.width)
        if self.min_height:
            geom.height = max(self.min_height, geom.height)
        if self.max_width:
            geom.width = min(self.max_width, geom.width)
        if self.max_height:
            geom.height = min(self.max_height, geom.height)

        if self.width_inc:
            geom.width -= (geom.width - self.base_width) % self.width_inc
        if self.height_inc:
            geom.height -= (geom.height - self.base_height) % self.height_inc

