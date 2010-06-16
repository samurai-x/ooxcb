from StringIO import StringIO
from string import Template

def tmpl(s, **kwargs):
    return Template(s).substitute(**kwargs)

EXTENSIONS = ('xproto', 'xtest', 'render', 'composite', 'shape', 'xfixes',
        'damage', 'screensaver', 'bigreq')

print 'all: %s\n' % ' '.join(EXTENSIONS)

for ext in EXTENSIONS:
    print tmpl(
"""$ext: ../ooxcb/protocol/$ext.py ../docs/source/api/protocol/$ext.rst

../docs/source/api/protocol/$ext.rst: $ext.rst
\tcp $ext.rst ../docs/source/api/protocol/$ext.rst

$ext.rst: ../ooxcb/protocol/$ext.py

../ooxcb/protocol/$ext.py: $ext.xml $ext.i
\tpython ooxcb_client.py $ext > ../ooxcb/protocol/$ext.py
""", ext=ext)

print tmpl("""clean:
\trm -f ../docs/source/api/protocol/{$exts}.rst ../ooxcb/protocol/{$exts}.py {$exts}.rst

.phony: $names
""", exts=','.join(EXTENSIONS), names=' '.join(EXTENSIONS))
