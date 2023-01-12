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

from datetime import date
td = date.today()

day = int(input("Введите день: "))
mon = int(input("Введите месяц: "))
year = int(input("Введите год: "))

age = td.year - year - ((td.month, td.day) < (mon, day))

print("Вам : {}".format(age))