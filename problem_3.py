def partition(input_list, left, right):
    pivot = input_list[right]
    i = left - 1

    for j in range(left, right):
        if input_list[j] >= pivot:
            i = i + 1
            (input_list[i], input_list[j]) = (input_list[j], input_list[i])

    (input_list[i + 1], input_list[right]) = (input_list[right], input_list[i + 1])

    return i + 1


def quickSort(array, left, right):
    if left < right:

        pi = partition(array, left, right)

        quickSort(array, left, pi - 1)

        quickSort(array, pi + 1, right)

def array_to_int(array):
    output = 0
    for number in array:
        output = output * 10 + number
    return output 


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) < 2:
        return [None, None]
    
    quickSort(input_list,0,len(input_list)-1) 

    num_1 = []
    num_2 = []
    add_to_1 = True
    for i in input_list:
        if add_to_1 is True:
            num_1.append(i)
        else:
            num_2.append(i)
        add_to_1 = not add_to_1
    return [array_to_int(num_1), array_to_int(num_2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test case 1
test_function([[1, 2, 3, 4, 5], [542, 31]])

#Test case 2
test_function([[4, 2, 2, 5, 7, 3, 1, 1, 9, 8], [97421, 85321]])

# Test case 3
print(rearrange_digits([1]))  # [None, None]

# Test case 4
print(rearrange_digits([]))  # [None, None]

# Test case 5
print(rearrange_digits([7, 2]))  # [7, 2]
