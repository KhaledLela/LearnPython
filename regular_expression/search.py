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
import re

with open('mbox-short.txt') as hand:
    for line in hand:
        line = line.rstrip()
        # if line.find('From:') != -1:
        # if re.search('From:', line):
        # if line.startswith('From:'):
        if re.search('^From:.+@', line):
            print(line)
