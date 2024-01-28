from logic import *
p,q = vars('p','q')
f = (p>>q)
print("If you get a 100 on the final exam, then you earn an A in the class.\n")
print("P: you get a 100 on the final exam\nQ: you earn an A in the class\n")
f.print_truth_table()