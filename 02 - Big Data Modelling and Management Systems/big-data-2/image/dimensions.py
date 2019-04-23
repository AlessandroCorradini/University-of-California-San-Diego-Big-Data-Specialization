#!/usr/bin/python

from PIL import Image
import sys

def getSize(size) :
    return str(size[0]) + ' columns x ' + str(size[1]) + ' rows'

def getMode(mode) :
    if(mode == 'RGB'):
        return '3x8-bit pixels, true colour'
    elif(mode == 'RGBA') :
        return '4x8-bit pixels, true colour with transparency mask'
    elif(mode == 'CMYK') :
        return '4x8-bit pixels, colour separation'
    elif(mode == 'L') :
        return '8-bit pixels, black and white'
    elif(mode == 'P') :
        return '8-bit pixels, mapped to any other mode using a colour palette'
    elif(mode == 'YCbCr') :
        return '3x8-bit pixels, colour video format'
    elif(mode == 'RGBA') :
        return '1-bit pixels, black and white, stored with one pixel per byte'
    elif(mode == 'I') :
        return '32-bit signed integer pixels'
    elif(mode == 'F') :
        return '32-bit floating point pixels'
    else :
        return 'Unknown'

im = Image.open(sys.argv[1])
print 'size = ' + getSize(im.size) 
print 'mode = ' + str(im.mode) + ' ' + getMode(im.mode)
