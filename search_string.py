str = "dyknbvcklijhbvcfgkmpojj,mnbvcgttyfjhkjbvbbvbc"
find = "bvc"
k = 0

for i in range(len(str)):
    if find == str[i:i+len(find)]:
        k = k + 1

print(k)