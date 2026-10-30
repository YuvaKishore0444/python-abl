balance = 1000.0

actions_queue = [1, (2, 500.0), (3, 200.0), 4]
step = 0

print("=== ATM Interactive System Simulation ===")

while step < len(actions_queue):
    action = actions_queue[step]

    if action == 1:
        print(f"[ACTION: Balance Inquiry] Current Balance: ${balance:.2f}")

    elif isinstance(action, tuple) and action[0] == 2:
        deposit_amt = action[1]
        balance += deposit_amt
        print(f"[ACTION: Deposit] Deposited ${deposit_amt:.2f}. New Balance: ${balance:.2f}")

    elif isinstance(action, tuple) and action[0] == 3:
        withdraw_amt = action[1]

        if withdraw_amt <= balance:
            balance -= withdraw_amt
            print(f"[ACTION: Withdraw] Withdrew ${withdraw_amt:.2f}. New Balance: ${balance:.2f}")
        else:
            print("[ACTION: Withdraw] Insufficient funds!")

    elif action == 4:
        print("[ACTION: Exit] Thank you for using our ATM system.")
        break

    step += 1