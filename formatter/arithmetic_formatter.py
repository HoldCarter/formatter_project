from formatter.calculate import result_expression

def length_of_expression(operand_1, operator, operand_2, result):
    return max(map(len, [operand_1, operator, operand_2, result])) + 2


def expression_definder(expression: str):
    symbols = ["-", "+", "/", '*']
    
    for symbol in symbols:
        if symbol in expression:
            operator = symbol
    operand_1, operand_2 = expression.split(operator)
    operand_1 = operand_1.strip()
    operand_2 = operand_2.strip()
    return operand_1, operator, operand_2

    
def arithmetic_merger(problems: list[str], need_result=True) -> str:

    first_line = []
    second_line = []
    third_line = []
    result_line = []
    res_total = []
    space_bw_problem = ' ' * 4

    for problem in problems:
        try:
            operand_1, operator, operand_2 = expression_definder(problem)
            result = result_expression(operand_1, operator, operand_2)
            slot = length_of_expression(operand_1, operator, operand_2, result)
            first_line.append(operand_1.rjust(slot))
            second_line.append(f'{operator.ljust(2)}{operand_2.rjust(slot - 2)}')
            third_line.append(f"{'-' * slot}")
            result_line.append(result.rjust(slot))
        except Exception:
            return "Error: Numbers must only contain digits and operator must be '+', '-', '/' or '*'. And don't divide by zero"    

    if need_result:
        lines_combain = [first_line, second_line, third_line, result_line]
    else:
        lines_combain = [first_line, second_line, third_line]

    for line in lines_combain:
        res_total.append(f'{space_bw_problem}'.join(line))

    return '\n'.join(res_total)
