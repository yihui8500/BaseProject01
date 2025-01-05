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