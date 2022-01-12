""" 
    Three is a Crowd
	Make a list of names that includes at least four people.
	Write an if test that prints a message about the room being crowded, if there are more than three people in your list.
	Modify your list so that there are only two people in it. Use one of the methods for removing people from the list,
    don't just redefine the list. Run your if test again. There should be no output this time, 
    because there are less than three people in the list.
	Bonus: Store your if test in a function called something like crowd_test.
"""
#ANSWER:
def crowd_test(lst):
    if len(lst) > 3:
        print("The room is crowded with people")
        lst.pop()
        lst.pop()
        print(lst)
    
name_list = ['John','Jordan','Jake','Joel']
print(crowd_test(name_list))


"""
    Three is a Crowd - Part 2
	Save your program from Three is a Crowd under a new name.
	Add an else statement to your if tests. If the else statement is run, have it print a message that the room is not very crowded.
"""
def crowd_test1(lst):
    if len(lst) > 3:
        print("The room is crowded with people")
        lst.pop()
        lst.pop()
        print(lst)
    else:
        print("Room is not very crowded")
    
name_list = ['John','Jordan','Jake']
print(crowd_test1(name_list))

"""
    Six is a Mob
	Save your program from Three is a Crowd - Part 2 under a new name.
	Add some names to your list, so that there are at least six people in the list.
	Modify your tests so that
    If there are more than 5 people, a message is printed about there being a mob in the room.
    If there are 3-5 people, a message is printed about the room being crowded.
    If there are 1 or 2 people, a message is printed about the room not being crowded.
    If there are no people in the room, a message is printed abou the room being empty.
"""
def crowd_test2(lst):
    if len(lst) > 5:
        print("There's a mob in the room")
    elif len(lst) > range(3, 5):
        print("The room is crowded with people")
    elif len(lst) == 1 or len(lst) == 2:
        print("The room is crowded with people")
    else:
        print("Room is empty")
    
name_list = ['John','Jordan','Jake','Joel','Joan','Jhal']
print(crowd_test2(name_list))