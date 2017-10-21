from collections import deque
string = "dyknbvcklijhbvcfgkmpbvc,mnbvcgttyfjhkjbvbbvcc"
find = "bvc"
string_array = list(string)
search_list = deque()
our_string = ''
k = 0

for i in string_array:
    if len(search_list) <= len(find):
        search_list.append(i)
        our_string = ''.join(search_list)
    if find == our_string:
        k += 1
    if len(search_list) == 3:
        search_list.popleft()

print(k)