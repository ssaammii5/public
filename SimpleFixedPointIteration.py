## Simple Fixed Point Iteration

def f(x):
    return 0.5 * x**2 + (1/4)

def fixed_point(f,x0, M, es,e):
    eAPp = 0.0
    print("Iteration\txi\t\tEa\t\t|f(xi)|\t\t|g(xi)|")
    print("0\t\t\t",x0, "\t\t0.0\t\t",abs(f(x0)), "\t\t", abs(f(x0)-x0))
    for i in range(1,M):
        x1 = f(x0)
        if x1!=0:
            eAPp = abs((x1-x0)/x1)

        print(i,"\t\t\t",eAPp,"\t\t",abs(f(x1)),"\t\t",abs(f(x1)-x1))
        if abs(eAPp)<es and abs(f(x1)-x1)<e:
            break
        else:
            x0 = x1
    print("Approximate Root: ",x1)

if __name__ == "__main__":
    fixed_point(f, 1,1000, 10**-5, 10**-6)