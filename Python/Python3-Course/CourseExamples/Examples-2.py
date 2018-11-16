
def sum_of_pairs(x, num):
    y = len(x) // 2
    print(y)
    i = 0
    for m in range(y):
        s = x[i] + x[i+1]
        if s == num:
            return [x[i], x[i+1]]
        i += 2
    return []

#x = [3, 6, 3, 5, 50, 20]
#res = sum_of_pairs(x, 100)
#print(res)


def vowel_count(str1):
    d = {}.fromkeys("aeiou", 0)
    for char in str1.lower():
        if char in "aeiou":
            d[char] += 1
    print(d)
    return {k:v for k,v in d.items() if d[k] > 0}
    
#ret = vowel_count("awesome")
#print(ret)

def titleize(str1):
    words = str1.split(" ")
    ret = ""
    for word in words:
        astr = word[0].upper() + word[1:]
        ret += astr + " "
    ret = ret[0:len(ret) - 1] # remove last space
    return ret

#ret = titleize("this is a string")
#print(ret)

def find_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]

#x = find_factors(10)
#print(x)

def search(collection, val, startidx = 0):
    if type(collection) is dict:
        return (val in collection.values())

    return val in collection[startidx:]

#d = {"a": 1, "b":20, "c":200}
#ret = search(d, 200)
#print("value in dictionary: " + str(ret))
#ret = search(d, 'a')
#print("value in dictionary: " + str(ret))

#s = "awesome"
#val = "s"
#ret = search(s, val, 1)
#print(s + " contains " + val + " " + str(ret))

#l = [2, 4, 5, 30, 21]
#val = 30
#ret = search(l, val, 4)
#print("{} contains {}: {}" .format(l, val, ret))

def repeat(str1, num):
    ret = ""
    for n in range(num):
        ret += str1
    return ret

#str1 = "*"
#ret = repeat(str1, 5)
#print(ret)

def truncate(str1, num):
    if num < 3:
        return "Truncation must be at least 3 characters."
    if num > len(str1):
        return str1
    str2 = str1[0:num-3]
    str2 += "..."
    return str2

#str1 = "Super Cool"
#print(truncate(str1,0))
#str1 = "Hello World"
#print(truncate(str1, 6))
#str1 = "Problem Solving is best!"
#print(truncate(str1, 10))
#str1 = "Another test"
#print(truncate(str1, 12))
#str1 = "Woah"
#print(truncate(str1, 4))
#print(truncate(str1, 3))    
#str1 = "YO"
#print(truncate(str1, 100))
#str1 = "Holy guacamole!"
#print(truncate(str1, 152))

def two_list_dictionaries(keylist, valuelist):
    ntimes = min(len(keylist), len(valuelist))
    d = {keylist[i]:valuelist[i] for i in range(ntimes) }
    if len(keylist) > len(valuelist):
        rest = {}.fromkeys(keylist[ntimes:], None)
        d.update(rest)
    return d

#keylist = [1,2, 3, 4, 5]
#valuelist = [14,13,12,11,10,9]
#print(two_list_dictionaries(keylist, valuelist))

def range_in_list(alist, startidx = 0, endidx = 0):
    print("start: {} end: {}" .format(startidx, endidx))
    if len(alist) == 0:
        return 0
    if endidx == 0 or endidx > len(alist):
        endidx = len(alist) - 1
    sum = 0
    for i in range(startidx, endidx + 1): sum += alist[i]
    return sum

#l = [1, 2, 3, 4]
#print(range_in_list(l, 0, 2))
#print(range_in_list(l, 0, 3))
#print(range_in_list(l, 1))
#print(range_in_list(l))
#print(range_in_list(l, 0,100))
#print(range_in_list([], 0,1))

def same_frequency(num1, num2):
    snum1 = str(num1)
    snum2 = str(num2)
    if len(snum1) != len(snum2):
        return False
    
    d1 = {}.fromkeys("0123456789", 0)
    d2 = d1.copy()
    for char in snum1:
        d1[char] += 1
    for char in snum2:
        d2[char] += 1
    for key in d1.keys():
        if d2[key] != d1[key]:
            return False
    return True
        
    
#num1 = 551122
#num2 = 221515
#ret = same_frequency(num1, num2)
#print("{} and {} has same frequency? {}" .format(num1,num2, ret))
#num1 = 321142
#num2 = 3212215
#ret = same_frequency(num1, num2)
#print("{} and {} has same frequency? {}" .format(num1,num2, ret))
#num1 = 1212
#num2 = 2211
#ret = same_frequency(num1, num2)
#print("{} and {} has same frequency? {}" .format(num1,num2, ret))

def nth(alist, idx):
    tlist = alist.copy()   # copy otherwise it removes from the list
    elem = tlist.pop(idx)
    return elem

