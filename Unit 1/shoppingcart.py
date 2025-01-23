def get_player_choice():
    print("Choose an option:")
    print("1. Add item to shopping_cart")
    print("2. See shopping cart list")
    print("3. Remove item from shopping cart")
    print("4. Edit item in shopping cart list")
    print("5. Remove all items from the shopping cart")
    print("6. Exit")
    return input("Enter your choice: ")

def add_item(shopping_cart):
    item = input("Enter the item to add: ")
    shopping_cart.append(item)
    print(f"'{item}' has been added to the shopping cart.")

def view_cart(shopping_cart):
    if shopping_cart:
        print("\nShopping Cart:")
        for item in shopping_cart:
            print(f"- {item}")
    else:
        print("\nYour shopping cart is empty.")

def remove_item(shopping_cart):
    if shopping_cart:
        item = input("Enter the name of the item to remove: ")
        if item in shopping_cart:
            shopping_cart.remove(item)
            print(f"'{item}' has been removed from the shopping cart.")
        else:
            print(f"'{item}' is not in the shopping cart.")
    else:
        print("Your shopping cart is empty.")

def edit_item(shopping_cart):
    if shopping_cart:
        old_item = input("Enter the name of the item to edit: ")
        if old_item in shopping_cart:
            new_item = input("Enter the new item: ")
            index = shopping_cart.index(old_item)
            shopping_cart[index] = new_item
            print(f"'{old_item}' has been updated to '{new_item}'.")
        else:
            print(f"'{old_item}' is not in the shopping cart.")
    else:
        print("Your shopping cart is empty.")

def clear_cart(shopping_cart):
    shopping_cart.clear()
    print("All items have been removed from the shopping cart.")

def main():
    shopping_cart = []
    while True:
        choice = get_player_choice()
        if choice == "1":
            add_item(shopping_cart)
        elif choice == "2":
            view_cart(shopping_cart)
        elif choice == "3":
            remove_item(shopping_cart)
        elif choice == "4":
            edit_item(shopping_cart)
        elif choice == "5":
            clear_cart(shopping_cart)
        elif choice == "6":
            print("Thank you for using Grocify. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()