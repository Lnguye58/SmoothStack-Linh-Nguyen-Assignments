""" Create a function func() which prints a text ‘Hello World’ """
#ANSWER
def PrintHello():
    print('Hello World')

PrintHello()

""" Create a function which func1(name)  which takes a value name and prints the output “Hi My name is Google" """
#ANSWER
def func1(name):
    print(f"Hi My name is {name}")
name = 'Google'
func1(name)

""" Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when z is false it should return y. 
    func3(‘hello’goodbye’,false)"""
#ANSWER
def func3(x,y,z):
    if z == True:
        print(x)
    else:
        print(y)

func3(3,4, False)
func3(3,4, True)

""" define a function func4(x,y) which returns the product of both the values"""
#ANSWER
def func4(x,y):
    z = x * y
    print(z)

func4(3,2)

""" define a function called as is_even that takes one argument , which returns true when even values is passed and false if it is not."""
#ANSWER
def is_even(x):
    if (x % 2 == 0):
        print(True)
    else:
        print(False)

is_even(6)

""" define a function that takes two arguments, and returns true if the first value is greater than the second value 
    and returns false if it is less than or equal to the second."""
#ANSWER
def func4(x,y):
    if (x > y):
        print(True)
    elif (x <= y):
        print(False)

func4(5,4)
func4(4,4)

""" Define a function which takes arbitrary number of arguments and returns the sum of the arguments."""
#ANSWER
def func5(*args):
    sum = 0
    for x in args:
        sum = sum + x
    print(sum) 

func5(8, 9 , 10)
func5(1, 3 , 1345)

""" Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even."""
#ANSWER
def func6(*args):
    lst = []
    for x in args:
        if (x % 2 == 0):
            lst.append(str(x))
        else: 
            continue
    print(lst)

func6(1, 2, 3, 4, 5, 6)

""" Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase """
#ANSWER
def StringCase(strs):
    lst = []
    for x in range(len(strs)):
        if (x % 2 == 0):
            lst.append(strs[x].upper())
        else:
            lst.append(strs[x].lower())
    print(' '.join(lst))

StringCase('elephant')
StringCase('chicken')

""" Write a function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd."""
#ANSWER
def func7(x, y):
    if (x % 2 == 0) and (y % 2 == 0):
        if y > x:
            return x
        if x > y:
            return y
    else:
        if x > y:
            return x
        else:
            return y

print(func7(6, 7))
print(func7(2, 4))
print(func7(245, 13))

""" Write a function which takes  two-strings and returns true if both the strings start with the same letter."""
#ANSWER
def SameString(x, y):
    if x[0] == y[0]:
        print(True)
    else:
        print(False)

SameString('dog', 'dancing')
SameString('dog', 'pig')

""" Given a value,return a value which is twice as far as other side of 7"""
#ANSWER
def Squaring(x):
    x = x*x
    print(x)

Squaring(8)
Squaring(5)

""" A function that capitalizes first and fourth character of a word in a string."""
#ANSWER
def capital(string):
    lst = list(string)
    for x in range(len(string)):
        if x == 0:
            lst[x] = lst[x].upper()
        elif x == 3:
            lst[x] = lst[x].upper()
    print(''.join(lst))

capital('chicken')
capital('saint')
