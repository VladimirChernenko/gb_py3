"""
3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное ДЗ.
"""

def task_1_3(x: int):
    str_x = 'ов'
    if 10 < x < 15:
        pass
    elif x % 10 == 1:
        str_x = ''
    elif 1 < x % 10 < 5:
        str_x = 'а'
    return str_x

if __name__ == "__main__":
    for i in range(21):
        print(f'{i} процент{task_1_3(i)}')
