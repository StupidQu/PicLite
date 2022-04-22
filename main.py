from colorama import Fore, Style
import command
from config import is_section_exist, get_config, set_config
import logging

version = "0.1.1"
is_dev_ver = False


def logger_init():
    if is_section_exist("Runtime") == False:
        runtime = "0"
    else:
        runtime = get_config("Runtime", "Runtime")
    set_config("Runtime", "Runtime", (int(runtime) + 1))
    logging.basicConfig(filename=runtime, level=logging.DEBUG,
                        format="[%(levelname)s] %(message)s")


def print_copyright():
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + "PIC LITE SOFTWARE " + Fore.CYAN + version)
    if is_dev_ver:
        print(Fore.RED + "WARNING:" + Style.NORMAL + Fore.MAGENTA + "You are using the development version.")
    
    print(Style.RESET_ALL)


if __name__ == "__main__":
    # logger_init()
    print_copyright()
    strin = input(Fore.CYAN + Style.BRIGHT + "> " + Style.RESET_ALL)
    while command.is_command(strin):
        command.run_command(strin)
        strin = input(Fore.CYAN + Style.BRIGHT + "> " + Style.RESET_ALL)
    exit()
