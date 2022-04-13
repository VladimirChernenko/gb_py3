"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

from random import randint


def get_jokes(n, stop_x=None):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    x = len(nouns) - 1
    if stop_x:
        if n > len(nouns):
            n = len(nouns)
        for i in range(n):
            if x:
                print(f'{nouns.pop(randint(0, x))} {adverbs.pop(randint(0, x))} '
                      f'{adjectives.pop(randint(0, x))}, ', end='')
            else:
                print(f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}, ', end='')
            x -= 1
    else:
        for i in range(n):
            print(f'{nouns[randint(0, x)]} {adverbs[randint(0, x)]} '
                f'{adjectives[randint(0, x)]}, ', end='')


if __name__ == '__main__':
    get_jokes(randint(1, 40), randint(0, 1))