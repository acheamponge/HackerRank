from collections import defaultdict

ordered_dictionary = defaultdict(list)
for i in range(int(raw_input())):
    a=[i for i in raw_input().split()]
       
    b=a[:-1]
    c =' '.join(b)
    ordered_dictionary[c].append(int(a[-1]))
for key, value in ordered_dictionary.items():
    print key, sum(value)
