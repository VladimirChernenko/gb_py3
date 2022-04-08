"""
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
"""

list_old = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_answer = ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут',
               'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
print(id(list_old), list_old)
def index_save(list_x):
    list_y = list()
    for i, el in enumerate(list_x):
        if el.isalpha():
            continue
        else:
            list_y.append(i)
    return list_y

def add_zero(list_x, list_y):
    for i in list_x:
        if list_y[i].isdigit():
            if len(list_y[i]) == 1:
                list_y[i] = '0' + list_y[i]
        else:
            if len(list_y[i][1:]) == 1:
                list_y[i] = list_y[i][:1] + '0' + list_y[i][1:]
    return list_y

def task_2_2(list_x):
    x = 0
    for i in index_save(list_x):
        list_x.insert(i + x, '"')
        list_x.insert(i + x + 2, '"')
        x += 2
    return list_x

def func_str(list_x):
    str_x = list_x[1]
    for i in list_x[1:]:
        if not i.isalpha() and not str_x[-1].isalpha():
            str_x += i
        else:
            str_x += ' ' + i
    return str_x

print(func_str(task_2_2(add_zero(index_save(list_old), list_old))))
print(id(list_old), list_old)