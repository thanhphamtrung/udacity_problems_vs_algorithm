# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point``
        suffixes = []
        for char, node in self.children.items():
            if node.is_word:
                suffixes.append(suffix + char)
            if node.children:
                suffixes += node.suffixes(suffix + char)
        return suffixes


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.insert(char)
            cur_node = cur_node.children[char]
        cur_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.children:
                return None
            cur_node = cur_node.children[char]

        return cur_node


# Test cases for find function:
# Test data:
list_word = ['teacher', 'chemistry', 'biology', 'geography', 'exercise']
prefix_list = ['t', 'ch', 'z', 'bio', 'pre']
trie = Trie()

for word in list_word:
    trie.insert(word)

for p in prefix_list:
    if trie.find(p):
        print('The prefix "{}" IS IN list word.'.format(p))
    else:
        print('The prefix "{}" IS NOT IN list word.'.format(p))


# Test cases for suffixes function:
trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    trie.insert(word)

word_to_find_suffixes = trie.find(prefix='a')

print(word_to_find_suffixes.suffixes())
