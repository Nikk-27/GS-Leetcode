class TrieNode:
    def __init__(self):
        self.children = {}
        self.endword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endword = True

    def search(self, word: str) -> bool:
        cur = self.root
        def dfs(n, child):
            cur = child

            for c in range(n, len(word)):
                if word[c] == '.':
                    for child in cur.children.values():
                        if dfs(c+1, child):
                            return True
                    return False
                else:
                    if word[c] not in cur.children:
                        return False
                    cur = cur.children[word[c]]
            return cur.endword

        return dfs(0, cur)

# TC = O(n) for both add and search
# SC = O(n + t)

# Where n is the length of the string and t is the total number of TrieNodes created in the Trie.
                


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)