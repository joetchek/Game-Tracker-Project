from game_manager import Game_Manager

def main():
    manager = Game_Manager()
    num = 0
    while num != 3:
        num = int(input('Select an option\n1. Add new game\n2. Print games list\n3. Quit program\n'))
        print(num)
        if num == 1:
            manager.user_prompt()
        elif num == 2:
            manager.print_game_list()
        else:
            print("Quitting!")


if __name__ == '__main__':
    main()