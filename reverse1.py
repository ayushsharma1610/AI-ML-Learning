num=int(input("Enter a number :"))
temp=num
rev=0
while num !=0 :
    rem= num % 10
    rev=rev * 10 + rem
    num=num // 10

    if rev == temp :
        print(rev,"is a reversed number ")
    else :
        print (rev,"is not a reversed number")    
