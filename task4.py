"""
Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
"""

def sort_list(lst):
    srtd_list=sorted(lst)
    rev_srtd_lst=sorted(lst, reverse=True)

    print(srtd_list,rev_srtd_lst)

lst=['12345678','123','12','123456','1']
sort_list(lst=lst)
