#1주차 과제.
from enum import Enum
class CalType(Enum):
    Plus = 1
    Min = 2
    Mul = 3
    Div = 4

def operatorCal(kind , a, b) :
    if kind == CalType.Plus :
        plus(a,b)
    elif kind == CalType.Min:
        min(a,b)
    elif kind == CalType.Mul:
        mul(a,b)
    elif kind == CalType.Div:
        div(a,b)

def plus(*values) :
    sum = 0
    for value in values :
        sum += value
    return printResult(sum)

def min(*values) :
    sum = 0
    for value in values :
        if values[0] == value :
            sum += value
        else :
            sum -= value
    return printResult(sum)

def mul(*values) :
    sum = 1
    for value in values :
        sum *= value
    return printResult(sum)

def div(*values) :
    sum = 0
    for value in values :
        if values[0] == value :
            sum += value
        else :
            sum /= value
    return printResult(sum)


def printResult(result) :
    print("결과 {}".format(result))

operatorCal(CalType.Min,1,2)