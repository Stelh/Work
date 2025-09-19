# Necessary import for Python 3
import sys

def process_input(input_string):
    # Try to copy the string to an integer
    try:
        integer_value = int(input_string)
    # If the conversion is successful, print the integer value
        print(integer_value)
    # If an error occurs during the conversion, print a custom error message
    except ValueError:
        print("Error: Input string is not a valid integer.")
input_string = sys.stdin.readline().strip()
process_input(input_string)