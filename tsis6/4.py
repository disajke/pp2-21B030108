import time
import math

# Prompt the user for the input values
number = int(input("Enter a number: "))
delay = int(input("Enter the delay in milliseconds: "))

# Convert the delay to seconds
delay_secs = delay / 1000

# Wait for the specified delay
time.sleep(delay_secs)

# Calculate the square root of the input number
sqrt_number = math.sqrt(number)

# Print the result
print(f"Square root of {number} after {delay} milliseconds is {sqrt_number}")