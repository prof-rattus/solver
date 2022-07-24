from equation_solver.rational import Rational


class Polynomial():
    """
      This class represents the mathematical concept of the polynomial expression.
    """
    def __init__(self, l):
        self.l = l 
        for i in self.l[::-1]:
            if i == 0:
                self.l.pop()
            else:
                break
    def __getitem__(self, key):
        return self.l[key]
    def __len__(self):
        return len(self.l)

    def __add__(self, b):
        r = []
        for i in range(max(len(self), len(b))):
            if len(self) <= i:
                r.append(b[i])
            elif len(b) <= i:
                r.append(self[i])
            else:
                r.append(self[i] + b[i])
        return Polynomial(r)
    
    def __sub__(self, b):
        r = []
        for i in range(max(len(self), len(b))):
            if len(self) <= i:
                r.append(b[i] * (-1))
            elif len(b) <= i:
                r.append(self[i])
            else:
                r.append(self[i] - b[i])
        return Polynomial(r)
    def shift(self, n):
        """
        This mehtod adds the nessesary zeroes.

        Parameters
        -----------
        self, n

        Returns
        ----------
        list representing Polynomial

        """
        b = [0] * n
        b.extend(self.l)
        return Polynomial(b)
    def __str__(self):
        r = []
        for i, k in enumerate(self.l):
            r.append(f"{k}x^{i}")
        return " + ".join(r)
    def __mul__(self, b):
        res = Polynomial([])
        for i1, c1 in enumerate(self.l):
            for i2, c2 in enumerate(b.l):
                res += Polynomial([c1 * c2]).shift(i1 + i2)
        return res
    def __pow__(self, b):
        if not isinstance(b, Rational):
            raise Exception("Invalid.")
        b = b.reduce()
        if b.b != 1:
            raise Exception("Invalid.")

        res = Polynomial([1])    
        for _ in range(b.a):
            res = self * res
        return res  
    def __truediv__(self, b):
        if isinstance(b, Polynomial) and len(b) == 1:
            b = Rational(b[0])
        elif not isinstance(b, Rational):
            raise Exception("Not Rational.") 
        b = Rational(b.b, b.a).poly()
        return self * b
