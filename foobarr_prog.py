import random
arr = []

while len(arr) < 50:
    arr.append(random.randint(0,1000))

for x in arr:
    if x % 5 == 0:
        arr[arr.index(x)] = 'bar'
    elif x % 3 == 0:
        arr[arr.index(x)] = 'foo'

print(arr)