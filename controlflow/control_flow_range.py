# https://docs.python.org/3.8/tutorial/controlflow.html#the-range-function

def test_range():
    for i in range(10):
        if i % 2 != 0:
            print(i)

test_range()

# 0,2,4,...,10

    # list(range(5, 10))
    # list(range(0, 10, 3))
    # list(range(-10, -100, -30))
    # a = ['Mary', 'had', 'a', 'little', 'lamb']
    # for i in range(len(a)):
    #     print(i, a[i])
    #  sum(range(4))  # 0 + 1 + 2 + 3