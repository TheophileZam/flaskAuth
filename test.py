from project import create_app,functions
import pytest
import random

random.seed(1)

def test_function():
    name = "Théophile"
    integ = random.randint(0,100)
    assert functions.format_name(name) == name + " du 62"