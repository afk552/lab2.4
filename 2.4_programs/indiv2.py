#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random

if __name__ == '__main__':
    option = input("Как заполнить список? ""'Вручную' или 'Автоматически': ")
    lst = []
    if option.lower() == "вручную":
        lst = list(map(float, input("Введите числа через пробел : ").split()))
    else:
        amount = int(input("Введите количество чисел: "))
        # Заполнение списка рандомными дробными значениями
        lst = [round(random.uniform(-100.9, 300.9), 2) for i in range(amount)]
    if not lst:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    else:
        print("Введенные значения: ", *lst, "\n")

    A = float(input("Введите левую границу: "))
    B = float(input("Введите правую границу: "))
    if A > B:
        A, B = B, A
        print("A > B, A и B были изменены местами!")
    print(f"Элементы, удовлетворяющие [{A} , {B}] >>",
          list(filter(lambda item: item >= A and item <= B, lst))
          )
    print("Количество элементов, удовлетворяющие условию: ",
          len(list(filter(lambda item: item >= A and item <= B, lst)))
          )

    i_max = lst.index(max(lst))
    # Взяв индекс максимального элемента, делаем срез
    print("Сумма чисел списка, начиная от максимального значения: ",
          sum(lst[i_max:len(lst)])
          )
    print("Отсортированный по убыванию модулей исходный список: ")
    lst.sort(key=abs, reverse=True)
    print(lst)
