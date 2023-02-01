def main():

    a=float(input("Type the value of a: "))
    b=float(input("Type the value of b: "))
    c=float(input("Type the value of c: "))
    print(solve_equation(a,b,c))
    

def solve_equation(a,b,c):
    import math
    delta=(b**2)-4*a*c
    if delta<0:
        return 0
    elif delta==0:
        x=-b/2*a
        return 1, x
    elif delta>0:
        x1=(-b+(math.sqrt(delta)))/(2*a)
        x2=(-b-(math.sqrt(delta)))/(2*a)
        if x1<=x2:
            return 2, x1, x2
        else:
            return 2, x2, x1

main()
