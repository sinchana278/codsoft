try:
 def add(p,q):
    return p+q
 def subtract(p,q):
    return p-q
 def multiply(p,q):
    return p*q
 def divide(p,q):
    return p/q

 print("Please select the operation.")
 print("a.Add")
 print("b,Subtract")
 print("c.Multiply")
 print("d.divide")

 choice=input("Please enter the choice(a/b/c/d):")

 num1=int(input("Please enter the first number: "))
 num2=int(input("Please enter the second number: "))

 if choice=='a':
    print(num1,"+",num2,"=",add(num1,num2))

 elif choice=='b':
    print(num1,"-",num2,"=",subtract(num1,num2))

 elif choice=='c':
    print(num1,"*",num2,"=",multiply(num1,num2))

 elif choice=='d':
    print(num1,"/",num2,"=",divide(num1,num2))

 else:
    print("This is an invalid input")
except:
    print("Invalid input")