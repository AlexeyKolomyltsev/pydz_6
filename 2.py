#Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from decimal import Decimal

def subtr_max_min(array):
    new_arr = [float(Decimal(str(value)) - int(value)) for value in array]                                                                        
    min = new_arr[0]
    max = new_arr[0]
    for i in new_arr:
        if i < min: min = i
        if i > max: max = i
    return max - min

arr = [1.1, 1.2, 3.1, 10.01]
print(subtr_max_min(arr))