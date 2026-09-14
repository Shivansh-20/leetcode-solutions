class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        #making initial dict d
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        #fidning max_f and max_n from dict
        for _ in range(k): #while k:
            max_f = 0
            max_n = None
            for key,value in d.items():
                if value > max_f:
                    max_f = value
                    max_n = key
            ans.append(max_n)
            d.pop(max_n)
            k-= 1
        return ans


        