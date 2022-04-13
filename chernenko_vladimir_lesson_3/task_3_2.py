"""
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
 реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
>>> >>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
"""
from task_3_1 import num_translate

def task_3_2(str_x: str):
    if str_x.istitle():
        return num_translate_adv(str_x)
    return num_translate(str_x)

def num_translate_adv(str_x: str):
    dict_x = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять' }
    return dict_x[str_x.lower()].capitalize()

if __name__ == '__main__':
    print(task_3_2('Eight'))
    print(task_3_2('three'))

