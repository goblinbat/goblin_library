"""
Includes *args, **kwargs, decorators, docstrings,
enumerate, for/else loops, lambda functions
"""
# ===========================================================

"""
*args and **kwargs
Python has a built in way to extend a function to take a large number of arguments
syntax: def some_func(some_val, *args)  <-- some_val is optional

**kwargs has to come after *args
"""
def add_nums(*args):
    the_sum = 0

    for n in args:
        the_sum += n
    
    return the_sum
a = add_nums(42, 50, 63, 90)

test_dict = {
    'name': 'bat',
    'age': '23',
    'grade': '18th'
}
def print_dict(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
print_dict(**test_dict)

# ===========================================================

'''
These are docstrings. They're actually rendered by python and are used for 
documentation
Useful for noting 
    what functions, classes, sections of code, etc. do
    what arguments/parameters things take
    what should be returned
    how sections of code work
    why a section is needed/ etc
'''

# ===========================================================

"""
Lambdas are anonymous functions 
    anonymous functions don't show if you call the file elsewhere
    you can also make anonymous variables by putting an _ before them (ex: _x)

normally: def name(args): 
    (some logic)
lambda args: manipulation(args)
"""
# The following function and lambda function are equivalent
def some_func(x):
    return x**2

x= lambda x: x**2

# ===========================================================

# For-Else
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)     # apparently this works (about) the same as an f-string
            break
    else:                                       # allows the if to run through all possibilities before the else is hit
        print(n, 'is a prime number')

# ===========================================================

"""
enumerate is a method that adds a counter to an iterable and returns it
syntax: enumerate(iterable, start=0) (start default = 1)

Can cast an enumerate as a list // tuple
ie... list(enumerate(item, start))
ie... tuple(enumerate(item, start))
"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in enumerate(letters):
    print(i)
for x,y in enumerate(letters):
    print(x)
    print(y)
def make_tuple_of_list(a_list):         # could also make a dictionary
    return tuple(enumerate(a_list))

# ===========================================================
"""
Callback function: function passed into another function as an argument and then called inside that function
"""

def do_math(math_func):     # math_func is a function
    return math_func(5)    # executes said function
mult = do_math(some_func)   #give do_math func some_func (and in doing so give some_func the numbers 5, 10, and 9)

# ===========================================================

# functions can be inside functions
def parent():
    def first_child():      # you can define functions inside functions
        print("i'm the first child")       # these functions can only be called from within the base function

    def second_child():
        print("i'm the second child")
    
    print("i'm the parent")
    second_child()
    first_child()
parent()

# ===========================================================

"""
Decorators allow you to reuse functions that take functions

Functions are 'first-class objects'

Importance: reusable by just adding a single line above other functions
also, can be easily toggled off by just commenting off decorator
"""
def my_decorator(func):         # decorators take in functions and return functions
    def wrapper(*args, **kwargs):       # allows the functions you pass in to take arguments if they need them
        print('before function')
        value = func(*args, **kwargs)       # needs to be assigned to a variable (which then needs to be returned) so that if the function returns a return value it can be captured
        print('after function')
        return value
    return wrapper

@my_decorator       # because of this, it knows to throw say_whee into my_decorator
def say_whee():
    print('whee')
say_whee()


