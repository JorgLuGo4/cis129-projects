# Module 5 Lab-5 
# Add your name here 
# Name: {Jorge Lucero]

# Add the date here 
# Date: [03/05/35]

# Describe what the program does here 
# This program calculates and displays the store and employee bonuses based on monthly sales and sales increase.

# The main function
def main():
    # declare local variables
    monthlySales = 0  # Monthly sales amount (to 0)
    storeAmount = 0   # Store bonus amount (o 0)
    empAmount = 0     # Employee bonus amount (to 0)
    salesIncrease = 0.0  # Percent of sales increase (to 0.0)

    # call to getSales() 
    monthlySales = getSales("Enter the monthly sales amount: ")

    # call to getIncrease()
    salesIncrease = getIncrease("Enter the sales increase percentage: ")

    # call to calcStoreBonus() 
    storeAmount = calcStoreBonus(monthlySales)

    # call to calcEmpBonus() 
    empAmount = calcEmpBonus(salesIncrease)

    # call to printBonus()
    printBonus(storeAmount, empAmount)

# This function gets the monthly sales
def getSales(prompt):
    monthlySales = float(input(prompt))  
    return monthlySales  

# This function gets the percent of increase in sales
def getIncrease(prompt):
    salesIncrease = float(input(prompt))  
    salesIncrease = salesIncrease / 100  
    return salesIncrease  

# This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000  
    elif monthlySales >= 100000:
        storeAmount = 5000  
    elif monthlySales >= 90000:
        storeAmount = 4000  
    elif monthlySales >= 80000:
        storeAmount = 3000  
    else:
        storeAmount = 0  
    return storeAmount  

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75  
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40  
    else:
        empAmount = 0 
    return empAmount  

# This function prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)  
    print("The employee bonus amount is $", empAmount)  
    
   
    if storeAmount == 6000 and empAmount == 75:
        print('Congrats! You have reached the highest bonus amounts possible!')

# calls main
main()
