num=int(input("Enter the number of find factorial:"))
factorial =1
if(num < 0):
       print("Sorry,factorial does not exist for negative numbers")
elif(num==0):
       print("The factoial of 0 is 1")
else:
       for i in range(1,num+1):
              factorial=factorial*i
print("The factorial of the given number",num,"is",factorial)
