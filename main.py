from sys import exit
from printer import print_menu
from contact import add_contact, show_all_contact


def main():
    contacts: list[dict] = [
        {"first_name": 'ali', 'last_name': 'valiyev', 'phone': '3241234123', "group": 'other'}
    ]
    
    while True:
        print_menu()

        choice = input("Menu tanlang: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            show_all_contact(contacts)
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            exit(0)

if __name__ == "__main__":
    main()
