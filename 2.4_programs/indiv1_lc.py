#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    option = str(input(
        "Введите, как заполнить список: \"Вручную\" или \"Автоматически\"\n"))
    A = []
    if option.lower() == "вручную":
        A = list(map(int, input("Введите 10 чисел через пробел: ").split()))
    else:
        A = [3, 21, 6, 8, 2, 1, 19, 20, 4, 16]
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    else:
        print("Введенные значения: ", *A, "\n")

    cnt = 0
    summ = 0
    A = [x for x in A if x > 2 if x < 20 if x % 8 == 0]
    print("Элементы, подходящие под условие: ", *A)
    print("Сумма элементов, подходящие под условие: ", sum(A))
    print("Количество элементов, подходящие под условие: ", len(A))
