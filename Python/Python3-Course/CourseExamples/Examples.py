# Set the message variable equal to any string containing a new-line escape sequence
message = "hi \n there"


# Add a string to the mountains variable that when printed results in: /\/\/\
# You will need to use an escape sequence more than once!
mountains = "/\\/\\/\\"


# Set the quotation variable to any string that contains an escaped double quotation mark

quotation = "hello \"there\" "


# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)
     
# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)
     
# 3 - Given the following variable:
values = [10,20,30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)
     
# 3 - Given the following variable
stuff = [1,3,1,5,2,5,1,2,5]
     
# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)

#Generating evens using a list comprehension:

def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]

#Generating evens using a loop:

def generate_evens1():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result

#The most straight forward solution is to use a large if-elif-else statement:

def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

#Another shorter solution involves using a dictionary that maps animal names to noises.

    noises = {
        "dog": "woof", 
        "pig": "oink", 
        "duck": "quack", 
        "cat": "meow"
    }

#Then, we just use the dictionary.get() method to retrieve the correct animal noise and save it to a variable called noise . get() will return None  if the animal is not in the dictionary.  Then we just check to see if noise  exists.  If it does, return noise .  Otherwise, return "?" 

    def speak(animal="dog"):
        noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
        noise = noises.get(animal)
        if noise:
            return noise
        return "?"


#Section 18, Lecture 161

#Here's a solution that uses what we've learned so far.  

#    Keep track of the days in a list.  
#    Check to make sure num isn't < 0 or  > 6.  
#    Return the corresponding day. Use days[num-1] because return_day(1) should return 0th item in list.

def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num < len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

#Section 18, Lecture 164

#In my solution, I use the built-in count()  to count the number of times letter  appears in string .  I also downcase both string  and letter  to make it case-insensitive (you could also upcase both instead)

    def single_letter_count(string,letter):
        return string.lower().count(letter.lower())

#Section 18, Lecture 165

# I used a dictionary comprehension. For each letter in the input string, I make the key the letter itself ("a" for example), and the corresponding value is the result of running count() of that letter in the string.

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

# Section 18, Lecture 166

# It's basically just a large if-elif-else statement:

def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

#Section 18, Lecture 167

#Here's the simpler version that doesn't ignore whitespace.  I reverse the string using a slice [::-1] and compare that to the original string, which returns True or False.  

def is_palindrome(string):
    return string == string[::-1]

#The Bonus Version:For the more advanced version that ignores whitespace, I first remove all whitespace from the input string using a string method called replace() . What I'm actually doing is replacing all spaces(" ") with empty strings ("").  I save the result to a new variable I call stripped .  Then, I simple check if stripped  is a palindrome, using the same logic I did in the previous solution.

def is_palindrome1(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]

#Section 18, Lecture 169

#    In my solution, I start with a variable called total.    Since we're working with multiplication, I start it off as 1.  Then I iterate through the list, checking if each num is cleanly divisible by 2 If it is, I multiply total by the number At the end, after the loop finishes, I return total

def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total

#My solution works by:

#    Slicing the first character (up to index 1) and capitalizing it. Adding that to the rest of the string (from index 1 onward)

def capitalize(string):
    return string[:1].upper() + string[1:]

#Write a function called compact. This function accepts a list and returns a list of values that are truthy values, without any of the falsey values.

#def compact(alist):
#    compact([0,1,2,"",[], False, {}, None, "All done"])     # [1,2, "All done"]

#Write a function called compact. This function accepts a list and returns a list of values that are truthy values, without any of the falsey values.
#Section 18, Lecture 171
#With a list comprehension

#You can write compact  in a nice single line of code.  How compact!

def compact(l):
    return [val for val in l if val]

#Without a list comprehension

#    I make a list to store all truthy values
#    I iterate over each value in the list
#    I check if the value is truthy (using a simple if val )
#        If the value is truthy, add it to the truthy_vals  list
#    return truthy_vals  at the end

def compact1(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals


#Write a function called intersection. This function should accept two lists and return a list with the values that are in both input lists.
"""
    intersection([1,2,3], [2,3,4])    #[2,3]
    intersection(['a','b','z'], ['x','y','z']) .  # ['z']
Sets Solution

This solution(submitted by Sebastian on the discussion boards) is the most efficient of the three.  It converts the lists to sets, which removes duplicate values, and then finds the intersection of them using &.  If you need review, watch the sets section again (it's super short).
"""

def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]


