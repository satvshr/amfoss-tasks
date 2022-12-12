T = int(input())
for i  in range(T):
    A = []
    N = int(input())
    a = 0
    b = 1
    c = 0
    while N > c:
        sums = 0
        c = a + b
        A.append(c)
        if c > N:
            A.remove(c)
        a = b
        b = c
    for i in A:
        if i % 2 == 0:
            sums += i
    print(sums)
            
        
        
