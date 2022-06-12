class Rational():
    '''
    Rational class represents rational numbers.
    '''

    def number_to_rational(self, a):
        '''Convert int, float or Rational to Rational

        Parameters
        ----------
        a : int, float, Rational
            the input number to convert
        
        Returns
        -------
        Rational
            the converted rational
        '''
        if type(a) == int:
            return Rational(a)
        elif type(a) == float:
            b = 1
            while (a - int(a) != 0):
                a *= 10
                b *= 10
            return Rational(int(a), int(b))
        return a

    def __init__(self, a, b = 1):
        if type(a) == int and type(b) == int:
            self.a = a
            self.b = b
            return
        
        a = self.number_to_rational(a)
        b = self.number_to_rational(b)
        self.a = a.a * b.b
        self.b = a.b * b.a

    def reduce(self):
        '''
        This method reduces object of Rational() class.Using the Euclides algorithm.

        Parameters
        --------------
        self:Rational

        Returns
        ------------
        raduced self:Rational

        '''
        if self.b == 0:
            raise Exception("You dumb?")
        if self.a == 0:
            return Rational(0)
        if self.a == 1 or self.b == 1:
            return self
        elif self.a == self.b:
            return Rational(1, 1)
        else:
            sign = 1
            if (self.a < 0) != (self.b < 0):
                sign = -1
            a = abs(self.a)
            b = abs(self.b)
            while a != b:
                if a > b:
                    a = a - b
                else:
                    b = b - a
            self.a = abs(self.a)
            self.b = abs(self.b)
            return Rational(self.a / a * sign, self.b / b)
    def __eq__(self, b):
        """
        Compares rationals.
        
        Parameters
        -----------
        self,b:Rational
        
        Returns
        ----------
        bool
        """
        b = Rational(b)
        a = self.reduce()
        b = b.reduce()
        return a.a == b.a and a.b == b.b
    
    def __add__(self, b):
        """
        This method adds Rationals.

        Parameters
        -----------
        self,b:Rational

        Return
        ----------
        self + b:Rational
        """
        a = self
        if type(b) == float or type(b) == int:
            b = Rational(b)
        return Rational(a.a * b.b + a.b * b.a, a.b * b.b).reduce()
    def __sub__(self, b):
        """
        This method subtracts Rationals from another Rationals.

        Parameters
        -----------
        self,b:Rational

        Return
        ----------
        self - b:Rational
        """
        if type(b) == float or type(b) == int:
            b = Rational(b)
        a = self
        return Rational(a.a * b.b - a.b * b.a, a.b * b.b).reduce()
    def __mul__(self, b):
        """
        This method multiplies Rationals.

        Parameters
        -----------
        self,b:Rational

        Return
        ----------
        self * b:Rational
        """
        a = self
        if type(b) == float or type(b) == int:
            b = Rational(b)
        return Rational(a.a * b.a, a.b * b.b).reduce()
    def __truediv__(self, b):
        """
        This method devides Rationals.

        Parameters
        -----------
        self,b:Rational

        Return
        --------
        self / b:Rational
        """
        a = self
        if type(b) == float or type(b) == int:
            b = Rational(b)
        return Rational(a.a * b.b, a.b * b.a).reduce()
    def __pow__(self, b):
        """

        This method raises self by the exponent b

        Parameters
        -----------
        a,b:Rational

        Return
        --------
        a ** b:Rational

        """
        
        a = self
        if type(b) == float or type(b) == int:
            b = Rational(b)
        if b.b != 1:
            top = a.a ** (b.a / b.b)
            bottom = a.b ** (b.a / b.b)
            if top == int(top) and bottom == int(bottom):
                return Rational(top, bottom)
            raise Exception("Yo, this programm isn't good enough to solve that, YET.\nPlus it is a early access, so it is still in development.\nThank you for being patient!\nHave a nice day")
        return Rational(a.a ** b.a, a.b ** b.a)

    def __radd__(self, a):
        """
        Reverse __add__
        """
        b = self
        if type(a) == float or type(a) == int:
            a = Rational(a)
        return a + b
    def __rsub__(self, a):
        """
        Reverse __sub__
        """
        b = self
        if type(a) == float or type(a) == int:
            a = Rational(a)
        return a - b
    def __rmul__(self, a):
        """
        Reverse __mul__
        """
        b = self
        if type(a) == float or type(a) == int:
            a = Rational(a)
        return a * b    
    def __rtruediv__(self, a):
        """
        Reverse __truediv__
        """
        b = self
        if type(a) == float or type(a) == int:
            a = Rational(a)
        return a / b    
    def __rpow__(self, a):
        """
        Reverse __pow__
        """
        b = self
        if type(a) == float or type(a) == int:
            a = Rational(a)
        return Rational(a) ** Rational(b)
    def __str__(self):
        """
        This method is built to print Rational formaatted, so users undestand.

        Parameters
        ------------
        self

        Returns
        -----------
        formatted plausible string represantation of self
        """
        if self.b == 1:
            return f"{self.a}"
        elif self.a > self.b:
            c = self.a // self.b
            d = self.a % self.b
            return f"({c}+{d}//{self.b}) "
        return f"{self.a} // {self.b}"
    def eval(self):
        """
        This method is a huge part of the system, in this case it's not quite needed, but there is a recursive sense why we decided so.

        Parameters
        ------------
        self

        Returns
        -----------
        self.reduce()(see line 41):Rational()
        """
        return self.reduce()
    def poly(self):
        return Polynomial([self.reduce()])

    def value(self):
        return self.a / self.b
    def expr(self):
        return f"{self.a} // {self.b}"


class Variable():
    """
    This class represents the mathematical conception of a variable in an expression.
    """
    def __init__(self, x):
        self.x = x
    def __eq__(self, b):
        return self.x == b.x
        
    def __str__(self):
        """
        This method is built to print Rational formatted, so users undestand.

        Parameters
        ------------
        self

        Returns
        -----------
        formatted plausible string represantation of self
        """
        return self.x
    def expr(self):
        """
        This method returns an expression as a string.
        
        Parameters
        ------------
        self

        Returns
        -----------
        self.x:str
        """
        return self.x
    def eval(self):
        """
        This method is a huge part of the system, in this case it's not quite needed, but there is a recursive sense why we decided so.
        """
        return self
    def poly(self):
        """
        This method is also very important, it turns an expression into a polynomial.
        Parameters
        ------------
        self

        Returns
        -----------
        Polynomial()

        """
        return Polynomial([Rational(0), Rational(1)])


from .polynomial import Polynomial
