# Предложить улучшения кода для уже решённых задач (4 задачи из любых семинаров, кроме первого):
# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# В ответе должны присутствовать старые и новые варианты решений.

# Задача 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# старый вариант решений
num = str(input("Введите число: "))
sum = 0
for i in num:
    if i.isdigit():
        sum = sum + int(i)
print("Сумма цифр числа равна: ", sum)

# новый вариант решений
a = float(input('Введите число: '))
new_sum = sum(map(int, str(a).replace('.', '')))
print(new_sum)

# Задача 2. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# старый вариант решений
lst = [2, 3, 5, 9, 3]
def summa(lst):
    sum = 0
    for i in range(1, len(lst), 2):
        sum = sum + lst[i]
    print(sum)
summa(lst)    

# новый вариант решений
a = [2, 9, 5, 9, 3]
sum_odd = sum2, 3, 5, 9, 3(a[item] for item in range(1, len(a), 2))
odd_el = str([a[item] for item in range(1, len(a), 2)]).strip('[]')
print(sum_odd)

# Задача 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# старый вариант решений
l = [1, 1, 1, 5, 55, 7, 3, 99, 9, 9]
new_l = []
count = 0
for i in l:
    if i not in new_l:new_l.append(i)
print(new_l)

# новый вариант решений
l = [1, 2, 3, 4, 4, 3, 8, 9, 1]
result_list = list(filter(lambda a: l.count(a) == 1, l))
print(result_list)

# Задача 4. Задайте список из n чисел последовательности (1+1/n)^n и 
# выведите на экран их сумму, округлённую до трёх знаков после точки.
# Для n = 6 -> 14.072

# старый вариант решений
n = int(input('Введите число: '))
sum = 0
a = []
b = 1
for i in range(1, n+1):
    b = (1+(1/i))**i
    a.append(round(b, 3))
    sum = sum + b
print(a)
print(round(sum, 3))

# новый вариант решений
n = int(input('Введите число: '))
s = 0
lst = [(1+1/i)**i for i in range(1,n+1)]
print(round(sum(lst),2))