x = list(map(int,input().split()))
y = list(map(int,input().split()))
sums = 0
for i in y:
    sums += i
if sums % 4 == 0:
    print(sums//4)
else:
    print((sums//4)+1)
