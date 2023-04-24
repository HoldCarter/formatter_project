from arithmetic_formatter import arithmetic_arranger


test_case = ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']

def test_arithmetic_arranger():
    assert arithmetic_arranger(test_case) == '    3      3801      45      123\n''+ 855    -    2    + 43    +  49\n''-----    ------    ----    -----'