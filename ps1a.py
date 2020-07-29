#PSET 1 PART A

# Variables
portion_down_payment = 0.25  # (25%)
current_savings = 0  # Savings.
months = 0  # This is a counter.
r = 0.04

# Inputs
annual_salary = float(input("Annual Salary: "))
portion_saved = float(input("percent of salaray to save: "))
total_cost = float(input("Cost of dream home: "))

# Get monthly salary and the goal of downPayment
monthly_salary = (annual_salary / 12)  # Monthly salary = annual salary / 12
downPayment = total_cost * portion_down_payment  # downPayment is fixed at 25%, total cost of house X downPayment

# Solution
while True:
    if current_savings >= downPayment: # Once the savings is higher/equal exit loop.
        break
    elif current_savings <= downPayment:
        months += 1 #  Months counter.
        current_savings += monthly_salary * portion_saved  # Savings
        current_savings += current_savings * r / 12  # The investment returns.

# Result
print(f"Your annual Salary: " + str(annual_salary))
print(f"percent of salary to save: " + str(portion_saved))
print(f"Cost of dream home: " + str(total_cost))
print("Number of months it would take: " + str(months))
