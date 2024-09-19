''' There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
'''
# Get input from the user
x = int(input("Enter the seating capacity of L1: "))
y = int(input("Enter the seating capacity of L2: "))
z = int(input("Enter the seating capacity of L3: "))
n = int(input("Enter the number of students: "))

# Initialize a dictionary to store the seating capacities
labs = {"L1": x, "L2": y, "L3": z}

# Filter out labs that cannot accommodate the students
suitable_labs = {lab: capacity for lab, capacity in labs.items() if capacity >= n}

# Find the lab with the minimal seating capacity among the suitable labs
if suitable_labs:
    optimal_lab = min(suitable_labs, key=suitable_labs.get)
    print(optimal_lab)
else:
    print("No lab can accommodate the students")
