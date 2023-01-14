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

