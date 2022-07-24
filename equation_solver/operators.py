from .rational import (Rational)

class BinOperator():
    """
    This class represents any binary operator.
    """
    sign = ""
    def __init__(self, a, b):
        if type(a) == int or type(a) == float:
            a = Rational(a)
        if type(b) == int or type(b) == float:
            b = Rational(b)
        self.a = a
        self.b = b
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
        if isinstance(self.a, Rational) and isinstance(self.b, Rational):
            return (self.a.reduce(), self.b.reduce())
        return (self.a.eval(), self.b.eval())
    def expr(self):
        """
        This method returns an expression as a string.

        Parameters
        ------------
        self

        Returns
        -----------
        self:str
        """
        return f"({self.a.expr()} {self.sign} {self.b.expr()})"


class Addition(BinOperator):
    sign = "+"
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
        return self.a.eval() + self.b.eval()
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
        return f"Addition({self.a}, {self.b})"
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
        return self.a.poly() + self.b.poly()
    def lineq(self):
        return self.a.lineq() + self.b.lineq()


class Subtraction(BinOperator):
    sign = "-"    
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
        return self.a.eval() - self.b.eval()
    def __str__(self):
        """
        This method is built to print Rational formatted, so users undestand.

        Parameters
        ------------
        self

        Returns
        -----------
        formatted plausible string represantation of self
        return f"Addition({self.a}, {self.b})"
        """
        return f"Subtraction({self.a}, {self.b})"
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
        return self.a.poly() - self.b.poly()
    def lineq(self):
        return self.a.lineq() - self.b.lineq()


class Multiplication (BinOperator):
    sign = "*"
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
        return self.a.eval() * self.b.eval()
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
        return f"Multiplication({self.a}, {self.b})"
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
        return self.a.poly() * self.b.poly()
    def lineq(self):
        return self.a.lineq() * self.b.lineq()


class Division(BinOperator):
    sign = "/"
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
        return self.a.eval() / self.b.eval()
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
        return f"Division({self.a}, {self.b})"
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
        a = self.a.poly()
        b = self.b.poly()
        if len(b) != 1:
            raise Exception("No Variables, yet.")
        return a / b[0]
    def lineq(self):
        return self.a.lineq() / self.b.lineq()


class Raise(BinOperator):
    sign = "^"
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
        return self.a.eval() ** self.b.eval()
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
        return f"Raise({self.a}, {self.b})"
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
        a = self.a.poly()
        b = self.b.poly()
        if len(b) != 1:
            raise Exception("Invalid.")
        return a ** b[0]
    def lineq(self):
        return self.a.lineq() ** self.b.lineq()