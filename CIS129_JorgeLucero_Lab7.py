#Script: Therater Seating lab - CIS129_JorgeLucero_Lab7
#Action: This code calculates the amount of tickets sales for all sections and gives you the results
#Author: Jorge Lucero
#Date: 4/01/25

# Number of total seats for each section
SECTION_A_SEATS = 300
SECTION_B_SEATS = 500
SECTION_C_SEATS = 200
# define prices for each section
PRICE_A = 20
PRICE_B = 15
PRICE_C = 10

def get_tickets_sold(section_name, max_seats):
    """Ask the user how many tickets they sold for a section and check if it's a valid number."""
    while True:
        try:
            tickets_sold = int(input(f"How many tickets were sold for section {section_name} (Max {max_seats}): "))

            if tickets_sold < 0 or tickets_sold > max_seats:
                print(f"Please enter a number between 0 and {max_seats}.")
            else:
                return tickets_sold
        except ValueError:
            print("Please enter a valid number.")

def calculate_income(tickets_sold, price_per_ticket):
    """Calculate total income for a section."""
    return tickets_sold * price_per_ticket

def main():
    print("Ready to see how many tickets you sold?")
    
    tickets_sold_A = get_tickets_sold("A", SECTION_A_SEATS)
    tickets_sold_B = get_tickets_sold("B", SECTION_B_SEATS)
    tickets_sold_C = get_tickets_sold("C", SECTION_C_SEATS)
    
    income_A = calculate_income(tickets_sold_A, PRICE_A)
    income_B = calculate_income(tickets_sold_B, PRICE_B)
    income_C = calculate_income(tickets_sold_C, PRICE_C)

    # dalculating total income 
    total_income = income_A + income_B + income_C

    # displayign results
    print("\nHere are the results:")
    print(f"Section A: {tickets_sold_A} tickets sold, ${income_A} income.")
    print(f"Section B: {tickets_sold_B} tickets sold, ${income_B} income.")
    print(f"Section C: {tickets_sold_C} tickets sold, ${income_C} income.")
    print(f"Total income from all sections: ${total_income}")

# call main to run the program
if __name__ == "__main__":
    main()
