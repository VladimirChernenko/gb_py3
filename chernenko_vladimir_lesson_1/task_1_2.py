"""
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
 сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!
"""

list_1 = [i**3 for i in range(1, 1000, 2)]
list_2 = [i+17 for i in list_1]

def check(x):
    answer = 0
    while x:
        answer += (x % 10)
        x //= 10
    if not answer % 7:
        return True


def task_1_2(list_x):
    answer = 0
    for i in list_x:
        if check(i):
            answer += i
    return answer

def check_1(x):
    return sum(map(int, list(str(x)))) % 7 == 0

def task_1_2_1(list_x):
    return sum(filter(check_1, list_x))




if __name__ == '__main__':
    print(f'Ответ1: {task_1_2(list_1)} {task_1_2_1(list_1)==task_1_2(list_1)}\nОтвет2: {task_1_2(list_2)} '
          f'{task_1_2_1(list_2)==task_1_2(list_2)}')
