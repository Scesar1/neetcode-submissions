class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = deque([])
        curr_max = arr[-1]
        res.append(-1)
        for i in range(len(arr) - 1, 0, -1):
            curr_max = max(curr_max, arr[i])
            res.appendleft(curr_max)
        return list(res)