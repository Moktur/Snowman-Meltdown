import random
import ascii
import game_logic
import short_menu

    
if __name__ == "__main__":
    wanna_play = True
    while wanna_play:
        game_logic.play_game()
        wanna_play = short_menu.short_menu()
        continue
