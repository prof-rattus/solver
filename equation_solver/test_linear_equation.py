from .ast import AST
from .rational import Rational
from .rational import Variable
from .operators import Multiplication
from .linear_equation import LinearEquation

R = Rational

def test_linear_equation_add():
    a = LinearEquation(
        R(5),
        {
            Variable("x"): R(5),
            Variable("y"): R(-4)
        }
    )
    b = LinearEquation(
        R(4),
        {
            Variable("y"): R(2),
            Variable("z"): R(4)
        }
    )
   

    sum = LinearEquation(
        R(9),
        {
            Variable("x"): R(5),
            Variable("y"): R(-2),
            Variable("z"): R(4)
        }
    )
    assert a + b == sum

def test_linear_equation_sub():
    a = LinearEquation(
        R(5),
        {
            Variable("x"): R(5),
            Variable("y"): R(-4)
        }
    )
    b = LinearEquation(
        R(4),
        {
            Variable("y"): R(2),
            Variable("z"): R(4)
        }
    )
    dif = LinearEquation(
        R(1),
        {
            Variable("x"): R(5),
            Variable("y"): R(-6),
            Variable("z"): R(-4)
        }
    )
    assert a - b == dif 

def test_linear_equation_mul():

    a = LinearEquation(R(5))
    b = LinearEquation(
        R(2), 
        {
            Variable("x"): R(3),
            Variable("y"): R(3),
            Variable("z"): R(7)
        }
    )
    pro = LinearEquation(
        R(10),
        {
            Variable("x"): R(15),
            Variable("y"): R(15),
            Variable("z"): R(35)  
        }
    )
    
    assert a * b == pro

def test_linear_eqution_division():
    a = LinearEquation(R(5))
    b = LinearEquation(
        R(2), 
        {
            Variable("x"): R(3),
            Variable("y"): R(3),
            Variable("z"): R(7)
        }
    )
    quo = LinearEquation(
        R(2, 5),
        {
            Variable("x"): R(3, 5),
            Variable("y"): R(3, 5),
            Variable("z"): R(7, 5)  
        }
    )
    assert b / a == quo


def test_linear_equation_pow():
    a = LinearEquation(R(2))
    b = LinearEquation(R(4))

    res = LinearEquation(R(16))

    assert a ** b == res

