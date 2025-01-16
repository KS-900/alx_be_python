def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            item = input("Enter an item to add to your shopping list: ").strip()
            shopping_list.append(item)
            print(f"{item} has been added to your shopping list")
            pass
        elif choice == '2':
            item = input("Enter the item you want to remove from the shopping list: ").strip()
            shopping_list.remove(item)
            print(f"{item} has been removed from your shopping list")
            pass
        elif choice == '3':
            if shopping_list:
                print("\nCurrent shopping list")
                for i ,item in enumerate(shopping_list, start=1):
                    print(f"{i}.{item}")
            else:
                print("The shopping list is empty. ")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()