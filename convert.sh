#!/usr/bin/env bash
set -o errexit
set -o pipefail
set -o nounset

mkdir -p sfd

export SOURCE_DATE_EPOCH="$(date +%s)"
if [[ "$USER" = "dembry" ]] || [[ "$USER" = "dse" ]] ; then
    export USER="Darren Embry"
fi

ffconvert --font-name='IBMCourier'              \
          --full-name='IBM Courier'             \
          --family-name='IBM Courier'            \
          --weight='Regular'                    \
          sources/cour.pfa                      \
          sfd/IBM-Courier.sfd                   \
          fonts/IBM-Courier.svg                 \
          fonts/IBM-Courier.ttf                 \
          fonts/IBM-Courier.otf                 \
          fonts/IBM-Courier.woff                \
          fonts/IBM-Courier.woff2
ffconvert --font-name='IBMCourier-Bold'         \
          --full-name='IBM Courier Bold'        \
          --family-name='IBM Courier'            \
          --weight='Bold'                       \
          sources/courb.pfa                     \
          sfd/IBM-Courier-Bold.sfd              \
          fonts/IBM-Courier-Bold.svg            \
          fonts/IBM-Courier-Bold.ttf            \
          fonts/IBM-Courier-Bold.otf            \
          fonts/IBM-Courier-Bold.woff           \
          fonts/IBM-Courier-Bold.woff2
ffconvert --font-name='IBMCourier-Italic'       \
          --full-name='IBM Courier Italic'      \
          --family-name='IBM Courier'            \
          --weight='Regular'                    \
          sources/couri.pfa                     \
          sfd/IBM-Courier-Italic.sfd            \
          fonts/IBM-Courier-Italic.svg          \
          fonts/IBM-Courier-Italic.ttf          \
          fonts/IBM-Courier-Italic.otf          \
          fonts/IBM-Courier-Italic.woff         \
          fonts/IBM-Courier-Italic.woff2
ffconvert --font-name='IBMCourier-BoldItalic'   \
          --full-name='IBM Courier Bold Italic' \
          --family-name='IBM Courier'            \
          --weight='Bold'                       \
          sources/courbi.pfa                    \
          sfd/IBM-Courier-Bold-Italic.sfd       \
          fonts/IBM-Courier-Bold-Italic.svg     \
          fonts/IBM-Courier-Bold-Italic.ttf     \
          fonts/IBM-Courier-Bold-Italic.otf     \
          fonts/IBM-Courier-Bold-Italic.woff    \
          fonts/IBM-Courier-Bold-Italic.woff2
