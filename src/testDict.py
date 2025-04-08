# from collections import defaultdict

# class TrieNode:
#     __slots__ = ("children", "is_word")

#     def __init__(self):
#         """
#         Initialize a Trie node with:
#         - children: dictionary mapping character to TrieNode.
#         - is_word: flag to indicate if the node represents the end of a valid word.
#         """
#         # self.children = {}
#         # self.is_word = False

#         """Initialize TrieNode with optimized dictionary storage."""
#         self.children = defaultdict(TrieNode)  # Avoids repeated 'if not in' checks
#         self.is_word = False


# class Dictionary:
#     def __init__(self, words=None):
#         """
#         Initialize the Dictionary using a Trie.
#         - words: Iterable of words to load into the Trie.
#         If no words are provided, it initializes an empty dictionary.
#         """
#         self.root = TrieNode()
#         # if words is None:
#         #     words = []
#         # for word in words:
#         #     self.insert(word.lower())
#         if words:
#             self.bulk_insert(words)
            


#     # def bulk_insert(self, words):
#     #     """Insert multiple words efficiently using a single traversal loop."""
#     #     for word in words:
#     #         node = self.root
#     #         for char in word:
#     #             node = node.children[char]  # Uses defaultdict to remove explicit checks
#     #         node.is_word = True

#     def bulk_insert(self, words):
#         """Insert multiple words efficiently using a single traversal loop."""
#         print(f"Inserting {len(words)} words into the Trie...")
#         count = 0
#         for word in words:
#             node = self.root
#             for char in word.lower():
#                 node = node.children[char]  # ✅ Uses defaultdict, so no need for explicit checks
#             node.is_word = True
#             count += 1
#             if count % 10000 == 0:  # Print every 10,000 words
#                 print(f"{count} words inserted so far...")
#         print(f"✅ Successfully inserted {count} words into the Trie.")


#     def insert(self, word):
#         """
#         Insert a word into the Trie.
#         """
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node = node.children[char]  # Uses defaultdict for efficiency
#                 # node.children[char] = TrieNode()
#                 # node = node.children[char]
#         node.is_word = True

#     def is_word(self, word):
#         """
#         Check if a word exists in the dictionary.
#         Returns True if the complete word is present, False otherwise.
#         """
#         # node = self.root
#         # for char in word.lower():
#         #     if char not in node.children:
#         #         return False
#         #     node = node.children[char]
#         # return node.is_word
#         node = self._traverse(word)
#         return node.is_word if node else False
    
#     def _traverse(self, sequence):
#         """Helper function to traverse the Trie efficiently."""
#         node = self.root
#         for char in sequence:
#             node = node.children[char]  # Avoids KeyError
#             if node is None:
#                 return None
#         return node


#     def has_prefix(self, prefix):
#         """
#         Check if there is any word in the dictionary that starts with the given prefix.
#         Returns True if the prefix exists in the Trie, False otherwise.
#         """
#         # node = self.root
#         # for char in prefix.lower():
#         #     if char not in node.children:
#         #         return False
#         #     node = node.children[char]
#         # return True
#         return self._traverse(prefix) is not None