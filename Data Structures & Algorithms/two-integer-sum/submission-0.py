class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map ={}

        for i, j in enumerate(nums):
            difference = target - j

            if difference in map:
                return [map[difference], i]
            map[j] = i
        return[] 