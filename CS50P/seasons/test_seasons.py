from seasons import dob_validate, convert2min
import pytest

def main():
    test_dob_validate()
    test_convert2min()

def test_dob_validate():
    assert dob_validate("1978-01-23") == dict({"date": '23', "month": '01', "year": '1978'})
    with pytest.raises(SystemExit):
         dob_validate("1978-1-3")
    with pytest.raises(SystemExit):
        dob_validate("January 1, 1999")

#def test_convert2min():
    #Should change the asserted value daily
#    assert convert2min(dict({"date": '23', "month": '01', "year": '1978'})) == "Twenty-three million, nine hundred fifty-four thousand, four hundred minutes"


if __name__ == "__main__":
    main()