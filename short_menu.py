def short_menu():
    """
    Short menu for to choose if someone want to play again.
    returns Boolean
    """
    print("Do you want to play again?")
    answer = ""
    while answer != 'yes' or answer != 'no':
        answer = input("Enter 'yes' for replay, enter 'no' to quit ")
        if answer == "yes":
            return True
        elif answer == "no":
            return False
