def add(a,b):
    ret_val = False
    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            ret_val = a+b
    return ret_val

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b
