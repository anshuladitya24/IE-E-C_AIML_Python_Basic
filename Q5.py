# Design an algorithm for comparing three values
def comparingThreeValues(a,b,c):
    if a>b:
        if c>a:
            return c
        else:
            return a
    else:
        if c>b:
            return c
        else:
            return b
print("enter three numbers: ")
x,y,z=int(input()),int(input()),int(input())
print(f"largest number equal: {comparingThreeValues(x,y,z)}")