''' write a program to determine the fee amount to be collected from a student. 
Refer the table below for fee details.
  Student Type  
  Student Type denoted as  
  Fee Details  
Merit Seat Day Scholar
MSDS

Tuition fee + Bus fee



Merit Seat Hosteller
MSH
Tuition fee + Hostel fee

Management Seat Day Scholar



MGSDS

150% of Tuition fee + Bus fee



Management Seat Hosteller
MGSH

150% of Tuition fee + Hostel fee




Input format:
The first input corresponds to the student type
The second input corresponds to the tuition fee
The third input corresponds to the bus fee or hostel fees
Output format:
Print the total fee amount of the corresponding student with 2 decimal places.
Refer below sample output for formatting
Sample Input:
MSH
40000
50000
Sample Output:
90000.00
'''
# Get input from the user
student_type = input("Enter the student type: ")
tuition_fee = float(input("Enter the tuition fee: "))
additional_fee = float(input("Enter the bus fee or hostel fee: "))

# Calculate the total fee based on the student type
if student_type == "MSDS":
    total_fee = tuition_fee + additional_fee
elif student_type == "MSH":
    total_fee = tuition_fee + additional_fee
elif student_type == "MGSDS":
    total_fee = 1.5 * tuition_fee + additional_fee
elif student_type == "MGSH":
    total_fee = 1.5 * tuition_fee + additional_fee
else:
    total_fee = 0
    print("Invalid student type")

# Print the total fee amount with 2 decimal places
if total_fee != 0:
    print(f"{total_fee:.2f}")

