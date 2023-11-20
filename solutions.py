# q1, q2, q4 and the WorkTool class, are solution to coding problems from one place
# and the other solution are to problems from another place

# ********** Q1 **********
def q1():
    num = int(input("Enter a number: "))
    print(num, end=' ')
    while num > 1:  # Collatz algorithm
        if num % 2 == 1:
            num = num * 3 + 1
        else:
            num = num // 2
        print('->', num, end=' ')
    print('-> Done')


# ********** Q2 **********
def q2():
    lst = two_dimensional_list()
    rotate_squares_list(lst)
    switch_squares_list(lst)
    print("Q2A =", sum_column(lst, 8))
    print("Q2B =", search(lst, 89))
    print("Q2C =", max_div_in_row(lst, 7, 7))


# make two-dimensional numbered list (12x12)
def two_dimensional_list():
    lst = list()  # two-dimensional list
    temp = list()  # the rows of the list
    for counter in range(1, 145):  # fill the list with numbers
        temp.append(counter)  # insert number to this row
        if len(temp) == 12:  # this row end
            lst.append(temp)
            temp = list()  # create new row
    return lst


# rotate 2x2 squares from list 12x12
def rotate_squares_list(lst):
    for i in range(0, 11, 2):
        ln1 = lst[i]  # the first line
        ln2 = lst[i + 1]  # the second line
        for j in range(0, 11, 2):
            if j % 4 == 0:  # rotate clockwise
                temp = ln1[j + 1]
                ln1[j + 1] = ln1[j]
                ln1[j] = ln2[j]
                ln2[j] = ln2[j + 1]
                ln2[j + 1] = temp
            else:  # rotate counterclockwise
                temp = ln1[j]
                ln1[j] = ln1[j + 1]
                ln1[j + 1] = ln2[j + 1]
                ln2[j + 1] = ln2[j]
                ln2[j] = temp


# switch between opposing 2x2 squares from list 12x12
def switch_squares_list(lst):
    for i in range(0, 12):  # switch the lines
        if i % 4 == 0 or i % 4 == 1:
            temp = lst[i]
            lst[i] = lst[i + 2]
            lst[i + 2] = temp
    for i in range(0, 12):  # for every line
        for j in range(0, 12):  # switch the columns
            if j % 4 == 0 or j % 4 == 1:
                temp = lst[i][j]
                lst[i][j] = lst[i][j + 2]
                lst[i][j + 2] = temp


# return sum of the numbers in specifically column from list 12x12
def sum_column(lst, column=0):
    counter = 0
    for i in range(0, 12):
        counter += lst[i][column]
    return counter


# search number in list 12x12
def search(lst, num):
    for i in range(0, 12):  # line number
        for j in range(0, 12):  # column number
            if lst[i][j] == num:
                return i
    return None


# the max number that divisible by specifically number at specifically line in list 12x12
def max_div_in_row(lst, number=1, line=0):
    max_num = -1
    for i in range(0, 12):  # line number
        temp = lst[line][i]
        if temp % number == 0 and max_num < temp:
            max_num = temp
    return max_num


# ********** Q3 **********
class WorkTool:
    def _init_(self, name, price, goal):
        self.name = name
        self.price = price
        self.goal = goal

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_goal(self, goal):
        self.goal = goal

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_goal(self):
        return self.goal


# ********** Q4 **********
def q4():
    arts = \
        [
            ['Mona Lisa', 5341, 67],
            ['Starry night', 8908, 27],
            ['A girl with a pearl earring', 5914, 13],
            ['This Kiss', 3922, 20],
            ['Las Meninas', 5046, 61],
            ['birth of venus', 5576, 44],
            ['Guernica', 5627, 43],
            ['Arrangement in gray and black', 6680, 46],
            ['the night watch', 4361, 75],
            ['The Last Supper', 4907, 13],
            ['Sunrise impression', 3580, 68],
            ['Freedom leads the people', 5657, 20],
            ['The gypsy woman', 3862, 60],
            ['The sailors\' feast', 5332, 27],
            ['Night hawks', 4420, 44],
            ['The jellyfish raft', 7026, 71],
            ['the swing', 9594, 73],
            ['June flames', 9340, 69],
            ['son of man', 9847, 38],
            ['A storm in the Sea of Galilee', 7555, 56]
        ]
    money = 80000
    to_but = buy(arts, money)
    print("Q4A =", len(to_but[2]))
    print("Q4B =", to_but[1])
    print("Q4C =", money - to_but[0])


# check which arts neet to buy with a count of money
# if we want the maximum people count who would go to public auction with that arts
# return list of the money that need to spend, the people count, and list of arts that need to bey to the public auction
def buy(arts, money=0):
    if len(arts) < 1 or money <= 0:
        return [0, 0, list()]
    option1 = buy(arts[1:], money)  # if not buy this art
    option2 = buy(arts[1:], money - arts[0][1])  # if buy this art
    # add the buying effect
    option2[0] += arts[0][1]  # add the money
    option2[1] += arts[0][2]  # add the people counter
    option2[2].append(arts[0])
    if option2[1] > option1[1] and option2[0] <= money:  # the second option better and can buy it
        return option2
    return option1


# solution to problem from code test
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
