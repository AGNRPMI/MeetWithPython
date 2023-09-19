import os
from pathlib import Path
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
    print("Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь \n"
          +"также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления \n"
          +"данных")    
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

    

def PrintListCommand(keys_dict = dict()):
    for keys, value in keys_dict.items():
        print(keys,":", value)

def TransformationCommand(path, phonebook_list=list()):
    hot_keys = {'1' : 'показать список', '2' : 'добавить контакт', '3':'сортировать элементы', 
                '4': 'удалить элементы', '5' : 'Поиск', '6' : 'Изменить',
                '0' : 'выход из меню'}
    
    command = None

    while not (command == hot_keys.keys):
        print("")
        PrintListCommand(hot_keys)
        print("")
        command = input("Введите команду: ")
        if command == '1':
            Show_Contacts(path)
        elif command == '2':
            Create_Contact(path)            
            print("контакт добавлен")
        elif command == '3':
            Sorting_Contacts(path, phonebook_list)
            print("контакты отсортированы")
        elif command == '4':
            Delete_Contact(path, phonebook_list)
        elif command == '5':
            Find_Contact(path)
        elif command == '6':
            Delete_Contact(path, phonebook_list)
            print("меняем данные")
            Create_Contact(path)
            print("контакт изменен")
        elif command == '0':
            print("")
            break
        else:
            print("команда не распознана, введите еще раз")
            print(" ")

def Show_Contacts(path):
    data = open(path, 'r',encoding='utf-8')

    for line in data:
        print(line)
    data.close()

def Create_Contact(path):
    first_name = input('Введите имя контакта:')
    last_name = input('Введите фамилию контакта:')
    phone = input('Введите номер телефона контакта:')
    category = input('Введите группу контакта (оставьте пустое, если не требуется):')

    if category=="": 
        category = "без категории"

    line = (f"{first_name};{last_name};{phone};{category};")
    
    data = open(path,'a',encoding='utf-8')
    data.writelines(f"{line}\n")
    data.close()

def Find_Contact(path):
    
    list_1=Update_List(path)
    
    temp_list = []
    print("")
    print("Поиск:")
    find_value = input("введите значение: ")
    find_value=find_value.lower()

    for list in list_1:
        for item in list:
            if item==find_value:
                temp_list.append(item)
                print(list)
    if len(temp_list)==0: print("данных не найдено")
    print("")

def Delete_Contact(path, phonebook_list=list()):
    data = open(path, 'r',encoding='utf-8')
    number =1

    for line in data:
        print(f"{number} | {line}")
        number+=1
    data.close()
    number=int(input("Введите порядковый номер, который хотите удалить:"))
    phonebook_list.pop(number-1)
    data = open(path,'w',encoding='utf-8')
    for item in phonebook_list:
        result = ";".join(item)+";"
        data.writelines(f"{result}\n")
    data.close()
    
    Update_List(path)



def Sorting_Contacts(path, phonebook_list=list()):
    up_or_down = None
    while not (up_or_down == 'u' or up_or_down == 'd'):
        print("сортировка по возрастанию(u) или по убыванию(d)")
        up_or_down = input("введите (u) или (d)")

        if up_or_down == 'u':
            print("по возрастанию: ")
            phonebook_list.sort()
            
        elif up_or_down == 'd':
            print("по убыванию: ")
            phonebook_list.sort()
            phonebook_list.reverse()
            
        else:
            print("команда не распознана, введите еще раз")
            
    data = open(path,'w',encoding='utf-8')
    for item in phonebook_list:
        result = ";".join(item)+";"
        data.writelines(f"{result}\n")
    data.close()
    
    Update_List(path)

def Update_List(path):
    list_1 = []
    with open(path,'r',encoding='utf-8') as data:
        
        for line in data:
            line = line.lower()
            splited_line = line.split(";")
            try: 
                splited_line.pop(4)
            except:
                None
            list_1.append(splited_line)

    #list_1.remove()
    return list_1

# начало главного метода
ClearConsole()
PrintTaskDescription()
isOpen = True # true задается по умолчанию для хотя бы одного запуска
while (isOpen):
    isOpen = WorkingProcess()

    if isOpen == True:
        # блок кода для исполнения программы
        path = 'Seminar08\Task38\phonebook.txt'
        phonebook_list = Update_List(path)
        print(phonebook_list)

        TransformationCommand(path, phonebook_list)






        
        




ClearConsole()
