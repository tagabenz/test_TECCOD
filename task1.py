"""
Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, 
содержащий только уникальные элементы из исходного списка.
"""

def func(numb: list) -> set:
    
    return list(set(numb))
    
func([1,1,1,3,4,])