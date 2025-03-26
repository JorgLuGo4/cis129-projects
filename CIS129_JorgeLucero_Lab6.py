#Script: Hot dogs - CIS129_JorgeLucero_Lab6
#Action: This script calculates the amount of hot dogs needed for a cookout and calculates the leftovers
#Author: Jorge Lucero
#Date: 2/26/25

import math

# calculating hotdogs
def get_total_hot_dogs():
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs = int(input("Enter the number of hot dogs for each person: "))
    total_hot_dogs = people * hot_dogs
    return total_hot_dogs

# display results
def show_results(dogs_left, min_dogs, buns_left, min_buns):
    print("Minimum packages of hot dogs needed:", min_dogs)
    print("Minimum packages of hot dog buns needed:", min_buns)
    print("Hot dogs left over:", dogs_left)
    print("Hot dog buns left over:", buns_left)

def main():
    DOGS = 10  # Hot dogs per package
    BUNS = 8   # Buns per package
    
    total = get_total_hot_dogs()
    
    # calculating the leftovers
    dogs_left = total % DOGS  
    buns_left = total % BUNS  
    
    # calculate the minimum number of packages needed
    min_dogs = math.ceil(total / DOGS)
    min_buns = math.ceil(total / BUNS)
    
    # display the results
    show_results(dogs_left, min_dogs, buns_left, min_buns)

# run the program
if __name__ == "__main__":
    main()