#Write a function called partition. This function accepts a list and a callback function (which you can assume returns True or False ). The function should iterate over each element in the list and invoke the callback function at each iteration. If the result of the callback function is True, the element should go into one list. If it's False, the element should go into another list. When it's finished, partition should return both lists inside of one larger list

#Section 18, Lecture 173
#"Traditional" Version

#Here's my solution that doesn't use a list comprehension:
"""
    I have two lists, to hold the true and false values
    I loop through the list, calling fn  with each value in the list
    If the result is True, I append the value to the trues  list
    Otherwise, I append the value to the falses  list
    At the end I return a list that contains both the trues  and falses  lists
"""
def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

"""
List Comprehension Version

Using a list comprehension, you can get this function down to a single line.  It's definitely a tradeoff though.  It's much short but also more difficult to understand.  It's a fine balance between brevity and readability. 
"""
def partition1(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

"""
**kwargs Exercise

Note: for this exercise, make use of **kwargs.  No default parameters allowed!

Write a function called combine_words  which accepts a single string called word and any number of additional key word arguments.  If a prefix is provided, return the prefix followed by the word.  If a suffix is provided, return the word followed by the suffix.  If neither is provided, just return the word.  It might sound confusing, but the examples should make this a lot clearer!
combine_words("child")  #'child'

combine_words("child", prefix="man")  #'manchild'

combine_words("child", suffix="ish")  #'childish'

combine_words("work", suffix="er")  #'worker'

combine_words("work", prefix="home")  #'homework'

Section 19, Lecture 177
combine_words solution

    I check if kwargs contains "prefix".
        If it does, I return the value of prefix + the word
    Otherwise, I check to see if "suffix" was provided as a kwarg
        If it was, I return the word followed by the value of suffix
    Otherwise, I just return the word on its own.
"""
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

"""
Oh boy, this is a complicated set of instructors.  Bear with me. Write a function called calculate that accepts a list of keyword arguments

    make_float , a boolean which returns a float if True or an integer if False.
    operation which is either 'add', 'subtract', 'multiply', and 'divide'. 
    first which is a number, second , which is another number, and message which is a string that can be added.

The function should return the result of actually running the specified operation with the first and second keyword arguments. The result of the operation with the first  and second  is an integer if the make_float  keyword argument is False , otherwise the result of the operation is a float. If a message is specified, it should return the message keyword argument + the result of the operation.  Otherwise, it should return the string  "The result is " joined with the result of the operation

See the examples below for some more information. Remember, you can't use f-strings on in the Udemy Editor.

Section 19, Lecture 182
Calculate Walkthrough

This solution uses dict.get() a lot. dict.get('first')  will return the value of 'first' if it exists, otherwise it returns None.  However, you can specify a second argument which will replace None as the default value. I use that in this solution a bunch of times.

    I defined a dictionary called operation_lookup  that maps a string like "add" to an actual mathematical operation involving the values of 'first' and 'second'
    I create a boolean variable called is_float, which is True if kwargs contains 'make_float', otherwise it's false
    Then I lookup the correct value from the operation_lookup dict using the operation that was specified in kwargs
        Basically, turning something like "subtract" into:kwargs.get('first', 0) - kwargs.get('second', 0) 
        Which in turns simplifies to a number
    I store the result in a variable called operation_value 
    I return a string containing either the specified message or the default 'The result is' string.  
    Whether operation_value  is interpolated as a float or int is determined by the is_float  variable.
    Note: this solution will divide by zero if a 2nd argument isn't provided for divide.  You may want to change the default value to 1.  We learn how to handle ZeroDivisionErrors later on in the course.  Thanks, Scott for pointing out the issue!
"""
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final


"""
Write a function called decrement_list  that accepts a single list of numbers as a parameter.  It should return a copy of the list where each item has been decremented by one. Use map to do this! For example:

decrement_list([1,2,3])   #[0,1,2]

decrement_list([20,14,11])  #[19,13,10]

Tips:

    Remember map doesn't return a list on its own.  decrement_list , however, should return a list.
    You can either pass map another name function or use a lambda.  A lambda is preferable, even if it is a little scary looking.

Section 20, Lecture 186
decrement_list solution

    I define the function decrement_list that accepts a list called l
    Inside, I call map and pass in a lambda and the list, l
        The lambda returns n-1 for each n in the list
    The last step is to convert the return value of map to a list
        Remember, map returns a <map object>, not a list
    Oh, and finally we return the result!
"""
def decrement_list(l):
    return list(map(lambda n: n-1, l))

"""
? Write a function called remove_negatives that accepts a list of numbers and returns a copy of the lists with all negative numbers removed. Use filter() in your implementation, not a list comprehension!

remove_negatives([-1,3,4,-99])     #[3,4]

remove_negatives([-7,0,1,2,3,4,5])      #[0, 1, 2, 3, 4, 5]

remove_negatives([50,60,70])   #[50,60,70]
"""

def remove_negatives(alist):
    return list(filter(lambda x: x >= 0, alist))

"""
Any/All Exercise

Implement a function is_all_strings  that accepts a single iterable and returns True if it contains ONLY strings.  Otherwise, it should return false.  

is_all_strings(['a', 'b', 'c'])  #True

is_all_strings([2,'a', 'b', 'c'])  #False

is_all_strings(('hello', 'goodbye'))  #True
"""

def is_all_strings(alist):
    return (all(type(word) == str for word in alist))

"""
? Extremes Exercise - Using Min and Max

Write a function called extremes  which accepts an iterable. It should return a tuple containing the minimum and maximum elements.  For example:

extremes([1,2,3,4,5])  # (1, 5)

extremes((99,25,30,-7))  # (-7, 99)

extremes("alcatraz")  #( 'a', 'z')

REMEMBER, RETURN A TUPLE!!!
"""
def extremes(nums):
    return(min(nums), max(nums))

"""
? Write a function max_magnitude  that accepts a single list full of numbers.  It should return the number with the largest magnitude(the number that is furthest away from zero).  

max_magnitude([300, 20, -900])   #900

max_magnitude([10, 11, 12])   #12

max_magnitude([-5, -1, -89])   #89

Hint: use max and abs!
"""
def max_magnitude(nums):
    return max(abs(num) for num in nums)

"""
? Write a function called sum_even_values. This function should accept a variable number of arguments and return the sum of all the arguments that are divisible by 2. If there are no numbers divisible by 2, the function should return 0.  To be clear, it accepts all the numbers as individual arguments!

    sum_even_values(1,2,3,4,5,6) # 12
    sum_even_values(4,2,1,10) # 16
    sum_even_values(1) # 0
"""
def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)

