#!/usr/bin/env python
# Author: Andrés Barriga Mozo
# License: Open Source based, so open source distribution.
import sys
import pdfkit
from barcode import Code128
from barcode.writer import ImageWriter

BARCODE_OPTIONS = {
    'font_size': 12,
    'text_distance': 2.0
}

PDF_OPTIONS = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

def main():
    if len(sys.argv) >= 2:
        ns = str(sys.argv[1])
        # Generación del código de barras
        with open('imgs/barcode.png', 'wb') as f:
            Code128(ns, writer=ImageWriter()).write(f, options=BARCODE_OPTIONS)

        # Generación el pdf desde el template
        pdfkit.from_file('template.html', "etiquetas/" + ns + ".pdf", options=PDF_OPTIONS)


if __name__ == '__main__':
    main()
