from account_manager import AccountManager

def main():
    
    # read in all the accounts from accounts.txt
    AccountManager.read_accounts()

    option = ''
    
    while option != 'f':
        
        print("a) Check Balance")
        print("b) Deposit")
        print("c) Withdraw")
        print("d) Create Account")
        print("e) Close Account")
        print("f) Exit")
        
        option = input("\nSelect an option: ")
        print()
        
        if option == 'a':
            AccountManager.check_balance()
        elif option == 'b':
            AccountManager.deposit()
        elif option == 'c':
            AccountManager.withdraw()
        elif option == 'd':
            AccountManager.create_account()
        elif option == 'e':
            AccountManager.close_account()
        elif option == 'f':
            print("Exiting...")
        else:
            print("You entered an invalid option")
            
        print("\n-----------------------------\n")
        
    # write all the accounts back to accounts.txt
    AccountManager.write_accounts()
    
    
if __name__ == "__main__":
    main()
        
            
            
