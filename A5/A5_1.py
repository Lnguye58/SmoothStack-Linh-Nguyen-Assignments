""" Let us apply our programming skills to some quasi-scientific problem - since it is bit dull to learn only abstract things.
    The simple measure of body constitution was proposed at the middle of XIX century.
    It depends only on the height and weight of a person - and is called Body Mass Index or BMI. It is defined as:
        BMI = weight / height^2
    Where weight is taken in kilograms and height in meters.
    Four general grades are proposed:
        Underweight     -           BMI < 18.5
        Normal weight   -   18.5 <= BMI < 25.0
        Overweight      -   25.0 <= BMI < 30.0
        Obesity         -   30.0 <= BMI
    For example, if I have weight of 80 kg and height of 1.73 m I can calculate:
        BMI = 80 / (1.73)^2 = 26.7
    i.e. somewhat overweight.
    We will not discuss how proper or improper this gradation is. Instead you should simply calculate grades for several people.
"""

def BMI():

    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kg: "))
    bmi = weight/(height**2) 

    if (bmi < 18.5):
        print("Underweight")
    elif (bmi >= 18.5 and bmi < 25.0):
        print("Normal weight")
    elif (bmi >= 25.0 and bmi < 30.0):
        print("Overweight")
    elif (bmi >= 30.0):
        print("Obesity")

BMI()
