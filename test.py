from project import create_app,format_name
import pytest
import random

random.seed(1)

def test_function():
    name = "Théophile"
    integ = random.randint(0,100)
    assert format_name(name) == name + " du 62"