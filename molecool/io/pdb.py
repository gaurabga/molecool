
"""
pdb.py

function for reading .pdb file

"""
import numpy as np

def open_pdb(file_location):
    """
    For opening a pdb file and returning its symbols and coordinates

    Parameters
    ---------- 
    file_location : str
    
    Return
    ------
    coordinates : np.ndarray
        An array for cartesian coordinates for atoms.
    symbol : list
        A list containing the symbols of atoms.
    """
    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in l[0:6] or 'HETATM' in l[0:6]:
            symbols.append(l[76:79].strip())
            atom_coordinates = [float(x) for x in l[30:55].split()]
            coordinates.append(atom_coordinates)

    # convert list to numpy array
    coordinates = np.array(coordinates)

    return symbols, coordinates



