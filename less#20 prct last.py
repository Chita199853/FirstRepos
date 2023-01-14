text = """Человек, не перегоревший в аду собственных страстей, не может их победить.
И они прячутся рядом, в соседнем доме, чего он даже не предполагает.
А пламя в любой момент может перекинуться и сжечь дом, который он считает своим.
То, от чего мы уходим, уклоняемся, якобы забывая, находится в опасной близости от нас.
И в конечном счете оно вернется, но с удвоенной силой.
       """.replace("\r","")
print(len(text))
splited_text = text.replace(",","").replace(".", "").strip().split("\n")
word_list = []
word_dickt = dict()
word_for_sort = []
for line_text in splited_text:
    print(line_text)
    split_for_word = line_text.split(" ")
    for word in split_for_word:
        word_list.append(word)


for list_str in word_list:
    check_in_dikt = word_dickt.get(list_str)
    if check_in_dikt == None:
        word_dickt[list_str] = 1
    else:
        word_dickt[list_str] = 1 + check_in_dikt
for key,val in word_dickt.items():
    res = val,key
    print(res)
    word_for_sort.append(res)
word_for_sort.sort()
print(word_for_sort[-1])
print("Встречается чаще всего встречается слово - {}".format(word_for_sort[-1]))