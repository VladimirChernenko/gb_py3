"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок
под конкретный проект; можно ли будет при этом расширять конфигурацию
и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

from os import mkdir, chdir, path


def main(name_project, *folders_project):
    if not path.exists(name_project):
        mkdir(name_project)
        chdir(name_project)
        for folder in folders_project:
            mkdir(folder)
    else:
        print(f'Folder: {name_project} exists!')


if __name__ == '__main__':
    main('my_project', 'settings', 'mainapp', 'adminapp', 'authapp')
