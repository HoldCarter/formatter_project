import operator

# def first_line(problems: list[str]):
#     res = ''
#     for element in problems:
#         slot = length_of_expression(element)
#         res += f'{element.split()[0].rjust(slot)}{free_area()}'

#     return res[:-4]


# def second_line(problems: list[str]):
#     res = ''
#     for element in problems:
#         slot = length_of_expression(element)
#         res += f'{element.split()[1]} {element.split()[2].rjust(slot - 2)}{free_area()}'
    
#     return res[:-4]


# def third_line(problems):
#     res = ''
#     for el in problems:
#         slot = length_of_expression(el)
#         res += '-' * slot + free_area()
    
#     return res[:-4]


# def fourth_line(problems):
#     res = ''
#     for el in problems:
#         slot = length_of_expression(el)
#         res += result_exp(el).rjust(slot) + free_area()
#     return res[:-4]

def result_expression(expression:str) -> int:
    lst_exp = expression.split()
    if lst_exp[1] == '+':
        result = operator.add(int(lst_exp[0]), int(lst_exp[2]))
    else:
        result = operator.sub(int(lst_exp[0]), int(lst_exp[2]))

    return str(result)


def space_bw_problem(separator=' ', space_count=4):
    res = separator * space_count
    return res

def arithmetic_arranger(problems: list[str], need_result=False) -> str:
    first_line = ''
    second_line = ''
    third_line = ''
    result_line = ''
    result = ''
    free_space = space_bw_problem()

    for problem in problems:
        slot = length_of_expression(problem)
        operand_1 = problem.split()[0].rjust(slot)
        operator =  problem.split()[1]
        operand_2 = problem.split()[2].rjust(slot)
        first_line += operand_1
        second_line += f'{operator} {operand_2}'
        third_line += f"{'-' * slot}"
        result_line += result_expression(problem).rjust(slot)
    
    result = [first_line, second_line, third_line, result_line]
    if need_result:
        return '\n'.join(result[:-1])
    return '\n'.join(result)


def length_of_expression(expression: str):
    return len(max(expression.split())) + 2


# def formatter(expression):
#     print(first_line(expression), second_line(expression), third_line(expression), fourth_line(expression), sep='\n')


test_case = ['148 + 3033','3536 - 868', '4143 + 23234']
print(arithmetic_arranger(test_case))

# formatter(test_case)