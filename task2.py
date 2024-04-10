"""
Написать функцию, которая принимает на вход два целых числа (минимум и максимум) 
и возвращает список всех простых чисел в заданном диапазоне.
"""

def func (min: int, max: int) -> list:
    res=list()

    for i in range(min,max+1): 
        for j in range(2, i): 
            if i%j == 0:
                break
        else:res.append(i)

    print(res)

func(5,19)