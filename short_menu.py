def short_menu():
	print("Do you want to play again?")
	answer = ""
	while answer != 'yes' or answer != 'no':
          answer = input("Enter 'yes' for replay, enter 'no' to quit")
          if answer == "yes":
              return True
          elif answer == "no":
              return False
      