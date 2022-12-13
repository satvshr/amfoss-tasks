n = int(input())
for i in range(n):
    m = int(input())
    def ispal(num):
        numstring = str(num)
        for i in range(0,int(len(numstring)/2+1)):
            if (numstring[i] != numstring[-i-1]):
                return False
        return True
    maxi = 0
    max1, max2 = 0,0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            while product <= m:
                if ispal(product):
                    if(product > maxi):
                        maxi = product
                        max1, max2 = i, j
    print(str(maxi))