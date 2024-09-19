'''A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00

'''
# Get input from the user
total_cost = float(input("Enter the total cost (Rs.): "))
sold_cost_per_banana = float(input("Enter the sold cost per banana (Rs.): "))

# Calculate the total selling price for a dozen bananas
total_selling_price = sold_cost_per_banana * 12

# Calculate profit or loss
profit_or_loss = total_selling_price - total_cost

# Determine if it's a profit or loss and print the result
if profit_or_loss > 0:
    print(f"Profit : Rs.{profit_or_loss:.2f}")
else:
    print(f"Loss : Rs.{-profit_or_loss:.2f}")
