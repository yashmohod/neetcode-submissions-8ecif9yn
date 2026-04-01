class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        s = []

        for i,temp in enumerate(temperatures):

            while len(s)>0 and s[-1][0]<temp:
                ctmp,idx = s.pop()
                res[idx] = i-idx
            s.append([temp,i])
        return res