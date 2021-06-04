from collections import Counter
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print([[x,z.count(x)] for x in set(z)])