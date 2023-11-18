.PHONY: FORCE

SOURCES = sfd/IBM-Courier.sfd sfd/IBM-Courier-Italic.sfd sfd/IBM-Courier-Bold.sfd sfd/IBM-Courier-Bold-Italic.sfd

TTF     = $(patsubst sfd/%.sfd,fonts/%.ttf,$(SOURCES))
WOFF    = $(patsubst sfd/%.sfd,fonts/%.woff,$(SOURCES))
WOFF2   = $(patsubst sfd/%.sfd,fonts/%.woff2,$(SOURCES))
SVG     = $(patsubst sfd/%.sfd,fonts/%.svg,$(SOURCES))
OTF     = $(patsubst sfd/%.sfd,fonts/%.otf,$(SOURCES))

default: FORCE $(TTF) $(WOFF) $(WOFF2) $(SVG) $(OTF)

fonts/%.ttf: sfd/%.sfd Makefile bin/convert.py
	bin/convert.py "$<" "$@"
fonts/%.woff: sfd/%.sfd Makefile bin/convert.py
	bin/convert.py "$<" "$@"
fonts/%.woff2: sfd/%.sfd Makefile bin/convert.py
	bin/convert.py "$<" "$@"
fonts/%.svg: sfd/%.sfd Makefile bin/convert.py
	bin/convert.py "$<" "$@"
fonts/%.otf: sfd/%.sfd Makefile bin/convert.py
	bin/convert.py "$<" "$@"
