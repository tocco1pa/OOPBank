from account import Account


class CheckingAccount(Account):    
    overdraft_fee = 20
    def __init__(self, account_id, first_name, last_name, balance, overdraft_protected):
        super(CheckingAccount, self).__init__(account_id, first_name, last_name, balance)
        self._overdraft_protected = overdraft_protected
        

   
    
    def withdraw(self, amount):
        """withdraw check function to determine if the withdraw can be completed

        Args:
            amount (float): the amount to be withdrawn

        Returns:
            super().withdraw(amount): completes the withdraw function from the Account class 
        """
        if(self._overdraft_protected == "True"):
            if((self.balance - amount) < 0):
                print("ERROR - This account does not allow overdrafting")
                return
            else:
                return super().withdraw(amount)
        else:
             if((self.balance - amount) < 0):
                return super().withdraw(amount- self.overdraft_fee)
             else:
                return super().withdraw(amount)