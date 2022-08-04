"""
5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки
 в виде словаря, в котором ключи те же, а значения — кортежи вида 
 (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке,
где запустили скрипт.
"""
import os
import json
from re import search

def degree_ten(x):
    y = 1
    while x:
        x //= 10
        y += 1
    return y

def file_json(x, n):
    with open(f'{os.path.basename(n)}_summary.json', 'w') as f:
        json.dump(x, f)

def func_main(name=os.getcwd()):
    dict_x = {}
    for path_x, folder, files in os.walk(name):
        for file in files:
            format_f = search(r'\.(.+)', file).group(1)
            key_x = 10 ** degree_ten(os.stat(os.path.join(path_x, file)).st_size)
            if dict_x.get(key_x):
                dict_x[key_x][0] += 1
                if format_f not in dict_x[key_x][1]:
                    dict_x[key_x][1].append(format_f)
            else:
                dict_x[key_x] = [1, [format_f]]
    file_json({el: tuple(i) for el, i in dict_x.items()}, name)


if __name__ == '__main__':
    func_main()