from functools import reduce
a = 39
print(reduce(int.__mul__,map(int,'39')))
# print(reduce(int.__mul__, 39)
