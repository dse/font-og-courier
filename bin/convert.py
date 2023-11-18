#!/usr/bin/env fontforge
# -*- mode: python; coding: utf-8 -*-

import fontforge
import os
import re
import string

def convert(source, dests):
    print("Reading %s" % source)
    font = fontforge.open(source)
    lastDest = None
    for dest in dests:
        print("< dest = %s" % dest)
        if re.fullmatch(r'^\.[A-Za-z0-9]+$', dest):
            if lastDest is None:
                raise Exception("first filename cannot be an extension: %s" % dest)
            else:
                dest = os.path.splitext(lastDest)[0] + dest
        print("> dest = %s" % dest)
        if os.path.splitext(dest)[1] == ".sfd":
            print("Writing %s using font.save()" % dest)
            font.save(dest)
        else:
            print("Writing %s using font.generate()" % dest)
            font.generate(dest)
        lastDest = dest

convert("sfd/IBM-Courier-Bold-Italic.sfd", ["fonts/IBM-Courier-Bold-Italic.ttf",
                                            ".otf", ".svg", ".woff", ".woff2"])
convert("sfd/IBM-Courier.sfd",             ["fonts/IBM-Courier.ttf",
                                            ".otf", ".svg", ".woff", ".woff2"])
convert("sfd/IBM-Courier-Italic.sfd",      ["fonts/IBM-Courier-Italic.ttf",
                                            ".otf", ".svg", ".woff", ".woff2"])
convert("sfd/IBM-Courier-Bold.sfd",        ["fonts/IBM-Courier-Bold.ttf",
                                            ".otf", ".svg", ".woff", ".woff2"])
