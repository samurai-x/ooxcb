import sys
sys.path.append('..')

import ooxcb
import ooxcb.protocol.xproto as X

conn = ooxcb.connect()

fonts = conn.core.list_fonts(1, '10x20').reply().names
font = X.Font.open(conn, fonts[0])
print font.query().reply()
#print vars(font.query_text_extents('foobar').reply())

# TODO: doesn't work :)
#p = conn.core.get_font_path().reply().path
#p.insert(-1, '/home/fred/')
#conn.core.set_font_path_checked(p).check()
#print conn.core.get_font_path().reply().path

# This way, you'll get a list of `ListFontsWithInfoReply`
# instances. Don't use `list_fonts_with_info`, it is
# tricky (gets multiple replies for one request)
#fonts = conn.core.list_all_fonts_with_info(3, '*')

conn.disconnect()
