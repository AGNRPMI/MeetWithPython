import os
import random
from random import randint
import time
import math
import sys
from itertools import combinations
from random import sample


def PrintTaskDescription():
    print(" ")
    print("************************************************************************************************")
    print("Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём \n"
          + "кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на\n"
          + "грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло\n "
          + "различное число ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система\n "
          + "автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.\n"
          + "Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого \n"
          + "куста и с двух соседних с ним.\n"
          + "Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход \n"
          + "собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.\n")
    print("************************************************************************************************")
    print(" ")


def WorkingProcess():
    choice = None
    while not (choice == 'y' or choice == 'n'):
        choice = input("желаете выполнить алгоритм? (y/n)")
        if choice == 'y':
            print("выполняется программа...")
            print(" ")
            _isOpen = True
        elif choice == 'n':
            print("завершение программы... Нажмите Enter")
            print(" ")
            _isOpen = False
        else:
            print("команда не распознана, введите еще раз")
            print(" ")
    return _isOpen


def ClearConsole():
    os.system('cls')


# начало главного метода
ClearConsole()
PrintTaskDescription()
isOpen = True  # true задается по умолчанию для хотя бы одного запуска
while (isOpen):
    isOpen = WorkingProcess()

    if isOpen == True:
        # блок кода для исполнения программы
        number = int(input('Введите кол-во кустов: '))
        list_1 = list(randint(1, 5) for i in range(number))
        maximum = sum((list_1))
        iteration = 0
        collecting = 0
        print(
            f"сгенерировались кусты черники, на {number} кустах черники содержится {maximum} ягод")
        
        while (maximum != 0):
            print(f"осталось собрать {maximum} ягод")
            print(list_1)
            a = int(input('Введите № куста, с куста которого осущестляется сбор: '))
            res = 0
            if a == 1:
                res = list_1[0] + list_1[1] + list_1[-1]
                list_1[0] = 0
                list_1[1] = 0
                list_1[-1] = 0

            elif a == len(list_1):
                res = list_1[-2] + list_1[-1] + list_1[0]
                list_1[-2] = 0
                list_1[-1] = 0
                list_1[0] = 0
            else:
                res = list_1[a-1] + list_1[a-2] + list_1[a]
                list_1[a-1] = 0
                list_1[a-2] = 0
                list_1[a] = 0
            maximum = maximum-res
            collecting = collecting+res
            iteration += 1
            print(f"собрано с куста и двух смежных {res} ягод")
            print("")

        print(f"{collecting} ягод собраны с {number} кустов за {iteration} заходов")
        print("")


input('')
ClearConsole()
