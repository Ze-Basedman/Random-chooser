import random, os, time, sys, colorama
from colorama import Fore

colorama.init()


def main():
    print(
        "Inputs are in numbers so if you wanna maybe wanna exit you type '6' not 'exit'"
    )
    time.sleep(2.5)
    os.system("cls")
    while True:
        print(f"{Fore.RED}1. Remove all: Removes All inputs")
        print(f"{Fore.GREEN}2. Put inputs/choices: Inserts inputs")
        print(f"{Fore.CYAN}3. Choose: Chooses a random input")
        print(f"{Fore.YELLOW}4. Clear: Clears All the text on the screen")
        print(f"{Fore.LIGHTRED_EX}5. Show/Removes certain line")
        print(f"{Fore.LIGHTGREEN_EX}6. Exit: Exits")
        print("\033[39m")

        potato = input("Choose: ")

        if potato == "1":
            print(f"{Fore.RED}")
            f = open("choices.txt", "w")
            f.write("")
            f.close()
            print("DONE")
            print("\033[39m")
            time.sleep(1)
        elif potato == "2":
            print(f"{Fore.GREEN}")
            print("type exit if you wanna return to main menu")
            while True:
                wat_write = input("What do you wanna write: ")
                f = open("choices.txt", "a")
                if wat_write.lower() != "exit":
                    f.write(wat_write + "\n")
                if wat_write.lower() == "exit":
                    f.close()
                    main()
            print("\033[39m")
        elif potato == "3":
            print(f"{Fore.CYAN}")
            with open("choices.txt", "r") as f:
                lines = f.readlines()

            if lines and lines[-1][-1] == "\n":
                lines[-1] = lines[-1][:-1]

            with open("choices.txt", "w") as f:
                f.writelines(lines)

            with open("choices.txt", "r") as f:
                arr = f.read().splitlines()

            if len(arr) == 0:
                print("File is empty")
                time.sleep(1.2)
                main()
            choice = random.choice(arr)
            print(choice)
            time.sleep(2.75)
            print("\033[39m")

        elif potato == "4":
            os.system("cls")

        elif potato == "5":
            print(f"{Fore.LIGHTRED_EX}")
            with open("choices.txt", "r+") as f:
                print(
                    "Note that index starts from 0, eg. if you want to remove the first line then you put 0 not 1 and if second like it's 2 and so on"
                    )
                time.sleep(2)
                os.system("cls")
                print(f.read() + "\n")
                ltr = int(input("Enter line to remove: "))
                with open("choices.txt", "r") as f:
                    lines = f.readlines()

                    lines[ltr] = ""

                    with open("choices.txt", "w") as f:
                        for line in lines:
                            f.write(line)
            print("Done\n")
            print("\033[39m")
            time.sleep(2)

        elif potato == "6":
            exit()

        else:
            print("Doesnt exist\n")


main()
