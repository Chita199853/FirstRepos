import delenie,summ,umn

print(delenie.delen(10, 2))
print(summ.summer(5,5))
print(umn.umn(5, 5))
print()
from module.mathem.umn import umn
from module.mathem.delenie import delen
from module.mathem.summ import summ
print(umn(4,2))
print(summ(15,15))
print(delen(40,5))

from module.str_worker.str_len_count import counter

text = "Vasy yoje hochet !"
print("Simvolov v texte : {}".format(counter(text)))