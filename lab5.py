#Lab 5 Beckham.Kwan

def cat_greeting (meow):
    
    print('Cats says {meow}')

cat_greeting("meow")

#Step 2

def generate_superhero_power():
    
    name = "Beckham"
    power = "Immortal"

    print (f"{name}'s power is being {power}")        
          
generate_superhero_power()

#Step 3 

def generate_superhero_power1():

  power = "Immortal"  
  return power 

print (generate_superhero_power1())

#Step 4

def generate_superhero_power2(user_name, super_power):

   message = user_name + " Has the power of " + super_power + "!"

   return message

print(generate_superhero_power2("Beckham" , "Immortal" ))

#Step 5 

def cat_greetings_loop():
    
    greeting = ("meow","purr","Growing","Chirp","trills")
    
    for i in greeting:
       
       print(f' The cat says {i}')

    

cat_greetings_loop()

#Step 6

def generate_multiple_powers(powers):
   
   for i in powers:
   
    print(i)
    
    powers = ["Flying", "Invisibility", "Super Strength","Being lmmortal"]

    generate_multiple_powers(powers)




