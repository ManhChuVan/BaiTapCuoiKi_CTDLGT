import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/MacOS
    else:
        _ = os.system('clear')

def run_array_method():
    os.system('python BTL_Cach1.py')

def run_tree_method():
    os.system('python BTL_Cach2.py')

def run_hash_table_method():
    os.system('python BTL_Cach3.py')

def main():
    while True:
        clear_screen()
        print("Please make your choice:")
        print("1. Method Array")
        print("2. Method Binary Search Tree (BST)")
        print("3. Method Hash Table")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            run_array_method()
        elif choice == '2':
            run_tree_method()
        elif choice == '3':
            run_hash_table_method()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
