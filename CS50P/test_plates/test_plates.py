from plates import is_valid

def test_validity():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("50CS") == False
    assert is_valid("C05S") == False

def test_validity_begalph():
    assert is_valid("CS") == True
    assert is_valid("1C") == False
    assert is_valid("C1") == False
    assert is_valid("11") == False



