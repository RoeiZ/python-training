from Costumer import Costumer

PATH = r"C:\Users\Zolberg\Desktop\python\course\Targilim\ATM\Costumers'_DB.txt"
COSTUMER_DB = open(PATH, 'r')
COSTUMER_DICT = {}


def make_dictionary(dictionary):
    for costumer in  COSTUMER_DB:
        costumer_data = costumer.split()
        new_costumer = Costumer(costumer_data[0], costumer_data[1], costumer_data[2])
        # The dicionery's value  includes the pointer to the object
        dictionary[new_costumer.get_ID()] = new_costumer
    return

def close_ATM(PATH, dictionary):
    new_costumers_info = ""
    for key in dictionary:
        current_costumer = dictionary[key]
        new_costumers_info += current_costumer.get_costumer_data() + "\n"
    new_DB = open(PATH, 'w')
    new_DB.write(new_costumers_info)
    print("Bye bye!")
    return

def do_action(user_choice, costumer):
    if user_choice not in [1, 2, 3, 4]:
        print("Invalid number.")
        return

    elif user_choice == 1:
        print("Your balance is {} $".format(costumer.get_balance()))
        return

    elif user_choice == 2:
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

    elif user_choice == 3:
        money_to_deposit = int(input("How much money do you want to diposit? \n"))
        if money_to_deposit < 0:
            print("Invalid value.")
            return

        new_balance = costumer.get_balance() + money_to_deposit
        costumer.set_balance(new_balance)

    else:
        new_password = input("Enter your new password: \n")
        costumer.set_password(new_password)

    return


def main():
    make_dictionary(COSTUMER_DICT)
    while True:
        user_ID = input("Welcome to the coolest ATM machine, Enter your ID: ")
        if int(user_ID) == -1:
            close_ATM(PATH,COSTUMER_DICT)
            return

        elif user_ID not in COSTUMER_DICT :
            print("ID does not exist in system.")
            continue

        user_password = input("Enter your password: ")
        if user_password != COSTUMER_DICT.get(user_ID).get_password():
            print("Incorrect password.")
            continue

        else:
            user_choice = input("""What would you like to do?\n1. Check the balance\n2. Cash withdrawal\
            \n3. Cash deposit\n4. Change password \n""")
            do_action(int(user_choice), COSTUMER_DICT.get(user_ID))



if __name__ == '__main__':
    main()
