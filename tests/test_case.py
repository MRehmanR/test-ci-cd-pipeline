from main import detect_type


def test_integer():
    assert detect_type("123") == "Integer"


def test_float():
    assert detect_type("3.14") == "Float"


def test_boolean():
    assert detect_type("true") == "Boolean"


def test_character():
    assert detect_type("A") == "Character"


def test_string():
    assert detect_type("Hello World") == "String"
