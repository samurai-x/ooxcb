all: xproto xtest render composite shape xfixes damage screensaver bigreq

xproto: ../ooxcb/protocol/xproto.py ../docs/source/api/protocol/xproto.rst

../docs/source/api/protocol/xproto.rst: xproto.rst
	cp xproto.rst ../docs/source/api/protocol/xproto.rst

xproto.rst: ../ooxcb/protocol/xproto.py

../ooxcb/protocol/xproto.py: xproto.xml xproto.i
	python ooxcb_client.py xproto > ../ooxcb/protocol/xproto.py

xtest: ../ooxcb/protocol/xtest.py ../docs/source/api/protocol/xtest.rst

../docs/source/api/protocol/xtest.rst: xtest.rst
	cp xtest.rst ../docs/source/api/protocol/xtest.rst

xtest.rst: ../ooxcb/protocol/xtest.py

../ooxcb/protocol/xtest.py: xtest.xml xtest.i
	python ooxcb_client.py xtest > ../ooxcb/protocol/xtest.py

render: ../ooxcb/protocol/render.py ../docs/source/api/protocol/render.rst

../docs/source/api/protocol/render.rst: render.rst
	cp render.rst ../docs/source/api/protocol/render.rst

render.rst: ../ooxcb/protocol/render.py

../ooxcb/protocol/render.py: render.xml render.i
	python ooxcb_client.py render > ../ooxcb/protocol/render.py

composite: ../ooxcb/protocol/composite.py ../docs/source/api/protocol/composite.rst

../docs/source/api/protocol/composite.rst: composite.rst
	cp composite.rst ../docs/source/api/protocol/composite.rst

composite.rst: ../ooxcb/protocol/composite.py

../ooxcb/protocol/composite.py: composite.xml composite.i
	python ooxcb_client.py composite > ../ooxcb/protocol/composite.py

shape: ../ooxcb/protocol/shape.py ../docs/source/api/protocol/shape.rst

../docs/source/api/protocol/shape.rst: shape.rst
	cp shape.rst ../docs/source/api/protocol/shape.rst

shape.rst: ../ooxcb/protocol/shape.py

../ooxcb/protocol/shape.py: shape.xml shape.i
	python ooxcb_client.py shape > ../ooxcb/protocol/shape.py

xfixes: ../ooxcb/protocol/xfixes.py ../docs/source/api/protocol/xfixes.rst

../docs/source/api/protocol/xfixes.rst: xfixes.rst
	cp xfixes.rst ../docs/source/api/protocol/xfixes.rst

xfixes.rst: ../ooxcb/protocol/xfixes.py

../ooxcb/protocol/xfixes.py: xfixes.xml xfixes.i
	python ooxcb_client.py xfixes > ../ooxcb/protocol/xfixes.py

damage: ../ooxcb/protocol/damage.py ../docs/source/api/protocol/damage.rst

../docs/source/api/protocol/damage.rst: damage.rst
	cp damage.rst ../docs/source/api/protocol/damage.rst

damage.rst: ../ooxcb/protocol/damage.py

../ooxcb/protocol/damage.py: damage.xml damage.i
	python ooxcb_client.py damage > ../ooxcb/protocol/damage.py

screensaver: ../ooxcb/protocol/screensaver.py ../docs/source/api/protocol/screensaver.rst

../docs/source/api/protocol/screensaver.rst: screensaver.rst
	cp screensaver.rst ../docs/source/api/protocol/screensaver.rst

screensaver.rst: ../ooxcb/protocol/screensaver.py

../ooxcb/protocol/screensaver.py: screensaver.xml screensaver.i
	python ooxcb_client.py screensaver > ../ooxcb/protocol/screensaver.py

bigreq: ../ooxcb/protocol/bigreq.py ../docs/source/api/protocol/bigreq.rst

../docs/source/api/protocol/bigreq.rst: bigreq.rst
	cp bigreq.rst ../docs/source/api/protocol/bigreq.rst

bigreq.rst: ../ooxcb/protocol/bigreq.py

../ooxcb/protocol/bigreq.py: bigreq.xml bigreq.i
	python ooxcb_client.py bigreq > ../ooxcb/protocol/bigreq.py

clean:
	rm -f ../docs/source/api/protocol/{xproto,xtest,render,composite,shape,xfixes,damage,screensaver,bigreq}.rst ../ooxcb/protocol/{xproto,xtest,render,composite,shape,xfixes,damage,screensaver,bigreq}.py {xproto,xtest,render,composite,shape,xfixes,damage,screensaver,bigreq}.rst

.phony: xproto xtest render composite shape xfixes damage screensaver bigreq

