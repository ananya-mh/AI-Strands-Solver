#This file was used to create the dictionary to efficiently store and check for the existence of words.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Dictionary:
    def __init__(self, words=None):
        self.root = TrieNode()
        if words is None:
            words = []
        for word in words:
            self.insert(word.lower())

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def is_word(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def has_prefix(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return True
