inp_val = str("58903")
tpls_char = set()

for char in inp_val:
    tpls_char.add(char)
tpls_char = sorted(tpls_char)
print("Max value : {}".format(tpls_char[-1]))