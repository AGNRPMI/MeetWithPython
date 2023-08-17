'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S 
и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''

import os
import random
from random import randint

def PrintTaskDescription():
    print(" ")
    print("************************************************************************************************")
    print("Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.")
    print("Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),")
    print("а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S")
    print("и их произведение P. Помогите Кате отгадать задуманные Петей числа.")
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
            print("завершение программы...")
            print(" ")
            _isOpen = False                
        else: 
            print("команда не распознана, введите еще раз")
            print(" ")
    return _isOpen

def ClearConsole():
        os.system('cls')

def FindNumbers(_numberX, _numberY):    
        _numTry = 3
        _isResolved = False
        _sum = _numberX + _numberY
        while _numTry > 0:
             _num = int(input("Угадай одно из чисел: "))
             if (_num == _numberX) or (_num== _numberY):
                  print(f"верно! загаданное число это {_num}, а второе число это, соответственно {_sum - _num}")
                  _isResolved = True
                  return _isResolved
                  break
             else:
                  _numTry -= 1
                  print(f"неверно, попробуй еще раз. Осталось попыток {_numTry}")
        return _isResolved




PrintTaskDescription()
isOpen = True
while (isOpen):
    isOpen = WorkingProcess()

    if isOpen == True:        
        numberX = randint(1, 1001)
        numberY = randint(1, 1001)
        sumXY = numberX + numberY
        multiplyXY = numberX * numberY

        print(f"Петя загадал два числа X и Y, сумма которых равна {sumXY}, а произведение равно {multiplyXY}") 
        print(f"попробуйте угадать числа раньше Маши! У вас 3 попытки")
        print(" ")
        isResolved = FindNumbers(numberX, numberY)
        if isResolved == False:
             print("вы исчерпали попытки. Маша представила решение. Она выразила одно уравнение из другого,")
             print("получив квадратичное уравнение. Затем она вычислила дискриминант и соответвующие два")
             print(f"корня. Первое число это {numberX}, второе это {numberY}")
    
input('')
ClearConsole()