import math
import cmath

def equal(a,b,c,d):
    print("This equation has no real solution")

def less(a,b,c,d):
    sqrt1 = (- b + cmath.sqrt(d)) / (2*a)
    sqrt2 = (- b - cmath.sqrt(d)) / (2*a)
    print("This equation has solutions:",sqrt1, sqrt2)

def greater(a,b,c,d):
    x1 = (-b+math.sqrt(d))/2*a
    x2 = (-b-math.sqrt(d))/2*a
    print("This equation has two solutions:",x1,x2)