a=int(input("Enter the start of the range: "))
b=int(input("Enter the end of the range: "))
print("Range is ({},{})".format(a,b))
print("Then the status of each number in the range is: ")
prime=0
compo=0
for i in range(a,b+1):
    flag=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            flag=1
    if flag==0:
        print(i,"is a prime number")
        prime=prime+1
    else:
        print(i,"is a composite number")
        compo=compo+1
print("Count: {} prime and {} composite numbers in the range".format(prime,compo))
