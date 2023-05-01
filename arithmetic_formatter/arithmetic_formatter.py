import operator


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


def length_of_expression(expression: str):
    return max(map(len, expression.split())) + 2


def arithmetic_arranger(problems: list[str], need_result=True) -> str:
    first_line = []
    second_line = []
    third_line = []
    result_line = []
    result = []

    for problem in problems:
        slot = length_of_expression(problem)
        operand_1 = problem.split()[0].rjust(slot)
        operand_2 = f'{problem.split()[1]} {problem.split()[2]}'.rjust(slot)
        first_line.append(operand_1)
        second_line.append(f'{operand_2}')
        third_line.append(f"{'-' * slot}")
        result_line.append(result_expression(problem).rjust(slot))


    if need_result:
        lines_combain = [first_line, second_line, third_line, result_line]
    else:
        lines_combain = [first_line, second_line, third_line]

    for line in lines_combain:
            result.append(f'{space_bw_problem()}'.join(line))

    return '\n'.join(result)


test_case = ['148 + 3033','3536 - 868', '4143 + 23234']
print(arithmetic_arranger(test_case))
