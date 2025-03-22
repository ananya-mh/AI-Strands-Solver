class TrieNode:
    def __init__(self):
        """
        Initialize a Trie node with:
        - children: dictionary mapping character to TrieNode.
        - is_word: flag to indicate if the node represents the end of a valid word.
        """
        self.children = {}
        self.is_word = False


class Dictionary:
    def __init__(self, words=None):
        """
        Initialize the Dictionary using a Trie.
        - words: Iterable of words to load into the Trie.
        If no words are provided, it initializes an empty dictionary.
        """
        self.root = TrieNode()
        if words is None:
            words = []
        for word in words:
            self.insert(word.lower())

    def insert(self, word):
        """
        Insert a word into the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def is_word(self, word):
        """
        Check if a word exists in the dictionary.
        Returns True if the complete word is present, False otherwise.
        """
        node = self.root
        for char in word.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def has_prefix(self, prefix):
        """
        Check if there is any word in the dictionary that starts with the given prefix.
        Returns True if the prefix exists in the Trie, False otherwise.
        """
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return True
