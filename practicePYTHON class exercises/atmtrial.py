# ATM Simulation

balance=int(input("Enter your balance: "))
amount=int(input("Enter amount to withdraw: "))
if amount <= 0:
    print("Invalid amount. Please enter a positive value.")
elif amount > balance:
    print("Insufficient funds.")
else:
    balance -= amount
    print(f"Withdrawal successful! New balance: {balance:.2f}")
