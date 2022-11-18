"""
Write a program ask user for
input sentence split by space
Then go through each word to
1. print word counts
2. print word that repeated more
3. print repetition count

ahmed ibrahim ibrahim ibrahim khaled abdelrahman
"""
s = input('Enter a sentence:\n')
words = s.split()
# wc = dict()
wc = {}
for word in words:
    wc[word] = wc.get(word, 0) + 1
print(wc)

max_count = 0
max_w = None
for word, count in wc.items():
    if count > max_count:
        max_count = count
        max_w = word
print("word count duplicated:", len(words))
print("word count unique:", len(wc))
print("Max repeated word:", max_w)
print("Max word count:", max_count)
