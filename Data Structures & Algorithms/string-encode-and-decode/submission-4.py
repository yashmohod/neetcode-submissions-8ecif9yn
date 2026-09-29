class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for i in strs:
            res += str(len(i)) + "#"+i
        
        return res

    def decode(self, s: str) -> List[str]:
        
        if s == "0#":
            return [""]
        res = []

        num = ""
        cur = ""
        numen = True
        for i in s:

            if numen :
                if i == "#":
                    numen = False
                    num = int(num) if num != "" else 0
                else:
                    num += i
            else:
                cur += i
                num -=1
                if num <1:
                    # print(cur)
                    res.append(cur)
                    cur = ""
                    num = ""
                    numen = True

        return res 