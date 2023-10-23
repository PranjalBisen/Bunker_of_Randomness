# Initialize balance, amn, and amn1 as instance variables
class Atm:
    def __init__(self):
        self.balance = 0
        self.amn = 0
        self.amn1 = 0
        self.pin = ""

        print("Welcome to Pranjal's Bank")
        self.Menu()

    def Menu(self):
        while True:
            print("Menu:")
            print("How Would You Like to Proceed? ")
            user_input = input("""
                 1. Create PIN
                 2. Check Balance
                 3. Deposit
                 4. Withdraw
                 5. Help
                 6. Exit
             """)
            if user_input == "1":
                print("CREATE PIN:")
                self.create_pin()
            elif user_input == "2":
                self.check_balance()
            elif user_input == "3":
                print("DEPOSIT:")
                self.deposit()
            elif user_input == "4":
                print("WITHDRAWAL:")
                self.withdraw()
            elif user_input == "5":
                print("HELP DESK")
                self.help()
            elif user_input == "6":
                print("Thank You for Using our Services")
                break

    def create_pin(self):
        print("Enter your PIN")
        self.pin = input("")

    def deposit(self):
        print("Enter the Amount of Money you wish to Deposit")
        self.amn = int(input())
        self.balance += self.amn
        print("Deposit Successful")

    def withdraw(self):
        print("Enter the Amount you want to Withdraw")
        self.amn1 = int(input())
        if self.amn1 > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= self.amn1
            print("Withdrawal Successful")

    def help(self):
        print("     Contact Info:")
        print("""     Phone: 9689230389
     Email ID: pranjalBank_HelpDesk@gmail.com
     Visit us @ 23, First Floor, Mumbai xxxxxx
""")

    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            print("Balance: ", self.balance)
        else:
            print("Invalid Pin")


# Create an instance of the ATM class to start the program
atm = Atm()