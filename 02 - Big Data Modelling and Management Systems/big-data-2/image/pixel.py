#!/usr/bin/python

from PIL import Image
import sys

im = Image.open(sys.argv[1])
pix = im.load()
print pix[int(sys.argv[2]), int(sys.argv[3])]