"""
? Write a function called sum_floats. This function should accept a variable number of arguments. The function should return the sum of all the parameters that are floats. If there are no floats the function should return 0

    I started by defining sum_floats , which accepts any number of arguments using *args 
    Much like the previous exercise, I use a generator expression to extract the values in args where type()  is float.
    I pass those values in to sum  and return the result
"""

def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)

"""
? Write a function interleave  that accepts two strings.  It should return a new string containing the 2 strings interwoven or zipped together. For example:

interleave('hi','ha')    # 'hhia'

interleave('aaa', 'zzz')  # 'azazaz'

interleave('lzr','iad') #  'lizard'

 This might seem like an easy task using zip , but in fact there are a couple intermediate steps to go from zip  back to a single string.  If you need help, I've written up a basic walkthrough of the steps:

    suppose we call interleave('hi', 'no')  
    zip  the two strings together, giving you a list of tuples (once you convert from the default zip_object) -  [('h','n'), ('i','o')]  
    For each of the tuples in the list, join them together using '"".join  resulting in ['hn', 'io']  - 
"""
def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))

"""
? Triple and Filter Solution

For my solution, I chose to use map and filter in combination.
"""
def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

"""
?Write a function called extract_full_name. This function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionary concatenated.
"""
def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

"""
? It's time to get some practice with built-in modules.  Here's your mission;

    Import the math  module
    Use math.sqrt  to find the square root of 15129 and save it to variable called answer .
# Use math.sqrt  to find the square root of 15129 and save it to variable called answer:
"""
import math
answer = math.sqrt(15129)

"""
? Define a function called contains_keyword  that accepts any number of string arguments.  It should return True  if any of the arguments are considered Python keywords (things like "def", "return", "if", etc.)  Otherwise it should return False.   Python has a built-in module called keyword  that contains a method called iskeyword .  Import keyword  and then use keyword.iskeyword  in you own function to determine if a given string is a keyword.

contains_keyword("hello", "goodbye")  #False

contains_keyword("def", "haha", "lol", "chicken", "alaska")  #True

contains_keyword("four", "for", "if")  #True

contains_keyword("blah", "doggo", "crab", "anchor")  #False

contains_keyword("grizzly", "ignore", "return", "False")  #True
"""

import keyword
def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True
    return False



