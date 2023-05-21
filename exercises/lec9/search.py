"""
Accept user input and search in json file loaded from same dir that convert the following :
# ask user to input search keyword:
# Load sample.json
# handle error read permission.
# collect result of search key nr of appearance
# save result into result.txt
# Keep searching til user enter "#"
# print each result and at the end print all result summary.
"""


def save_results(results):
    try:
        with open('results.txt', 'w') as file:
            file.write(results)
            print("file saved successfully!")
    except IOError as error:
        print(f"Error during saving! {error}")


#
# def load_summary():
#     file = None
#     try:
#         file = open('summary.json', 'r')
#         summary = file.read()
#         return summary
#     except Exception as ex:
#         print(f"Something went wrong: {ex}")
#     finally:
#         if file is not None:
#             file.close()

def load_summary():
    try:
        with open("summary.json", "r") as file:
            return file.read()
    except Exception as ex:
        print(f"Something went wrong: {ex}")


summary = load_summary()

results = {}


# Search for the keyword in the JSON file
def search_keyword(keyword):
    count = 0
    for word in summary:
        if keyword == word:
            count += 1
    print(f"{keyword : {count}}")
    results[keyword] = count


# Ask the user to input the search keyword
while True:
    keyword = input("Enter search keyword:\n")
    if keyword is "#":
        break
    search_keyword(keyword)

# Save the result into result.txt
print(results)
