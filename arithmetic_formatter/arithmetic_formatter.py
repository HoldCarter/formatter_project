import operator


def arithmetic_arranger(problems: list[str], need_result=False) -> str:
    operand_1 = problems.split()[0]
    operator = problems.split()[1]
    operand_2 = problems.split()[2]
    lenght_exp = (max(len(operand_1), len(operand_2)) + 2)
    second_line = operator + ' ' + operand_2.rjust(lenght_exp - 2)
    separator = '-' * lenght_exp
    res_exp = str(result_exp(problems)).rjust(lenght_exp)

    result = f'{operand_1.rjust(lenght_exp)}\n{second_line}\n{separator}'
    if need_result:
        result += f'\n{res_exp}'

    # first_line = ''
    # second_line = ''
    # third_line = ''
    # fourth_line = 
    
    # for element in problems:
    #     first_line += f'{element.split()[0]} '

    # return res


    return result
    

def result_exp(expression:str) -> int:
    lst_exp = expression.split()
    if lst_exp[1] == '+':
        result = operator.add(int(lst_exp[0]), int(lst_exp[2]))
    else:
        result = operator.sub(int(lst_exp[0]), int(lst_exp[2]))

    return result
    




test_case_0 = '300 - 8550000'
test_case_1 = ['3 + 855']
test_case_2 = ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']

# print(arithmetic_arranger(test_case_0, True))


def first_line(problems: list[int], separator=' ', spaces_count=4):
    res = ''
    for element in problems:
        slot = length_of_expression(element)
        need_area = separator * spaces_count
        res += f'{element.split()[0].rjust(slot)}{need_area}'

    return res

def line_formatter():
    '''Функция формирует строку
    '''
    
    pass


def length_of_expression(expression: str):
    return len(max(expression.split())) + 2


# print(length_of_expression(test_case_0))
print(first_line(test_case_2))