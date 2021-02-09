def remove_even(list):
    # List comprehension to iter over List and add to new list if not even
    return [number for number in list if number % 2 != 0]


print(remove_even([3, 2, 41, 3, 34]))