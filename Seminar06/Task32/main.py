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
    print("Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному \n"
          + "диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)")
    print("************************************************************************************************")
    print(" ")

def GenerateList():
    print("генерируем список")
    min_value = int(input("Введи минимальное число: "))
    max_value = int(input("Введи максимальное число: "))
    row = int(input("Введи количество чисел в диапазоне: "))
    list = sample(range(min_value, max_value), row)
    return list

def FindIndex(list_1):
    print("найдем индексы значений в диапазоне: ")
    min_value=int(input("Введи минимальное значение диапазона: "))
    max_value=int(input("Введи максимальное значение диапазона: "))
    list_index=list()
    i=0
    if min_value>max_value:
        temp=max_value
        max_value=min_value
        min_value=temp
    for value in list_1:
        if (value>=min_value and value<=max_value):
            list_index.append(i)
        i+=1

    print("индексы значений в заданном диапазоне: ")
    print(list_index)

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
        
        list_1 = GenerateList()
        print(list_1)
        FindIndex(list_1)

        print("")


input('')
ClearConsole()
