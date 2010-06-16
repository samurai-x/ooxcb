import sys
sys.path.append('..')

import ooxcb
from ooxcb.protocol import xproto
import ooxcb.contrib.pil

ooxcb.contrib.pil.mixin()

conn = ooxcb.connect()
root = conn.setup.roots[conn.pref_screen].root

image = root.get_pil_image()
image.save("screenshot.png")

conn.disconnect()
