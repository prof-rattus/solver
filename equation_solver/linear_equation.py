


from .rational import Rational


class LinearEquation:

    def __init__(self, free = 0, descript = {}):
        self.free = free
        self.descript = descript

    def __add__(self, b):
        res = {}

        keys = set([*self.descript.keys(), *b.descript.keys()])
        for i in keys:
            ka = self.descript.get(i, Rational(0))
            kb = b.descript.get(i, Rational(0))
            res[i] = ka + kb
        return LinearEquation(self.free + b.free, res).reduce()

    def __sub__(self, b):
        return self + b * LinearEquation(Rational(-1))

    def reduce(self):
        res = {}
        for i in self.descript:
            if self.descript[i] != Rational(0):
                res[i] = self.descript[i]
        return LinearEquation(self.free, res)


    def __truediv__(self, b):
        if b.descript:
            raise Exception(
                "The result of this division would not be linear.")
        return self * LinearEquation(1 / b.free)

        

    def __mul__(self, b):
        res = {}
        if self.descript and b.descript:
            raise Exception(
                "The result of this multiplication would not be linear.")

        if self.descript:
            eq = self
            free = b.free
        else:
            eq = b
            free = self.free

        for i in eq.descript:
            res[i] = free * eq.descript[i]

        return LinearEquation(free * eq.free, res).reduce()

    def __pow__(self, b):
        if self.descript or b.descript:
            raise Exception(
            "This raise is not going to give a linear result."
            )
        else:
            return LinearEquation(self.free ** b.free)

    def __eq__(self, b):
        return self.descript == b.descript and self.free == b.free

    def __str__(self):
        res = [str(self.free)]
        for i in self.descript:
            res.append(f"{self.descript[i]}{i.x}")
            # if self.descript[i] >= Rational(0):
            #     res =+ f"{self.descript[i]}{i.x}"
            # if self.descript[i] < Rational(0):
            #     res =+ f"({self.descript[i]}{i.x})"

        return "+".join(res)
    
    #>= for Rational method name



# <  __lt__
# <= __le__
# >  __gt__
# >= __ge__
# != __ne__































#                         ,d     
#                         88     
# 8b,dPPYba, ,adPPYYba, MM88MMM  
# 88P'   "Y8 ""     `Y8   88     
# 88         ,adPPPPP88   88     
# 88         88,    ,88   88,    
# 88         `"8bbdP"Y8   "Y888 