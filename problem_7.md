This problem is quite same with problem 5. I used Trie to store all the paths (children) that split by `/`.

For split method, I just apply what lecture teach me in this course. - Time complexity: O(n)
        - Space complexity: O(n)

For lookup method, I used find and split_path method with both O(n), so       - Time complexity analysis: O(n)
                    - Space complexity analysis: O(n)

# RouteTrie
## __init__(self):
- Time: O(1)
- Space: O(1)

## insert_node(self, path, handler):
- Time: O(n)
- Space: O(n)

## find(self, path):
- Time: O(n)
- Space: O(1)

# RouteTrieNode
## __init__(self):
- Time: O(1)
- Space: O(1)

## insert(self, path):
- Time: O(1)
- Space: O(1)

# Router
## __init__(self):
- Time: O(1)
- Space: O(1)

## add_handler(self, path, handler):
- Time: O(n)
- Space: O(n)

## lookup(self, path):
- Time: O(n)
- Space: O(n)

## split_path(self, path):
- Time: O(n)
- Space: O(n)
