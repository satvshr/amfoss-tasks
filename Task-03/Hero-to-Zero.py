t=int(input())
mana = 0
counter = 0
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    l=len(a)
    a.sort()
        
    if (a[0] > 0):
        counter = 0
        for i in range(l-1):
            f1 = a[i]
            f2 = a[i+1]
            if (f1 == f2) and (a[0] != 0):
                q = l
                break
            elif (f1 != f2):
                counter += 1
                q = counter + 2

    if (a[0]==0):
        counter = 0
        for i in range(l):
            if (a[i] == 0):
                counter += 1
        q = l - counter
    print(q)
