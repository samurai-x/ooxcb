from time import time
import Xlib, Xlib.display

NUM_NAMES = 500
NAMES = ['NAME%d' % i for i in xrange(NUM_NAMES)]
atoms = []

display = Xlib.display.Display()
begin = time()

for name in NAMES:
    atoms.append(display.intern_atom(name))

end = time()

print 'Elapsed time: %f' % (end - begin)
