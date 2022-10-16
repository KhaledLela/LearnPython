str1 = 'hello'
str2 = ','
str3 = 'world'
str4 = str1 + str3

# print(str3[-1])   # d
# print(str3[-5])   # w
# print(str3[-6])   # error out of range
# print(str3[5])    # error out of range
# print(str3[:-1])  # str3[0:len(str3)-1] => worl
# print(str1[1:])   # str1[1:len()] => ello
# print(str4[1:9])  # helloworl
# print(str4[1:9:2]) # helloworld => elloworl => elwr
# print(str4[::-1])  # helloworld => dlrowolleh