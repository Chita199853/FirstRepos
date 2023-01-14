"""with open("book.txt","r",encoding="utf-8") as f:
    total_ball = []
    for line in f:
        slited_line = line.replace("\n", "").split(":")
        if int(slited_line[-1]) < 3:
            print("Двоечник ! : {}".format(line))
        total_ball.append(int(slited_line[-1]))
    print("Ball po clasu : {}".format(sum(total_ball)/len(total_ball)))
"""

"""with open("file.txt","w") as f:
    while True:
        inpit_data = input("ведите строку (что бы закончить ввод - нажимте Enter): ")
        f.write(inpit_data + "\n")
        if inpit_data == "":
            break"""

"""count_word_in_line  = []
count_simv_in_text = []
line_iter = 1
with open("news.txt","r",encoding="utf-8") as f:
    word_in_line = []
    simv_in_line = []
    for line in f:
        splited_line = line.replace(","," , ").replace(".", " . ").replace("  ", " ").replace("\n", " ").split(" ")
        for word in splited_line:
            if word.isalpha() or word.find("-") != -1 and word != '':
                word_in_line.append(word)
            else:
                simv_in_line.append(word)

        print("В строке {} = Слов : {} / Символов : {} ".format(line_iter, len(word_in_line), len(simv_in_line)))
        line_iter +=1
        word_in_line.clear()
        simv_in_line.clear()
    print("Строк в файле : {}".format(line_iter-1))"""


"""

import math

print(1 ** 100)
print(2 ** 16)
print(2 - 1000)
print(2 + 2 * 2)
print(60 / 3)
print(math.sqrt(144))
print(2 + (5 * 14))
print(66 -11)
print(math.sqrt(16 - 8))"""

""" Сгенерировать n множеств.
 Вывести элементы кратные трём и не входящие в
  первое множество."""

"""mn_1= set([i for i in range(1,55,6)])
mn_2= set([i for i in range(1,55,1)])
for j in mn_2-mn_1:
    if j % 3 == 0:
        print("Kratno 3 : {}".format(j))"""

