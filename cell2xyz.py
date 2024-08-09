#!/usr/bin/env python3 
import sys
from ase.io import write, read
from os import environ

castep_cmd = "/home/diamond/phrfzk/castep.mpi"
environ["CASTEP_COMMAND"] = castep_cmd
from ase.calculators.castep import Castep
Castep.castep_keywords = "/home/diamond/phrfzk/scripts/castep_keywords.json"


def xyz2cell(arg1):
    try:
        file = read(f"{arg1}.cell")
    except:
        file = read(f"{arg1}")
        arg1 = arg1[0:-5]
    write(f"{arg1}.xyz", file, format='xyz')

if __name__ == "__main__":
    arg1 = sys.argv[1]
    xyz2cell(arg1)    
