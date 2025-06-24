#Lab3 By Beckham Kwan

#Task 1

Food = 'Apples'

print(Food[0:3])

print(Food[-3:-1])

(first_last) = Food [0] + Food [-1]

print(first_last)

Food_list = Food.split()

print(Food_list)

joined_food =' '.join(Food_list)

print(joined_food)

#Task 2 

number_list = [12,15,10,69,420]

number_list.append(50)

number_list.insert(2,100)

number_list.pop(0)

number_list.remove(15)

print(number_list)

print(number_list[0:3])
print(number_list[-3:])

print(number_list)

#Task 3 
# (key : value)
Books = {"J.K Rowing" : "Harry Potter Series" , "J.R.R Tolkien" : "The LOTHR" , "Stephenie Meyer" : "Twilight Saga","The Da Vinci Code":"Dan Browm"} # Step 1 

print(Books.keys()) #2
print(Books.values())#3
print(Books.get("J.R.R Tolkien"))#4
Books.pop("Stephenie Meyer")
del Books["J.K Rowing"]
print(Books)











