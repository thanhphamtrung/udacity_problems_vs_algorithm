The idea is use low for `0`, mid for `1` and high for `2`, whenever 
- input_list[mid] == 0 swap mid with low
- input_list[mid] == 2 swap mid with high,
- input_list[mid] == 1 do nothing,

Time and Space Complexities:
- Time: O(n)
- Space: O(1)