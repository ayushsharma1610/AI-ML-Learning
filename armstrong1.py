num=int(input("enter a number:"))

sum=0
temp=num

while num != 0 :
    rem = num % 10
    sum=sum + rem ** 3
    num= num // 10 

if temp ==sum  :
    print(temp,"is a armstrong number")
else :
    print(temp,"is not a armstrong number")       