class Account:

    def __init__(self, account_id, first_name, last_name, balance):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    
    
    def withdraw(self, amount):
        """withdraws an amount of money from the account balance

        Args:
            amount (float): the amount being withdrawn
        """
        self.balance -= amount
        print("Withdraw Successful")

    def deposit(self, amount):
        """deposits an amount of money to the account balance

        Args:
            amount (float): the amount being deposited
        """
        self.balance += amount
        print("Deposit Successful")
        

    def __str__(self):
        """string replacement function for proper formatting

        Returns:
            string: the object's attributes formated with comma separators
        """
        return "{},{},{},{}".format(self.account_id, self.first_name, self.last_name, self.balance)
        