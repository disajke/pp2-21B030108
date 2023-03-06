from functools import reduce

numbers = input("Enter a list of numbers separated by spaces: ").split()
# The input() function returns a string, so we split it into a list of strings

numbers = [int(num) for num in numbers]  # Convert each string to an integer

result = reduce(lambda x, y: x * y, numbers)

print(result)