"""
Write a program ask user for
input sentence
Then go throw each word to
1. print word counts
2. print word that repeated more times
"""
s = input('Enter a sentence:\n')
w_counts = dict()

words =s.split()
for word in words:
    w_counts[word] = w_counts.get(word, 0) + 1

print(w_counts)
print("repetition count", len(words))


+9*-