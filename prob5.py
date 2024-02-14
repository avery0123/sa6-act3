def raise_to_power(numbers, n):
    powered_list = list(map(lambda x: x**n, numbers))
    return powered_list


numbers_list = [2, 3, 4, 5]
constant_n = 3
result_powered_list = raise_to_power(numbers_list, constant_n)

print(f"The list after raising each number to the power of {constant_n} is: {result_powered_list}")
