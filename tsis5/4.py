import re 
temp = str(input("Enter text: "))
def text_match(text):
    patterns = "^a.*?b$"
    if re.search(patterns,  text):
                return 'Found a match!'
    else:
                return('Not matched!')
    
print(text_match(temp))