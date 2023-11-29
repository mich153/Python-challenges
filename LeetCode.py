# https://leetcode.com/problems/two-sum/submissions/1108686291
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = list()
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    return output
                j += 1
            i += 1
