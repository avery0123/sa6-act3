# Function to find the intersection of two lists
def find_intersection(list1, list2):
    intersection = list(filter(lambda x: x in list2, list1))
    return intersection
list1 = [1, 2, 3, 4, 5, 7]
list2 = [3, 4, 5, 6, 7]
result_intersection = find_intersection(list1, list2)

print(f"The intersection of the two lists is: {result_intersection}")
