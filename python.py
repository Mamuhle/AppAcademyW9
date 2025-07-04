#strings

message = """Bob's World
is cool"""

print(message)

message = 'Hello World!'
print(message.strip())#Remove leading and trailing whitespace
print(message.lower())#Convert all characters to lowercase
print(message.split(','))#Split the string into a list based on the coma

#upper method
#replace method
#Numeric data

num = 3
print(type(num))

num2 = 3.14

print(type(num2))

#Variables
my_variable = 10
total_count = 0

#Operators
#Addition (+)
#Subtraction(-)
#Multiplication(x)
#Division(/)
#Modulus(%)
#Exponent(**)

x = 10
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x-y)
print(x/y)
print(x%y)

#Operators with strings
stri1 ='Hello'
stri2 ='World'

print(stri1 +' ' + stri2 + "" + stri2)
print(stri1 * 3)

#Control Statements

num = 10
if num > 0:
    print("This number is positive")
    
else:
    print("This number is negative")
    
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    
    #Loops
    fruits =["apple", "banana","cherry"]
    for fruit in fruits:
        print(fruit)
     #Using while loop to count from 1 to 5   
    count =1 
    while count <=5:
        print(count)
        count += 1 #Increments the count by 1
        
  #Loop Control statements
   
    count = 0
    while count < 5:
        print(count)
    count +=1
   # if count == 3:
       # break
    
    
