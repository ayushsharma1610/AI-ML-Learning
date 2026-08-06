num=int(input("enter a number:"))

a=0
b=1
if num <= 0 :
    print( "write the positive number ")
elif( num ==1) :
    print("Fibonacci series ")
    print ( a )
else :
    print (a,end=" " )  
    print (b,end=" ")  

    for i in range (2 , num):

        c= a + b
        print(c , end=" ")
        a=b
        b=c