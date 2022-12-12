a = list(map(int,input().split()))
b = a[0]
c = a[1]
magic = []
english = []
answer = []

for i in range (c):
    s = list(map(str,input().split()))

    magic.append(s[0])
    english.append(s[1])

# print(magic)
# print(english)

# key={}
# for i in magic:
#     for j in english:
#         if len(i) > len(j):
#             key[j] = i
#         if len(i) < len(j):
#             key[i] = j
#         else:
#             key[j] = i
#         english.remove(j)
#         break

# print(key)
x = list(map(str,input().split()))
for i in x:
                index = magic.index(i)
                if len(english[index]) < len(magic[index]):  
                    answer.append(english[index])
                if len(english[index]) > len(magic[index]):
                    answer.append(magic[index])
                if len(english[index]) == len(magic[index]):
                    answer.append(magic[index])

                
print(" ".join(answer))

            
        
        

        
# for i in [expecto,patronum,expecto]:
#     for j in {'defend': 'expecto', 'patronum': 'incantation'}:
# for i in range(c):
#     if magic[i] > english[i]:
#         answer.append(magic[i])
    
#     elif magic[i] < english[i]:
#         answer.append(english[i])
    
#     else:
#         answer.append(magic[i])

        