"""
? Suppose we have a big ol chicken coop in our backyard full of very productive hens. We're going to model our chickens with python! We want to keep track of how many eggs each individual Chicken lays, and at the same time we want to track the total number of eggs all hens have laid. 

 Create a Chicken  class.  Each Chicken has a species  and a name , as well as an integer attribute called eggs . eggs should always start out at 0. 

Each Chicken should also have an instance method called lay_egg() which should increment and then return that particular Chicken's eggs  attribute. lay_egg()  should also increment a class variable called total_eggs

    c1 = Chicken(name="Alice", species="Partridge Silkie")
    c2 = Chicken(name="Amelia", species="Speckled Sussex")
    Chicken.total_eggs #0
    c1.lay_egg()  #1
    Chicken.total_eggs #1
    c2.lay_egg()  #1
    c2.lay_egg()  #2
"""
class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs


"""
?
Introduction

Your goal in this exercise is to implement two classes, Card  and Deck .

Specifications

Card 

    Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
    Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
    Card 's __repr__  method should display the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

Deck 

    Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
    Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
    Deck 's __repr__  method should display information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
    Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
    Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".
    Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck.
    Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck.
"""

"""
? Create a class Train  that has one attribute: num_cars  which is specified when the train is instantiated.

There should also be two special/magic/dunder methods on it:

    One method that describes the train when we call print  on it by saying "x car train" where x is the number of cars (see example below)
    One method that denotes the length of the train when we call len  on it

Example:

    a_train = Train(4)
    print(a_train)  # 4 car train
    len(a_train)  # 4

Note: You do not need to instantiate Train  for the tests to pass. The tests will try to instantiate Train  for you.
"""
class Train():
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
        return "{} car train".format(self.num_cars)

    def __len__(self):
        return self.num_cars

"""
? Week Generator Exercise

Write a function called week, which returns a generator that yields each day of the week, starting with Monday and ending with Sunday.  After Sunday, the generator is exhausted.  It does not start over.
"""
def week():
    x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in x:
        yield day

"""
yes_or_no

Write a function called yes_or_no, which returns a generator that first yields yes , then no , then yes , then no , and so on.
'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''
"""
def yes_or_no():
    curr = "yes"
    while True:
        yield curr
        if curr == "yes":
            curr = "no"
        else:
            curr = "yes"

# Alternate solution
def yes_or_no1():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"

"""
Write a function called make_song, which takes a count and a beverage, and returns a generator that yields verses from a popular song about a the beverage. The number of verses in the song is determined by the count. Each verse of the song should involve one fewer beverage, until there are no beverages remaining. (Check the examples for details on the structure of the lyrics.)

The default count should be 99, and the default beverage should be soda.

kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'

"""
def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)


"""
?Write a function called get_multiples, which accepts a number and a count, and returns a generator that yields the first count multiples of the number. 

The default number should be 1, and the default count should be 10.
'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
"""
def get_multiples(num = 1, count = 10):
    x = 1
    while x <= count:
        yield x * num
        x += 1

"""
? Write a function called get_unlimited_multiples, which accepts a number and returns a generator that will yield an unlimited number of multiples of that number.

The default number should be 1.
'''
sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''
"""
def get_unlimited_multiples(num = 1):
    x = 1
    while True:
        yield x * num
        x += 1

"""
? Write a function called show_args which accepts a function and returns another function. Before invoking the function passed to it, show_args should be responsible for printing two things: a tuple of the positional arguments, and a dictionary of the keyword arguments.
'''
@show_args 
def do_nothing(x, y):
    pass
    
do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines): 
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''
    from functools import wraps
"""  
def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
    return wrapper

"""
? Write a function called double_return which accepts a function and returns another function. double_return should decorate a function by returning two copies of the inner function's return value inside of a list.
'''
@double_return 
def add(x, y):
    return x + y
    
add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''
"""
from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

"""
? Write a function called ensure_fewer_than_three_args which accepts a function and returns another function. The function passed to it should only be invoked if there are fewer than three positional arguments passed to it. Otherwise, the inner function should return "Too many arguments!"
'''
@ensure_fewer_than_three_args
    def add_all(*nums):
        return sum(nums)

    add_all() # 0
    add_all(1) # 1
    add_all(1,2) # 3
    add_all(1,2,3) # "Too many arguments!"
    add_all(1,2,3,4,5,6) # "Too many arguments!"
'''
"""
#from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        return "Too many arguments!"
    return wrapper

