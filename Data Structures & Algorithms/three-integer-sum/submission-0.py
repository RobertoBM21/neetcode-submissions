class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                return res
            
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                currentSum = a + nums[left] + nums[right]

                if currentSum < 0:
                    left += 1
                elif currentSum > 0:
                    right -= 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res
