# with expression [as target]:
#     # Code block
# x = 10
# if x >2 :
# else:
# try:
#     x = 10 / 0
#     print(x)
# except NameError as ex:
#     print(ex)
# except Exception as ex:
#     print(ex)
# else:
#     print("do else!")
# finally:
#     print("clean resources")

# file = open('../../AI/langchain/sample.json')
# cont = file.read()
# items = cont.split("\\n")
# print(len(items), end="\n")
with open('../../AI/langchain/sample.json') as file:
    print(file.read())