"""
? Write a function called only_ints which accepts a function and returns another function. The function passed to it should only be invoked if all of the arguments passed to it are integers. Otherwise the inner function should return "Please only invoke with integers".

'''
@only_ints 
def add(x, y):
    return x + y
    
add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''
"""
#from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner

"""
? Write a function called ensure_authorized which accepts a function and returns another function. The function passed to it should only be invoked if there exists a keyword argument with a name of "role" and a value of "admin". Otherwise, the inner function should return "Unauthorized"
'''
@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="admin") # "Shh! Don't tell anybody!"
show_secrets(role="nobody") # "Unauthorized"
show_secrets(a="b") # "Unauthorized"
'''
"""
def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper

"""
? Write a function called delay which accepts a time and returns an inner function that accepts a function. When used as a decorator, delay will wait to execute the function being decorated by the amount of time passed into it. Before starting the timer, delay will also print a message informing the user that there will be a delay before the decorated function gets run.

(Hint: take a look at the sleep function from the built-in time module if you want to pause code execution for a certain amount of time.)

'''
@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
'''
"""
#from functools import wraps
from time import sleep

def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(timer, fn.__name__))
            sleep(timer)
            return fn(*args, **kwargs)
        return wrapper
    return inner


"""
? Write a function called copy, which takes in a file name and a new file name and copies the contents of the first file to the second file. 

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.

    copy('story.txt', 'story_copy.txt') # None
    # expect the contents of story.txt and story_copy.txt to be the same
    def copy(file_name, new_file_name):
        with open(file_name) as file:
            text = file.read()
        
        with open(new_file_name, "w") as new_file:
            new_file.write(text)
? write in reverse order
    def copy_and_reverse(file_name, new_file_name):
        with open(file_name) as file:
            text = file.read()
     
        with open(new_file_name, "w") as new_file:
            new_file.write(text[::-1])


?Write a function called statistics, which takes in a file name and returns a dictionary with the number of lines, words, and characters in the file.

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)

'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''
"""
def statistics(file1):
    nwords = 0
    nchars = 0
    with open(file1) as f1:
        data = f1.readlines()
        
    nlines = len(data)
    for n in data:
        nchars += len(n)
        words = n.split(" ")
        nwords += len(words)
        
    return {"lines": nlines, "words": nwords, "characters": nchars}

def statistics1(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }

"""
? Write a function called find_and_replace, which takes in a file name, a word to search for, and a replacement word. Replaces all instances of the word in the file with the replacement word.

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)
'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''
"""
def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()

"""
For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:

add_user : Takes in a first name and a last name and adds a new user to the users.csv file.
'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johonson
'''
"""
from csv import writer
def add_user(first, last):
    with open("users.csv", "a") as file:
        csv_writer = writer(file)
        csv_writer.writerow([first, last])

"""
?For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:

print_users : prints out all of the first and last names in the users.csv file
'''
print_users() # None
# prints to the console:
# Colt Steele
'''
"""
import csv

def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader: 
            print("{} {}".format(row['First Name'], row['Last Name']))

"""
? For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:

find_user : Takes in a first name and a last name and searches for a user with that first and last name in the users.csv file. If the user is found, find_user  returns the index where the user is found. Otherwise it returns a message stating that the user wasn't found.
'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
"""
#import csv

def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)


"""
?For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:

update_users : Takes in an old first name, an old last name, a new first name, and a new last name. Updates the users.csv file so that any user whose first and last names match the old first and last names are updated to the new first and last names. The function should return a count of how many users were updated.

'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''
"""
#import csv

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
     
        return "Users updated: {}.".format(count)
#import csv

