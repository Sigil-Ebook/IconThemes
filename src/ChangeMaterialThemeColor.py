#!/usr/bin/env python3

import sys
import os

color_original = '#1abc9c'
color_blue = '#27AAE1'
color_gray = '#888888'
color_lilac = '#B978D8'
color_orange = '#DA8100'
color_pink = '#D33F81'
color_red = '#DC143C'

color_names = ['blue', 'gray', 'lilac', 'orange', 'pink', 'red']

def print_usage():
    print("Usage: python3 ./ChangeMaterialThemeColor.py COLOR DESTINATION")
    print("  where:  ")
    print("    COLOR       is one of 'blue', 'gray', 'lilac', 'orange', 'pink', or 'red'")
    print("                or a single 6 digit hex color value prefaced with #")
    print(" ")
    print("    DESTINATION is path to an empty folder to populate")
    
def main():
    argv = sys.argv
    if len(argv) != 3:
        print_usage()
        return -1
    if argv[1].startswith('#') and len(argv[1]) != 7:
        print_usage()
        return -1
    elif not argv[1].startswith('#') and argv[1] not in color_names:
        print_usage()
        return -1
    if not os.path.isdir(argv[2]):
        print_usage()
        return -1

    destination = argv[2]
    cname = argv[1]

    new_color = color_original

    if cname.startswith('#'):
        new_color = cname
        cname = cname[1:]
    elif cname == 'blue':
        new_color = color_blue
    elif cname == 'gray':
        new_color = color_gray
    elif cname == 'lilac':
        new_color = color_lilac
    elif cname == 'orange':
        new_color = color_orange
    elif cname == 'pink':
        new_color = color_pink
    elif cname == 'red':
        new_color = color_red
        
    for root, dires, files in os.walk('material'):
        for filename in files:
            if filename.endswith('.svg'):
                print("  ... processing: ", filename)
                data = ''
                with open(os.path.join('material', filename), 'rb') as f:
                    data = f.read()
                data = data.decode('utf-8')
                data = data.replace(color_original, new_color)
                data = data.encode('utf-8')
                with open(os.path.join(destination, filename), 'wb') as fo:
                    fo.write(data)
            elif filename == 'material.qrc':
                newname = 'material-' + cname + '.qrc' 
                print("  ... processing: ", newname)
                data = b''
                with open(os.path.join('material', filename), 'rb') as fi:
                    data = fi.read()
                with open(os.path.join(destination, newname), 'wb') as fq:
                    fq.write(data)
    print("Done")
    return 0

if __name__ == '__main__':
    sys.exit(main())

