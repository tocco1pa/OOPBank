from account import Account


class SavingAccount(Account):    
    max_balance = 500000
    def __init__(self, account_id, first_name, last_name, balance, interest_rate):
        super(SavingAccount, self).__init__(account_id, first_name, last_name, balance)
        self._interest_rate = float(interest_rate)

    
    def deposit(self, amount):
        """Deposit check function to determine if the deposit can be completed

        Args:
            amount (float): the amount to be deposited

        Returns:
            super().deposit(amount): completes the deposit function from the Account class
        """
        if((self.balance + amount) > self.max_balance):
            print("ERROR - This account does not allow a balance over $500,000")
            return
        else:
            return super().deposit(amount)