from jar import Jar
import pytest

def test_init():
    test_str()
    test_deposit()
    test_withdraw()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(11)
    assert jar.size == 11


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(1)
    assert jar.size == 10
