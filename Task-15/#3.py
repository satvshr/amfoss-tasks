import math
N = int(input())
for j in range(N):
    T = int(input())
    prime = []
    for i in range(1, T+1):
        if T % i == 0:
            prime.append(i)
            for j in range(2, int(math.sqrt(i))):
                if i % j == 0:
                    prime.remove(i)
    largest = 0
    for p in prime:
        if T % p == 0:
            largest = p
            
    print (largest)

# N = int(input())
# for j in range(N):
#     n = int(input())
#     prime = []
#     i = 2
#     while i * i <= n:
#         is_prime = True
#         for p in prime:
#             if p * p > i:
#                 break
#             if i % p == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime.append(i)
#         i += 1
#     print(prime)
#     largest = 0
#     for p in prime:
#         if n % p == 0:
#             largest = p
#     print(p)