# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:15:33 2020

@author: masou
"""
import unittest
import numpy as np
from Molecule import Molecule
from Benzene import benzene

class Test(unittest.TestCase):
    def test_0(self):
        assert Molecule
        assert Molecule.find_bond_order
        assert Molecule.find_deloc_energy
        assert Molecule.find_charge_density
        assert Molecule.find_nodes
        assert Molecule.set_constants
        assert Molecule.generate_eigen
        assert Molecule.generate_H
        assert Molecule.energy_level_plot
        assert Molecule.delete_connections
        assert Molecule.add_connections
        assert Molecule.__str__
        assert Molecule.__init__

    def test_name(self):
        self.assertAlmostEqual(benzene.name, "Benzene")
        
    def test_type_1(self):
        self.assertRaises(TypeError, benzene.name, True)
        
    def test_deloc_energy_value(self):
        self.assertAlmostEqual(benzene.deloc_energy, -2.00000001)
        
    def test_type_2(self):
        self.assertRaises(TypeError, benzene.deloc_energy, True)
        
if __name__ == "__main__":
    unittest.main()

#%%

import Benzene
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given


@given(beta=st.integers(-1, Benzene.benzene.beta))
@settings(max_examples=1)
def test_beta(beta):
    model = Benzene.benzene.beta
    assert model == -1
    abs_model = np.abs(model)
    assert abs_model.all() == 1

@given(alpha=st.integers(0, Benzene.benzene.alpha))
@settings(max_examples=1)
def test_alpha(alpha):
    model = Benzene.benzene.alpha
    assert model == 0
    abs_model = np.abs(model)
    assert abs_model.all() == 0

if __name__ == "main":
    pass







