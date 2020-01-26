"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys

def test_molecular_mass(test_molecule):
    symbols = ['C', 'H', 'H', 'H', 'H']
    
    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = molecool.atom_data.atom_weights['C'] + molecool.atom_data.atom_weights['H'] +\
         molecool.atom_data.atom_weights['H'] + molecool.atom_data.atom_weights['H'] + molecool.atom_data.atom_weights['H']
    
    assert actual_mass == calculated_mass



def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules
