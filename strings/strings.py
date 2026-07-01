# Reversing a string (Easiest O(N) way) slicing
my_str = "Hello World"
print(my_str[::-1])

# Basic Slicing (Gets indices 0, 1, 2, and 3)
text = "Python"
print(text[0:4])    # Output: "Pyth"

# Return a string with characters converted to uppercase
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

#Return a string with all characters converted to lowercase

my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

#  Returns a new string with the specified leading and 
#trailing characters removed. If no argument is passed 
#it removes leading and trailing whitespace.

my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"

#Returns a new string with all occurrences 
#of old replaced by new.

my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world


#Splits a string on a specified separator into a list of strings.
#If no separator is specified, it splits on whitespace.

my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']

#Joins elements of an iterable into a string with a separator.
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world

#Returns a boolean indicating if a string starts with the specified prefix.
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

#Returns the index of the first occurrence of substring, or -1 if it doesn't find one.
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6

# Returns the number of times a substring appears in a string.
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2