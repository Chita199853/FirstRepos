"""print("Приветствуем вас в нашем калькуляторе! Выберите что вам нужно сделать ! : ")
try:
    change_ual = int(input("1)+ \n 2)-\n 3)/ \n 4)*\n"))
    a = int(input("Число 1 : \n"))
    b = int(input("Число 2 : \n"))
    if change_ual == 1:
        print("Sum:{}".format(a+b))
    elif change_ual == 2:
        print("Minus_res: {}".format(a-b))
    elif change_ual == 3:
        print("Del: {}".format(a/b))
    elif change_ual == 4:
        print("Umn_res: {}".format(a * b))
    else:
        print("Не верно выбрано условие! ")
except ZeroDivisionError:
    print("Делить на 0 нельзя! ")
except TypeError:
    print("Мы работаем только с числами :)")
except ValueError:
    print("Не верно выбрано условие, или не корректно указано значение переменных! ")"""


"""
from datetime import date
td = date.today()

day = int(input("Введите день: "))
mon = int(input("Введите месяц: "))
year = int(input("Введите год: "))

age = td.year - year - ((td.month, td.day) < (mon, day))

print("Вам : {}".format(age))"""
"""
age_1 = [2, 10 ,1998]
age_2 = [2, 10 ,1998]
sum_age_1 = sum(age_1)
sum_age_2 = sum(age_2)

if sum_age_1 < sum_age_2:
    print("Age_1 старше Age_2 ! ")
elif sum_age_1 == sum_age_2:
    print("Ровестники! ")
else:
    print("Age_2 Старше Age_1 !")"""


"""number = str(323)
number_res_sum = 0
number_res_proizv = 1

for num in number:
    number_res_sum += int(num)
    number_res_proizv *= int(num)
print("Сумма : {} ; Произведение : {}".format(number_res_sum, number_res_proizv))"""

"""min = int(input("Enter Min value:  "))
max = int(input("Enter Max value: "))
step = int(input("Enter step values: "))
list_number = []

if min >0 and max > 0 and step > 0:
    for i in range(min, max, step):
        list_number.append(i)
    print(list_number)
else:
    print("Введены не корекктные данные! ")"""


