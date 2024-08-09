#!/usr/bin/env python3 
import sys
from ase.io import write, read
from os import environ

castep_cmd = "/home/diamond/phrfzk/castep.mpi"
environ["CASTEP_COMMAND"] = castep_cmd
from ase.calculators.castep import Castep
Castep.castep_keywords = "/home/diamond/phrfzk/scripts/castep_keywords.json"

def geom2cell(name, index='-1'):
    try:
        traj = read(f'{name}.geom', index=str(index))
    except:
        traj = read(f'{name}', index=str(index))
        name = name[0:-5]    
    write(f'{name}_relaxed.cell', traj)

if __name__ == "__main__":
    name = sys.argv[1]
    try:
        if sys.argv[2] != None:
            index = sys.argv[2]
            geom2cell(name, index)
    except:
        geom2cell(name)  
