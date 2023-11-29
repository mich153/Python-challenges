# https://leetcode.com/problems/two-sum/submissions/1108686291
# find the two numbers' places, where the numbers sum if the given number
# there are exactly two places
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = list()
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target: # found the places
                    output.append(i)
                    output.append(j)
                    return output
                j += 1
            i += 1

# https://leetcode.com/problems/3sum/submissions/1108736217
# find all of the triples of numbers, that them sum is zero
class Solution:
    def threeSum(self, nums: List[int]) -> List[list[int]]:
        output = list()
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                q = j + 1
                while q < len(nums):
                    if nums[i] + nums[j] + nums[q] == 0: # the sum is zero
                        new = True
                        for triple in output: # check if it is new triple
                            temp = [nums[i], nums[j], nums[q]]
                            if triple.count(nums[i]) == temp.count(nums[i]) and triple.count(nums[j]) == temp.count(nums[j]) and triple.count(nums[q]) == temp.count(nums[q]): # doesn't new: the tuple is already added
                                new = False
                        if new: # add the triple if it new
                            triple = [nums[i], nums[j], nums[q]]
                            output.append(triple)
                    q += 1
                j += 1
            i += 1
        if len(output) > 0:
            return output
