#!/usr/bin/env python3

import sys
import os
import inspect
import subprocess

# add new contributed icon set folders to list
# everything except material--which is special-cased
contributed = ['legacy']

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
working_dir = os.path.join(parentdir, 'src')
sys.path.insert(0, working_dir)

build_dir = os.path.join(working_dir, 'build')

for iconset in contributed:
    src_dir = os.path.join(working_dir, iconset)
    command = ['rcc',
            '--binary',
            '--output',
            '{}.rcc'.format(os.path.join(build_dir, iconset)),
            '{}.qrc'.format(os.path.join(src_dir, iconset)),
            ]
    proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if proc.returncode:
        exit(-1)


from ChangeMaterialThemeColor import color_dict, ChangeTheme as ct

material_src_dir = os.path.join(working_dir, 'material')
for color in color_dict.keys():
    new_dir = os.path.join(working_dir, 'material-{}'.format(color))
    os.mkdir(new_dir)
    rcc_file = os.path.join(working_dir, 'build', 'material-{}.rcc'.format(color))
    qrc_file = os.path.join(new_dir, 'material-{}.qrc'.format(color))
    new_ct = ct(color, new_dir, material_src_dir)
    new_ct.changeColor()
    command = ['rcc',
            '--binary',
            '--output',
            '{}'.format(rcc_file),
            '{}'.format(qrc_file),
            ]
    print(command)
    proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if proc.returncode:
        exit(-1)
