import math
T = int(input())
for i in range(T):
    n = int(input())
    import math
    ans = 1
    for i in range(1, n+1):
        ans *= i // math.gcd(i, ans)
    print(str(ans))

