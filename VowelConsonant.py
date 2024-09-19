'''Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
'''
# Get input from the user
char = input("Enter a character: ")

# Check if the input is a single alphabet character
if len(char) == 1 and char.isalpha():
    # Convert the character to lowercase for uniformity
    char = char.lower()
    # Check if the character is a vowel
    if char in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
