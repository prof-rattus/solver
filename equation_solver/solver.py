from .eqaution import Equation
from .ast import AST

# Linear equations
# 3x + 4y + z + 0 = 0
#  x -  y - z - 5 = 0
#       y + z - 1 = 0


# [3, "*", "x", "+," 4, "*", "y", "+", "z", "=", 0]
# [3, "*", "x", "+," 4, "*", "y", "+", "z"] [0]

# Addition(
#   Multiplication(3, Variable("x")),
#   Addition(Multiplication(4, Variable("y")), ))
# )
# [3, "*", "x", "+," 4, "*", "y", "+", "z", "-", 0]

# variables: ["x", "y", "z"]
# matrix: [
#   [3, 4, 1, 0],
#   [1, -1, -1, -5],
#   [0, 1, 1, -1]
# ]

## a*x^2 + b*x + c
## [c, b, a]

# 4x + 5y = 0, 5y + 6z = 8, 9z + 4a = 0, 8x = 0
# x = -5y / 4
# y =

class Solver():
    def __init__(self, equations):
        self.equations = equations

    def solve(self):
        res = []
        vars = set()
        for i in self.equations:
            if not isinstance(i, Equation):
                raise Exception("Equation required.")
            lineq = i.lineq()
            res.append(lineq)
            vars.update(lineq.descript.keys())
        if len(vars) != len(self.equations):
            raise Exception("Insolvable")

    def parser(self):
        res = []
        res1 = []
        for i in self.equations:
            single_parse = ""
            for o in i:
                single_parse = + o
                if o == ",":
                    res1.append(single_parse)
                    single_parse = ""
        for i in res1:
            res.append(AST(i).parse.lineq())
        print(res)
        return res


# s = Solver([LinearEquation(), LinearEquation(), ...]).solve()


# 3x + 4y + 5z + 6 = 0
# -x + 2y + 9z - 3 = 0
# 5x +  y + 2z + 1 = 0

# 3x + 4y + 5z + 6 = 0
# 0x + 8y + 9z - 3 = 0
# 0x + 0y + 2z + 1 = 0


# A = B
# k * A = k * B

# C = D

# A + C = A + D
# A + C = B + D


#  k*A + C = k*B + D

# M = [
#   [x0, y0, z0, c0] -> L0,
#   [x1, y1, z1, c1] -> L1,
#   [x2, y2, z2, c2] -> L2
# ]
# L0 * (-x1 / x0) + L1 -> L1
# L0 * (-x2 / x0) + L2 -> L2

# M = [
#   [x0, y0, z0, c0] -> L0,
#   [0,  y1, z1, c1] -> L1,
#   [0,  y2, z2, c2] -> L2
# ]
# L1 * (-y2 / y1) + L2 -> L2

# M = [
#   [x0, y0, z0, c0] -> L0,
#   [0,  y1, z1, c1] -> L1,
#   [0,  0,  z2, c2] -> L2
# ]
# L2 * (-z1/ z2) + L1 -> L1
# L2 * (-z0/ z2) + L0 -> L0

# M = [
#   [x0, y0, 0,  c0] -> L0,
#   [0,  y1, 0,  c1] -> L1,
#   [0,  0,  z2, c2] -> L2
# ]
# L1 * (-y0/ y1) + L0 -> L0

# M = [
#   [x0, 0,  0,  c0] -> L0,
#   [0,  y1, 0,  c1] -> L1,
#   [0,  0,  z2, c2] -> L2
# ]

# [c0/x0, c1/y1, c2/z2]

# l1 ln
# al1 + Ln -> Ln
#a = l1[x c.] / ln[x coefficent]
