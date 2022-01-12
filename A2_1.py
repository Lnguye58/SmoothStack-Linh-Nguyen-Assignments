""" 1.	Write a string that returns just the letter ‘r’ from ‘Hello World’
For example, ‘Hello World’[0] returns ‘H’. You should write one line of code. Don’t assign a variable name to the string."""
#ANSWER:
print('Hello World'[8])

""" 2.	String slicing to grab the word ‘ink’ from the word  ‘thinker’S=’hello’,what is the output of h[1] """
#ANSWER:
# output is e

""" 3.	S=’Sammy’ what is the output of s[2:]”"""
#ANSWER:
# return mmy

""" 4.	With a single set function can you turn the word ‘Mississippi’ to distinct character word."""
#ANSWER:
print(set('Mississippi'))

""" 5.	The word or whole phrase which has the same sequence of letters in both directions is called a palindrome."""
#ANSWER:
u_input = input("Enter a phrase or sequence: ")
u_input = u_input.lower() 
u_input = u_input.replace(" ", "")
reverse = u_input[::-1]
if(u_input == reverse):
    print('Y')
else:
    print('N')

