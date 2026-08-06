
print ("simple calculator")
print ("1. Addition")
print ("2. substraction")
print ("3. Multiplication")
print ("4. Division")
choices = int(input("Enter any choice btw 1-4 :"))

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

if choices == 1 :
    print (num1 +num2)
elif ( choices ==2) :
    print(num1 - num2)
elif (choices == 3) :
    print (num1 * num2)
elif(choices == 4) :
    if num2 !=0 :


        print ( num1 / num2)
    else :

         print("Division is not possible" )
else:
    print ("invalid  choices")                     

