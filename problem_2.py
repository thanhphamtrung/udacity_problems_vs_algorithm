def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list is None or len(input_list) == 0:
        return -1

    r_index = len(input_list)
    p = get_pivot_index(input_list, 0, r_index-1)

    # The list was sorted
    if p == -1:
        return binary_search(input_list, number, 0, r_index-1)

    if input_list[p] == number:
        return p

    if input_list[0] <= number:
        return  binary_search(input_list[:p], number)
    return p + 1 + binary_search(input_list[p+1:], number)


# Get pivot position
def get_pivot_index(array, l, r):
    if l == r:
        return l
    elif l > r:
        return -1

    mid = int((l + r)/2)

    if mid > l and array[mid-1] > array[mid]:
        return mid-1
    if r > mid and array[mid] > array[mid + 1]:
        return mid
    if array[mid] > array[l]:
        return get_pivot_index(array, mid + 1, r)
    return get_pivot_index(array, l, mid-1)


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# edge case
print(rotated_array_search([], 11))
print(rotated_array_search(None, 11))
print(rotated_array_search([1], 11))
