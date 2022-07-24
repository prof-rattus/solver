from .ast import AST
from .rational import Rational
from .rational import Variable
from .operators import Multiplication


def test_ast_readNumber():
    res = AST("")
    assert res.readNumVar("4") == (4, 1)
    assert res.readNumVar("-1234567890") == (-1234567890, 11)
    assert res.readNumVar("- 1234567890") == (-1234567890, 12)
    assert res.readNumVar("1.234567890") == (1.234567890, 11)
    assert res.readNumVar("-1.234567890") == (-1.234567890, 12)
    assert res.readNumVar("- 1.234567890") == (-1.234567890, 13)
    assert res.readNumVar("34x") == (34, 2)
    assert res.readNumVar("x34") == ("x", 1)
    assert res.readNumVar("-34x") == (-34, 3)
    assert res.readNumVar("-x34") == ("-x", 2)
    assert res.readNumVar("123.45.5678") == (123.45, 6)
    assert res.readNumVar(".56789") == (0, 0)
    assert res.readNumVar("a") == ("a", 1)
    assert res.readNumVar("-a") == ("-a", 2)


def test_ast_tokenizer():
    assert AST("1").tokenizer() == [1]
    assert AST("4a").tokenizer() == [4, "a"]
    assert AST("4 + a").tokenizer() == [4, "+", "a"]
    assert AST("4 * (3 + a)").tokenizer() == [4, "*", "(", 3, "+", "a", ")"]
    assert AST("5 + (3 - a)").tokenizer() == [5, "+", "(", 3, "-", "a", ")"]

def test_ast_tok_to_list():
    assert AST("").tok_to_list([4, "*", "(", 3, "+", "a", ")"]) == [4, "*",[  3, "+", "a"]]

  


def test_ast_split():
    assert AST("").split([4, "x"]) == (
        [Rational(4), Variable("x")], [Multiplication])
    assert AST("").split([5, "a"]) == (
        [Rational(5), Variable("a")], [Multiplication])

