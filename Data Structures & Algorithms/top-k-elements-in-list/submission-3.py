class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        freq_bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            freq_bucket[freq].append(num)
        
        res = []

        for i in range(len(freq_bucket) -1, 0, -1):
            for num in freq_bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res



        