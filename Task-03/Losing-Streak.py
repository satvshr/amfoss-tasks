a = list(map(int,input().split()))
y = a[0]
x = a[1]
ans = 0
z = x/y
while z%2==0:
    z=z/2
    ans += 1
while z%3==0:
    z=z/3
    ans +=  1

if x == y:
    print(0)
elif z==1 :
    print(ans)
else:
    print(-1)
