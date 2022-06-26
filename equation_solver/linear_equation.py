## variables:      [Variable("x"), Variable("y"), ...]
# coefficients:   [freeConstant, k_x, k_y, ....]

# 2 * x -> Mul(Rat(2), Var("x"))
# Rat(2) -> LE(coef: [2], vars: [])
# Var("x") -> LE(coef: [0, 1], vars: [Var("x")])
# Mul() -> LE(coef: [2], vars: []) * LE(coef: [0, 1], vars: [Var("x")])

# LE(coef: [4, 0], vars: [Var("x")]) -> 4 + 0 * x = 4

# LE(coef: [4, 1, 2], vars: [Var("x")], Var("y")) + LE(coef: [0, 4, 3], vars: [Var("y")], Var("x"))

# LE(coef: [4, 1, 2], vars: [Var("x")], Var("y")) + LE(coef: [0, 4, 3], vars: [Var("y")], Var("z"))
# 4 + x + 2y + 4y + 3z = 4 + x + 6y + 3z ->
# = LE(coef: [4, 1, 6, 3], vars: [Var("x"), Var("y")], Var("z"))

#Idea : nerkayacnel vorpes dict:
# a = {"free":-5, Var(x): 2, Var(y): 3, Var(z): -5}


from numbers import Rational

alphabet = "abcdefghijklmnopqrstuvwxyz"


class LinearEquation3:

    def __init__(self, coef = [],  freeK=Rational(0), vars=None):
        self.freeK = freeK
        if vars is not None:
            self.vars = [vars]
            self.coef = [1]
        else:
            self.vars = []
            self.coef = []

    def __add__(self, b):
        pass
            