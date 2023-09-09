'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

import os
import random
from random import randint

def PrintTaskDescription():
    print(" ")
    print("************************************************************************************************")
    print("Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.")  
    print("************************************************************************************************")
    print(" ")

def WorkingProcess():
    choice = None
    while not(choice=='y' or choice == 'n'):
        choice = input("желаете выполнить алгоритм? (y/n)")
        if choice =='y':
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

def RaiseDegree(_maximum):    
    _score = 1
    while _score <= maximum:
        print(_score, end=' ')
        _score = _score * 2




PrintTaskDescription()
isOpen = True
while (isOpen):
    isOpen = WorkingProcess()

    if isOpen == True:        
        maximum = int(input('введите максимальное число, для которого требуется вывести все степени двойки 2^k: '))
        print(" ")
        RaiseDegree(maximum)
        print(" ")

    
input('')
ClearConsole()