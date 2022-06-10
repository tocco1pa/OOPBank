from checking_account import CheckingAccount
from saving_account import SavingAccount
import csv
class AccountManager():
    accounts = {}
    @classmethod
    def read_accounts(cls):
        """
        starter method to read the account information from the csv to a dictionary
        """
        with open('accounts.txt') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if row[0] == "checking":
                    cls.accounts[row[1]] = CheckingAccount(row[1], row[2], row[3], float(row[4]), row[5])
                elif row[0] == "saving":
                    cls.accounts[row[1]] = SavingAccount(row[1], row[2], row[3], float(row[4]), row[5])

    @classmethod
    def create_account(cls):
        """
        method to create an account and add it to the dictionary
        """
        account_id = str(int(list(reversed(cls.accounts.keys()))[0]) + 1)

        acct_type = input("Enter C for Checking or S for Saving: ").lower()
        first_name = input("First name: ")
        last_name = input("Last name: ")
        
        if acct_type == "c":
            answer = input("Overdraft Protection? (y/n): ").lower()
            if answer == "y":
                overdraft_protection = "True"
            elif answer == "n":
                overdraft_protection = "False"
            cls.accounts[account_id] = CheckingAccount(account_id, first_name, last_name, 0.00, overdraft_protection)
            print("Checking Account Successfully Created")
        elif acct_type == "s":
            interest_rate = input("Interest Rate: ")
            cls.accounts[account_id] = SavingAccount(account_id, first_name, last_name, 0.00, interest_rate)
            print("Saving Account Successfully Created")

    @classmethod
    def close_account(cls):
        """
        method to delete an account from the dictionary 
        """
        account_id = input("Account ID: ")
        del cls.accounts[account_id]
        print("Account closed")

    @classmethod
    def deposit(cls):
        """
        method to deposit an amount of money to a designated account
        """
        account_id = input("Account ID: ")
        amount = int(input("Amount: "))
        cls.accounts[account_id].deposit(amount)

    @classmethod
    def withdraw(cls):
        """
        method to withdraw an amount of money from a designated account
        """
        account_id = input("Account ID: ")
        amount = int(input("Amount: "))
        cls.accounts[account_id].withdraw(amount)

    @classmethod
    def check_balance(cls):
        """
        method to check the current balance of an account
        """
        account_id = input("Account ID: ")
        print("Balance is ${:.2f}".format(cls.accounts[account_id].balance))
    @classmethod
    def write_accounts(cls):
        """
        helper method to update the accounts.txt file with the dictionary's information
        """
        with open('accounts.txt', 'w') as f:
            for key, value in cls.accounts.items():
                if isinstance(value, SavingAccount):
                    f.write('{},{},{},{},{},{}\n'.format("saving", key, value.first_name, value.last_name, value.balance, value._interest_rate))
                if isinstance(value, CheckingAccount):
                    f.write('{},{},{},{},{:.2f},{}\n'.format("checking", key, value.first_name, value.last_name, value.balance, value._overdraft_protected))