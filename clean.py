#!/usr/bin/env python3 
import os
import shutil
import sys
import glob

def clean(name):
    os.rename(f'{name}.cell', f'tmp_{name}.cell')
    os.rename(f'{name}.param', f'tmp_{name}.param')
    for f in glob.glob(f'{name}*'):
        os.remove(f)
    os.rename(f'tmp_{name}.cell', f'{name}.cell',)
    os.rename(f'tmp_{name}.param', f'{name}.param',)

if __name__ == '__main__':
    arg = sys.argv[1]
    clean(arg)
