# Solution for this exercise: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/tutorial/
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.weights = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word,weight):
        node = self.root
        for char in word:
            if char not in node.children:
                new_node = TrieNode()
                node.children[char] = new_node
                node = new_node
            else:
                node = node.children[char]
            if weight > node.weights:
                node.weights = weight
        node.end=True

    def search(self,word):
        node = self.root

        for char in word:
            if char not in node.children:
                return -1
            else:
                node = node.children[char]
        return node.weights

if __name__=="__main__":
    entries,queries = list(map(int,input().split()))
    t = Trie()
    #adding entries
    while entries:
        string,weight = list(input().split())
        t.insert(string,int(weight))
        entries-=1
    #querying
    while queries:
        string = input()
        print(t.search(string))
        queries-=1
'''



class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                new_node = TrieNode()
                node.children[char] = new_node
                node = new_node
            else:
                node = node.children[char]
        node.end = True
    
    def search(self,word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end

    def prefix(self,word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        
    
if __name__ == "__main__":
    t = Trie()
    t.insert('apple')
    t.insert('cat')
    print(t.search('apple'))
    print(t.search('dog'))
    print(t.prefix('apl'))    
    
