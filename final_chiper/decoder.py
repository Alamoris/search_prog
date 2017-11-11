import json
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--inp_text', action='store', help='Path to decoding text')
parser.add_argument('-F', '--inp_dict', action='store', help='Path to decoding dictionary')
parser.add_argument('-O', '--out_file', action='store', help='Output path result')




def decoding(decoding_array, decoding_dict):
    decode_dict = {}
    decode_string = ''
    decode_array = []
    for k, v in decoding_dict.items():
        decode_dict[v] = k
    for line in decoding_array:
        for x in line:
            if x in decode_dict:
                decode_string += decode_dict[x]
            else:
                decode_string += x
        decode_array.append(decode_string)
        decode_string = ''
    return decode_array

inp_text = parser.parse_args().inp_text
inp_dict = parser.parse_args().inp_dict
out_file = parser.parse_args().out_file

if bool(inp_text):  # Введен ли оператор -f
    with open('{}'.format(inp_text)) as f:
        final = f.readlines()
else:
    final = sys.stdin.readlines()

with open('{}'.format(inp_dict), 'r') as read_dict:  # Получение пути к словарю из аргумента -F
    decode = json.load(read_dict)

result_array = decoding(final, decode)

if bool(out_file):  # Введен ли оператор -О
    with open('{}'.format(out_file), 'w') as f:
        for x in result_array:
            f.write(x)
else:
    for x in result_array:
        sys.stdout.write(x)



