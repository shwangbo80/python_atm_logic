def show_balance(balance):
  print("Your balance is: $" + str(balance))

def deposit(balance):
  amount = input("Enter amount to deposit: $")
  return (float(balance) + float(amount))

def withdraw(balance):
  amount = input("Enter amount to withdraw: $")
  if balance < float(amount):
    print("You have insufficient funds")
    return balance
  else:
    return (float(balance) - float(amount))

def logout(name):
  print("Goodbye, " + name)