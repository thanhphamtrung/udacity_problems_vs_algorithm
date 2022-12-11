This problem is solved with Trie data structure. Words are inserted as the dictionary problem.
=> The insert method is implemented like what lectures show in this course => O(n)
=> in worst case: we need n node for n non-duplicate character => space: O(n)

- find method: I just loop through the trie once so in worst case (non-duplicate character in trie):
    Time and Space Complexities:
    - Time: O(n)
    - Space: O(1)

- suffixes method: I also loop through the entire trie once, but we dont know how deep the trie is, so:
    Time and Space Complexities:
    - Time: O(n)
    - Space: O(n)