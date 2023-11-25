from working import convert
import pytest


def main():
    test_convert_format()
    test_convert_value()
    test_convert_hour()
    test_convert_minute()
    test_convert_formato()

def test_convert_format():
    with pytest.raises(ValueError):
        convert('8 AM - 4 PM')
        convert('8 AM to 4PM')
        convert('8AM : 4 PM')

def test_convert_value():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_convert_hour():
    with pytest.raises(ValueError):
         convert('09:00 AM to 25:00 PM')

def test_convert_minute():
    with pytest.raises(ValueError):
         convert('9:60 AM to 5:60 PM')

def test_convert_formato():
    with pytest.raises(ValueError):
        convert('8 AM 4 PM')

def test_convert_houroor():
    with pytest.raises(ValueError):
        convert('10:00 to 25:00')

