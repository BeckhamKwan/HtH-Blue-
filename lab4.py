#Task 1 
checking = "yes"

while checking == "yes":
    print("What is your age")
    user_input = input()

    if int(user_input) >= 18:
        print("Yes you can vote")

    else:
        print("You can't vote")
    print("Would you like to check another age? " )
    user_input2 = input()
    checking = user_input2

#Task 2 

list1 = [-3,-1,0,3,6]

for x in list:
   
   if x > 0:
    
     print("The value is positive")
   
if x < 0:
   
   print("The value is Negtiive")
else: 
   print('0')    







#Task 3 

Inventory = ["Bedrock","Gold","Iron","CobbleStone","netherite"]

for i in (Inventory):
  if i == "Bedrock":
      print("Why do you have this in your inventory")

  elif i == "Bedrock":
    print("Placed Bedrock arould Johnny Diaz's Home" )

for i in ("Gold"):
  print(f"You got {i} pog")











