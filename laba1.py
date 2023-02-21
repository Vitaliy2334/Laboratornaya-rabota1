import random
import math
import datetime


def task1():
    print("TASK #1\n")

    num = input("Введите вещественное число: ")

    if float(num) < 0:
        print("Отрицательное число")
    else:
        left, right = num.replace(',', '.').split('.')
        print(f"{left} руб. {right} коп.")


def task2(arr: list):
    print("\nTASK #2")

    print("Массив: ", arr)
    print(True) if [x for x in range(len(arr) - 1) if arr[x] <= arr[x + 1]] else print(False)


def task3():
    print('\nTASK #3')
    card = input("Введите номер карты: ").replace(' ', '')
    print(card[:4] + ' ' + '*' * 4 + ' ' + '*' * 4 + ' ' + card[12:len(card)]) if len(card) == 16 else print(
        "Неверный формат карты!")


def task4():
    print('\nTASK #4')
    words = input("Введите текст: ").replace('.', ' ').replace(',', ' ').split(' ')
    print("Слова длинной более 7 символов: ", [x for x in words if len(x) > 7])
    print("Слова длинной от 4 до 7 символов: ", [x for x in words if 4 <= len(x) <= 7])
    print("Слова длинной менее 4 символов: ", [x for x in words if len(x) < 4])


def task5():
    print('\nTASK #5')
    words = input('Введите ваш текст: ').replace(',', ' ').replace('.', ' ').split(' ')
    print(' '.join(word.upper() if word[0] == word[0].title() else word for word in words))


def task6():
    print("\nTASK #6")
    text = input("Введите текст: ")
    print("Символы, которые встречаются в тексте всего по 1 разу: ", ', '.join([x for x in text if text.count(x) == 1]))


def task7():
    print('\nTASK #7')
    sites = ['www.google.com', 'vk.com', 'www.ya.ru', 'donnu.ru']
    res = [y + '.com' if not y.endswith('.com') else y for y in ['http://' + x if ('www.' in x) else 'http://www.' + x for x in sites]]
    print(res)


def task8():
    print('\nTASK #8')
    max_size = 50
    arr = [random.randint(1, max_size) for _ in range(0, random.randint(1, max_size))]
    length = 2 ** math.ceil(math.log2(len(arr)))
    print(f"Размер массива до изменения: {len(arr)}")
    print("Массив до изменения: ", arr)
    [arr.append(0) for _ in range(len(arr), length)]
    print(f"Размер массива после: {len(arr)}")
    print("Массив после изменения: ", arr)


def task9():
    print('\nTASK #9')
    bank = {1000: 20, 500: 10, 100: 10, 50: 10}
    bank_summ = sum(x * y for x, y in bank.items())
    print("Всего денег в банкомате: ", bank_summ)
    request = int(input("Введите сумму, которую хотите снять: "))
    if request > bank_summ:
        print("Вы ввели сумму большую, чем есть в банкомате!")
    elif request % 50 != 0:
        print("Введите сумму, кратное 50!")
    else:
        for nominal in bank.keys():
            _val = int(request / nominal) // 1 if int(request / nominal) // 1 <= bank[nominal] else bank[nominal]
            request -= _val * nominal
            bank[nominal] = _val
        print(str(bank).replace(': ', '*').replace(', ', ' + '))


def task10():
    print("\nTASK #10")

    password = 'T3st_Passw0rd'
    lst = []
    print('Пароль: ', password)
    if len(password) < 8:
        lst.append("Пароль слишком короткий!")
    elif password.isdigit():
        lst.append("Пароль не может состоять только из цифр!")
    elif password.lower() == password:
        lst.append("Пароль не может содержать только нижний регистр букв!")
    elif True if [x for x in password if x.isdigit()] and len(password) > 8 else False:
        print("Пароль хороший!")


def frange(start, end, step):
    while start <= (end - step):
        yield float('{:.1f}'.format(start + step))
        start += step


def task11():
    print('\nTASK #11')
    for x in frange(1, 5, 0.1):
        print(x)


def get_frames(signal, size=1024, overlap=0.5):
    length = int(size * overlap)
    step = 0

    while step < len(signal) - 1:
        yield signal[step: step + size]
        step += length


def task12():
    print('\nTASK #12')
    length = int(input('Введите длину сигнала: '))
    signal = [x for x in range(length)]
    for frame in get_frames(signal, 4, 0.5):
        print(frame)


def extra_enumerate(x):
    tmp = 0
    for y in x:
        tmp += y
        yield y, tmp, tmp / sum(x)


def task13():
    print("\nTASK #13")
    x = [1, 2, 3, 4]
    for elem, summ, frac in extra_enumerate(x):
        print(elem, summ, frac)


def non_empty(func):
    def wrap():
        ret = func()
        removed = 0

        for x in ret:
            if x is None or x == '':
                ret.pop(removed)
            removed += 1
        return ret

    return wrap


@non_empty
def getList():
    return ['1', '', '2', 3, '', 4]


def task14():
    print('\nTASK #14')
    print(getList())


def pre_proccess(a=0.97):
    def decorator(func):
        def wrap(*args):
            s = args[0]
            for x in range(len(s)):
                s[x] = s[x] - a * s[x - 1]
                # print(f'a = {a}')
                func(s)

        return wrap

    return decorator


@pre_proccess(a=0.95)
def plot_signal(s):
    for sample in s:
        print(sample)


def task15():
    print('\nTASK #15')
    signal = [1, 1, 2, 3, 4, 5, 8, 10, 15, 20, 25, 31]
    plot_signal(signal)


def task16():
    print('\nTASK #16')

    teams = ['Ливерпуль', 'Динамо-Киев', 'Динамо-Питер', 'ПСЖ',
             'Реал-Мадрид', 'Барселона', 'Арсенал', 'Балтика',
             'Ювентус', 'Челси', 'Милан', 'Бавария',
             'Боруссия', 'Шахтер', 'Манчестер Сити', 'Зенит']
    playDate = datetime.datetime(2022, 9, 14, 22, 45)

    random.shuffle(teams)
    groups = [teams[x * 4: x * 4 + 4] for x in range(4)]
    [print('Группа #', x + 1, ': ', groups[x]) for x in range(len(groups))]

    for x in range(len(teams)):
        print('Игра #', x, ': ', playDate.strftime("%d/%m/%Y %H:%M"))
        playDate += datetime.timedelta(days=14)


def main():
    task1()

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 4, 3, 2, 1]
    task2(arr1)
    task2(arr2)

    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
    task11()
    task12()
    task13()
    task14()
    task15()
    task16()


if __name__ == '__main__':
    main()