#l = ['a', 'b', 'c', 'd']
#idx = 1
#print("{} {}th element at {}" .format(l, idx, nth(l, idx)))
#idx = -2
#print("{} {}th element at {}" .format(l, idx, nth(l, idx)))
#idx = 0
#print("{} {}th element at {}" .format(l, idx, nth(l, idx)))
#idx = -4
#print("{} {}th element at {}" .format(l, idx, nth(l, idx)))
#idx = -1
#print("{} {}th element at {}" .format(l, idx, nth(l, idx)))
#idx = 3
#print("{} {}th element at {}" .format(l, idx, nth(l, idx)))

def find_the_duplicate(alist):
    for item in alist:
        if alist.count(item) > 1:
            return item
    return None

#l = [1, 2, 3, 1, 4, 7, 9]
#print("{} contains {} more than once" .format(l, find_the_duplicate(l)))
#l = [1, 2, 3, 4]
#print("{} contains {} more than once" .format(l, find_the_duplicate(l)))

def sum_of_diagonals(alist):
    total = 0
    ci = 0
    list1 = []
    for i in range(len(alist)):
        list1.append(alist[i][ci])
        ci+=1
    print(list1)
    list2 = []
    ci = -1
    for i in range(len(alist)):
        list2.append(alist[i][ci])
        ci -= 1
    print(list2)
    total = sum(list1) + sum(list2)
    return total

#l1 = [[1,2], [3,4]]
#print("{} sum is {}" .format(l1, sum_of_diagonals(l1)))
#l2 = [[1,2,3],[4,5,6],[7,8,9]]
#print("{} sum is {}" .format(l2, sum_of_diagonals(l2)))
#l3 = [[4,1,0], [-1,-1,0], [0,0,9]]
#print("{} sum is {}" .format(l3, sum_of_diagonals(l3)))
#l4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
#print("{} sum is {}" .format(l4, sum_of_diagonals(l4)))

def min_max_key_in_dictionary(adict):
    return [min(adict.keys()), max(adict.keys())]

#d1 = {2:"a", 7:"b", 1:"c", 10:"d", 4:"e"}
#print("min max keys in {} are {}" .format(d1, min_max_key_in_dictionary(d1)))
#d2 = {1: "Elie", 4:"Matt", 2:"Tim"}
#print("min max keys in {} are {}" .format(d2, min_max_key_in_dictionary(d2)))

def find_greater_numbers(alist):
    if len(alist) == 0:
        return 0
    total = 0
    l1 = alist.copy()
    num = l1[0]
    while len(l1) != 1:
        for i in range((len(l1) - 1)):
            if num < l1[i+1]:
                total += 1
        x = l1.pop(0)
#        print("poped {}" .format(x))
        num = l1[0]
    return total

#l1 = [1,2,3]
#print("{} total {}" .format(l1, find_greater_numbers(l1)))
#l2 = [6,1,2,7]
#print("{} total {}" .format(l2, find_greater_numbers(l2)))
#l3 = [5, 4, 3, 2, 1]
#print("{} total {}" .format(l3, find_greater_numbers(l3)))
#l4 = []
#print("{} total {}" .format(l4, find_greater_numbers(l4)))

def two_oldest(alist):    
    alist.sort()
    return [alist[-2], alist[-1]]

#l1 = [1, 2, 10, 8]
#print("{} 2 oldest items are: {}" .format(l1, two_oldest(l1)))
#l2 = [6, 1, 9, 10, 4]
#print("{} 2 oldest items are: {}" .format(l2, two_oldest(l2)))
#l3 = [4, 25, 3, 20, 19, 5]
#print("{} 2 oldest items are: {}" .format(l3, two_oldest(l3)))

import string
def is_odd_string(str1):
    CHARS = list(string.ascii_lowercase)
    CHARS.insert(0, "X")
    total = 0
    for char in str1:
        total += CHARS.index(char)
    return (total % 2 != 0)

#str1 = 'a'
#print("{} has odd alphabets {}" .format(str1, is_odd_string(str1)))
#str2 = 'aaaa'
#print("{} has odd alphabets {}" .format(str2, is_odd_string(str2)))
#str3 = 'amazing'
#print("{} has odd alphabets {}" .format(str3, is_odd_string(str3)))
#str4 = 'veryfun'
#print("{} has odd alphabets {}" .format(str4, is_odd_string(str4)))
#str5 = 'veryfunny'
#print("{} has odd alphabets {}" .format(str5, is_odd_string(str5)))

def valid_paranthesis(str1):
    if str1[0] == ')' or len(str1) == 1:
        return False
    ocount = str1.count('(')
    ccount = str1.count(')')
    print("open {} close {}" .format(ocount, ccount))
    if ocount != ccount:
        return False
    ocount = 0
    ccount = 0
    for char in str1:
        if char == "(":
            ocount += 1
        if char == ")":
            ccount += 1
        if ccount > ocount:
            return False
    return True

