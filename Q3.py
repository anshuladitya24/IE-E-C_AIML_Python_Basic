#3) Write and execute a simple, four-operation calculator program
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
oper=str(input("Enter the operation (+,-,*,/) : "))
if oper=="+":
    print(f"{x}+{y}={x+y}")
elif oper=="-":
    print(f"{x}-{y}={x-y}")
elif oper=="*":
    print(f"{x}*{y}={x*y}")
elif oper=="/":
    print(f"{x}/{y}={float(x/y)}")
else:
    print("Invalid")

