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

# https://leetcode.com/problems/sort-colors/submissions/1108749593
# sort list of the colors red, white and blue
# when used the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

# https://leetcode.com/problems/3sum-closest/submissions/1108777837
# find the sum of three of the numbers that it is the closest sum to given number
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        output = nums[0] + nums[1] + nums[2]
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                q = j + 1
                while q < len(nums):
                    if abs(nums[i] + nums[j] + nums[q] - target) == 0:
                        return nums[i] + nums[j] + nums[q]
                    elif abs(nums[i] + nums[j] + nums[q] - target) < abs(output - target):
                        output = nums[i] + nums[j] + nums[q]
                    q += 1
                j+=1
            i += 1
        return output

# https://leetcode.com/problems/group-anagrams/submissions/1108897155
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = list()
        temp = strs.copy()
        temp.sort(key=str_ln)
        words = list()
        for word in temp:
            words.append(word)
            temp[temp.index(word)] = set(word)
        temp, words = zip(*sorted(zip(temp, words)))
        temp = list(temp)
        words = list(words)
        while len(temp) > 0:
            word_set = temp[0]
            lst = list()
            i = temp.count(word_set)
            while i > 0:
                word_str = words[temp.index(word_set)]
                if lst != []:
                    for ch in lst[0]:
                        if lst[0].count(ch) != word_str.count(ch):
                            output.append(lst)
                            lst = list()
                            break
                lst.append(words[temp.index(word_set)])
                temp.remove(word_set)
                words.remove(word_str)
                i -= 1
            output.append(lst)
        if (len(output) > 0):
            return output

def str_ln(word):
    return len(word)