#str1 = "()"
#print("{} has valid paranthesis: {}".format(str1,valid_paranthesis(str1)))
#str1 = ")(()))"
#print("{} has valid paranthesis: {}".format(str1,valid_paranthesis(str1)))
#str1 = "("
#print("{} has valid paranthesis: {}".format(str1,valid_paranthesis(str1)))
#str1 = "(())(())()())"
#print("{} has valid paranthesis: {}".format(str1,valid_paranthesis(str1)))
#str1 = "))(("
#print("{} has valid paranthesis: {}".format(str1,valid_paranthesis(str1)))
#str1 = "())("
#print("{} has valid paranthesis: {}".format(str1,valid_paranthesis(str1)))
#str1 = "()()()()())()("
#print("{} has valid paranthesis: {}".format(str1,valid_paranthesis(str1)))

def reverse_vowels(str1):
    vowels = "aeiouAEIOU"
    x = [char for char in str1 if char in vowels]
    ret = ""
    idx2 = -1
    for char in str1:
        if char not in vowels:
            ret += char
        else:
            ret += x[idx2]
            idx2 -= 1
    return ret

#str1 = 'Hello!'
#print("{} with reversed vowels {}" .format(str1, reverse_vowels(str1)))
#str1 = 'Tomatoes'
#print("{} with reversed vowels {}" .format(str1, reverse_vowels(str1)))
#str1 = 'Reverse Vowels In A String'
#print("{} with reversed vowels {}" .format(str1, reverse_vowels(str1)))
#str1 = 'aeiou'
#print("{} with reversed vowels {}" .format(str1, reverse_vowels(str1)))
#str1 = 'why try, shy fly?'
#print("{} with reversed vowels {}" .format(str1, reverse_vowels(str1)))

def three_odd_numbers(alist):
    ntimes = len(alist)  - 2
    idx = 0
    for i in range(ntimes):
        x = [alist[idx], alist[idx+1], alist[idx+2]]
        if sum(x) % 2 != 0:
            return True
        idx += 1
    return False

#l1 = [1, 2, 3, 4, 5]
#print("{} 3 consecutive numbers are odd {}" .format(l1,three_odd_numbers(l1)))
#l1 = [0,-2,4,1,9,12,4,1,0]
#print("{} 3 consecutive numbers are odd {}" .format(l1,three_odd_numbers(l1)))
#l1 = [5, 2, 1]
#print("{} 3 consecutive numbers are odd {}" .format(l1,three_odd_numbers(l1)))
#l1 = [1, 2, 3, 3, 2]
#print("{} 3 consecutive numbers are odd {}" .format(l1,three_odd_numbers(l1)))

# look for non collection solution in notes
from collections import Counter
def mode(nums):
    cnt = Counter(nums)
    x  = cnt.most_common(1)
    return x[0][0]

#l1 = [2, 4,1,2,3,4,4,5,4,4,6,4,6,7,4]
#print("{} most frequent {}" .format(l1, mode(l1)))


def running_average():
    count = 0
    laverage = 0
    def average(x):
        nonlocal count
        nonlocal laverage
        count += 1
#        print("count {} laverage {} x {}" .format(count, laverage, x))
        laverage += x
        return laverage / count
    return average

#rAvg1 = running_average()
#print(rAvg1(10))
#print(rAvg1(11))
#print(rAvg1(12))

#rAvg2 = running_average()
#print(rAvg2(1))
#print(rAvg2(3))


def letter_counter(str1):
    word = str1
    def counter(x):
        times = word.lower().count(x)
        return times
    return counter

#counter = letter_counter("amazing")
#print(counter('a'))
#print(counter('m'))
#counter1 = letter_counter("This is really fun!")
#print(counter1('i'))
#print(counter1('t'))

def add(a,b):
    return a+b
def once(fn):
    called = False
    def onlyonce(x,y):
        nonlocal called
        if called:
            return None
        called = True
        return fn(x,y)
    return onlyonce

#oneAdd = once(add)
#print(oneAdd(2,4))
#print(oneAdd(2,4))
#print(oneAdd(10,50))

import math
# This is a generator
#def next_prime():
#    prime = 2
#    num = 2
#    while True:
#        yield prime
#        for x in range(1, num+1):
#         for x in range(2, int(math.sqrt(num)) + 1):
#             print(x)
#            print(num)
#            if num % x == 0:
#                num = num + 1
#            else:
#                prime = num

def isPrime(num):
    if num < 2:
        return False
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

def next_prime():
    num = 2
    while True:
        if isPrime(num):
            yield num
        num += 1

        
primes = next_prime()
x = [next(primes) for i in range(30)]
print(x)
