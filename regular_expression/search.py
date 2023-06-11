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
