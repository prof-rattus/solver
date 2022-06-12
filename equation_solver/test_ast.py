from .ast import  AST
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
    assert AST("4b").tokenizer() == [4, "b"]
    assert AST("4c").tokenizer() == [4, "c"]
    assert AST("4d").tokenizer() == [4, "d"]
    assert AST("4e").tokenizer() == [4, "e"]
    assert AST("4f").tokenizer() == [4, "f"]
    assert AST("4g").tokenizer() == [4, "g"]
    assert AST("4h").tokenizer() == [4, "h"]
    assert AST("4i").tokenizer() == [4, "i"]
    assert AST("4j").tokenizer() == [4, "j"]
    assert AST("4k").tokenizer() == [4, "k"]
    assert AST("4l").tokenizer() == [4, "l"]
    assert AST("4m").tokenizer() == [4, "m"]
    assert AST("4n").tokenizer() == [4, "n"]
    assert AST("4o").tokenizer() == [4, "o"]
    assert AST("4p").tokenizer() == [4, "p"]
    assert AST("4q").tokenizer() == [4, "q"]
    assert AST("4r").tokenizer() == [4, "r"]
    assert AST("4s").tokenizer() == [4, "s"]
    assert AST("4t").tokenizer() == [4, "t"]
    assert AST("4u").tokenizer() == [4, "u"]
    assert AST("4v").tokenizer() == [4, "v"]
    assert AST("4w").tokenizer() == [4, "w"]
    assert AST("4x").tokenizer() == [4, "x"]
    assert AST("4y").tokenizer() == [4, "y"]
    assert AST("4z").tokenizer() == [4, "z"]
    assert AST("4 + a").tokenizer() == [4, "+", "a"]

    
def test_ast_split():
    assert AST("").split([4, "x"]) == ([Rational(4), Variable("x")], [Multiplication])
