#Script: "Check Protection" - 8.1 exercise 
#Action: This code follows the instructions under 8.1 exercise in Deitel & Deitel
#Author: Jorge Lucero
#Date: 4/23/25

def check_protected_amount():
    amount = float(input("Enter the dollar amount: ")) # Do not use "," otherwise the code wont run, decimal points don't show problems

    amount_string = f"{amount:.2f}"

    final_amount = f"{amount_string:*>10}"

    print(f"Amount:   {final_amount}")
    print("Position: 0123456789")

check_protected_amount()
