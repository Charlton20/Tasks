import math
# Print instruction for user
print("""Choose either 'investment' or 'bond' below to proceed:
""")

# Print Definition of Investment and Bond for user
print("INVESTMENT - To calculate the amount of interest you will earn on interest.")
print("""BOND - To calculate the amount you will have to pay on a home loan.
""")

# Request calculation from user
user_calculation = input("Choose either investment or bond: ").lower()


if user_calculation == "investment":
    # Print user_calculation if user selects Investment

    # Ask user for their deposit amount
    user_amount_deposit = float(input("Enter your amount of deposit here: "))

    # Ask user to enter the interest rate
    user_interest_rate = float(input("Enter your interest rate: "))

    # Ask user to enter the number of years
    user_num_of_years = float(input("Enter number of years: "))

# Ask user if they wnt simple or compound interest
    interest = input("Do you want simple or compound interest?: ").lower()

    if interest == 'simple':

        # Below is the formula for simple interest
        simple_interest = user_amount_deposit*(1+(user_interest_rate/100)*user_num_of_years)
        print('Your simple interest is -', round(simple_interest))

    elif interest == 'compound':

        # Below is the formula for compound interest
        compound_interest = user_amount_deposit * math.pow((1+(user_interest_rate/100)), user_num_of_years)
        print('Your compound interest is -', round(compound_interest))

elif user_calculation == "bond":

    # Ask user for the present value of the house
    present_house_value = float(input('Please enter the present value of the house?: '))

    # Ask user for the interest rate
    interest_rate = float(input('Please enter the interest rate: '))

    # Ask user to enter their number of months they plan on repaying
    num_of_months_to_repay = float(input('Enter the number of months you plan on repaying the bond: '))

    # Below is the formula for calculating the bond
    bond_amount = ((interest_rate/100/12)*present_house_value)/(1-(1+(interest_rate/100/12))**(-num_of_months_to_repay))
    print('Your bond amount is -', round(bond_amount))