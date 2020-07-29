#PSET 1 PART B 100%

# Variables
portion_down_payment = 0.25  # (25%)
current_savings = 0  # Savings.
months = 0  # This is a counter.
r = 0.04

# Inputs
annual_salary = float(input("Annual Salary: "))
portion_saved = float(input("percent of salaray to save: "))
total_cost = float(input("Cost of dream home: "))
semi_annual_raise = float(input("Raise: "))

# Get monthly salary and the goal of downPayment
monthly_salary = (annual_salary / 12)  # Monthly salary = annual salary / 12
downPayment = total_cost * portion_down_payment  # downPayment is fixed at 25%, total cost of house X downPayment

# Solution
while current_savings <= downPayment: # Once the savings is higher/equal exit loop.
    current_savings += monthly_salary * portion_saved + (current_savings * r) / 12  # Savings  # The investment returns.
    months += 1  # Months counter.
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise

# Result
print(f"Your annual Salary: " + str(annual_salary))
print(f"percent of salary to save: " + str(portion_saved))
print(f"Cost of dream home: " + str(total_cost))
print("Number of months it would take: " + str(months))
