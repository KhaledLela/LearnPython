# https://docs.python.org/3/tutorial/controlflow.html#defining-functions

# def keyword to define the function.
# DRY
def add_two(x, y=3, z=4):
    print(x + y + z)


add_two(2)  # 2+3+4 =9
add_two(y=2, x=0)  # 0+2+4 =6
add_two(z=10, x=20)  # 20+3+10 =33
add_two(2, z=10)
