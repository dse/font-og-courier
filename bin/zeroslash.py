#!/usr/bin/env fontforge
# -*- mode: python; coding: utf-8 -*-

import fontforge
import os
import re
import string
import argparse

def copyChar(font, sourceCharName, destCharName, encoding=-1):
    if not destCharName in font:
        if encoding < 0:
            raise Exception("%s not found and no encoding specified" % destCharName)
        font.createChar(encoding, destCharName)
    if not (sourceCharName in font):
        raise Exception("%s not found" % sourceCharName)
    sourceChar = font[sourceCharName]
    destChar = font[destCharName]
    pen = destChar.glyphPen(replace=True)
    sourceChar.draw(pen)
    pen = None                  # finalize pen drawing
    destChar.width = sourceChar.width
    font.selection.none()
    font.selection[sourceChar.encoding] = True
    font.cut()

def zeroSlashFont(source, dest):
    print("Reading %s" % source)
    font = fontforge.open(source)

    charName = args.char
    copyChar(font, charName, "zero", 48)
    copyChar(font, "l.coding", "l", 108)
    copyChar(font, "asciitilde.coding", "asciitilde", 126)

    if charName == "zerodot":
        font.familyname = "OG Courier Zero Dot"
        font.fontname = font.fontname.replace("OGCourier", "OGCourierZeroDot")
        font.fullname = font.fullname.replace("OG Courier", "OG Courier Zero Dot")
    elif charName == "zeroslash":
        font.familyname = "OG Courier Zero Slash"
        font.fontname = font.fontname.replace("OGCourier", "OGCourierZeroSlash")
        font.fullname = font.fullname.replace("OG Courier", "OG Courier Zero Slash")
    else:
        raise Exception("no --char specified or unsupported --char")

    if os.path.splitext(dest)[1] == ".sfd":
        print("Writing %s using font.save()" % dest)
        font.save(dest)
    else:
        print("Writing %s using font.generate()" % dest)
        font.generate(dest)

parser = argparse.ArgumentParser(prog="zeroslash", description="zero replacer")
parser.add_argument("--char", default="zeroslash")
parser.add_argument("source", help="source font file")
parser.add_argument("dest",   help="destination font file (extension determines format)")

args = parser.parse_args()
zeroSlashFont(args.source, args.dest)
