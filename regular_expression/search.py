"""
https://www.py4e.com/html3/11-regex
https://www.py4e.com/lectures3/Pythonlearn-11-Regex-Handout.txt

Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
"""

# Search for lines that contain 'From'
import json
import re

# def load_json():
#     try:
#         with open("mbox-short.json", "r") as file:
#             # return file.read()
#             return json.load(file)  # load as json dic {} key-value
#     except Exception as ex:
#         print(f"Something went wrong: {ex}") 

# def search(file , word:str):
#     for key in file:
#         if key == word:
#             print(file.get(key))


# file= load_json()
# search(file, 'name')


#
name = 'name'
def read_file():
     with open('mbox-short.txt') as txt:
        s = txt.read()
        return s
def find(name):
    if re.search(f'"{name}": ', s):
        lst = re.search(f'"{name}": "([^"]+)"', s)
        print(lst)
        print(lst.group(1))

    else:
        print('false')   
s = read_file()
find(name)



# with open('mbox-short.txt') as hand:
#     for line in hand:
#         line = line.rstrip()
#         # if line.find('From:') != -1:
#         # if re.search('From:', line):
#         # if line.startswith('From:'):
#         if re.search('^From:.+.*@', line):
#             print(line)

# s= 'X-j: 0.6961'
# x = re.findall('^X-.+: [0-5.7-9]+', s)
# print(x)


# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
    
#     if len(x) > 0:
#         print(x)


# hand = open('mbox-short copy.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('^X\S*: ([0-9.]+)', line)
#     if len(x) > 0:
#         print(x)