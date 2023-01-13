"""comp_1 = {"google", "yandex", "1qa", "mail.ru"}
comp_2 = {"qiwi", "yandex", "google", "paypal"}
print(comp_1&comp_2)"""

"""stroka = "В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее. Словом считается последовательность непробельных символов, идущих подряд. Слова разделены одним или большим числом пробелов или символами конца строки."
dict_counter = dict()
splited_text = stroka.replace(".", "").replace(",","").split(" ")
for i in splited_text:
    if dict_counter.get(i) == None:
        dict_counter[i] = 1
    else:
        dict_counter[i] = dict_counter.get(i) + 1
list1 = []
for key,val in dict_counter.items():
    res_values = val,key
    list1.append((val,key))
list1.sort()
print("Max count in text : {} - {} разА".format(max(list1)[1],max(list1)[0]))"""

