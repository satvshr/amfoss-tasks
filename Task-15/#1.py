T = int(input())
for i  in range(T):
    sums=0
    N = int(input())
    for i in range(1, N):
        if (i % 3 == 0 or i % 5 == 0):
            sums += i
    print (sums)
