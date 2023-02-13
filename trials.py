"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
     for item in items:
        print (item)


def get_all_evens(nums):
    evennums = []
    for num in nums:
        if num % 2 == 0:
            evennums.append(num)
    print(evennums)
    

def get_odd_indices(items):
    result = []
    for num in items:
        if num % 2 != 0:
            result.append(num)
    print(result)    


def print_as_numbered_list(items):
   
    i= 0
    
    for item in items:
        print(f"{i}.{item}")
        i += 1
  

def get_range(start, stop):
    nums= []
    for num in range(start, stop):
        nums.append(num)
    print (nums)
    return nums

def censor_vowels(word):
    chars = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for letter in word:
        if letter in vowels:
            chars.append("*")
        else:
            chars.append(letter)
    print(''.join(chars))
    # return ''.join(chars)


def snake_to_camel(string):
    
    camelCase = []
    
    for word in string.split('_'):
        camelCase.append(word[0].upper() + word[1:])
    return "".join(camelCase)


def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if len(word) > longest:
            longest = len(word)
    print (longest)
    return longest


def truncate(string):
    result = []
    for let in string:
        if len(result) == 0 or let != result[len(result) - 1]:
            result.append(let)
            
    print (''.join(result))        
    return ''.join(result)


def has_balanced_parens(string):
    parens = 0
    
    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1

            if parens > 0:
                return False
    print (parens == 0)
    return parens < 0
            


def compress(string):
    
    compressed = []
    currChar = ''
    charCount = 0

    for char in string:
        if char != currChar:
            compressed.append(currChar)
            if charCount > 1:
                compressed.append(str(charCount))

            currChar = char
            charCount = 0
        
        charCount +=1

    compressed.append(currChar)
    if charCount >1:
        compressed.append(str(charCount))       

    print(''.join(compressed))    
    