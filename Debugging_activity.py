#Debugging_Activity Beckham Kwan 

# Task 1 

x = 10
y = 5
result = x / y
print("Result:", result)

# Got an ZeroDivisionError added 5 to Y

print("Task_2 -----")

# Task 2 

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])

# Got an Index Error removed +1 from line 18 

print("Task_3----")

# Task 3 

def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

#Got an Syntax Error added an : on line 26 

print("Task_4")

# Task 4 

def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))



# Got an Indentation Error , Added missing colons from if and else statements

print("Task_5")

# Task 5 

for i in range(5):
   print(i)

   # Got SyntaxError ,Added missing colon 


print("Task_6")

# Task  6 

def greet(name):
   return "Hello", name

# Got SyntaxError , moved missing quote right side of Hello

print("Task_7")

# Task 7 

numbers = [1, 2, 3, 4, 5]

sum = 0

for number in numbers:
    
    sum += number

print("Sum of numbers:", sum)

# Got an Indentation Error , Indented line 78 

print("Task_8")

# Task 8

def factorial(n):
   if n == 0:
     return 1 
   else:
       return n * factorial(n-1)
 
print(factorial(5))

print("Task_9")

# Task 9 

name = input("Enter your name: ")
if name == ("Alice" or "Bob"):
   print("Hello",  + name)
else:
   print("Hello, stranger!")

# Got an logic error added Parenthesis to "Alice" or "Bob":

# Task 10 

def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 5
print(divide_numbers(num1, num2))

#Got ZeroDivisionError repaced 0 with an 5