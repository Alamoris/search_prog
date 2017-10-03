import json

cipher = open('cipher.txt', 'r')
transcript = open('transcript.txt', 'r')
result_string= ''
cipher_arr = json.load(cipher)
transcript_dict = json.load(transcript)

for i in range(len(cipher_arr)):
    result_string = result_string + ' {0}'.format(transcript_dict[str(cipher_arr[i])])

print(result_string)

cipher.close()
transcript.close()