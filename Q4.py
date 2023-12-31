#4) Write and execute a simple program that takes the average of an integer list
def aver(L):
    sum=0
    for j in range(0,len(L)):
        sum=sum+L[j]
    c=sum/len(L)
    return c

list=[]
a= int(input("Enter number of element you wanna enter: "))
print("Enter the element : ")
for i in range(0,a):
    x=int(input())
    list.append(x)
    x=0
print(f"the average of this list equals to: {aver(list)}")