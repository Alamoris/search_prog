import secrets
import sys
import random
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--alph', action='store', help='Adding alphabet')
parser.add_argument('-f', '--file', action='store', help='Text file name')
#parser.add_argument('-c', '--code', action='store', help='Run coding')
#parser.add_argument('-O', '--open', action='store', help='Dictionary path')
#parser.add_argument('-F', '--file_store', action='store', help='File name. Read the first line as an alphabet ')


def add_alphabet(alphabet_str):
    alphabet = []
    pre_alphabet = [x for x in alphabet_str]
    for x in pre_alphabet:
        if x not in alphabet:
            alphabet.append(x)
    return alphabet


def alhpa_missing(text_list):
    alphabet_list = []
    for line in text_list:
        for char in line:
            if char not in alphabet_list:
                alphabet_list.append(char)
    return alphabet_list


def shuffle(alphabet):
    working_alph = []
    for x in alphabet:
        if x not in working_alph:
            working_alph.append(x)
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


def input_data(alph, file):
    line = ''
    if alph is not None and file is None:
        alphabet = alph
        for stdin_symbol in sys.stdin.read():
            line += stdin_symbol
        text_list = line.split('\n')
        return alphabet, text_list
    elif alph is not None and file is not None:
        text_list = []
        alphabet = alph
        with open('{0}'.format(file), 'r') as text_file:
            for in_string in text_file:
                in_string = in_string.strip()
                text_list.append(in_string[:len(in_string)-1])
        return alphabet, text_list

    elif alph is None and file is None:
        i = 0
        alphabet = ''
        text_list = []
        for stdin_simbol in sys.stdin.read():
            line += stdin_simbol
        file_list = line.split('\n')
        for line in file_list:
            line = line.strip()
            if i == 0:
                if line[:8] == 'alphabet':
                    alphabet = line[9:]
                    if len(alphabet) <= 2:
                        print('Неверно введен алфавит, должно быть более 2 символов')
                        sys.exit()
                else:
                    print('Неверно введен алфавит, вводите ключевое слово alphabet:')
                    sys.exit()
            elif i == 1:
                if line != 'text:':
                    print('Неверно введен текст, вводите ключевое слово text:')
                    sys.exit()
            else:
                text_list.append(line)
            i += 1
        return alphabet, text_list

    elif alph is None and file is not None:
        i = 0
        alphabet = ''
        text_list = []
        with open('{0}'.format(file), 'r') as text_file:
            for in_string in text_file:
                in_string = in_string.strip()
                if i == 0:
                    alphabet = in_string.strip()
                else:
                    text_list.append(in_string[:len(in_string)])
                i += 1
        return alphabet, text_list


def coding(alpha, text_list):
    if len(alpha) == 0:
        alpha = alhpa_missing(text_string)
    alpha_dict = shuffle(alpha)
    code_text = ''
    for line in text_list:
        for x in range(len(line)):
            if line[x] in alpha_dict:
                code_text += alpha_dict[line[x]]
            else:
                code_text += line[x]
        code_text += '\n'
    return code_text, alpha_dict


def decoding(decoding_array, decoding_dict):
    decode_dict = {}
    decode_string = ''
    decode_array = []
    for k,v in decoding_dict.items():
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

input_alphabet, text_array = input_data(parser.parse_args().alph, parser.parse_args().file)
alphabet = add_alphabet(input_alphabet)
final, decode = coding(alphabet, text_array)
result_array = decoding(final, decode)



with open('chiper.v2.0_dict.txt', "w") as f:
    json.dump(decode, f)

#Вывод текста для себя и проверка работоспособности
decode_array = []
for k, v in decode.items():
    decode_string = "{0} ---> {1}\n".format(k, v)
    decode_array.append(decode_string)

with open('test.txt', 'w') as file:
    file.write('Закодированный текст\n\n' + final + '\n\n' + "Словарь для расшифровки текста\n\n")
    for x in decode_array:
        file.write(x)
    file.write("Расшифрованный текст" + '\n\n')
    for i in result_array:
        file.write(i)