def delete_users(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users deleted: {}.".format(count)


"""
? Write a function called is_valid_time  that accepts a single string argument.  It should return True  if the string is formatted correctly as a time, like 3:15 or 12:48 and return False otherwise.  Note that times can start with a single number (2:30) or two (11:18).  

    is_valid_time("10:45")       #True
    is_valid_time("1:23")        #True
    is_valid_time("10.45")       #False
    is_valid_time("1999")        #False
    is_valid_time("145:23")      #False
In order to return True, the string should ONLY contain the time, and no other characters

    is_valid_time("it is 12:15") #False
    is_valid_time("12:15")       #True

Don't worry about impossible times like 88:76, just focus on the formatting!

    is_valid_time("34:55") #True
"""
import re
# Define is_valid_time below:
def is_valid_time(str1):
    pattern = re.compile(r'^\d{1,2}:\d{1,2}$')
    match = pattern.search(str1)
    if match:
        return True
    return False

"""
? Write a function called parse_bytes  that accepts a single string.  It should return a list of the binary bytes contained in the string.  Each byte is just a combination of eight 1's or 0's. For example:

parse_bytes("11010101 101 323")    # ['11010101']

parse_bytes("my data is: 10101010 11100010")    # ['10101010', '11100010']

parse_bytes("asdsa")   # []

Hints: take advantage of \b Not all bytes will have a space before and after, some come at the beginning of a file or at the end.  Use findall!
"""
# don't forget to import re
#import re
# define parse_bytes below:

def parse_bytes(str1):
    pattern = re.compile(r'\b([01]{8})\b')
    return pattern.findall(str1)

#import re
 
def parse_bytes1(str1):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(str1)
    return results

"""
? Define a function called parse_date  that accepts a single string.  Your code should check to see if the string matches a date format.  We're going to use the DMY format of "dd/mm/yyyy", but it should also work with "dd.mm.yyyy" and "dd,mm,yyyy". If you are American, note that Day if before Month!  However, rather than simply returning True or False if the string matches...you should instead return a dictionary containing the three parts of the date with the keys "d" , "m" , and "y"  like so:

    parse_date("01/22/1999") # {'d': '01', 'm': '22', 'y': '1999'}

 Note: the string should be an EXACT match, containing the date and nothing else. If there is no match, return None

    parse_date("12,04,2003")  #{'d': '12', 'm': '04', 'y': '2003'}
    parse_date("12.11.2003")  #{'d': '12', 'm': '11', 'y': '2003'}
    parse_date("12.11.200312") #None
"""
#import re

def parse_date(str1):
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(str1)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None

#import re

def censor(str1):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", str1)

"""
? Write a function called reverse_string which accepts a string and returns a new string with all the characters reversed. 
'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''
"""
def reverse_string(str1):
    return str1[::-1]

"""
? Write a function called list_check, which accepts a list and returns True if each value in the list is a list. Otherwise the function should return False.
'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''
"""
def list_check(alist):
    for item in alist:
        if type(item) != list:
            return False
    return True

"""
? Write a function called remove_every_other that accepts a list and returns a new list with every second value removed.
'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''
"""
def remove_every_other(alist):
    x = alist[::2]
    return x

"""
? Write a function called sum_pairs which accepts a list and a number and returns the first pair of numbers that sum to the number passed to the function.
'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''
"""
def sum_pairs(alist, num):
    numtimes = len(alist) // 2
    i = 0
    for m in range(numtimes):
        if (alist[i] + alist[i+1]) == num:
            return [alist[i], alist[i+1]]
        i += 2
    return []

"""
? Write a function called vowel_count that accepts a string and returns a dictionary with the keys as the vowels and values as the count of times that vowel appears in the string.
'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''
"""
def vowel_count(str1):
    d = {}.fromkeys("aeiou", 0)
    for char in str1.lower():
        if char in "aeiou":
            d[char] += 1
    return {k:v for k,v in d.items() if d[k] > 0}

"""
? Write a function called titleize which accepts a string of words and returns a new string with the first letter of every word in the string capitalized.
'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''
"""
def titleize(str1):
    words = str1.split(" ")
    ret = ""
    for word in words:
        astr = word[0].upper() + word[1:]
        ret += astr + " "
    ret = ret[0:len(ret) - 1]  # remove last space
    return ret

"""
?Write a function called find_factors which accepts a number and returns a list of all of the numbers which are is divisible by starting from 1 and going up to the number.
'''
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''
def find_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]

? Write a function called includes which accepts a collection, a value, and an optional starting index. The function should return True if the value exists in the collection when we search starting from the starting index. Otherwise, it should return False.

The collection can be a string, a list, or a dictionary. If the collection is a string or array, the third parameter is a starting index for where to search from. If the collection is a dictionary, the function searches for the value among values in the dictionary; since objects have no sort order, the third parameter is ignored.
'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''
"""
def includes(collection, val, startidx = 0):
    if type(collection) is dict:
        return (val in collection.values())
    return val in collection[startidx:]

"""
? Write a function called repeat, which accepts a string and a number and returns a new string with the string passed to the function repeated the number amount of times. Do not use the built in repeat method!
'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''
"""
def repeat(str1, num):
    ret = ""
    for n in range(num):
        ret += str1
    return ret

"""
?Given a string and a number n, truncate the string to a shorter string containing at most n characters. If the string gets truncated, the truncated return string should have a "..." at the end. Because of this, the smallest number passed in as a second argument should be 3.
'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''
"""
def truncate(str1, num):
    if num < 3:
        return "Truncation must be at least 3 characters."
    if num > len(str1):
        return str1
    return str1[0:num-3] + "..."

"""
?two_list_dictionary
Write a function called two_list_dictionary which accepts two lists of varying lengths.The first list consists of keys and the second one consists of values. Your function should return a dictionary created from the keys and values. If there are not enough values, the remaining keys should have a value of null. If there not enough keys, just ignore the remaining values.
'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': null}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': null}
'''
"""
def two_list_dictionary(keylist, valuelist):
    ntimes = min(len(keylist), len(valuelist))
    d = {keylist[i]:valuelist[i] for i in range(ntimes) }
    if len(keylist) > len(valuelist):
        rest = {}.fromkeys(keylist[ntimes:], None)
        d.update(rest)
    return d

"""
? range_in_list

Write a function called range_in_list which accepts a list and start and end indices, and returns the sum of the values between (and including) the start and end index.

If a start parameter is not passed in, it should default to zero. If an end parameter is not passed in, it should default to the last value in the list. Also, if the end argument is too large, the sum should still go through the end of the list.
'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''
"""
def range_in_list(alist, startidx = 0, endidx = 0):
    if len(alist) == 0:
        return 0
    if endidx == 0 or endidx > len(alist):
        endidx = len(alist) - 1
    sum = 0
    for i in range(startidx, endidx + 1): sum += alist[i]
    return sum

"""
?same_frequency
Write a function called same_frequency which accepts two numbers and returns True if they contain the same frequency of digits. Otherwise, it returns False.
'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''
"""
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
        if d1[key] != d2[key]:
            return False
    return True

"""
Write a function called nth, which accepts a list and a number and returns the element at whatever index is the number in the list. If the number is negative, the nth element from the end is returned.

You can assume that number will always be between the negative value of the list length, and the list length minus 1.
'''
nth(['a', 'b', 'c', 'd'], 1);  # 'b' 
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
'''
"""
def nth(alist, idx):
    tlist = alist.copy()
    return tlist.pop(idx)

"""
?find_the_duplicate
Write a function called find_the_duplicate which accepts an array of numbers containing a single duplicate. The function returns the number which is a duplicate or None if there are no duplicates.
'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''
"""
def find_the_duplicate(alist):
    for item in alist:
        if alist.count(item) > 1:
            return item
    return None

"""
?
sum_up_diagonals
Write a function called sum_up_diagonals which accepts an NxN list of lists and sums the two main diagonals in the array: the one from the upper left to the lower right, and the one from the upper right to the lower left.
'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
];
 
sum_up_diagonals(list1); # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
];
 
sum_up_diagonals(list2); # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
];

sum_up_diagonals(list3); # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
];
 
sum_up_diagonals(list4); # 68
'''
"""
def sum_up_diagonals(alist):
    ci = 0
    list1 = []
    for i in range(len(alist)):
        list1.append(alist[i][ci])
        ci += 1
    list2 = []
    ci = -1
    for i in range(len(alist)):
        list2.append(alist[i][ci])
        ci -= 1
    total = sum(list1) + sum(list2)
    return total

"""
? min_max_key_in_dictionary
Write a function called min_max_key_in_dictionary which returns a list with the lowest key in the dictionary and the highest key in the dictionary. You can assume that the dictionary will have keys that are numbers.
'''
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
'''
"""
def min_max_key_in_dictionary(adict):
    return [min(adict.keys()), max(adict.keys())]

"""
?
find_greater_numbers

Write a function called find_greater_numbers which accepts a list and returns the number of times a number is followed by a larger number.
'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''
"""
def find_greater_numbers(alist):
    if len(alist) == 0:
        return 0
    total = 0
    mylist = alist.copy()
    num = mylist[0]
    while len(mylist) != 1:
        for i in range((len(mylist) - 1)):
            if num < mylist[i+1]:
                total += 1
        x = mylist.pop(0)
        num = mylist[0]
    return total

"""
?two_oldest - Write a function called two_oldest. The function should take a list of numbers as its argument and return the two highest numbers within the list. The returned value should be a list in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order.
'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''
"""
def two_oldest_ages(alist):
    alist.sort()
    return [alist[-2], alist[-1]]

"""
? is_odd_string - Write a function called is_odd_string which returns true if sum of each character's position in the alphabet is odd. For example, "a" is in the first position, "b" is in the second position, and so on. If the sum is even, return false.
'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''
"""
import string
def is_odd_string(str1):
    CHARS = list(string.ascii_lowercase)
    CHARS.insert(0, " ")  # to push index of a to 1
    total = 0
    for char in str1:
        total += CHARS.index(char)
    return (total % 2 != 0)

"""
? - valid_parentheses
Write a function called valid_parentheses that takes a string of parentheses, and determines if the order of the parentheses is valid. valid_parentheses should return true if the string is valid, and false if it's invalid.

'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''
"""
def valid_parentheses(str1):
    if str1[0] == ")" or len(str1) == 1:
        return False
    if str1.count("(") != str1.count(")"):
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

"""
? reverse_vowels - Write a function called reverse_vowels. This function should reverse the vowels in a string. Any characters which are not vowels should remain in their original position. You should not consider "y" to be a vowel.
'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''
"""
def reverse_vowels(str1):
    vowels = "aeiouAEIOU"
    x = [char for char in str1 if char in vowels]
    ret = ""
    idx = -1
    for char in str1:
        if char not in vowels:
            ret += char
        else:
            ret += x[idx]
            idx -= 1
    return ret

"""
? three_odd_numbers - Write a function called three_odd_numbers, which accepts a list of numbers and returns True  if any three consecutive numbers sum to an odd number.
'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''
"""
def three_odd_numbers(alist):
    ntimes = len(alist) - 2
    idx = 0
    for i in range(ntimes):
        x = [alist[idx], alist[idx+1], alist[idx+2]]
        if sum(x) % 2 != 0:
            return True
        idx += 1
    return False

"""
? mode - This is another trickier exercise.  Don't feel bad if you get stuck or need to move on and come back later on!

Write a function called mode. This function accepts a list of numbers and returns the most frequent number in the list of numbers. You can assume that the mode will be unique.

    mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])  # 4
"""

from collections import Counter
def mode(nums):
    cnt = Counter(nums)
    x = cnt.most_common(1)
    return x[0][0]
"""
Mode Solution

This is another trickier exercise.  Don't feel bad if you were unable to complete it!

I start by defining the function, which accepts a single argument we'll call collection .

Next, I create a new dictionary that maps items in the collection to the number of times they appear in the collection. I used a dictionary comprehension along with count()  to achieve this.

    count = {val: collection.count(val) for val in collection}

If collection was the string "happy", the resulting count dict would look like this:

    {
        'h': 1, 
        'a': 1, 
        'p': 2, 
        'y': 1
    }
     

Now, I just need to find the maximum number in all the values (2 in my example).  To do that, I use

    max_value = max(count.values())

Now we know what the maximum value is, we just have to find the corresponding key. (we have 2, and need to work backwards to find 'p').  This is harder than you might think.

I convert the values in the dict to a list.  I do the same thing to all the keys.  Then, I find the index of max_value in the values and use that to access the corresponding key.

    #find index of max_value in the values
    correct_index = list(count.values()).index(max_value)
    #use that index to find the correct key
    return list(count.keys())[correct_index]

Here is the complete code:
"""

def mode1(collection):
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]

