# solution to Tree Constructor challenge from Coderbyte
# https://coderbyte.com/results/mich100:First%20Reverse:Python3
def FirstReverse(strParam):
  i = len(strParam) - 1
  reverse = ''
  while i >= 0:
    reverse += strParam[i]
    i -= 1
  return reverse


# solution to Tree Constructor challenge from Coderbyte
# https://coderbyte.com/results/mich100:Longest%20Word:Python3
import string

def LongestWord(sen):
  s = ''
  for i in sen:
    if i not in string.punctuation:
      s += i
  longest = ''
  for word in s.split():
    if len(word) > len(longest):
      longest = word
  return longest


# solution to Tree Constructor challenge from Coderbyte
# https://coderbyte.com/results/mich100:Tree%20Constructor:Python3
def TreeConstructor(strArr):
    children = list()
    parents = list()
    root = None
    for i in strArr:
        numbers = i[1:-1].split(',')
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        children.append(num1)
        if children.count(num1) > 1:  # can be only one parent for any children
            return False
        parents.append(num2)
        if parents.count(num2) > 2:  # can be at the most 2 children to parent
            return False
    for i in parents:  # find the root
        counter = children.count(i)
        if counter == 0:
            if root is None:
                root = i
            elif root != i:  # can be only one without parent
                return False
    return True


# solution to problem from Coderbyte task
# check if it is possible to make palindrome (with length higher than 3) from string
# by removing at the more 2 characters
def string_challenge(strParam):
    if check_poly(strParam):
        return "palindrome"
    i = 0
    while i < len(strParam):
        temp = strParam[:i] + strParam[i + 1:]
        if check_poly(temp):
            return strParam[i]
        j = i
        while j < len(temp):
            temp2 = temp[:j] + temp[j + 1:]
            if check_poly(temp2):
                return strParam[i] + temp[j]
            j += 1
        i += 1
    return "not possible"


def check_poly(s):
    if len(s) < 3:
        return False
    i = 0
    while i < len(s) // 2:
        if s[i] != s[len(s) - 1]:
            return False
        i += 1
    return True


# solution to problem from Coderbyte task
# get list of integers stored in the following format: [K, r1, r2, r3, ...] 
# where K represents the number of desks in a classroom, 
# and the rest of the integers in the array will be in sorted order and will represent the desks that are already occupied. 
# All of the desks will be arranged in 2 columns, 
# where desk #1 is at the top left, desk #2 is at the top right, desk #3 is below #1, desk #4 is below #2, etc. 
# The program should the number of ways 2 students can be seated next to each other. 
# This means 1 student is on the left and 1 student on the right, or 1 student is directly above or below the other student.
def ArrayChallenge(arr):
  K = arr[0]
  desks = arr[1:]
  i = 1
  counter = 0
  while i < K:
    if i % 2 == 1 and desks.count(i) == 0 and desks.count(i + 1) == 0:
      counter += 1
    if i + 2 <= K and desks.count(i) == 0 and desks.count(i + 2) == 0:
      counter += 1
    i += 1
  return counter
