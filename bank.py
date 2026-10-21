def withdraw(amount, balance):
    if amount > balance:
        raise Exception("Insufficient Funds")
    return balance - amount