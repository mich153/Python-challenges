import math

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

# https://leetcode.com/problems/valid-parentheses/solutions/4345661/solution-in-python3/
# chack if it valid string of brackets
    def isValid(self, s: str) -> bool:
        stack = list()
        for ch in s:
            if ch in ['(', '[', '{']: #open bracket
                stack.append(ch)
            elif ch in [')', ']', '}']: #close bracet
                #chack if open brackets closed in the correct order
                #and closed by the same type of btackets
                if len(stack) == 0:
                    return False
                opn = stack.pop()
                if opn == '(' and ch != ')':
                    return False
                elif opn == '[' and ch != ']':
                    return False
                elif opn == '{' and ch != '}':
                    return False
            else: #illegal charecter
                return False
        return len(stack) == 0 #all the open brackets closed
        
# https://leetcode.com/problems/simplify-path/solutions/4345855/simple-solution-in-python3/
# get absolute path and return the convert to simplified canonical path
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        while lst.count('') > 0:
            lst.remove('')
        stack = list()
        for x in lst:
            if x == '..' and len(stack) > 0:
                stack.pop()
            elif x != '.' and x != '..':
                stack.append(x)
        return '/' + '/'.join(stack)

# https://leetcode.com/problems/evaluate-reverse-polish-notation/solutions/4346036/solution/
# solve excersice
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for ch in tokens:
            if ch in ['+', '-', '*', '/']:
                num2 = stack.pop()
                num1 = stack.pop()
                if ch == '+':
                    result = num1 + num2
                elif ch == '-':
                    result = num1 - num2
                elif ch == '*':
                    result = num1 * num2
                else:
                    result = num1 / num2
                    if result >= 0:
                        result = math.floor(result)
                    else:
                        result = math.ceil(result)
                stack.append(result)
            else:
                stack.append(int(ch))
        return stack[0]

# https://leetcode.com/problems/find-the-winner-of-the-circular-game/solutions/4346167/solution-in-python3/
# game simulation
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n + 1))
        i = 0
        while len(friends) > 1:
            i += k - 1 #step over 2 poeple
            i %= len(friends)
            lose = friends[i]
            friends.remove(lose)
        return friends[0]

# https://leetcode.com/problems/happy-number/solutions/4346944/solution-in-python/
# check if it is happy number
    def isHappy(self, n: int) -> bool:
        nums = [n]
        while n != 1:
            temp = n
            s = 0
            while temp > 0:
                s += (temp % 10) ** 2
                temp //= 10
            if s in nums:
                return False
            nums.append(s)
            n = s
        return True 
        
