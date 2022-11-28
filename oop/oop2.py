#Decorators: 
#A way to dynamically alter the functionality of the functions.
#*args and **kwargs ensure that you can pass any number of positional or keyword parameters
'''
#Function Decorator
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function #display = decorated_function(display)
def display():
    print("Display function ran")

@decorator_function
def display_info(name, age):
    print("display_info ran with arguments ({}, {}) ".format(name,age))

display_info("Rushikesh",21)
display()

def decorated_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()

    return wrapper_function


@decorated_function #display = decorated_function(display)
def display():
    print("Now execute display")


display()
'''

def decorated_function(myDis):
    def wrapper(val):
        if isinstance(val,int):
            print(val*2)
        else:
            print(val)
        return myDis(val)

    return wrapper

@decorated_function   #display = decorated_function(display)
def display(val):
    print("In display, val is :{}".format(val))

display("Hello")

def decorated_function(val1):
    def wrapper(func):
        print("Executing wrapper",val1)
        def again_wrapper(val):
            print("Executing again wrapper ",end="")
            if isinstance(val,int):
                print(val*2)
            else:
                print(val)
            return func(val)
        return again_wrapper
    return wrapper

@decorated_function(100)   #display = decorated_function(display)
def display(val):
    print("In display, val is :{}".format(val))

print("AGAIN WRAPPER EXECUTOR")
display("Hello")
