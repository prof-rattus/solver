from equation_solver import AST


from equation_solver.eqaution import Equation




while True:
    inp = input("Please write the equation or any expression, you want to be solved:\n")
    a = AST(inp).parse()
    if isinstance(a, Equation):
        s = a.solve()
        for i in s:
            print("Solution:", i.eval())
    else:
        print(a.eval())

