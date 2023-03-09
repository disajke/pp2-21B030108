def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

input_str = input("Enter a list of numbers: ")

num_str_lst = input_str.split()
num_lst = [int(num_str) for num_str in num_str_lst]

result = multiply_list(num_lst)
print("Result:", result)