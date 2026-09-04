class WordDictionary:

    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str) -> None:
        d = self.dictionary
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['#'] = '#'

    def search(self, word: str) -> bool:
        d = self.dictionary

        def rec(i, curr):
            # Base Case: processed all characters, check if end-of-word marker exists
            if i == len(word):
                return '#' in curr
            
            c = word[i]

            if c == ".":
                # Try all branch nodes (excluding end-of-word marker '#')
                for k, v in curr.items():
                    if k != '#' and rec(i + 1, v):
                        return True
                return False
            
            elif c in curr:
                # Advance to the next character index and child dictionary
                return rec(i + 1, curr[c])
            
            # Character mismatch
            return False

        return rec(0, d)