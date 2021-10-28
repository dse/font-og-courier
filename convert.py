#!/usr/bin/env fontforge
# -*- mode: python; coding: utf-8 -*-

import fontforge
import os
from datetime import datetime

now = datetime.now()
os.environ['SOURCE_DATE_EPOCH'] = now.strftime('%s')
if os.environ['USER'] == 'dembry' or os.environ['USER'] == 'dse':
    os.environ['USER'] = 'Darren Embry'

MACSTYLE_BOLD      = 1
MACSTYLE_ITALIC    = 2
MACSTYLE_UNDERLINE = 4
MACSTYLE_OUTLINE   = 8
MACSTYLE_SHADOW    = 16
MACSTYLE_CONDENSED = 32
MACSTYLE_EXTENDED  = 64

extensions = ['ttf', 'otf', 'svg', 'woff', 'woff2']

def roman():
    print('==> sources/cour.pfa <==')
    font = fontforge.open('sources/cour.pfa')
    font.fontname   = 'IBMCourier'
    font.fullname   = 'IBM Courier'
    font.familyname = 'IBM Courier'
    font.italicangle = 0.0
    font.weight = 'Book'

    print("{}".format(font.sfnt_names))
    font.sfnt_names = (
        ('English (US)', 'Family', 'IBM Courier'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'Fullname', 'IBM Courier'),
        ('English (US)', 'PostScriptName', 'IBMCourier'),
    ) + font.sfnt_names
    print("{}".format(font.sfnt_names))

    font.save('sfd/IBM-Courier.sfd')
    for extension in extensions:
        font.generate('fonts/IBM-Courier.' + extension)
def bold():
    print('==> sources/courb.pfa <==')
    font = fontforge.open('sources/courb.pfa')
    font.fontname   = 'IBMCourier-Bold'
    font.fullname   = 'IBM Courier Bold'
    font.familyname = 'IBM Courier'
    font.italicangle = 0.0

    font.sfnt_names = (
        ('English (US)', 'Family', 'IBM Courier'),
        ('English (US)', 'SubFamily', 'Bold'),
        ('English (US)', 'Fullname', 'IBM Courier Bold'),
        ('English (US)', 'PostScriptName', 'IBMCourier-Bold'),
    ) + font.sfnt_names

    font.save('sfd/IBM-Courier-Bold.sfd')
    for extension in extensions:
        font.generate('fonts/IBM-Courier-Bold.' + extension)
def italic():
    print('==> sources/couri.pfa <==')
    font = fontforge.open('sources/couri.pfa')
    font.fontname   = 'IBMCourier-Italic'
    font.fullname   = 'IBM Courier Italic'
    font.familyname = 'IBM Courier'
    font.italicangle = -12.0
    font.weight = 'Book'

    font.sfnt_names = (
        ('English (US)', 'Family', 'IBM Courier'),
        ('English (US)', 'SubFamily', 'Italic'),
        ('English (US)', 'Fullname', 'IBM Courier Italic'),
        ('English (US)', 'PostScriptName', 'IBMCourier-Italic'),
    ) + font.sfnt_names

    font.save('sfd/IBM-Courier-Italic.sfd')
    for extension in extensions:
        font.generate('fonts/IBM-Courier-Italic.' + extension)
def boldItalic():
    print('==> sources/courbi.pfa <==')
    font = fontforge.open('sources/courbi.pfa')
    font.fontname   = 'IBMCourier-BoldItalic'
    font.fullname   = 'IBM Courier Bold Italic'
    font.familyname = 'IBM Courier'
    font.italicangle = -12.0

    font.sfnt_names = (
        ('English (US)', 'Family', 'IBM Courier'),
        ('English (US)', 'SubFamily', 'Bold Italic'),
        ('English (US)', 'Fullname', 'IBM Courier Bold Italic'),
        ('English (US)', 'PostScriptName', 'IBMCourier-BoldItalic'),
    ) + font.sfnt_names

    font.save('sfd/IBM-Courier-Bold-Italic.sfd')
    for extension in extensions:
        font.generate('fonts/IBM-Courier-Bold-Italic.' + extension)

roman()
bold()
italic()
boldItalic()
