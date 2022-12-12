n = int(input())
c = []
ans = 0

for i in range(n):
    a = list(map(int,input().split()))
    c.append(a)

    


for z in c:
    counter = 0
    for i in c:
      #  print([z[0],i[0]],[z[1],i[1]])
    
        if (z[0] == i[0]) and (z[1] > i[1]):
            counter += 1
            continue
        elif (z[0] == i[0]) and (z[1] < i[1]):
            counter += 1
            continue
        elif (z[0] < i[0]) and (z[1] == i[1]):
            counter += 1
            continue
        elif (z[0] > i[0]) and (z[1] == i[1]):
            counter += 1
            continue
    #print(counter)
    if counter == 5:
            ans += 1
            continue
print(ans)

# for x in c:
#     for i in x:
#         print(i)
    
    
    
    
        
    
    
    
