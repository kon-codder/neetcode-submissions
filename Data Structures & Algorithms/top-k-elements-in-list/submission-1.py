class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        listt = []

        for key, val in freq.items():
                listt.append([val,key])
        listt.sort()

        res = []
        while len(res) < k:
            res.append(listt.pop()[1])



        return res
