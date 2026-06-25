class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max, res = 0, 0
        
        for num in nums:
            if num == 0:
                res = max(curr_max, res)
                curr_max = 0
            curr_max += num
        
        return max(res, curr_max)
