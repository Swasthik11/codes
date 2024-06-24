# Print a welcome message
print("Welcome to the tip calculator")

# Input the total bill amount from the user
bill = float(input("What was the total bill? $"))

# Input the tip percentage the user wants to give (10, 12, or 15)
print("What percentage tip would you like to give? 10, 12, or 15?")
tip_percentage = int(input())

# Input the number of people splitting the bill
num_people = int(input("How many people to split the bill? "))

# Calculate the tip amount based on the percentage
tip_amount = bill * (tip_percentage / 100)

# Calculate the total bill including the tip
total_bill = bill + tip_amount

# Calculate the amount each person should pay
amount_per_person = total_bill / num_people

# Display the amount each person should pay, formatted to two decimal places
print(f"Each person should pay: ${amount_per_person:.2f}")
