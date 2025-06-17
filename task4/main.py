def parse_input(user_input): # Function to parse user input into command and arguments
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#-------------------------------------------
def all_contacts_error(func): # Decorator to handle errors in the all_contacts function
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"An error occurred: {e}"
    return inner

@all_contacts_error
def all_contacts(contacts): # Function to print all contacts
    print(f"Contacts:{contacts}")
    return "Contacts printed"
#-------------------------------------------
def add_contact_input_error(func):# Decorator to handle errors in the add_contact function
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please." 
        except KeyError:
            return "Give me name and phone please."
    return inner

@add_contact_input_error
def add_contact(args, contacts):# Function to add a new contact
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact already exist. Use command 'change' to update the contact."
#-------------------------------------------
def chahge_contact_input_error(func):# Decorator to handle errors in the change_username_phone function
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please." 
        except KeyError:
            return "Give me name and phone please."
    return inner
    
@chahge_contact_input_error
def change_username_phone(args, contacts):# Function to change an existing contact's phone number
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found."
#-------------------------------------------
def phone_error(func):# Decorator to handle errors in the phone_username function
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name please."
        except IndexError:
            return "Give me name please." 
        except KeyError:
            return "Give me name please."
    return inner
    
@phone_error
def phone_username(args, contacts):# Function to get a contact's phone number by name
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."
#-------------------------------------------
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "break"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "all":
            all_contacts(contacts)
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()