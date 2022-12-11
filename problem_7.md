This problem is quite same with problem 5. I used Trie to store all the paths (children) that split by `/`.

For split method, I just apply what lecture teach me in this course. - Time complexity: O(n)
        - Space complexity: O(n)

For lookup method, I used find and split_path method with both O(n), so       - Time complexity analysis: O(n)
                    - Space complexity analysis: O(n)

# RouteTrie
## __init__(self):
I just assign 
        self.root = RouteTrieNode()
        self.handler = root_handle
- Time: O(1)
- Space: O(1)

## insert_node(self, path, handler):
I loop through input path to insert each item in the path to the current point of the path, so 
- Time: O(n)
- Space: O(n)

## find(self, path):
I loop through input path till it have no children to find out the handler, so:
- Time: O(n)
- Space: O(1)

# RouteTrieNode
## __init__(self):
I just assign
        self.childrens = {}
        self.handler = None
- Time: O(1)
- Space: O(1)

## insert(self, path):
I just assign 
       self.childrens[path] = RouteTrieNode()
- Time: O(1)
- Space: O(1)

# Router
## __init__(self):
I just assign
        self.router = RouteTrie(handler)
        self.error = "not found handler"
- Time: O(1)
- Space: O(1)

## add_handler(self, path, handler):
I used split_path and RouteTrie.insert method, so the complexity is come from these method
- Time: O(n)
- Space: O(n)

## lookup(self, path):
I used split_path and RouteTrie.find method, so the complexity is come from these method
- Time: O(n)
- Space: O(n)

## split_path(self, path):
I loop through all the item in the splited path from the input path (splited path is a array from str.split method), so:
- Time: O(n)
- Space: O(n)
