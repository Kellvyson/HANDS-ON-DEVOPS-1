import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.calculadora import soma

def test_soma():  
    assert soma(2, 3) == 5  
    assert soma(-1, 1) == 0  
    assert soma(0, 0) == 0

def test_soma_numeros_grandes():
    assert soma(100, 200) == 300

def test_soma_numeros_negativos():
    assert soma(-5, -3) == -8
