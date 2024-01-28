from logic import *
p,q = vars('p','q')
f = (p>>q)&(q>>p)
print("It is raining outside if and only if it is a cloudy day.\n")
print("P: It is raining outside\nQ: It is a cloudy day.\n")
f.print_truth_table()