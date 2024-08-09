#!/usr/bin/env python3 
from ase.io import read, write
import sys

def traj2extxyz(name, index=':'):
    try:
        traj = read(f'{name}.traj', index=str(index))
    except:
        traj = read(f'{name}', index=str(index))
        name = name[0:-5]    
    write(f'{name}.extxyz', traj)

if __name__ == "__main__":
    name = sys.argv[1]
    try:
        if sys.argv[2] != None:
            index = sys.argv[2]
            traj2extxyz(name, index)
    except:
        traj2extxyz(name)  
