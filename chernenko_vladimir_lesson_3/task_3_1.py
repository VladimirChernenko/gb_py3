"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
>>> >>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
"""

# from googletrans import Translator
# def task_3_1(x: str):
#     tr = Translator()
#    return tr.translate(x, src='en', dest='ru')
# AttributeError: 'NoneType' object has no attribute 'group'
# так и не разобрался из-за чего ошибка.


def num_translate(str_x: str):
    dict_x = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять' }
    return dict_x[str_x.lower()]

if __name__ == '__main__':
    print(num_translate('eIght'))
