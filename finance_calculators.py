import math

# Output options for the user
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Prompt the user to select a calculation option
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed:")

# Normalize the user input to lowercase
user_input = user_input.lower()

# Branch based on user's choice of calculation: 'investment' or 'bond'
if user_input == "investment":

    # Gather necessary inputs for investment calculation
    amount = int(input("Please enter the amount of money that you are depositing"))
    rate = int(input("Please enter the interest rate as a percentage without '%'"))
    rate = rate / 100
    time = int(input("Please enter the number of years you plan on investing"))
    interest = input("Please enter either 'simple' or 'compound'")

    # Calculate interest based on user's choice: 'simple' or 'compound'
    if interest == "simple":
        simple_interest = amount * (1 + (rate * time))
        print("The amount you will get back is: " + str(simple_interest))
    elif interest == "compound":
        compound_interest = amount * math.pow((1+rate),time)
        print("The amount you will get back is: " + str(compound_interest))
    else:
        print("Please enter a valid input")

elif user_input == "bond": 

    # Gather necessary inputs for bond repayment calculation
    house_value = int(input("Please enter the present value of the house as a number only"))
    interest_rate = int(input("Please enter the interest rate as a number only"))
    interest_rate = (interest_rate / 100) / 12
    months = int(input("Please enter the number of months you plan to take to repay the bond"))

    # Calculate monthly repayment for the bond
    repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-months))
    print("The amount of money you will have to repay each month is: " + str(repayment))

else:
    print("Please enter a valid input")
