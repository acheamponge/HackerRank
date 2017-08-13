from collections import deque
a = int(raw_input())
b = deque()
for i in range(a):
    a = raw_input().split()
    if 'append' in a:
        b.append(int(a[-1]))
    elif 'appendleft' in a:
        b.appendleft(int(a[-1]))
    elif 'pop' in a:
        b.pop()
    elif 'popleft' in a:
        b.popleft()

for i in b:
    print i,

