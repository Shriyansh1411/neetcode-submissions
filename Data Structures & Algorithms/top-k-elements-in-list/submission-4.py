class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_nums=[]
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]=freq.get(i,0)+1

        freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        for i,key in enumerate(freq):
            if i>=k:
                break
            k_nums.append(key)
        return k_nums