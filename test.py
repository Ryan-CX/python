from collections import Counter, OrderedDict
s = 'leetcode'

for i, j in OrderedDict(Counter(s)).items():
    print(OrderedDict(Counter(s)))
    print(Counter(s))

    if j == 1:
        print(s.index(i))
    else:
        print('-1')

