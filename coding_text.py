import random
import json

k = 0
arr = []
dict = {}
final_str = ''
cipher = open('cipher.txt', 'w')
transcript = open('transcript.txt', 'w')
string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tincidunt nibh ac porta ornare. Vivamus mattis mattis congue. Sed at faucibus sapien. Pellentesque non tortor sapien. Aliquam vestibulum ex ac blandit tincidunt. Etiam congue, sapien nec convallis imperdiet, justo dolor tempor diam, ac lacinia leo turpis molestie diam. Phasellus vel sem in mauris convallis tincidunt et in elit. Maecenas auctor pretium libero eget congue. Vivamus sagittis, leo id auctor auctor, purus magna aliquam nunc, eu tincidunt nibh lorem ac metus. Donec congue lorem ut rutrum interdum. Etiam ante lorem, ullamcorper at pharetra blandit, laoreet in velit. Nunc enim orci, tempor non nibh a, maximus fermentum leo. Suspendisse id imperdiet ante, eget lacinia nunc. Cras sit amet justo in arcu aliquet fermentum. Pellentesque malesuada venenatis neque et blandit. In justo sem, mollis ac urna ac, fermentum porta diam."
word_arr = string.split()

while len(arr) < len(string.split()):
    arr.append(k)
    k = k + 1

random.shuffle(arr)

for i,j in zip(arr, word_arr):
    dict[i] = j

json.dump(arr, cipher)
json.dump(dict, transcript)
cipher.close()
transcript.close()
#for i in range(len(arr)):
    #final_str = final_str + ' {0}'.format(dict[arr[i]])


