"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...

"""



def add_nums(n):
    for i in range(1, n+1, 2):
        yield i

if __name__ == '__main__':
    add_to_15 = add_nums(15)
    for i in range(8):
        print(next(add_to_15))