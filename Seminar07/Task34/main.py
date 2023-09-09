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
    print("Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться \n"
          +"в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. \n"
          +"Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе \n"
          +"стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они \n"
          +"разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает \n"
          +"в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, \n"
          +"если с ритмом все не в порядке")    
    print("************************************************************************************************")
    print(" ")

def rhythm(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])




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
isOpen = True # true задается по умолчанию для хотя бы одного запуска
while (isOpen):
    isOpen = WorkingProcess()

    if isOpen == True:
        # блок кода для исполнения программы
        str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
        print(str_1)
        if rhythm(str_1):
            print('Парам пам-пам')
        else:
            print('Пам парам')
        str_2 = 'пара-ра-рам рам-пам-па па-ра-па-да'
        print(str_2)
        if rhythm(str_2):
            print('Парам пам-пам')
        else:
            print('Пам парам')
        
        print("")
        



input('')
ClearConsole()
