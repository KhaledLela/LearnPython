grade = float(input("Enter your degree:\n"))
'''
Between 3 quotes you can add comments with multi lines.
# Single line comment 
# if grade > 1.0 and grade < 0: # should with valid range
# if 1.0 < grade < 0: # and can be simplified 
'''
if grade > 1.0 or grade < 0:
    print("Out of range")
elif grade >= 0.9:  # grade = 0.92
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
else:
    print("F")
