import secrets
import sys
import random
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--alph', action='store', help='Adding alphabet')
parser.add_argument('-f', '--file', action='store', help='Text file name')
parser.add_argument('-c', '--code', action='store_const', const='1', help='Run coding')
parser.add_argument('-O', '--open_dict', action='store', help='Dictionary path')
parser.add_argument('-F', '--file_store', action='store', help='File name. Read the first line as an alphabet ')


def input_processing(alph, file_path, file_store_alph):
    init_tuple = ((bool(alph), bool(file_path), bool(file_store_alph)))
    if init_tuple[0] == True and init_tuple[2] == True:
        print('Конфликт операторов: введите или алфавит или файл с первой строкой алфавита')
        sys.exit()
    else:
        return input_data(alph, file_path, file_store_alph)


def alhpa_missing(text_string):
    alphabet_list = []
    for char in text_string:
        if char not in alphabet_list:
            if char != '\n':
                alphabet_list.append(char)
    return alphabet_list


def shuffle(alphabet):
    working_alph = []
    for x in alphabet:
        if x not in working_alph:
            working_alph.append(x)
    shuffle_alphabet_dict = {}
    shuffle_list = working_alph.copy()
    i = False
    while True:
        k = 0
        if not i:
            random.shuffle(shuffle_list)
        for x in range(len(working_alph)):
            if working_alph[x] == shuffle_list[x]:
                k += 1
                break
            if i:
                shuffle_alphabet_dict[working_alph[x]] = shuffle_list[x]
            if i and x == len(working_alph) - 1:
                return shuffle_alphabet_dict
            if x == len(working_alph)-1 and k == 0:
                i = True
                break


def input_data(alph, text, alph_file):
    '''Doc string'''

    def one_string_alph(alph_file):
        with open('{}'.format(alph_file), 'r') as f:
            alphabet = f.readline()
        return alphabet


    inp = ((bool(alph), bool(text)))
    text_string = ''
    if inp == (True, False):
        alphabet = alph
        for stdin_line in sys.stdin.readlines():
            text_string += stdin_line
        return alphabet, text_string

    elif inp == (True, True):
        alphabet = alph
        with open('{0}'.format(text), 'r') as text_file:
            for in_string in text_file.readlines():
                in_string = in_string.strip()
                text_string += in_string
        return alphabet, text_string

    elif inp == (False, False):
        i = 0
        alphabet = ''
        text = ''
        for stdin_line in sys.stdin.readlines():
            text_string += stdin_line
        for line in text_string.split('\n'):
            line = line.strip()
            if i == 0:
                if bool(alph_file):
                    alphabet = one_string_alph(alph_file)
                else:
                    alpha_line = line.split(':')
                    if alpha_line[0] == 'alphabet':
                        alphabet = alpha_line[1]
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
                text += line
                text += '\n'
            i += 1
        return alphabet, text

    elif inp == (False, True):
        i = 0
        alphabet = ''
        text_list = []
        with open('{0}'.format(text), 'r') as text_file:
            for in_string in text_file.readlines():  # Изменить на считывание строк а не всего файла
                in_string = in_string.strip()
                if i == 0:
                    if bool(alph_file):
                        alphabet = one_string_alph(alph_file)
                    else:
                        alphabet = in_string
                else:
                    if in_string == 'text:':
                        ...
                    else:
                        text_string += in_string
                        text_string += "\n"
                i += 1
        return alphabet, text_string


def coding(alpha, text_string):
    if len(alpha) == 0:
        alpha = alhpa_missing(text_string)
    alpha_dict = shuffle(alpha)
    code_text = ''
    for x in range(len(text_string)):
        if text_string[x] in alpha_dict:
            code_text += alpha_dict[text_string[x]]
        else:
            code_text += text_string[x]
    return code_text, alpha_dict


def start_coding(starter):
    if bool(starter):
        alphabet, text_str = input_processing(parser.parse_args().alph, parser.parse_args().file,
                                              parser.parse_args().file_store,)
        dict_path = '-.txt'
        if bool(parser.parse_args().open_dict):
            dict_path = parser.parse_args().open_dict

        final, decode = coding(alphabet, text_str)

        with open('{}'.format(dict_path), "w") as f:
            json.dump(decode, f)

        sys.stdout.write(final)

        # Проверка закодированного текста и словаря
        decode_array = []
        for k, v in decode.items():
            decode_string = "{0} ---> {1}\n".format(k, v)
            decode_array.append(decode_string)

        with open('test.txt', 'w') as writing_file:
            writing_file.write('Закодированный текст\n\n' + final + '\n\n' + "Словарь для расшифровки текста\n\n")
            for x in decode_array:
                writing_file.write(x)
    else:
        print('Не введена команда начала кодирования')
        sys.exit()

start_coding(parser.parse_args().code)
'''def decoding(decoding_array, decoding_dict):
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


input_alphabet, text_str = input_processing(parser.parse_args().alph, parser.parse_args().file,
                                            parser.parse_args().file_store)
alphabet = add_alphabet(input_alphabet)
dict_path = '-.txt'
if bool(parser.parse_args().open_dict):
    dict_path = parser.parse_args().open_dict


if bool(parser.parse_args().code):
    decode_array = []
    final, decode = coding(alphabet, text_str)

    for k, v in decode.items():
        decode_string = "{0} ---> {1}\n".format(k, v)
        decode_array.append(decode_string)

    with open('test.txt', 'w') as writing_file:
        writing_file.write('Закодированный текст\n\n' + final + '\n\n' + "Словарь для расшифровки текста\n\n")
        for x in decode_array:
            writing_file.write(x)

    with open('{}'.format(dict_path), "w") as f:
        json.dump(decode, f)
else:
    print("Не введена команда запуска кодирования")
    sys.exit()

with open('chiper.v2.0_dict.txt', "w") as f:
    json.dump(decode, f)'''

