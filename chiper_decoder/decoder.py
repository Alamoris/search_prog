import json
import sys


def decoding(decoding_string, decoding_dict):
    decode_dict = {}
    decode_string = ''
    for k,v in decoding_dict.items():
        decode_dict[v] = k
    for x in decoding_string:
        if x in decode_dict:
            decode_string += decode_dict[x]
        else:
            decode_string += x
    return decode_string


with open('chiper.v2.0_dict.txt', 'r') as f:
    decode = json.load(f)

final = sys.stdin.readline()
print(decoding(final, decode))