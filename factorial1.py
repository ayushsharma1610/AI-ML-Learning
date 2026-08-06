num=int(input("enter a number:"))

fact = 1

if num < 0 :
    print(" number does not exist for negative number ")
else :
    for i in range (1,num + 1) :
        fact=fact * i
    print ("Factorial of" , num ,"is" ,fact)    
