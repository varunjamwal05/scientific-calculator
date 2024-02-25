import basic as bs
import trigo as tr
import complex as cp
import log as lg
import quadratic as qd
import factorial as fc

def modeSelection():
    choose = input("Choose mode :- Basic(B)/Trigo(T)/Complex(C)/Logarithm(L),Quadratic(Q)/Factorial(F):")
    if choose == "B":
        basic()
    elif choose == "T":
        trigo()
    elif choose == "C":
        comp()   
    elif choose == "L":
        log() 
    elif choose == "Q":
        quad()
    elif choose == "F":
        fact()
    else:
        print("Wrong Choice")

def basic():

    # User Input
    print("Operations (+,-,*,/,//,%)")
    print("For Changing Mode (CM)")
    action = input("action : ")

    # Mode Selection
    if action == "CM":
        modeSelection()
        return 0

    # Basic Opretions
    num1 = float(input('num1: '))
    num2 = float(input('num2: '))
    if action=="+":
        print(bs.add(num1, num2))
    elif action=="-":
        print(bs.sub(num1,num2))
    elif action=="*":
        print(bs.mul(num1,num2))
    elif action=="/":
        print(bs.div(num1,num2))
    elif action=="%":
        print(bs.mod(num1,num2))
    elif action=="//":
        print(bs.floordiv(num1,num2))
    else:
        print("ERROR")

def trigo():
    # User Input
    print("Operations (sin,tan,cos,asin,acos,atan)")
    print("For Changing Mode (CM)")
    action = input("action : ")
    
    # Mode Selection
    if action == "CM":
        modeSelection()
        return 0
    
    # Trigo Opretions
    num = float(input('num: '))
    if action == "sin":
        print(tr.sine(num))
    elif action == "cos":
        print(tr.cosine(num))
    elif action == "tan":
        print(tr.tangent(num))
    elif action == "asin":
        print(tr.arcsine(num))
    elif action == "acos":
        print(tr.arccosine(num))
    elif action == "atan":
        print(tr.arctangent(num))
    else:
        print("ERROR")

def comp():
    #User Input
    print("Operations (squareroot,cuberoot,square,cube)")
    print("For Changing Mode (CM)")
    action = input("action: ")

    #Mode Selection
    if action == "CM":
        modeSelection()
        return 0
    
    num = float(input("num: "))
    if action == "squareroot":
        print(cp.squareroot(num))
    elif action == "cuberoot":
        print(cp.cuberoot(num))
    elif action == "square":
        print(cp.square(num))
    elif action == "cube":
        print(cp.cube(num))
    else:
        print("ERROR")

def log():
    #User Input
    print("Operations (ln,log)")
    print("For Changing Mode (CM)")
    action = input("action: ")

    #Mode Selection
    if action == "CM":
        modeSelection()
        return 0

    if action == "ln":
        num = float(input("num: "))
        print(lg.log(num))
    elif action == "log":
        num = float(input("num: "))
        base = int(input("b: "))
        print(lg.logb(num,base))
    
def quad():
     #User Input
    print("For Changing Mode (CM)")
    action = input("action: ")

    #Mode Selection
    if action == "CM":
        modeSelection()
        return 0
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = b*b - 4*a*c
    print("d =",d)
    if d == 0:
        qd.equal(a,b,c,d)
    elif d < 0:
        qd.less(a,b,c,d)
    else:
        qd.greater(a,b,c,d)

def fact():
    #User Input
    print("For Changing Mode (CM)")
    action = input("action: ")

    #Mode Selection
    if action == "CM":
        modeSelection()
        return 0
    
    num = int(input("num: "))
    fc.factorial(num)

# Starting Point Of Calculator
modeSelection()