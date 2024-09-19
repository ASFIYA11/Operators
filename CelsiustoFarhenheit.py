'''You are given a temperature in Celsius. You need to convert it to Fahrenheit.
Input and Output Format
Input Format:
A single integer celsius.
Output Format:
A single line containing the temperature in Fahrenheit.
To convert a temperature from Celsius to Fahrenheit, you use the following formula:
Multiply the temperature in Celsius by 9/5.
Add 32 to the result of step 1.
Sample Input 1
0
Sample Output 1
32.0
Sample Input 2
25
Sample Output 2
77.0
Sample Input 3
100
Sample Output 3
212.0
'''

# Input the temperature in Celsius
celsius = float(input())

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Output the temperature in Fahrenheit
print(fahrenheit)
