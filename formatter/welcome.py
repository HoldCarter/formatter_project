def welcome_user():
    print("""Welcome to the Arithmetic Formatter!
Please enter expressions, split by button 'Enter'.
Maximum number of expressions is 10.
When you're done, press 'Enter' twice.""")
    problems = []
    for _ in range(10):
        exp = input()
        if exp == '':
            break
        problems.append(exp)
    return problems
