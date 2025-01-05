def add(a,b):
    return a+b

def swap(a,b):
    c=a
    a=b
    b=c
    return(a,b)
    
def add2(a,b,c):
    d=add(a,b)
    e=d+c
    return e

def add3(a,b,c,d):
    e=add3(a,b,c)
    f=e+d
    return f