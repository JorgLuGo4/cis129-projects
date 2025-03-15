# Module 5 Lab 5 
# Add your name here 
# Name: {Jorge Lucero]

# Add the date here 
# Date: [03/15/35]

# Describe what the program does here
# The program tracks bottles returned each week, calculates the payout, and lets the user enter data for more weeks if they want.

# Step 1: Declare variables
totalBottles = 0
counter = 1
totalPayout = 0.0
keepGoing = "y"

# Step 2: Loop 
while keepGoing == "y":
    totalBottles = 0  # Reset total bottles for the new week
    counter = 1       

    # Loop for 7 days
    while counter <= 7:
        todayBottles = int(input(f"Enter number of bottles returned for day #{counter}: "))
        totalBottles += todayBottles  # Add the day's bottles to total
        counter += 1  # Move to the next day

    totalPayout = totalBottles * 0.10  # Calculate payout (10 cents per bottle)

    # Display results
    print(f"Total bottles: {totalBottles}")
    print(f"Total payout: ${totalPayout:.2f}")

    # Ask if the user wants to continue
    keepGoing = input("Do you want to enter another week's data? (y/n): ")

