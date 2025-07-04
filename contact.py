from printer import print_status, print_all_contact

def add_contact(contacts: list[dict]):
    first_name = input("first name: ")
    last_name = input("last name: ")
    phone = input("phone: ")
    group = input("group (family, friend, work, other): ")

    contacts.append({
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "group": group,
    })

    print_status('success')

def show_all_contact(contacts: list[dict]):

    if contacts:
        print_all_contact(contacts)
    else:
        print_status('error')

def search_contact():
    pass

def add_contact():
    pass

def update_contact():
    pass

# O'zim qiishni boshlagan joyim.


def load_contacts_from_file(filename):
    contacts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():
                    name, phone = line.strip().split(',')
                    contacts[name] = phone
    except FileNotFoundError:
        print(f"{filename} topilmadi, yangi bo‘sh ro‘yxat yaratildi.")
    return contacts


def save_contacts_to_file(contacts, filename):
    with open(filename, 'w') as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")
    print(f"Kontaktlar {filename} ga saqlandi.")


def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"Kontakt qo'shildi yoki yangilandi: {name} - {phone}")


def find_contact(contacts, name):
    return contacts.get(name, "Kontakt topilmadi.")


def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"{name} o'chirildi.")
    else:
        print(f"{name} topilmadi.")


def list_contacts(contacts):
    if not contacts:
        print("Kontaktlar ro'yxati bo'sh.")
    else:
        print("Kontaktlar ro'yxati:")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")


def main():
    filename = "contacts.txt"
    contacts = load_contacts_from_file(filename)

    while True:
        print("\n--- Kontakt Menejeri ---")
        print("1. Kontakt qo'shish")
        print("2. Kontaktni qidirish")
        print("3. Kontaktni o'chirish")
        print("4. Kontaktlar ro'yxatini ko'rish")
        print("5. Dasturdan chiqish")
        choice = input("Tanlovingizni kiriting (1-5): ")

        if choice == '1':
            name = input("Ismni kiriting: ").strip()
            phone = input("Telefon raqamini kiriting: ").strip()
            add_contact(contacts, name, phone)
            save_contacts_to_file(contacts, filename)

        elif choice == '2':
            name = input("Qidirilayotgan ismni kiriting: ").strip()
            result = find_contact(contacts, name)
            print(f"Natija: {result}")

        elif choice == '3':
            name = input("O'chiriladigan ismni kiriting: ").strip()
            delete_contact(contacts, name)
            save_contacts_to_file(contacts, filename)

        elif choice == '4':
            list_contacts(contacts)

        elif choice == '5':
            print("Dastur yakunlandi.")
            break

        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")


if __name__ == "__main__":
    main()