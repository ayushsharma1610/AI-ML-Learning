f=open("student.txt",'w')

f.write("name:Ayush\n")
f.write("course:BCA\n")
f.write("Learning:PYTHON\n")

f.close( )

f=open("student.txt","r")

content=f.read()
print(content)

f.close ( )