"""list = []
summ_plus = 0
for i in range(-15,15,1):
    list.append(i)

for j in list:
    if j % 2 == 0:
        if j > 0:
            summ_plus += j
print(summ_plus)"""

"""list_num = []
for i in range(1, 180, 1):
    list_num.append(i)
sum_sr_arifm = sum(list_num)/len(list_num)
for j in list_num:
    if j < sum_sr_arifm:
        print("{} - нам подходит! Оно меньше! ".format(j))
"""

"""list_n = [1, 4, 2, 1, 4, 5, 67, 554]
min_val = min((list_n))
counter = list_n.count(min_val)
print("Минимальное значение в списке : {} ,в количестве {} штук!".format(min_val, counter))
"""

"""list_n = [1, 4, 2, 1, 4, 35, 67, 554]
for i in list_n:
    print(i)
    if i > 3 and i < 34:
        list_n.remove(i)
        list_n.append(0)
print(list_n)"""

"""matrix1 = [[6,5,3],[0,1,4],[5,8,2]]
diag = []
iter = 0
for m in matrix1:
    num_diag = matrix1[iter][iter]
    iter+=1
    diag.append(num_diag)
print(diag)
print("Max value diag : {}".format(max(diag)))"""


"""matrix1 = [[-6,5,3],[-3,1,4],[-5,8,-8]]
diag = []
pod_diG = []
iter = 0

for m in matrix1:
    print(m)
    num_diag = matrix1[iter][iter]
    try:
        pod = matrix1[iter][:iter]
        for j in pod:
            if j <0:
                pod_diG.append(j)
    except IndexError:
        continue
    finally:
        iter += 1
    diag.append(num_diag)

print("Max value diag : {}".format(max(diag)))
print("Отрицательные числа под главной диагональю : {} , Количество : {}".format(pod_diG, len((pod_diG))))"""

