from .operators import Subtraction, Addition, Raise, Division, BinOperator 
from .rational import Rational

class Equation(BinOperator):
    sign = "="
    def eval(self):
        """
        
        This method calles itself recursively,to reduce all the fractiones in the expression and to execute all the expressions.
        
        Parameters
        ------------
        self

        Returns
        -----------
        either:
        request for eval on the particular operators
        or:
        the reduced answer:Rational

        """
        diff = self.a.eval() - self.b.eval()
        return diff.a == 0
    def __str__(self):
        """
        This method is built to print Rational formaatted, so users undestand.

        Parameters
        ------------
        self

        Returns
        -----------
        formatted plausible string represantation of self
        return f"Addition({self.a}, {self.b})"
        """
        return f"Equation({self.a}, {self.b})"
    def solve(self):
        """
        This method solves linear Eqautions

        Parameters
        ------------
        self

        Returns
        -----------
        What x shall be:Rational()

        """
        dif = Subtraction(self.a,  self.b).poly()
        if len(dif) == 2:
            return [-1 * dif[0] / dif[1]]
        elif len(dif) == 1:
            return []
        elif len(dif) == 0:
            return []
        elif len(dif) == 3:
            # x1,2 = (-b +- sqrt(D)) / (2a) = -b / 2a + sqrt(D) / 2a
            # a * x ^ 2 + b * x + c == 0
            # dif[0] * x ^ 0 + dif[1] * x ^ 1 + diff[2] * x ^ 2
            a = dif[2]
            b = dif[1]
            c = dif[0]
            D = b * b  - 4 * a * c

            # D = 3
            # (-4 + 3 ^ (1/2)) / 5
            D = D.value()
            if D < 0:
                return []
            elif D == 0:
                return [-1 * b / (2 * a)]
            else:
                return [Addition(
                    -1 * b / (2 * a),
                    Division(
                        Raise(
                            D,
                            Rational(1, 2)
                        ),
                        2 * a
                    )
                ), Subtraction(
                    -1 * b / (2 * a),
                    Division(
                        Raise(
                            D,
                            Rational(1, 2)
                        ),
                        2 * a
                    ))]
    def lineq(self):
       return Subtraction(self.a, self.b).lineq()

# -2 + 5x + 7y = 0, 3x - 4y = 9

# f1(x, y, ...) = 0,
# f2(x, y, ...) = 0,
# f3(x, y, ...) = 0,
# ....

# x(y) = (-7y + 2) / 5
# x(y, z, ...) = g11, g12

# f2(g12, y, z, ...)
# y(z, ...) = g21, g22
# 

# 3((-7y + 2) / 5) - 4y = 9
# -21y / 5 + 6/5 - 4y = 9
# -21y + 6 - 40y = 45
# -61y = 39
# y = -39 / 61
