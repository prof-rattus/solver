from .rational import (
    Rational, 
    Variable
)
from .operators import (
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Raise
)
from .eqaution import Equation

NUMS = "0123456789"
STATE_NUMBER = 'NUMBER'
STATE_OPERATOR = 'OPERATOR'
STATE_BRACE_OPEN = '('
STATE_BRACE_CLOSE = ')'
OPERATORS="+-*/=^"
OPTOCLASS = {
    "+": Addition,
    "-": Subtraction,
    "*": Multiplication,
    "/": Division,
    "^": Raise
}

class AST():
    """
    This class represents the conception of an Abstract Syntax Tree

    Parameters
    ----------
    expression as a string,which will be parsed later:BinOperator
    """
    def __init__(self, expr):
        self.expr = expr
    def readNumVar(self, part):
        """
        This method is able to read a sindle numerical expression or variable x.

        Parameters
        ------------
        part:str

        Returns
        -----------
        int(part) (enhanced)
        """
        a = part
        mul = 1
        s = 0
        if a[0] == "-":
            mul = -1
            a = a[1:]
            s = 1
        
        seenNumber = False
        res = 0
        for k, b in enumerate(a):
            if b == " ":
                s += 1
                continue
            if b == ".":
                s += 1
                break
            if k == 0 and b == "+":
                s += 1
                continue
            if b == "x":
                seenNumber = True
                s += 1
                res = "x"
                break
            if b not in NUMS:
                break

            s += 1
            res = res * 10 + NUMS.index(b)
            seenNumber = True
        
        if not seenNumber:
            return (0, 0)
        
        if b == ".":
            div = 1
            for c in a[k+1:]:
                if c == " ":
                    s += 1
                    continue
                if c not in NUMS:
                    break 
                s += 1
                div = div * 10
                c = NUMS.index(c)
                res = res + c / div

        if res == "x":
            if mul == -1:
                return ("-x", s)
            else:
                return ("x", s)
        return (res * mul, s)


    def tokenizer(self):
        """
        This method reads a string smaple, and transfers it into tokens. 
        Example
        ---------
        "4 + 5" -> [4, "+", 5]

        Parameters
        ------------
        self.expr

        Returns
        -----------
        token:list
        """
        a = self.expr
        currentState = None
        nextStates = [STATE_NUMBER, STATE_BRACE_OPEN]
        k = 0
        res = []
            
        while k < len(a):
            if a[k] == " ":
                k += 1
                continue

            if STATE_BRACE_OPEN in nextStates and a[k] == "(":
                res.append(a[k])
                k += 1
                nextStates = [STATE_BRACE_OPEN, STATE_NUMBER]
                currentState = STATE_BRACE_OPEN
                continue
            elif STATE_BRACE_CLOSE in nextStates and a[k] == ")":
                res.append(a[k])
                k += 1
                nextStates = [STATE_BRACE_CLOSE, STATE_OPERATOR]
                currentState = STATE_BRACE_CLOSE
                continue
            elif STATE_NUMBER in nextStates:
                (n, s) = self.readNumVar(a[k:])
                if s == 0:
                    raise Exception(f"From the {k}th symbol is unlear, check your syntax.")
                k += s
                res.append(n)
                currentState = STATE_NUMBER
                nextStates = [STATE_OPERATOR,STATE_BRACE_CLOSE]
            elif STATE_OPERATOR in nextStates:
                if a[k] not in OPERATORS:
                    raise Exception(f"{a[k]} is not an operator at {k}th")
                res.append(a[k])
                k += 1
                currentState = STATE_OPERATOR
                nextStates = [STATE_NUMBER, STATE_BRACE_OPEN]

        if currentState not in [STATE_NUMBER, STATE_BRACE_CLOSE]:
            raise Exception("Invalid syntax.")

        return res

    def split(self, toks):
        """
        This method splits tokens into numbers and operators.

        Parameters
        ------------
        toks

        Returns
        -----------
        ([nums], [ops]):tuple

        """
        nums = []
        ops = []
        for a in toks:
            if type(a) == int or type(a) == float:
                nums.append(Rational(a))
            elif a == "x":
                nums.append(Variable(a))
            elif a == "-x":
                nums.append(Multiplication(Variable(a), Rational(-1)))
            elif type(a) == list:
                nums.append(self.split(a))
            elif a in OPTOCLASS:
                ops.append(OPTOCLASS[a])
            else:
                raise Exception("The input given is wrong.Check it, otherwise this won't work.")
        return (nums,ops)


    def evaluate_ops(self,nums, ops, opsToEvaluate):
        """
        This method filters out which operators should be evaluated first.Also transfers into classes.

        Parameters
        ------------
        nums, ops:list
        opsToEvaluate:list with constants

        Returns
        -----------

        """
        nums2 = []
        ops2 = []
        
        r = nums.pop(0)
        while nums and ops:
            o = ops.pop(0)
            s = nums.pop(0)
            
            if o in opsToEvaluate:
                r = o(r, s)
            else:
                ops2.append(o)
                nums2.append(r)
                r = s

        nums2.append(r)
        
        return nums2, ops2


    def tok_to_list(self, tok):
        """
        This method excutes the parntheses logic.

        Example
        --------
        ["(", 4, "+", 5") "+" 5] -> [[4, +, 5], "+",5]

        Parameters
        ------------
        tok

        Returns
        -----------
        a recursive list, in case there are parenttheses:list
        """
        root = []
        lists = []
        current = root
        while tok:
            c = tok.pop(0)
            if c == STATE_BRACE_OPEN:
                new_list = []
                current.append(new_list)
                lists.append(current)
                current = new_list
            elif c == STATE_BRACE_CLOSE:
                if not current:
                    raise Exception("empty parentheses")
                current = lists.pop()
            else:
                current.append(c)
        if lists:
            raise Exception("not closed parenthes")
        return root


    def eval(self, nums, ops):
        """
        This method builds everything together into an AST
        
        Parameters
        ------------
        nums,ops

        Returns
        -----------
        builded AST
        
        
        """
        for i,k in enumerate(nums):
            if type(k) == tuple:
                nums[i] = self.eval(k[0], k[1])
        (nums,ops) = self.evaluate_ops(nums,ops,[Raise])
        (nums, ops) = self.evaluate_ops(nums, ops, [Multiplication, Division])
        (nums, ops) = self.evaluate_ops(nums, ops, [Addition, Subtraction])
        if len(nums) != 1 or ops:
            raise Exception("invalid syntax")
    
        return nums.pop()

    def parse(self):
        """
        In this method, all the methods are called, so that it is easier execute.

        Parameters
        -----------
        self

        Returns
        ------------
        AST
        """
        toks = self.tokenizer()
        toks = self.tok_to_list(toks)
        if "=" in toks:
            if toks.count("=") > 1:
                raise Exception("More than one ='s are not accepted")
            index = toks.index("=")
            tok = toks[0:index]
            tok2 = toks[index + 1:]
            (nums,ops) = self.split(tok)
            (nums2,ops2) = self.split(tok2)
            expr_a = self.eval(nums, ops)
            expr_b = self.eval(nums2, ops2)
            return Equation(expr_a,expr_b)
        else:
            (nums,ops) = self.split(toks)
            return self.eval(nums,ops)