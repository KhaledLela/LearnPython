"""
String indexing operations
"""
s = 'abcdefgh'
# s[3] = 'j'        # string immutable
# s = 'j' + s[2:4]  # re-bind or reassign

# range(5) => [0,1,2,3,4]
# for i in range(0,len(s),2):
#     print(s[i])
#
# i =0
# while i<len(s):
#     print(s[i])
#     i+=1
#
# while True:
#     print(s[i])
#     i+=1
#     if i >= len(s):
#         break

for char in s:
    print(char)
