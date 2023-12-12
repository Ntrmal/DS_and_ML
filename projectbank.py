class BranchCustomer:
    def __init__(self, name, PhoneNumber, address, type=None):
        self.name = name
        self.type = type if type else "Customer"
        self.PhoneNumber = PhoneNumber
        self.address = address

    def display(self, total=None):
        print("\n\n")
        print("Name:", self.name)
        print("Type:", self.type)
        print("Phone Number:", self.PhoneNumber)
        print("Address:", self.address)
        if total is not None:
            print("Total Balance:", total)
        print("\n\n")


class BankingSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, name, PhoneNumber, address, type=None, initial_balance=0):
        if name not in self.users:
            user = BranchCustomer(name, PhoneNumber, address, type)
            self.users[name] = {"user": user, "balance": initial_balance}
            print(f"User {name} registered successfully with initial balance: {initial_balance}")
        else:
            print(f"User {name} already exists.")

    def credit(self, name, amount):
        if name in self.users:
            self.users[name]["balance"] += amount
            print(f"Amount {amount} credited to {name}. New balance: {self.users[name]['balance']}")
        else:
            print(f"User {name} does not exist. Register, then Proceed")

    def debit(self, name, amount):
        if name in self.users:
            if self.users[name]["balance"] >= amount:
                self.users[name]["balance"] -= amount
                print(f"Amount {amount} debited from {name}. New balance: {self.users[name]['balance']}")
            else:
                print(f"Insufficient funds for {name}.")
        else:
            print(f"User {name} does not exist.")

    def display_balance(self, name):
        if name in self.users:
            user = self.users[name]["user"]
            balance = self.users[name]["balance"]
            user.display(balance)
        else:
            print(f"User {name} does not exist.")


if __name__ == "__main__":
    bank = BankingSystem()

    while True:
        print("\nBanking System Menu:")
        print("1. Register User")
        print("2. Credit Amount")
        print("3. Debit Amount")
        print("4. Display Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            PhoneNumber = input("Enter Phone Number: ")
            address = input("Enter Address: ")
            type = input("Enter type (default is None): ")
            initial_balance = float(input("Enter initial balance (default is 0): "))
            bank.register_user(name, PhoneNumber, address, type, initial_balance)

        elif choice == "2":
            name = input("Enter name: ")
            amount = float(input("Enter amount to credit: "))
            bank.credit(name, amount)

        elif choice == "3":
            name = input("Enter name: ")
            amount = float(input("Enter amount to debit: "))
            bank.debit(name, amount)

        elif choice == "4":
            name = input("Enter name: ")
            bank.display_balance(name)

        elif choice == "5":
            print("Exiting the Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
