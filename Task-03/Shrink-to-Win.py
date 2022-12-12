n = input()
x = True
count = 0
result = []
if int(n) < 10:
    x = False
for i in n:
    result.append(i)
while x==True:
    sums=0
    for i in result:
        sums += int(i)
    a = str(sums)
    count += 1
    result = list(a)
    if sums < 10:
        x = False
print(count)
    
