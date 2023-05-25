import pytest
import os
from formatter.arithmetic_formatter import arithmetic_merger

test_cases = [
    ("test_case_1.txt", "expected_1.txt"), 
    ("test_case_2.txt", "expected_2.txt")
]

def get_path(local_filename):
    return os.path.join('tests/fixtures', local_filename)

@pytest.mark.parametrize("file, expected", test_cases)
def test_arithmetic_merger(file, expected):
    with open(get_path(file)) as test:
        inp = test.readlines()
    with open(get_path(expected)) as res:
        out = res.read()
    assert arithmetic_merger(inp) == out