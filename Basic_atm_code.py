class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        while True:  # Use a loop to keep the ATM session active
            user_input = input('''
            0. Enter 0 to create PIN 
            1. Enter 1 to check balance 
            2. Enter 2 to deposit 
            3. Enter 3 to withdraw 
            4. Enter 4 to exit 
    ''')
            if user_input == '0':
                print("Processing to create PIN:")
                self.create_pin()
            elif user_input == '1':
                print("Check Balance processing:")
                self.check_balance()
            elif user_input == '2':
                print("Deposit Processing:")
                self.deposit_money()
            elif user_input == '3':
                print("Processing to withdraw:")
                self.withdraw_balance()
            elif user_input == '4':
                print("Exiting the ATM")
                break  # Exit the loop and end the ATM session
            else:
                print("Invalid input. Please select a valid option.")

    def create_pin(self):
        self.pin = input("Please enter a 4-digit PIN: ")
        if len(self.pin) != 4 or not self.pin.isdigit():
            print("Invalid PIN. Please enter a 4-digit numerical PIN.")
            self.create_pin()
        else:
            print("PIN created successfully")

    def check_balance(self):
        temp_pin = input("Enter your PIN: ")
        if temp_pin == self.pin:
            print("Your balance is: $", self.balance)
        else:
            print("Invalid PIN. Please verify your PIN.")

    def deposit_money(self):
        temp_pin = input("Enter your PIN: ")
        if temp_pin == self.pin:
            amount = float(input("Enter the amount to deposit: $"))
            if amount > 0:
                self.balance += amount
                print("Deposit successful. Your balance is now: $", self.balance)
            else:
                print("Invalid amount. Please enter a positive amount.")
        else:
            print("Invalid PIN. Please verify your PIN.")

    def withdraw_balance(self):
        temp_pin = input("Enter your PIN: ")
        if temp_pin == self.pin:
            amount = float(input("Enter the amount to withdraw: $"))
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print("Withdrawal successful. Your balance is now: $", self.balance)
                else:
                    print("Insufficient balance. You cannot withdraw more than your balance.")
            else:
                print("Invalid amount. Please enter a positive amount.")
        else:
            print("Invalid PIN. Please verify your PIN.")

# Create an instance of the ATM class
obj1 = Atm()
