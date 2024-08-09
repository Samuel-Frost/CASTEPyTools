#!/usr/bin/env python3 
import sys
import argparse
from ase.io import write, read
from os import environ

castep_cmd = "/home/diamond/phrfzk/castep.mpi"
environ["CASTEP_COMMAND"] = castep_cmd
from ase.calculators.castep import Castep
Castep.castep_keywords = "/home/diamond/phrfzk/scripts/castep_keywords.json"


def xyz2cell(name, spacing, rattle, fix):
    try:
        atoms = read(f"{name}.xyz")
    except:
        atoms = read(f"{name}")
        name = name[0:-4]
    
    atoms.pbc = fix
    atoms.rattle(rattle)
    calc = Castep(kpts=[spacing]*3)
    atoms.calc = calc

    write(f"{name}.cell", atoms, format='castep-cell')
    with open(f'{name}.cell', "a") as file:
        file.write("FIX_ALL_CELL: TRUE\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str)
    parser.add_argument("--spacing", type=int, default = 4)
    parser.add_argument("--rattle", type=float, default = 0)
    parser.add_argument("--fix", type=bool, default = True)
    args = parser.parse_args()
    xyz2cell(args.name, args.spacing, args.rattle, args.fix)   
