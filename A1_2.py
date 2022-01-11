#Coding Ex: 2

""" 1.	Numbers: Example code to add two numbers 50+50 and 100-10 and print it. """
a = (50 + 50)
b = (100 - 10)
print((50+50) + (100-10))
print(a + b)
print(a, b)

""" 2.	30+*6, 6^6, 6**6, 6+6+6+6+6+6 """
#a = 30+*6
b = 6^6
c = 6**6
d = 6+6+6+6+6+6
print(b ,c ,d)

"""3. Print “Hello World” on the console output. Print output “Hello World : 10” // Make sure capitalization and spacing matches."""
print("Hello World")
print("Hello World: 10")

"""4.	Below is a mathematical calculation exercise :

    Mathematically, mortgage works by the following algorithm:
    •	Joel borrows big money sum P from bank (and performs purchase);
    •	bank tells him its interest rate R in percents - the speed of growth of the debt;
    •	at the end of each month the debt is increased by R / 12 percents;
    •	immediately after it Joel gives to bank some predefined small sum M to decrease the debt;
    •	debt is considered settled when its value is reduced to zero (this could take several years).
    For example, Joel takes P = $800,000 from bank with interest rate of R = 6%. He is willing to pay M = $10000 at the end of each month.

ANSWER: MAX months to pay back is 81 Months (6.75 years) with Monthly Payment = $9926 Dollars. 
        If he willing to pay $10000 at the end of each month.
""" 
# b_amount = Amount Wants to Borrow 
b_amount = input("Amount Want to Borrow: ")
b_amount = int(b_amount)

# i_rates = Interest Rates
i_rates = (0.06/12)
print('Interest Rate: 6%')

# months = Months wanted to pay back
months = input("Months to Pay Back: ")
months = int(months)

# m_payment = amount needed to pay back each month
m_payment = ((b_amount + (b_amount * i_rates)) / months)
m_payment = round(m_payment)

print(f"Monthly payment is: ${m_payment} dollars")
