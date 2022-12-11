This problem is solved with Trie data structure. Words are inserted as the dictionary problem.
=> The insert method is implemented like what lectures show in this course => O(n)
=> in worst case: we need n node for n non-duplicate character => space: O(n)

 - find method: I just loop through the trie once so in worst case (non-duplicate character in trie):
 - suffixes method: I also loop through the entire trie once, but we dont know how deep the trie is, so:

# TrieNode
## __init__(self): 
I just assign         
    self.is_word = False
    self.children = {}
- Time: O(1)
- Space: O(1)

## insert(self, char):
I just assign  
    self.children[char] = TrieNode()
- Time: O(1)
- Space: O(1)

## suffixes(self, suffix = ''):
I loop through all node below the point, so:
- Time: O(n)
- Space: O(n)


# Trie
## __init__(self):
I just assign
    self.root = TrieNode()
- Time: O(1)
- Space: O(1)

## insert(self, word):
For each word need to insert, I loop through all char in that word, so
- Time: O(n)
- Space: O(n)

## find(self, prefix):
For each word need to find, I loop through all char in that prefix, so
- Time: O(n)
- Space: O(1)