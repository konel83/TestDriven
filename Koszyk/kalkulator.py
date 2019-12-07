import math

def add(a,b,c=0):
    ret_val = False
    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            if isinstance(c, (int, float)):
                ret_val = a+b+c
    return ret_val

def sub(a,b):
    ret_val = False
    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            ret_val = a-b
    return ret_val

def div(a,b):
    ret_val = False
    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            if b!=0:
                ret_val = a/b
    return ret_val

def mul(a,b):
    ret_val = False
    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            ret_val = a*b
    return ret_val

def sqr(a):
    ret_val = False
    if isinstance(a, (int, float)):
        ret_val = a**2
    return ret_val

def sqrt(a):
    ret_val = False
    if isinstance(a, (int, float)):
        if a>=0:
            ret_val = math.sqrt(a)
    return ret_val
