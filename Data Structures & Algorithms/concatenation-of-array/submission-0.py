class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        res[0:n - 1] = nums
        res[n:-1] = nums

        return res