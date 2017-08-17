a = int(raw_input())

for i in range(a*2):
    a = raw_input()
    
    if i % 2 != 0:
        b = [int(i) for i in a.split()]
        c = int(len(b)-1)
        a = 'Yes'   
        j = 0
        for i in range(c):
            if b[j] < b[c]:
                c -= 1
                j += 1
                a = 'No'
       
                
        print a
