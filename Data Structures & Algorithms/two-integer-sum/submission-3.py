class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #Map each value con its index

        for i, n in enumerate(nums):
            diff = target - n #this will give us the value we are looking for
            if diff in prevMap: #if the diff is in the dictionary,
                return [prevMap[diff], i] #we return both characters positions.
            prevMap[n] = i #Map the value with its position (index)


        