#!/usr/bin/env fontforge
# -*- mode: python; coding: utf-8 -*-

import fontforge
import os
import re
import string
import argparse

def convertFont(source, dest):
    print("Reading %s" % source)
    font = fontforge.open(source)
    if os.path.splitext(dest)[1] == ".sfd":
        print("Writing %s using font.save()" % dest)
        font.save(dest)
    else:
        print("Writing %s using font.generate()" % dest)
        font.generate(dest)

parser = argparse.ArgumentParser(prog="convert", description="font converter")
parser.add_argument("source", help="source font file")
parser.add_argument("dest",   help="destination font file (extension determines format)")

args = parser.parse_args()
convertFont(args.source, args.dest)
