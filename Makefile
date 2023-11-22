.PHONY: FORCE

SFD_SOURCES    := sfd/IBMCourier.sfd sfd/IBMCourier-Italic.sfd sfd/IBMCourier-Bold.sfd sfd/IBMCourier-BoldItalic.sfd
SFD_ZERO_SLASH := $(patsubst sfd/IBMCourier%sfd,sfd/zero-slash/IBMCourierZeroSlash%sfd,$(SFD_SOURCES))
SFD_ZERO_DOT   := $(patsubst sfd/IBMCourier%sfd,sfd/zero-dot/IBMCourierZeroDot%sfd,$(SFD_SOURCES))
SFD            := $(SFD_SOURCES) $(SFD_ZERO_SLASH) $(SFD_ZERO_DOT)

TTF     := $(patsubst sfd/%.sfd,fonts/%.ttf,$(SFD))
WOFF    := $(patsubst sfd/%.sfd,fonts/%.woff,$(SFD))
WOFF2   := $(patsubst sfd/%.sfd,fonts/%.woff2,$(SFD))
SVG     := $(patsubst sfd/%.sfd,fonts/%.svg,$(SFD))
OTF     := $(patsubst sfd/%.sfd,fonts/%.otf,$(SFD))

default: FORCE $(TTF) $(WOFF) $(WOFF2) $(SVG) $(OTF)

sfd: $(SFD_ZERO_SLASH) $(SFD_ZERO_DOT)

echo: FORCE
	for file in $(TTF) $(WOFF) $(WOFF2) $(SVG) $(OTF) ; do echo $$file ; done

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

sfd/zero-dot/IBMCourierZeroDot%sfd: sfd/IBMCourier%sfd Makefile bin/zeroslash.py
	mkdir -p $(<D)
	bin/zeroslash.py --char zerodot "$<" "$@.tmp.sfd"
	mv "$@.tmp.sfd" "$@"
sfd/zero-slash/IBMCourierZeroSlash%sfd: sfd/IBMCourier%sfd Makefile bin/zeroslash.py
	mkdir -p $(<D)
	bin/zeroslash.py --char zeroslash "$<" "$@.tmp.sfd"
	mv "$@.tmp.sfd" "$@"

clean:
	/bin/rm $(SFD_ZERO_SLASH) $(SFD_ZERO_DOT) $(TTF) $(WOFF) $(WOFF2) $(SVG) $(OTF) >/dev/null 2>/dev/null || true
