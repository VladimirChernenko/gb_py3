"""
3. Создать структуру файлов и папок, как написано в задании 2
 (при помощи скрипта или «руками» в проводнике). 
 Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание,
что html-файлы расположены в родительских папках (они играют роль пространств имён);
предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
например, во фреймворке django.
"""

import os
import shutil

def func_main(name):
   if os.path.isdir(name):
      os.chdir(name)
      if not os.path.isdir('templates'):
         os.mkdir('templates')
      base_dir = os.path.join(os.getcwd(), 'templates')
      for dir in (i for i in os.listdir() if os.path.isdir(i)):
         os.chdir(dir)
         if os.path.isdir('templates'):
            os.chdir('templates')
            for data in os.listdir():
               shutil.move(data, base_dir)
            os.chdir('..')
            shutil.rmtree('templates')
         os.chdir('..')
          

if __name__ == '__main__':
   func_main('my_project')