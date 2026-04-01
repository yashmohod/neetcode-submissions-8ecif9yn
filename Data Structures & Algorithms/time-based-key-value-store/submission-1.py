class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store :
            self.store[key].append([timestamp,value])
        else:
            self.store[key] =[[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        data = self.store[key]
        if timestamp < data[0][0]:
            return ""
        l,r = 0, len(data)-1
        p = 0
        while l<=r:
            m = (l+r) //2

            if data[m][0] <= timestamp:
                l = m+1
                p = m
            else:
                r = m-1
        return data[p][1] 
