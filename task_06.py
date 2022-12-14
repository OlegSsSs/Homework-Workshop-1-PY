# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет 
# счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

n = int(input('Введите возможно свой счастливый билет: '))
x = (n // 100000) % 10
y = (n // 10000) % 10
z = (n // 1000) % 10
a = (n // 100) % 10
b = (n // 10) % 10
c = n % 10
if (x + y + z) == (a + b + c):
    print(n, '-> yes')
else:
    print(n, '-> no')
