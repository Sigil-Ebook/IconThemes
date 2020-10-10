#!/usr/bin/env python3

import sys
import os

color_original = '#1abc9c'
color_dict = {
    'blue'    : '#27AAE1',
    'gray'    : '#888888',
    'lilac'   : '#B978D8',
    'orange'  : '#DA8100',
    'pink'    : '#D33F81',
    'red'     : '#DC143C'
}

def print_usage():
    print("Usage: python3 ./ChangeMaterialThemeColor.py COLOR DESTINATION")
    print("  where:  ")
    print("    COLOR       is one of 'blue', 'gray', 'lilac', 'orange', 'pink', or 'red'")
    print("                or a single 6 digit hex color value prefaced with #")
    print(" ")
    print("    DESTINATION is path to an empty folder to populate")

class ChangeTheme:
    def __init__(self, cname, dest, src='material'):
        self.cname = cname
        self.src = os.path.abspath(src)
        self.destination = os.path.abspath(dest)

    def changeColor(self):
        if self.cname.startswith('#'):
            new_color = self.cname
            self.cname = self.cname[1:]
        else: # has to be one of the usable colors at this point 
            new_color = color_dict[self.cname]
        for root, dires, files in os.walk(self.src):
            for filename in files:
                if filename.endswith('.svg'):
                    print("  ... processing: ", filename)
                    data = ''
                    with open(os.path.join(self.src, filename), 'rb') as f:
                        data = f.read()
                    data = data.decode('utf-8')
                    data = data.replace(color_original, new_color)
                    data = data.encode('utf-8')
                    with open(os.path.join(self.destination, filename), 'wb') as fo:
                        fo.write(data)
                elif filename == 'material.qrc':
                    newname = 'material-' + self.cname + '.qrc' 
                    print("  ... processing: ", newname)
                    data = b''
                    with open(os.path.join(self.src, filename), 'rb') as fi:
                        data = fi.read()
                    with open(os.path.join(self.destination, newname), 'wb') as fq:
                        fq.write(data)

    
def main():
    argv = sys.argv
    if len(argv) != 3:
        print_usage()
        return -1
    if argv[1].startswith('#') and len(argv[1]) != 7:
        print_usage()
        return -1
    elif not argv[1].startswith('#') and argv[1] not in color_dict:
        print_usage()
        return -1
    if not os.path.isdir(argv[2]):
        print_usage()
        return -1

    change = ChangeTheme(argv[1], argv[2])
    change.changeColor()

    print("Done")
    return 0

if __name__ == '__main__':
    sys.exit(main())

