import secrets
from itertools import groupby


def add_text():
    text_string = []
    input_text = "text: Lorem ipsum dolor sit amet, consectetur adipiscing elit.".split(':')
#    input_text = input().split(':')
    if input_text[0] == 'text':
        text_string = input_text[1].strip()
    return text_string


def add_alphabet():
    alphabet = []
    input_alphabet = "alphabet: l o r e m i p p s u m".split(':')
#    input_alphabet = input().split(':')
    if input_alphabet[0] == 'alphabet':
        alphabet_str = input_alphabet[1].strip()
        pre_alphabet = alphabet_str.split(' ')
        alphabet = [x for x, _ in groupby(pre_alphabet)]
    return alphabet


def consist(v, array):
    try:
        array.index(v)
        return True
    except ValueError:
        return False


def coding(alpha, text_string):
    code_text = ''
    decode_dict = {}
    for x in range(len(text_string)):
        if consist(text_string[x], alpha):
            k = alpha.index(text_string[x])
            while True:
                j = secrets.randbelow(len(alpha))
                if k != j:
                    code_text += alpha[j]
                    decode_dict[x] = text_string[x]
                    break
        else:
            code_text += text_string[x]
    return code_text, decode_dict


def decoding(decoding_string, decode_dict):
    decode_string = ''
    for x in range(len(decoding_string)):
        if x in decode_dict:
            decode_string += decode_dict[x]
        else:
            decode_string += decoding_string[x]
    return decode_string


'''if input_alphabet[0] == 'alphabet':
    alphabet_str = input_alphabet[1].strip()
    pre_alphabet = alphabet_str.split(' ')
    alphabet = [x for x, _ in groupby(pre_alphabet)]

if input_text[0] == 'text':
    text_string = input_text[1].strip()'''


our_alphabet = add_alphabet()
our_text_string = add_text()

final, decode = coding(our_alphabet, our_text_string)
print(final)
print(our_text_string)
print(decode)
print(our_alphabet, end="\n\n\n\n")
print(decoding(final, decode))
