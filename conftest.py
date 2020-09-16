'''
Created on 16 Sep 2020

@author: peter
'''

import pytest

@pytest.fixture
def my_fixture():
    return 42

""" Ex of a fixture using a fixture, capsys is called/used
here also so that 'hello' is captured. This is how hello and
more are captured in out """
@pytest.fixture
def captured_print(capsys):
    """ hello here does not go to stdout, instead goes to
    the capsys fixture """
    print("hello")
    