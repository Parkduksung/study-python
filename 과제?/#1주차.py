#1주차 과제.
from enum import Enum
class CalType(Enum):
    Plus = 1
    Min = 2
    Mul = 3
    Div = 4

def printResult(result) :
    print("결과 {}".format(result))

plus_lambda = lambda x, y : x+y
min_lambda = lambda x, y : x-y
mul_lambda = lambda x, y : x*y
div_lambda = lambda x, y : x/y

def operatorCal(kind , a, b) :
    if kind == CalType.Plus :
        printResult(plus_lambda(a,b))
    elif kind == CalType.Min:
        printResult(min_lambda(a,b))
    elif kind == CalType.Mul:
        printResult(mul_lambda(a,b))
    elif kind == CalType.Div:
        printResult(div_lambda(a,b))

operatorCal(CalType.Min,1,2)

