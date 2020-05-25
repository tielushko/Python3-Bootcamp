from termcolor import colored
import pyfiglet

msg = input("What would you like to print?\n")
color = input("What color? \n")

ascii_art = pyfiglet.figlet_format(msg)
try:
    colored_ascii = colored(ascii_art, color=color)
except KeyError:
    print("Invalid Color entered! Applying default color white")
    colored_ascii = colored(ascii_art, color="white")
finally:
    print(colored_ascii)