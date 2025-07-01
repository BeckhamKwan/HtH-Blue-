cookbook = []

def read(Index):
    print(cookbook[Index])

def create(Recipe):
    cookbook.append(Recipe)

    print(f"The recpie {Recipe} has been added")

def read(index):
    if index<len(cookbook):
        return cookbook[index] 
    else:
        print("Please pick an index from 1-6") 

def update(Index,Recipe):
    if Index<len(cookbook):
        cookbook[Index]= Recipe
        print(cookbook)[Index]
    else:
        print("please pick an Index")
        
        
def destroy(Index):
    if Index<len(cookbook):
        cookbook.pop(Index)
    print(f"The Recpie has been destroyed")

def list_all_recpies():

    print(cookbook)


def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recpies()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()
