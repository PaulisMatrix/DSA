class A:
    def __init__(self,val):
        self.a = val

    def __add__(self,o):
        return self.a + o.a * pow(10,-3)


g = A(1)
kg = A(1)

print(g + kg)


import time
#decorators to time your functions
def fib_helper(n):
    if n < 2:
        return n
    return fib_helper(n-1) + fib_helper(n-2)

    
def fib(n):
    return fib_helper(n)

#with memoization
def fib_m_helper(n):
    mydict = {0:0,1:1}

    if n in mydict.keys():
        return mydict[n]

    mydict[n] = fib_m_helper(n-1) + fib_m_helper(n-2)

    return mydict[n]


def fib_m(n):
    return fib_m_helper(n)

def timeit(fn): 
    # *args and **kwargs are to support positional and named arguments of fn
    def get_time(*args, **kwargs): 
        start = time.time() 
        output = fn(*args, **kwargs)
        print(f"Time taken in {fn.__name__}: {time.time() - start:.7f}")
        return output  # make sure that the decorator returns the output of fn
    return get_time 

@timeit
def fib(n):
    return fib_helper(n)

@timeit
def fib_m(n):
    return fib_m_helper(n)

fib(30)
fib_m(30)









