import random
""" Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). 
    Go to the editor 
"""
#ANSWER:
nlist = []
for x in range(1500, 2700):
   if (x % 7 == 0) and (x % 5 == 0):
        nlist.append(str(x))
print (','.join(nlist))


""" Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
    [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
    Expected Output : 
    60°C is 140 in Fahrenheit
    45°F is 7 in Celsius 
"""
#ANSWER
temp = int(input("Enter Temperature: "))
units = input("In 'C' for Celsius or 'F' for Fahrenheit: ")

if units == 'f' or units == 'F':
    cel = round((9/5 * temp) + 32)
    print(f"{temp}C is {cel} in Fahrenheit")
elif units == 'c' or units == 'C':
    fah = round(5/9 * (temp - 32))
    print(f"{temp}F is {fah} in Celsius")


""" Write a Python program to guess a number between 1 to 9. Go to the editor
    Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, 
    on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""
#ANSWER
r_number = random.randint(1,9)
u_input = int(input("Guess a number between 1 and 9: "))

while  (u_input != r_number):
    u_input = int(input("Not the right number, guess again: "))
    if (u_input == r_number):
        print("Well Guessed!")



""" Write a Python program to construct the following pattern, using a nested for loop."""
#ANSWER
x = 5
for i in range(x):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(x,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

""" Write a Python program that accepts a word from the user and reverse it. Go to the editor"""
#ANSWER
u_input = input("Write a word")
reverse = u_input[::-1]
print("Your reverse word is: " + reverse)

""" Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
    Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
    Expected Output : 
    Number of even numbers : 5
    Number of odd numbers : 4
"""
#ANSWER
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
even = 0
odd = 0
for i in numbers:
    if (i % 2):
        even += 1
    else:
        odd += 1
print (f"Number of even numbers: {even}")
print (f"Number of odd numbers: {odd}")


""" Write a Python program that prints each item and its corresponding type from the following list.
    Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
"""
#ANSWER
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in datalist:
    print(f"Type, {i} is", type(i))

""" Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
    Note : Use 'continue' statement. 
    Expected Output : 0 1 2 4 5 
"""
#ANSWER:
for i in range(0, 6):
    if (i == 3) or (i == 6):
        continue
    else:
        print(i, end = ' ')

