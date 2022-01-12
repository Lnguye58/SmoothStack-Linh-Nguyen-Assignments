"""1.	Create a list with one number, one word and one float value. Display the output of the list. """
#ANSWER:
a = [1, 'cat', 3.14]
print(a)

"""2.	I have a nested list [1,1[1,2]], how to grab the value of 2 from the list. """
#ANSWER:
n_list = [1,1,[1,2]]
print(n_list[2][1])

"""3.	lst=['a','b','c'] What is the result of lst[1:]? """
#ANSWER:
print(['b','c'])

"""4.	Create a dictionary with weekdays an keys and week index numbers as values.do assign dictionary to a variable """
#wording confusing needs to be clearer.
#ANSWER:
d = {"Weekdays" : [1,2,3,4,5,6,7]}
print(d)

"""5.	D={‘k1’:[1,2,3]} what is the output of d[k1][1] """
#Punctuation missing for ["k1"]
#ANSWER: Invalid because it's trying to access the list of k1 instead of the key "k1" 

"""6.	Can you create a list [1,[2,3]] into a tuple """
#ANSWER:
c = [[1],[2,3]]
tuples = [tuple(x) for x in c]
print(tuples)

"""7.	With a single set function can you turn the word ‘Mississippi’ to distinct character word. """
#ANSWER:
a = set('Mississippi')
print(a)

"""8.	Can you add an element ‘X’ to the above created set """
#ANSWER:
i = set('Mississippi')
i.add('X')
print(i)

"""9.	Output of set([1,1,2,3]) """
#ANSWER:
#Output = {1, 2, 3}


"""Question #1 
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).
	The numbers obtained should be printed in a comma-separated sequence on a single line.
	Hints: Consider use range(#begin, #end) method
"""
#ANSWER:
nlist = []
for x in range(2000, 3200):
   if (x % 7 == 0) and (x % 5 != 0):
        nlist.append(str(x))
print (','.join(nlist))


"""Question #2 
    Write a program which can compute the factorial of a given numbers.
	The results should be printed in a comma-separated sequence on a single line.
	Suppose the following input is supplied to the program:
	8
	Then, the output should be:
	40320
	
	Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
#ANSWER:
def factorial(x):
	if x == 0:
	    return 1
	return x * factorial(x - 1)
	
num = input()
num = int(num)
print (factorial(num))


"""Question #3
    With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
    such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
	Suppose the following input is supplied to the program:
	8
	Then, the output should be:
	{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
	
	Hints:
	In case of input data being supplied to the question, it should be assumed to be a console input.
	Consider use dict()
"""
#ANSWER:
n_input = input()
n_input = int(n_input)
d = dict()

for x in range(1, n_input + 1):
	d[x]= x * x

print(d)

"""Question #4 
    Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
	Suppose the following input is supplied to the program:
	34,67,55,33,12,98
	Then, the output should be:
	['34', '67', '55', '33', '12', '98']
	('34', '67', '55', '33', '12', '98')
	
	Hints:
	In case of input data being supplied to the question, it should be assumed to be a console input.
	tuple() method can convert list to tuple
"""
#ANSWER:
u_input = input()
lst = u_input.split(",")
tup = tuple(lst)
print(lst)
print(tup)

"""Question #5 
    Define a class which has at least two methods:
	getString: to get a string from console input
	printString: to print the string in upper case.
	Also please include simple test function to test the class methods.
	
	Hints:
	Use __init__ method to construct some parameters
"""

#ANSWER:
class StringInput():
	def __init__(self):
	    self.u_input = ""
	
	def getString(self):
	    self.u_input = input()
	
	def printString(self):
	    print (self.u_input.upper())	

s_input = StringInput()
s_input.getString()
s_input.printString()
