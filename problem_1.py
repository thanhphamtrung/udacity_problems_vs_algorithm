def   sqrt(number):
      """
      Calculate the floored square root of a number

      Args:
         number(int): Number to find the floored squared root
      Returns:
         int: Floored Square Root
      """
      return binary_search(number,2,number//2)


def binary_search(target, start, end):
    if target == 1 or target == 0:
        return target
    start_index = start
    end_index = end
    mid = (start_index + end_index) // 2
    if mid*mid == target:
         return mid
    elif mid*mid < target:
         # 0.5 just a constant to get the floor value
         if (mid + 0.5) * (mid + 0.5) > target:
            return mid
         return binary_search(target, mid + 1, end_index)
    else:
         return binary_search(target, start_index, mid - 1)


# print("Pass" if (3 == sqrt(9)) else "Fail")
# print("Pass" if (0 == sqrt(0)) else "Fail")
# print("Pass" if (4 == sqrt(16)) else "Fail")
# print("Pass" if (1 == sqrt(1)) else "Fail")
# print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (65071685350 == sqrt(4234324234324234234234)) else "Fail")
