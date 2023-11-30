# https://leetcode.com/problems/two-sum/solutions/4343671/solution-in-python3/
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

# https://leetcode.com/problems/add-two-numbers/solutions/4345486/solution-in-python3-for-problem-number-two/
# sum two lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.fromListToNum(l1)
        num2 = self.fromListToNum(l2)
        return self.fromNumToList(num1 + num2)

    def fromListToNum(self, lst: Optional[ListNode]) -> int:
        num = ''
        while lst:
            num = str(lst.val) + num
            lst = lst.next
        return int(num)

    def fromNumToList(self, num: int) -> ListNode:
        lst = list()
        nextNode = None
        if num == 0:
            lst.append(0)
        while num > 0:
            lst.append(num % 10)
            num //= 10
        lst.reverse()
        for num in lst:
            temp = ListNode(val = num, next = nextNode)
            nextNode = temp
        return nextNode
