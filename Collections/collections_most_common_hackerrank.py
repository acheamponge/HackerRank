from collections import Counter

s = list(Counter(raw_input()).most_common(3))
for i in s:
    print  i[0], i[1]

