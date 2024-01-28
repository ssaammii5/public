from logic import *
p,q = vars('p','q')
f = (p&~q)|(~p&q)
print("Take either 2 Advil or 3 Tylenol\n")
print("P: Take 2 Advil\nQ: Take 3 Tylenol\n")
f.print_truth_table()