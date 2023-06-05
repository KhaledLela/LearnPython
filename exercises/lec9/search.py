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
import json


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
            # return file.read()
            return json.load(file)  # load as json dic {} key-value
    except Exception as ex:
        print(f"Something went wrong: {ex}")


summary = load_summary()  # dic {key:value}
# print(summary)
results = {}


# Search for the keyword in the JSON file
# list [3,'ahmed',true]
# {}
# Tuple ()
def search_keyword():
    count = 0
    # for key in summary:
    # for key, value in summary.items():
    for value in summary.values():
        # check if value is array or str
        if isinstance(value, str):
            count += make_count(value)
        else:
            for text in value:
                count += make_count(text)
    print(f"{keyword}:{count}")
    results[keyword] = count


#
#
def make_count(text: str):
    count = 0
    for word in text.split():
        # if keyword == word: # Google != Google's
        # if word.__contains__(keyword):
        if keyword in word:
            count += 1
    return count


# Ask the user to input the search keyword
while True:
    keyword = input("Enter search keyword:\n")
    if keyword == "#":
        break
    search_keyword()


def save_results():
    try:
        with open("result.txt", "a") as file:
            # file.write(results)  # save results error occurred
            # file.write(str(results))
            file.write(f"\n{results}\n")
    except Exception as ex:
        print(f"Something went wrong: {ex}")


# Save the result into result.txt
save_results()
print(results)
