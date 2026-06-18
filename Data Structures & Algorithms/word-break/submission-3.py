class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {len(s):True}

        def check(idx):

            if idx in mem:
                return mem[idx]

            for word in wordDict:
                if (idx+len(word)) <=len(s) and s[idx:idx+len(word)] == word:
                    if check(idx+len(word)):
                        mem[idx] = True
                        return True

            mem[idx] = False
            return False
        
        return check(0)