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

    return str(result)
    

# print(arithmetic_arranger(test_case_0, True))


def first_line(problems: list[str]):
    res = ''
    for element in problems:
        slot = length_of_expression(element)
        res += f'{element.split()[0].rjust(slot)}{free_area()}'

    return res[:-4]


def second_line(problems: list[str]):
    res = ''
    for element in problems:
        slot = length_of_expression(element)
        res += f'{element.split()[1]} {element.split()[2].rjust(slot - 2)}{free_area()}'
    
    return res[:-4]


def third_line(problems):
    res = ''
    for el in problems:
        slot = length_of_expression(el)
        res += '-' * slot + free_area()
    
    return res[:-4]


def fourth_line(problems):
    res = ''
    for el in problems:
        slot = length_of_expression(el)
        res += result_exp(el).rjust(slot) + free_area()
    return res[:-4]


def free_area(separator=' ', space_count=4):
    res = separator * space_count
    return res

def line_formatter():
    '''Функция формирует строку
    '''
    pass


def length_of_expression(expression: str):
    return len(max(expression.split())) + 2


def formatter(expression):
    print(first_line(expression), second_line(expression), third_line(expression), fourth_line(expression), sep='\n')


test_case = ['148 + 3033','3536 - 868', '4143 + 23234']

formatter(test_case)