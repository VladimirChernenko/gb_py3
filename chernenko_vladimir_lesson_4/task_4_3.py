"""
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""

from datetime import date
from time import strptime
from task_4_2 import currency_rates, file

def task_4_3():
    print(date(*strptime(' '.join(file.headers['Date'].split()[1: 4]),'%d %b %Y')[:3]))
    currency_rates(file, 'gbp')



if __name__ =='__main__':
    task_4_3()