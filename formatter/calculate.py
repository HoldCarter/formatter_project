import operator as op


def add(first_operand, second_operand):
    return op.add(first_operand, second_operand)


def sub(first_operand, second_operand):
    return op.sub(first_operand, second_operand)


def mul(first_operand, second_operand):
    return op.mul(first_operand, second_operand)


def div(first_operand, second_operand):
    if op.mod(first_operand, second_operand) == 0:
        return op.floordiv(first_operand, second_operand)
    else:
        return op.truediv(first_operand, second_operand)


OPERATIONS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def result_expression(first_operand, operator, second_operand):
    num_1 = int(first_operand)
    num_2 = int(second_operand)
    operation = OPERATIONS[operator]
    result = operation(num_1, num_2)
    return str(result)
