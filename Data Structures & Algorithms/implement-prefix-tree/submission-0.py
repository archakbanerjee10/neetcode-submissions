class PrefixTree:

    def __init__(self):
        self.trie_dict={}
        

    def insert(self, word: str) -> None:
        d=self.trie_dict
        for c in word :
            if c not in d:
                d[c]={}
            d=d[c]
        
        d['.']='.'


    def search(self, word: str) -> bool:
        d=self.trie_dict
        for c in word :
            if c not in d:
                return False
            d=d[c]
        return '.' in d
        

    def startsWith(self, prefix: str) -> bool:
        d=self.trie_dict
        for c in prefix :
            if c not in d:
                return False
            d=d[c]
        return True
    
        
        