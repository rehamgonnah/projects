import math

# output shown to the user as the program runs
# asks the user to input what they want to calculate
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed:")

# unify the inputs regardless of how the user inputs their choice of calculation
user_input = user_input.lower() # changes all input to lower case 

# if-elif-else statement based on the user's choice of calculator: 'investment' or 'bond'
if user_input == "investment":

    # ask user to input values to calculate interest if 'investment' calculator chosen
    amount = int(input("Please enter the amount of money that you are depositing"))
    rate = int(input("Please enter the interest rate as a percentage without '%'"))
    rate = rate / 100
    time = int(input("Please enter the number of years you plan on investing"))
    interest = input("Please enter either 'simple' or 'compound'")

    # nested if-elif-else statement if user chooses 'investment' calculator to calculate the interest based on type: 'simple' or 'compound'
    if interest == "simple":
        simple_interest = amount * (1 + (rate * time)) # calculates simple interest
        print("The amount you will get back is: " + str(simple_interest)) # prints value calculated
    elif interest == "compound":
        compound_interest = amount * math.pow((1+rate),time) # # calculates compound interest by calling function from math package
        print("The amount you will get back is: " + str(compound_interest)) # prints value calculated
    else:
        print("Please enter a valid input") # output if neither 'simple' or 'compound' was inputted

elif user_input == "bond": 
    # ask user to input values to calculate repayment if 'bond' calculator chosen
    house_value = int(input("Please enter the present value of the house as a number only"))
    interest_rate = int(input("Please enter the interest rate as a number only"))
    interest_rate = (interest_rate / 100) / 12
    months = int(input("Please enter the number of months you plan to take to repay the bond"))
    repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-months)) # calculates repayment 
    print("The amount of money you will have to repay each month is: " + str(repayment))

else:
    print("Please enter a valid input")




