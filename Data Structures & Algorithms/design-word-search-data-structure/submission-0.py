class Node:
    def __init__(self, c, isWord):
        self.c = c
        self.next = {}
        self.isWord = isWord
class WordDictionary:

    def __init__(self):
        self.d = Node("",False)

    def addWord(self, word: str) -> None:
        if word == '':
            self.d.isWord = True
        node = self.d
        for c in word:
            if c in node.next:
                node = node.next[c]
            else:
                node.next[c] = Node(c,False)
                node = node.next[c]
        node.isWord = True
        

    def search_node(self,node,word):
        if word == '':
            return node.isWord
        if not node:
            return False
        if word[0] in node.next: 
            return self.search_node(node.next[word[0]],word[1:])
        elif word[0] == '.':
            result = False
            for key in node.next.keys():
                result = result or self.search_node(node.next[key],word[1:])
            return result
        return False

    def search(self, word: str) -> bool:
        return self.search_node(self.d,word)


