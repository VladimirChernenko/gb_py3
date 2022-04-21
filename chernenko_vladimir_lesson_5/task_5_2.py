"""
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""

def add_nums(n):
    return (i for i in range(1, n+1, 2))

if __name__ == '__main__':
    add_to_15 = add_nums(15)
    print(next(add_to_15))
    print(next(add_to_15))
    print(next(add_to_15))

    