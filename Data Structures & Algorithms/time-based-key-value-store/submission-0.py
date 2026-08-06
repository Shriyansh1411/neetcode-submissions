class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key]=[]
        self.time_map[key]=self.time_map.get(key,[])+[[value,timestamp]]
    #   self.time_map[key].append([value,timestamp,0])        

    def get(self, key: str, timestamp: int) -> str: 
        '''
        "get", ["alice", 1] =   'happy'

        '''
        res=''
        left=0
        lst=self.time_map.get(key,[])
        right=len(self.time_map.get(key,[]))-1
        while left<=right:
            mid=(left+right)//2
            if timestamp>=lst[mid][1]:
                res= lst[mid][0]
                left=mid+1
            elif timestamp < lst[mid][1]:
                right=mid-1
        return res
        
