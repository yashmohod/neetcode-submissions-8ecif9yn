class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def check(idx):
            if idx == len(s):
                return True
            res = False
            for word in wordDict:
                if s[idx:idx+len(word)] == word:
                    res = res or check(idx+len(word))
            
            return res
        
        return check(0)