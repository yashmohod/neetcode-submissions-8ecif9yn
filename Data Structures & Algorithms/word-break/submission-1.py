class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {8:True}
        def check(idx):
            if idx in mem:
                return mem[idx]
            res = False
            for word in wordDict:
                if s[idx:idx+len(word)] == word:
                    c = check(idx+len(word))
                    res = c
                    if c:
                        mem[idx] = True
            
            return res
        
        return check(0)