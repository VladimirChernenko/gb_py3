"""
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами,
 его можно создать в любом текстовом редакторе «руками» (не программно);
 предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

from yaml import load
from yaml.loader import BaseLoader
import os

def func_dict(d):
    for k, i in d.items():
        if not os.path.isdir(k):
            os.mkdir(k)
            os.chdir(k)
            func_type(i)
            os.chdir('..')
        else:
            print(f'Folder named {k} exists\nProject not created')
            

def func_list(l):
    for i in l:
        func_type(i)

def func_str(s):
    with open(s, 'w', encoding='utf-8') as f:
        pass

def func_type(t):
    if type(t) == str:
        func_str(t)
    elif type(t) == list:
        func_list(t)
    elif type(t) == dict:
        func_dict(t)

def func_main(file_x):
    with open(file_x) as f:
        try:
            file = load(f, Loader=BaseLoader)
            func_type(file)
        except:
            print(f'Проблемы с файлом: {file_x}')

if __name__ == '__main__':
    func_main('config.yaml')