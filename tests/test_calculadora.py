# tests/test_calculadora.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.calculadora import soma

def test_soma():  
    assert soma(2, 3) == 5  
    assert soma(-1, 1) == 0  
    assert soma(0, 0) == 0
