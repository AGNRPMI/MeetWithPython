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
    print("Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая \n"
          +"принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы \n"
          +"num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. \n"
          +"Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией \n"
          +"называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.")    
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

def print_operation_table(operation, num_rows=6, num_columns=6):
    res = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in res:
        print(*[f"{x}" for x in i])


    


# начало главного метода
ClearConsole()
PrintTaskDescription()
isOpen = True # true задается по умолчанию для хотя бы одного запуска
while (isOpen):
    isOpen = WorkingProcess()

    if isOpen == True:
        # блок кода для исполнения программы
        print_operation_table(lambda x, y: x * y)
        print("")
        



input('')
ClearConsole()
