x = 10
y = x   # Copy
print(x)    # x = 10
print(y)    # y = 10
y = 3
x, y = y, x     # x <-> y change
print(x)    # x = 3
print(y)    # y = 10
