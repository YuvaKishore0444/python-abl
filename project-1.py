initial_balance = 1000.0
withdrawal_limit = 500.0
transactions = [200, -150, -600, 50, -100]

balance = initial_balance
successful_count = 0
rejected_count = 0

for txn in transactions:
    if txn > 0:
        balance += txn
        successful_count += 1
    else:
        withdrawal_amount = abs(txn)
        if withdrawal_amount <= balance and withdrawal_amount <= withdrawal_limit:
            balance -= withdrawal_amount
            successful_count += 1
        else:
            rejected_count += 1

print(f"Initial Balance: ${initial_balance:.2f}")
print(f"Final Balance: ${balance:.2f}")
print(f"Successful Transactions: {successful_count}")
print(f"Rejected Transactions: {rejected_count}")