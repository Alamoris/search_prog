import secrets
import sys
result_array = []
divider_dict = {}


def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def run():
    """Run the print dividers transformation program"""
    foobar_array = [secrets.randbelow(1000) for x in range(50)]

    if len(divider_dict) <= 1:
        return "Вы ввели меньше одного делителя, введите делители заново"

    for x in foobar_array:
        temp = ''
        i = 0
        for k, v in divider_dict.items():
            if x % k == 0:
                temp = temp + '{0}'.format(v)
                i = i + 1
        if i >= 2:
            temp = temp + '!'
        if temp == '':
            result_array.append(x)
        else:
            result_array.append(temp)
    print(foobar_array, "\n", result_array)
    refresh()


def end():
    """Exit program"""
    sys.exit()


def refresh():
    divider_dict.clear()
    result_array.clear()


def add():
    """Add dividers"""
    refresh()
    print('Вводите число - делитель через пробел, для завершения воода делителей, введите пустую строку')

    while True:
        string_divider = input().strip()

        if string_divider == '':
            print("Список делителей:")
            print(divider_dict)
            break

        pre_divider_array = string_divider.split()
        firs_divider = pre_divider_array[0]

        if isint(firs_divider):
            divider_dict[int(firs_divider)] = string_divider[len(firs_divider)+1:]

        '''for x in range(0, len(pre_divider_array), 2):
            if int(pre_divider_array[x]) <= 1:  # Прописать try exept обработчик для < 1 поскольку получается ошибка
                sys.stderr.write("Веден отрецательный делитель или делитель равный еденице, он не будет учитываться\n")
            else:
                divider_dict[int(pre_divider_array[x])] = pre_divider_array[x + 1]'''


def go():
    print(divider_dict)


while True:
    print('Для добавления делителей напишите add а затем вводите делители через пробел')
    print('Для запуска программы введите run, а для выхода из программы введите exit')
    command = input().strip()
    if command == 'add':
        add()
    elif command == 'run':
        print(run())
    elif command == 'exit':
        end()
    elif command == 'go':
        go()
    else:
        print('Непонятная команда попробуйте еще раз')

