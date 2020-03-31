class Costumer:

    def __init__(self, ID, password, starting_balance):
        self.__ID = ID
        self.password = password
        self.balance = int(starting_balance)

    def get_ID(self):
        return self.__ID

    def get_password(self):
        return self.password

    def set_password(self, new_password):
        self.password = new_password

    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        self.balance = new_balance

    def get_costumer_data(self):
        return "{} {} {}".format(self.__ID, self.password, self.balance)

    def __str__(self):
        print("Costumer's ID: {}\nCostumer's balance: {}".format(self.__ID, self.balance))
