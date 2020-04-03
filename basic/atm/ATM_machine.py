from Costumer import Costumer

PATH = r"C:\Users\Zolberg\Desktop\python\course\Targilim\ATM\Costumers'_DB.txt"
COSTUMER_DICT = {}


def make_dictionary(dictionary, costumer_db):
    for costumer in costumer_db:
        costumer_data = costumer.split()
        new_costumer = Costumer(costumer_data[0], costumer_data[1], costumer_data[2])
        # The dicionery's value  includes the pointer to the object
        dictionary[new_costumer.get_ID()] = new_costumer


def close_ATM(PATH, dictionary):
    new_costumers_info = ""
    for key in dictionary:
        current_costumer = dictionary[key]
        new_costumers_info += current_costumer.get_costumer_data() + "\n"
    with open(PATH, 'w') as new_db:
        new_db.write(new_costumers_info)
    print("Bye bye!")

def atm_options(user_choice,costumer):
    switcher = {
        '1': print("Your balance is {} $".format(costumer.get_balance())),
        '2': withdraw(costumer),
        '3': deposit(costumer),
        '4': change_password(costumer)
    }
    return switcher.get(user_choice, 'Invalid')

def change_password(costumer):
    new_password = input("Enter your new password: \n")
    costumer.set_password(new_password)

def withdraw(costumer):
    money_to_withdraw = int(input("How much money do you want to withdrawl? \n"))
    if money_to_withdraw < 0:
        print("Invalid value.")
        return

    if money_to_withdraw >= costumer.get_balance():
        answer = input("Pay attention that you are going to minus, do you still want to continue y/n 12")
        if answer == 'n':
            return
        elif answer != 'y':
            print("Invalid value.")
            return
        else:
           new_balance = costumer.get_balance() - money_to_withdraw
           costumer.set_balance(new_balance)

def deposit(costumer):
    money_to_deposit = int(input("How much money do you want to diposit? \n"))
    if money_to_deposit < 0:
        print("Invalid value.")
        return

    new_balance = costumer.get_balance() + money_to_deposit
    costumer.set_balance(new_balance)
    return

def main():
    costumer_db = open(PATH, 'r')
    make_dictionary(COSTUMER_DICT, costumer_db)
    while True:
        user_ID = input("Welcome to the coolest ATM machine, Enter your ID: ")
        if int(user_ID) == -1:
            close_ATM(PATH, COSTUMER_DICT)
            return

        elif user_ID not in COSTUMER_DICT:
            print("ID does not exist in system.")
            continue

        user_password = input("Enter your password: ")
        if user_password != COSTUMER_DICT.get(user_ID).get_password():
            print("Incorrect password.")
            continue

        else:
            user_choice = input("What would you like to do? \n"
                                "1. Check the balance\n"
                                "2. Cash withdrawal\n"
                                "3. Cash deposit\n"
                                "4. Change password\n")
            atm_options(user_choice, COSTUMER_DICT.get(user_ID))


if __name__ == '__main__':
    main()
