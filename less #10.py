"""a = 45
b = 50
c = 45

a_i = int(input("a: "))
b_i = int(input("b : "))
c_i = int(input("c : "))

print("Input data {}, {}, {}".format(a_i, b_i, c_i))

if a != a_i or b != b_i or c != c_i:
    print("Такого треугольника нет!")
else:
    print("Такой треугольник есть!")
"""

age = int(input("Input you age:"))

if age <= 4:
    print(" Мне {} год!".format(age))
elif age >= 5 and age <= 20:
    print("Мне {} лет !".format(age))
elif age > 20 and age < 100:
    print("Мне {} года!".format(age))
else:
    print("По условию - столько не живут! (Или не корректно число, или это не число, проверку ж не просили делать))))")