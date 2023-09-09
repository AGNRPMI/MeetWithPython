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
    print("Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность \n"
          + "и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: \n"
          + "an = a1 + (n-1) * d.             \n"
          + "Каждое число вводится с новой строки.")
    print("************************************************************************************************")
    print(" ")

def Progressia():
    element_first = int(input("Введите значение первого элемента арифметическй прогрессии: "))
    increment = int(input("Введите положительное или отрицательное значение приращения: "))
    element_quantity = int(input("Введите количество элементов арифметической прогрессии: "))
    print(element_first)
    while element_quantity!=1:
        element_first=element_first+increment
        element_quantity-=1
        print(element_first)
    

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
        Progressia()


input('')
ClearConsole()
