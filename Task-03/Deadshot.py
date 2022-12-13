n = int(input())
c = []
ans = 0
p = 1
q = 2
r = 3
s = 4
for i in range(n):
    a = list(map(int,input().split()))
    c.append(a)

    


for z in c:
    d = []
    counter = 0
    for i in c:
      #  print([z[0],i[0]],[z[1],i[1]])
    
        if (z[0] == i[0]) and (z[1] > i[1]):
            d.append(p)
        elif (z[0] == i[0]) and (z[1] < i[1]):
            d.append(q)
        elif (z[0] < i[0]) and (z[1] == i[1]):
            d.append(r)
        elif (z[0] > i[0]) and (z[1] == i[1]):
            d.append(s)
        if p in d:
            if q in d:
                if r in d:
                    if s in d:
                        ans+= 1
                        break
print(ans)

# for x in c:
#     for i in x:
#         print(i)
    
    
    
    
        
    
    
    