from equation_solver import AST
from equation_solver import Solver
from equation_solver.eqaution import Equation


while True:
    inp = input(
        "Please write the equation or any expression, you want to be solved:\n")
    eqs = inp.split(",")
    asts = []
    for i in eqs:
        asts.append(AST(i).parse())

    solver = Solver(asts)
    print(solver.solve())

    # if isinstance(a, Equation):
    #     s = a.solve()
    #     for i in s:
    #         print("Solution:", i.eval())
    # else:
    #     print(a.eval())
