from project import create_app,functions
from flask_testing import LiveServerTestCase
import pytest
import random

random.seed(1)

def test_function():
    name = "Théophile"
    integ = random.randint(0,100)
    assert functions.format_name(name) == name + " du 62"
1

class TestUserTakesTheTest(LiveServerTestCase):
    def test_user_login(self):
        # On ouvre le navigateur avec l'adresse du serveur.
        self.driver.get(self.get_server_url())
        # L'adresse dans l'url doit être celle que l'on attend.
        assert self.driver.current_url == 'https://auth-deploiement.azurewebsites.net/'