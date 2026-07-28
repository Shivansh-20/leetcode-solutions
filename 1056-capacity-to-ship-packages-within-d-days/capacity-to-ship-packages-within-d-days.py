class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low+high) //2
            day = self.findday(mid,weights)#findday(self,mid,weights)
            if day <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
    def findday(self,mid,weights):
        cs = 0
        day = 1 # atleast 1 day if array  has value
        for weight in weights:
            if cs + weight <= mid:
                cs+= weight
            else:
                cs = weight
                day+=1
        return day
        


        