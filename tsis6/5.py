# Prompt the user to enter the elements of the tuple
elements = input("Enter the elements of the tuple separated by spaces: ").split()

# Convert the input elements to booleans
my_tuple = tuple(map(lambda x: x.lower() == 'true', elements))

if all(my_tuple):
    print("All elements of the tuple are true")
else:
    print("Not all elements of the tuple are true")