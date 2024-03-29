"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
 в котором ключи — верхняя граница размера файла (пусть будет кратна 10), 
 а значения — общее количество файлов (в том числе и в подпапках), 
 размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os 

def degree_ten(x):
    y = 1
    while x:
        x //= 10
        y += 1
    return y

def func_main(name=os.getcwd()):
    dict_x = {}
    for path_x, folder, files in os.walk(name):
        for file in files:
            key_x = 10 ** degree_ten(os.stat(os.path.join(path_x, file)).st_size)
            if dict_x.get(key_x):
                dict_x[key_x] += 1
            else:
                dict_x[key_x] = 1
    return dict_x

if __name__ == '__main__':
    print(func_main())