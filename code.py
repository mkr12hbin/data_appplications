import math  # Import the math module to use the sqrt function

def sqrt_of_sum(num1, num2):
    # Calculate the sum of the two numbers
    sum_of_numbers = num1 + num2
    
    # Calculate the square root of the sum using the math.sqrt function
    square_root_of_sum = math.sqrt(sum_of_numbers)
    
    # Return the sum and the result of the square root calculation
    return sum_of_numbers, square_root_of_sum

# Example usage:
number1 = float(input("Enter the first number: "))  # Get the first number as input from the user
number2 = float(input("Enter the second number: "))  # Get the second number as input from the user

sum_result, sqrt_result = sqrt_of_sum(number1, number2)  # Call the function with the input numbers and store the results

# Print the sum and the square root result with formatted strings
print(f"The sum of {number1} and {number2} is: {sum_result}")
print(f"The square root of the sum is: {sqrt_result}")