"""
? running_average - Create a function running_average that returns a function. When the function returned is passed a value, the function returns the current average of all previous function calls. You will have to use closure to solve this. You should round all answers to the 2nd decimal place.
'''
rAvg = running_average();
rAvg(10) // 10.0;
rAvg(11) // 10.5;
rAvg(12) // 11;

rAvg2 = running_average()
rAvg2(1) // 1
rAvg2(3) // 2
'''
"""
def running_average():
    count = 0
    total = 0
    def average(x):
        nonlocal count
        nonlocal total
        count += 1
        total += x
        return total / count
    return average

"""
? letter_counter - Write a function called letter_counter which accepts a string and returns a function. When the inner function is invoked it should accept a parameter which is a letter, and the inner function should return the number of times that letter appears. This inner function should be case insensitive.
'''
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''
"""
def letter_counter(str1):
    word = str1
    def counter(x):
        return word.lower().count(x)
    return counter

"""
? once - Write a function called once. This function accepts a function and returns a new function that can only be invoked once. If the function is invoked more than once, it should return None. Hint you will need to define a new function inside of your once function and return that function. You can add properties to your inner function to see if it has run already.

'''
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
'''
"""
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

"""
Next Prime Generator

Write a function called next_prime, which returns a generator that will yield an unlimited number of primes, starting from the first prime (2).

Recall that a prime number is any whole number that has exactly two divisors: one and the number itself. The first few primes are 2, 3, 5, 7, 11, ... .
'''
primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''
"""
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
