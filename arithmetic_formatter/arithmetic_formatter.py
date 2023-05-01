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
    if len(problems) > 5:
        return 'Error: Too many problems.'
    first_line = []
    second_line = []
    third_line = []
    result_line = []
    result = []

    for problem in problems:
        
        slot = length_of_expression(problem)
        operand_1 = problem.split()[0]
        operator = problem.split()[1]
        if operator[0] not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        operand_2 = problem.split()[2]

        if not operand_1.isdigit() or not operand_2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(operand_1) > 4 or len(operand_2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_line.append(operand_1.rjust(slot))
        second_line.append(f'{operator.ljust(2)}{operand_2.rjust(slot - 2)}')
        third_line.append(f"{'-' * slot}")
        result_line.append(result_expression(problem).rjust(slot))

    if need_result:
        lines_combain = [first_line, second_line, third_line, result_line]
    else:
        lines_combain = [first_line, second_line, third_line]

    for line in lines_combain:
        result.append(f'{space_bw_problem()}'.join(line))

    return '\n'.join(result)


test_case = ['148 + 3033','3536 - 868', '4143 + 3234']
print(arithmetic_arranger(test_case))
