"""
Math, parsing, lists, tuples, dictionaries, 
strings, condtionals, none vs 0

press ctrl + alt + m to run file
"""


# MATH
a = 1
a += 2  # a = 3
a -= 1  # a = 2
a *= 5  # a = 10
a /= 2  # a = 5
a % 2   # 1 (returns remainder)
print(x // 2)   # // rounds down, / doesn't
# pemdas
print(x * (2 + 5))


# PARSING
f = "1"
g = int(f)   # int() converts strings to integers
h = float(f) # float() will convert string numbers with decimals to a usable number


# LISTS
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
for i in my_list:
    print(i)
my_list.append(9)    # adds the number 9 to the end of the list
print(my_list[0])    # returns first item in list (item at index 0)
print(my_list[:3])   # returns everything up to index 3   (3: would return everything after index 3)
print(my_list[3:6])  # returns items from index 3 to index 6
print(len(my_list))  # tells you how long the string/list/etc is
print(min(my_list))   # min gets smallest number
print(max(my_list))   # max gets biggest number
print(my_list.index(2))   # finds how far along in the collection the searched-for input is (index value of input)
print(my_list.count(1))   # tells you how many of the searched-for input are in the collection (in this example, how many 1's)
# len(), min(), max() can be used on different data types, while .index and .count can only be used on collections


# TUPLES
# tuples are immutable; you cannot add or remove things to/from them
my_tuple = (1, 2, 3)
a, b, c = my_tuple             # unpacks a tuple (a=1, b=2, c=3)


# DICTIONARIES
billy = {
    'key': 'value',
    'name': 'billy stone',
    'age': 20,
    'id': 10,
    'class': 'Python'
}
print(billy['name'])


# STRINGS
name = 'connor'
upper_name = name.upper()
print(upper_name)
lower_name = name.lower()
print(lower_name)
print(name[2]) # returns third letter (n)
for i in name:
    print(i)
name_list = name.split()    # splits string into list of characters
name = name.replace('n', 'b')  # changes connor to cobbor
name = name[::-1]       # changes cobbor to robboc

b = input('Dear friend, what is your name? ')
print('Hello there, ' + b.capitalize() +'! Good to see you!')


# CONDITIONALS
'''
Variable assignment: =
Is equal: ==
Not equal: !=
Greater than: >    Or equal to: >=
Less than: <       Or equal to: <=
'''
c = 0
if 1 < c < 10:
    print('tap dance')
elif c >= 10:
    print('ballet')
else:
    print("tango")

d = input('Enter a number: ')
e = int(d)
if e % 3 == 0 and e % 5 != 0:
    print('fizz')
elif e % 5 == 0 and e % 3 != 0:
    print('buzz')
elif e % 3 == 0 and e % 5 == 0:
    print('fizzbuzz')
else:
    print(e)

guess = input('pick a number: ")
for guess in range(101)
    if guess %5 == 0:
        if guess % 3 == 0:
            print('fizzbuzz')
    elif guess % 3 == 0: 
        print('fizz')
    else:
        print(guess)
# Due to "for guess in range", it runs every number 0-guess (up to 101), giving a lot of outputs

name = input("what is your name? ")
for i in name:
    print(i)


# NONE AND ZERO
x = None   # creates empty box with absolutely nothing in it
y = 0   # stores 0 in a box
# y is truthy, x is falsey
