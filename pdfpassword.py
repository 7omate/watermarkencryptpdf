#!/usr/bin/python
# coding: utf-8

import os, sys, argparse, re
from Quartz import PDFDocument, kCGPDFContextAllowsCopying, kCGPDFContextAllowsPrinting, kCGPDFContextUserPassword, kCGPDFContextOwnerPassword
from CoreFoundation import (NSURL)

parser = argparse.ArgumentParser(description='Create a protected PDF')
parser.add_argument('-i', '--input', type=str, dest='filename', action='store',
                    help='input PDF file that will be protected')
parser.add_argument('-o', '--output', type=str, dest='outfile', action='store',
                    help='output PDF file that is protected')
parser.add_argument('-p', '--password', dest='copyPassword', action='store',
                    help='password used to protect PDF')
parser.add_argument('-q', '--quiet', dest='quiet', action='store', default=False,
                    help='silence output after creating file')

args = parser.parse_args()
#print(args)
try:
    args.copyPassword
    args.filename
    if args.copyPassword is None or args.filename is None:
        raise Exception()
    if args.outfile is None:
        raise Exception()
except:
    parser.print_help()
    exit(-1)

#copyPassword = "12345678" # Password for copying and printing
openPassword = args.copyPassword # Password to open the file.
# Set openPassword as '' to allow opening with no password.

def encrypt(filename):
    filename =filename.decode('utf-8')
    if not filename:
        print 'Unable to open input file'
        sys.exit(2)
    #shortName = os.path.splitext(filename)[0]
    #outputfile = shortName+" locked.pdf"
    pdfURL = NSURL.fileURLWithPath_(filename)
    pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
    if pdfDoc :
        options = {
            kCGPDFContextAllowsCopying: False,
            kCGPDFContextAllowsPrinting: False,
            kCGPDFContextOwnerPassword: args.copyPassword,
            kCGPDFContextUserPassword: openPassword}
        pdfDoc.writeToFile_withOptions_(args.outfile, options)
    return

if __name__ == "__main__":
    if not args.quiet:
        print("Created {} with {}".format(args.outfile, args.copyPassword))
    encrypt(args.filename)
