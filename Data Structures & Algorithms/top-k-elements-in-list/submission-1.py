class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = defaultdict(int)
        for num in nums:
            freq_count[num] += 1
        freq_bucket = [[] for i in range(len(nums) + 1)]
        for n, c in freq_count.items():
            freq_bucket[c].append(n)

        res = []
        for i in range(len(freq_bucket) - 1, 0, -1):
            for n in freq_bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res

