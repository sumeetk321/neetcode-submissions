class TimeMap:

    def __init__(self):
        self.m = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m.keys():
            self.m[key] = dict()
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m.keys():
            return ""
        if timestamp not in self.m[key].keys():
            lis = sorted(list(self.m[key].keys()))
            l = 0
            r = len(lis)
            while l < r:
                mid = l+(r-l)//2
                if lis[mid]>timestamp:
                    r = mid
                else:
                    l = mid+1
            print(lis, l)
            if lis[l-1] <= timestamp:
                return self.m[key][lis[l-1]]
            else:
                return ""
        return self.m[key][timestamp]
