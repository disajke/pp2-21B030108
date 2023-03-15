import re

string = input('Enter a string: ')

pattern = r'[A-Z][^A-Z]*'

result = re.findall(pattern, string)

print(result)