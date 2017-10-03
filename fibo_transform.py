import random

dict = {0: 0, 1: 1}
arr = []
arr_result = []

for i in range(2,101):
    dict[i] = dict[i-1] + dict[i-2]

while len(arr) < 50:
    arr.append(random.randint(0,100))
    print(arr[len(arr)-1], end = ' ')

print(' ')

for i in arr:
    arr_result.append(dict[i])

for x in arr_result:
    print(x, end = ' ')