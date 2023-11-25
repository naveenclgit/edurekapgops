from fuel import convert, gauge
import pytest

def main():
    test_convertgauge()

def test_convertgauge():
    assert convert("3/4") == 75 and  gauge(75) == "75%"
    assert convert("1/4") == 25 and  gauge(25) == "25%"
    assert convert("4/4") == 100 and gauge(100) == "F"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("0/4") == 0 and gauge(0) == "E"
    assert convert("1/100") == 1 and gauge(1) == "E"
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('cat/dog')

if __name__ == "__main__":
    main()