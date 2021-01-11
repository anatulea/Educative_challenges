'''Given a list, can you rotate its elements by one index from right to left'''
# Solution #1: Manual Rotation #
def right_rotate(lst, k):
    k = k % len(lst)
    rotatedList = []
    # get the elements from the end
    for item in range(len(lst) - k, len(lst)):
        rotatedList.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - k):
        rotatedList.append(lst[item])
    return rotatedList


print(right_rotate([10, 20, 30, 40, 50], abs(3)))

# Solution #2: Pythonic Rotation
def right_rotate(lst, k):
    # get rotation index
    k = k % len(lst)

    return lst[-k:] + lst[:-k]


print(right_rotate([10, 20, 30, 40, 50], abs(3)))