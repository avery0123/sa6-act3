def find_maximum(numbers, compare_function):
    if not numbers:
        return None
    maximum = numbers[0]

    for num in numbers[1:]:
        maximum = compare_function(maximum, num)

    return maximum

numbers_list = [12, 5, 8, 23, 3, 15]
greater_of_two = lambda x, y: x if x > y else y
max_number = find_maximum(numbers_list, greater_of_two)

print(f"The maximum number in the list is: {max_number}")
