# https://docs.python.org/3.8/tutorial/controlflow.html#for-statements
# Measure some strings:
x = 10  # int
x = 2.5  # float
# name = 'My name'


def test_for(words):
    for w in words:
        print(w, len(w))


# test_for(['KH','AML','AH'])
# test_for(['Python','is','Awsome'])


users = {'KL': '01020', 'AH': '01010', 'IML': '01010'}

def test_for_copy():
    # Create a sample collection
    # Strategy:  Iterate over a copy
    for name, phone in users.copy().items():
        print('Name is:' + name + ' Phone is:' + phone)
        # if status == 'inactive':
        #     del users[user]

test_for_copy()



def test_for_new():
    # Strategy:  Create a new collection
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status