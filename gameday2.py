from bank import withdraw

balance = 100 

try:
    amount = int(input("Please enter the amount you want to withdraw"))

    balance = withdraw(amount, balance)
except:
        print("Invalid amount.")

has_error = True

while has_error:
    try:
        number = int(input("Enter a number:"))
        print(number)

        has_error = False

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except KeyboardInterrupt:
        print("You stoped the program.")
    except:
        print("You got some random error.")
        break