import re

string = input("Enter a string: ")

pattern = r'a.+b$'

match = re.search(pattern, string)

print(match.group() if match else None)
