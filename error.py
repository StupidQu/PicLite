from colorama import *

PREFIX = Fore.RED + Style.BRIGHT + "E: " + Style.RESET_ALL


def parameters_amount_error(parm_amount):
    return Fore.RED + Style.BRIGHT + "E: " + Style.RESET_ALL + "Requires " + Fore.CYAN + parm_amount + Fore.RESET + " parameters, but provides more or less."


def not_a_command_error(cmd):
    return Fore.RED + Style.BRIGHT + "E: " + Style.RESET_ALL + Fore.MAGENTA + cmd + Fore.RESET + " is not a command."


def parameter_input_error(parm, need, input):
    return Fore.RED + Style.BRIGHT + "E: " + Style.RESET_ALL + "Parameter " + Fore.CYAN + parm + Fore.RESET + " must be " + Fore.BLUE + need + Fore.RESET + ", but the input is " + Fore.MAGENTA + input + Fore.RESET + "."


def upload_image_error(message):
    return Fore.RED + Style.BRIGHT + "E: " + Style.RESET_ALL + "Upload image failed! message:" + Fore.CYAN + message + Fore.RESET


def file_do_not_exist_error(file_name):
    return PREFIX + "File " +  Fore.CYAN + file_name + Fore.RESET + " doesn\'t exist."

def clip_empty_error():
    return PREFIX + "Clipboard is empty!"

# if __name__ == "__main__":
#     print(parameter_input_error("1", "Markdown or Plain", "MarkUp"))
#     print(parameters_amount_error("1"))
#     print(not_a_command_error("Muteme"))
#     print(upload_image_error("Image is not a image."))
