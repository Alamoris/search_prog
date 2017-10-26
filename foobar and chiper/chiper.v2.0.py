import secrets
from itertools import groupby
import sys
import random


def add_text():
    text_string = []
    #input_text = "text: Lorem ipsum dolor sit amet, consectetur adipiscing elit.".split(':')
    input_text = input().split(':')
    if input_text[0] == 'text':
        text_string = input_text[1].strip()
    else:
        print('Неверно введен текст')
        sys.exit()
    return text_string


def add_alphabet():
    alphabet = []
#    input_alphabet = "alphabet:lorem ipsum"
    input_alphabet = input()
    if input_alphabet[:8] == 'alphabet':
        alphabet_str = input_alphabet[9:].strip()
        pre_alphabet = [x for x in alphabet_str]
        alphabet = [x for x, _ in groupby(pre_alphabet)]
    else:
        print("Неверно введен алфавит, что бы задать программе алфавит введите alphabet:(алфавит)")
        sys.exit()
    return alphabet


def alhpa_missing(text_string):
    alphabet_list = []
    for x in text_string:
        if x not in alphabet_list:
            alphabet_list.append(x)
    return alphabet_list


def shuffle(alphabet):
    working_alph = []
    for x in alphabet:
        if x not in working_alph:
            working_alph.append(x)
    print(len(working_alph))
    shuffle_alphabet_dict = {}
    shuffle_list = working_alph.copy()
    while True:
        random.shuffle(shuffle_list)
        k = 0
        for x in range(len(working_alph)):
            if working_alph[x] == shuffle_list[x]:
                k += 1
                break
        if k == 0:
            for x in range(len(working_alph)):
                shuffle_alphabet_dict[working_alph[x]] = shuffle_list[x]
            break
    return shuffle_alphabet_dict

def coding(alpha, text_string):
    if len(alpha) == 0:
        alpha = alhpa_missing(text_string)
    elif 1 <= len(alpha) < 3:
        print("Недостаточная длинна алфавита")
        sys.exit()
    alpha_dict = shuffle(alpha)
    code_text = ''
    for x in range(len(text_string)):
        if text_string[x] in alpha_dict:
            code_text += alpha_dict[text_string[x]]
        else:
            code_text += text_string[x]
    return code_text, alpha_dict


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

our_text_string = add_text()
our_alphabet = add_alphabet()

final, decode = coding(our_alphabet, our_text_string)
print(final)
print(our_text_string)
print(decode)
print(our_alphabet, end="\n\n\n\n")
print(decoding(final, decode))
