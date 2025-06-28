import pytest

def get_random_ingredients(kind=None):
    return ["shells", "gorgonzola", "parsley"]

# Test suite for get_random_ingredients
def test_return_type():
    result = get_random_ingredients()
    assert isinstance(result, list), "The result should be a list"

def test_return_contents():
    result = get_random_ingredients()
    expected = ["shells", "gorgonzola", "parsley"]
    assert result == expected, "The result should match the expected list of ingredients"

def test_return_with_kind_none():
    result = get_random_ingredients(kind=None)
    expected = ["shells", "gorgonzola", "parsley"]
    assert result == expected, "The result should match the expected list of ingredients when kind is None"

def test_return_with_kind_other():
    result = get_random_ingredients(kind="any")
    expected = ["shells", "gorgonzola", "parsley"]
    assert result == expected, "The result should match the expected list of ingredients regardless of kind"

