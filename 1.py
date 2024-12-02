import random

def IsPower5(k):
    while True:
        if k == 5:
            return True
        elif k % 5 != 0:
            return False
        k /= 5

def main():
    lst = []


    try:
        lst = list(map(int, input("Введите 10 целых положительных чисел через пробел: ").strip().split(' ')))

        if all(lst) <= 0 or len(lst) != 10:
            print('Ошибка ввода!')       
        else:
            counter = 0

            for el in lst:
                if IsPower5(el) == True:
                    counter += 1

            print("Набор целых чисел: ", end = '')
            for el in lst:
                print (el, end=' ')
            print("\nКоличество степеней числа 5:", counter)

    except ValueError:
        print('Ошибка ввода!')

#main
main()


