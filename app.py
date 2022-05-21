from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          "
)

while True:    
  name = input("Enter name to register: ")
  if len(name) > 10:
    print("The name is too long. Please choose a shorter name")
  else:
    break

while True:
  pin = input("Enter PIN: ")
  if len(pin) != 4:
    print("The length of PIN must be 4 chracters.")
  else:
    break

balance = input("Initial deposit amount")

print(name, "has been registered with a starting balance of $" + balance)

while (True):
  name_to_validate = input("Enter username:")
  pin_to_validate = input("Enter PIN:")
  if name_to_validate == name and pin_to_validate == pin :
      print("Login successful!")
      break
  elif name_to_validate != name or pin_to_validate != pin:
    print("Invalid credentials!")

while (True):
  atm_menu(name)
  option = input("Choose an option: ")
  if option == "1":
    account.show_balance(balance)
  elif option == "2":
    balance = account.deposit(balance)
    print("Current balance: $" + str(balance))
  elif option == "3":
    balance = account.withdraw(balance)
    print("Current balance: $" + str(balance))
  elif option == "4":
    account.logout(name)
    break
