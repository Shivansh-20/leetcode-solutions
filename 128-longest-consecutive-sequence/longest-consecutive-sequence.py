class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_streak = 0
        current_streak = 0
        for i in nums:
            if i - 1 not in nums: #in used only for presence check not acess
                current_no = i
                current_streak = 1 #if i - 1 is in nums, move loop forward
                while current_no + 1 in nums:
                    current_no += 1
                    current_streak += 1
                    #if while loop not true check max go back to if 
                max_streak = max(max_streak,current_streak) #update max_streak
        return max_streak #max_streak is not list but length count and variable so no bracket
            
        