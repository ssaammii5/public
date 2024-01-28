from logic import *
p,q = vars('p','q')
f = (p|q)
print("She studied hard or she is extremely bright.\n")
print("P: She studied hard\nQ: She is extremely bright\n")
f.print_truth_table()