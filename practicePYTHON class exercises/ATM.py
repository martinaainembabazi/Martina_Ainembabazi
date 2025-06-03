

def atm_withdraw(balance):
    print("Welcome to the ATM!")
    print(f"Your current balance is: ${balance:.2f}")
    try:
        amount =(input("Enter amount to withdraw: $"))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"Withdrawal successful! New balance: ${balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    initial_balance = 1000.0  # Example starting balance
    atm_withdraw(initial_balance)