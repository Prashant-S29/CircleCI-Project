from colorama import Fore

def sayHello():
    name = input("\nWhat's your name:  ")
    print(f"\nHello {Fore.MAGENTA}{name}{Fore.WHITE}! Nice to see you.")
    print("Today we are learning Circle CI Pipeline\n")

sayHello()
