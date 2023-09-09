'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
'''

import os
import random
from random import randint

def PrintTaskDescription():
    print(" ")
    print("************************************************************************************************")
    print("Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. ")
    print("Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты ")
    print("вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть")
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
            print("клавиша не распознана, введите еще раз")
            print(" ")
    return _isOpen

def FindNumberCoins(_number, _eagleCoins):    
        if(_eagleCoins==0 ):
            print(f"так случилось, что все монеты уже лежат решкой вверх, ничего переворачивать не нужно")
            print(" ")
        elif(_eagleCoins==_number ):
            print(f"так случилось, что все монеты уже лежат орлом вверх, ничего переворачивать не нужно")
            print(" ")
        elif(_eagleCoins>_number - _eagleCoins):
            print(f"необходимо перевернуть {_number - _eagleCoins} монет решкой вниз")
            print(" ")
        else:
            print(f"необходимо перевернуть {_eagleCoins} монет орлом вниз")
            print(" ")

def ClearConsole():
        os.system('cls')


PrintTaskDescription()
isOpen = True
while (isOpen):
    isOpen = WorkingProcess()

    if isOpen == True:        
        number = int(input('введите N монет, лежащих на столе: '))
        eagleCoins = randint(0, number)
        print(f"Пусть из {number} монет, лежащих на столе, {eagleCoins} из них лежат вверх орлом,") 
        print(f"остальные {number - eagleCoins} - вверх решкой")
        print(" ")
        FindNumberCoins(number, eagleCoins)

    
input('')
ClearConsole()