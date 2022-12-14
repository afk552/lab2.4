#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    option = str(input(
        "Введите, как заполнить список: \"Вручную\" или \"Автоматически\"\n"))
    A = []
    if option.lower() == "вручную":
        print("Введите 10 чисел (Каждое на отдельной строке): ")
        for i in range(10):
            A.append(int(input()))
    else:
        A = [3, 21, 6, 8, 2, 1, 19, 20, 4, 16]
    print("Введенные значения: ", *A, "\n")

    summ = 0
    cnt = 0
    for i, elem in enumerate(A):
        if 2 < A[i] < 20 and A[i] % 8 == 0:
            summ += elem
            cnt += 1
            print(elem, end=" ")
    print("\nСумма элементов, подходящих под условие: ", summ)
    print("Количество элементов, подходящих под условие: ", cnt)
