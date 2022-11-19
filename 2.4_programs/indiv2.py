#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random

if __name__ == '__main__':
    option = str(input(
        "Введите, как заполнить массив: \"Вручную\" или \"Автоматически\"\n"))
    mas = []
    if option.lower() == "вручную":
        mas = list(map(float, input("Введите числа через пробел: ").split()))
    else:
        amount = int(input("Введите количество чисел: "))
        mas = [round(random.uniform(-100.9, 300.9), 2) for i in range(amount)]
    if not mas:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    else:
        print("Введенные значения: ", *mas, "\n")

    A = float(input("Введите левую границу: "))
    B = float(input("Введите правую границу: "))
    print(
        f"Элементы, удовлетворяющие [{A} , {B}] >>",
        list(filter(lambda item: item >= A and item <= B, mas))
    )
    print(
        "Количество элементов, удовлетворяющие условию: ",
        (len(list(filter(lambda item: item >= A and item <= B, mas))))
    )

    i_max = mas.index(max(mas))
    print(
        "Сумма чисел списка, начиная от максимального значения: ",
        sum(mas[i_max:len(mas)])
    )
    print(
        "Отсортированный по убыванию модулей исходный список: ",
        sorted(mas, key=abs, reverse=True)
    )