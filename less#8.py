word = "гиппопотомомонстросесквиппедалиофобия"
word_ne_chetn = word[0::2]
word_chetn = word[1::1]
revers_word = word[-1:-(len(word))-1:-1]
word_six = word[5::1]
word_nosix = word[:5:1]
revers_minus_odin = word[-2:-(len(word))+2:-1]

res_line = """
            - Весь лист: {};
            - нечётные по порядку элементы : {};
            - чётные по порядку элементы: {};
            - все элементы в обратном порядке: {};
            - все элементы, начиная с шестого: {};
            - все элементы, не доходя до шестого: {};
            - все элементы от предпоследнего до третьего в обратном порядке: {}.            
           """.format(word, word_ne_chetn, word_chetn, revers_word, word_six, word_nosix, revers_minus_odin)
print(res_line)