from logic import *
p,q,r = vars('p','q','r')
f = ((p|q)&~p)>>q
f.print_truth_table()
