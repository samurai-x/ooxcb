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

# TODO: rename `ooxcb.types`, so we can do `from types import FunctionType` here
def _f():
    pass

FunctionType = type(_f)
del _f

class cached_property(object):
    """
        A simple cached property descriptor.
        from http://ronny.uberhost.de/simple-cached-for-properties-done-right
    """
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, obj, type=None):
        if obj is None:
            return self

        result = self.func(obj)
        setattr(obj, self.name, result)
        return result

class cached_classproperty(object):
    """
        a modified version of :class:`cached_property` that allows to define
        cached properties on classes.
    """
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, obj, type):
        # equal if we call it bound to an instance or not.
        result = self.func(type)
        setattr(type, self.name, result)
        return result

def mixin_functions(functions, into):
    """
        Add all functions in *functions* to the class *into*.
    """
    for function in functions:
        setattr(into, function.__name__, function)

def _inject_class(cls, meth):
    def classmeth(_, *args, **kwargs):
        return meth.__get__(None, cls)(*args, **kwargs)
    return classmethod(classmeth)

class MixinMeta(type):
    """
        a metaclass for mixin classes that transforms all methods
        to static methods. So the user is able to mix them into
        the class *or* to call them manually if he wants that.
    """
    def __new__(mcs, name, bases, dct):
        dct['methods'] = methods = {}
        for name in dct.keys():
            obj = dct[name]
            if isinstance(obj, FunctionType): # TODO: add staticmethod?
                methods[name] = obj
                dct[name] = staticmethod(obj)
            elif isinstance(obj, classmethod):
                if name != 'mixin': # don't wrap the builtin mixin method
                    methods[name] = obj
                    dct[name] = _inject_class(dct['target_class'], obj)
        return type.__new__(mcs, name, bases, dct)

class Mixin(object):
    """
        Base class for all mixins.
        They should have one class attribute set:

        .. attribute:: target_class

            The class this class provides some additional methods for.

        Do not try to instantiate.
    """
    __metaclass__ = MixinMeta
    target_class = None
    methods = {}

    def __init__(self, *args, **kwargs):
        raise RuntimeError("You can't instantiate mixin classes.")

    @classmethod
    def mixin(cls):
        """
            mix all additional methods into the target class.
        """
        assert cls.target_class is not None
        for name, function in cls.methods.iteritems():
            setattr(cls.target_class, name, function)

