A =[]
size =int(input("enter the size of array"))
for i in range(size):
    val =int(input("enter the element of array  "))
    A.append(val)
print("original list is ",A)
p =int(input("enter the position from where you want to rotate "))
D =int(input("enter the direction only zero or 1 "))
if p>len(A):
    print("p must be less than ",len(A))
if D==1:#left shift karunga
    s =A[p:]+A[:p]
    print(s)
elif D==0:#right shift karunga
    for count in range(p):
        x =A[len(A)-1]
        for i in range(len(A)-2,-1,-1):
            A[i+1] =A[i]
        A[0]=x
    print(A)
else:
    print("please enter the number 0 or 1")