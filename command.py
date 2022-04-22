import os
import usr_token
import config
import picture
import pyperclip
from error import *


def is_command(cmd):
    if cmd == "exit":
        return False
    else:
        return True


def run_command(cmd_raw):
    cmd = cmd_raw.split(" ")
    if cmd[0] == "token":
        return command_token(cmd_raw)
    elif cmd[0] == 'detail':
        return command_detail(cmd_raw)
    elif cmd[0] == 'cleartmp':
        return command_remove_tmp(cmd_raw)
    elif cmd[0] == 'upload':
        return command_upload(cmd_raw)
    elif cmd[0] == 'setformat':
        return command_setformat(cmd_raw)
    elif cmd[0] == 'clip':
        return command_clip(cmd_raw)
    else:
        print(not_a_command_error(cmd[0]))


def command_clip(cmd_raw):
    cmd = cmd_raw.split(' ')
    if len(cmd) != 1:
        print(parameters_amount_error("0"))
    os.system("xclip -selection clipboard -t image/png -o > tmp.png")
    path = os.getcwd()
    res = picture.upload_image(path + "/tmp.png")
    os.remove(path + "/tmp.png")
    if res is None:
        return
    if config.is_exist("Format") == False:
        config.set_config("Format", "Format", "markdown")
    if config.get_config("Format", "Format") == 'markdown':
        pyperclip.copy("![](" + res["url"] + ")")
    else:
        pyperclip.copy(res["url"])
    print("Upload" + Fore.GREEN + " successfully" + Fore.RESET + ". URL:" + Fore.CYAN +  res["url"] + Fore.RESET + "(Copied)" + Fore.RESET)
    

def command_remove_tmp(cmd_raw):
    cmd = cmd_raw.split(" ")
    if len(cmd) != 1:
        print(parameters_amount_error("0"))
        return
    path = os.getcwd()
    confpath = path + "/settings.conf"
    os.remove(confpath)


def command_detail(cmd_raw):
    cmd = cmd_raw.split(" ")
    if (len(cmd) != 1 and len(cmd) != 2):
        print(parameters_amount_error("0 or 1"))
        return
    if len(cmd) == 2 and cmd[1] != "True" and cmd[1] != "False":
        print(parameter_input_error("1", "True or False", cmd[1]))
        return
    if len(cmd) == 2:
        config.set_config("detail", "toggle", cmd[1])
    if len(cmd) == 1:
        if config.is_exist("detail"):
            if config.get_config("detail", "toggle") == "False":
                config.set_config("detail", "toggle", "True")
            else:
                config.set_config("detail", "toggle", "False")
        else:
            config.set_config("detail", "toggle", "True")


def command_token(cmd_raw):
    cmd = cmd_raw.split(" ")
    if len(cmd) == 1:
        token = usr_token.Get_Token()
    elif len(cmd) == 3:
        token = usr_token.Get_Token(cmd[1], cmd[2])
    else:
        print(parameters_amount_error("0 or 2"))
        return
    print("your token is " + token + "(using now)")
    return token


def command_upload(cmd_raw):
    cmd = cmd_raw.split(" ", 1)
    if len(cmd) != 2:
        print(parameters_amount_error("1"))
        return
    end = len(cmd[1]) - 1
    # print(cmd[1])
    while cmd[1][end] == ' ':
        end = end - 1
    if cmd[1][0] == '\'':
        res = picture.upload_image(cmd[1][1:end])
    else:
        res = picture.upload_image(cmd[1])

    if res is None:
        return

    if config.is_exist("Format") == False:
        config.set_config("Format", "Format", "markdown")
    if config.get_config("Format", "Format") == 'markdown':
        pyperclip.copy("![](" + res["url"] + ")")
    else:
        pyperclip.copy(res["url"])
    print("Upload" + Fore.GREEN + " successfully" + Fore.RESET + ". URL:" + Fore.CYAN +  res["url"] + Fore.RESET + "(Copied)" + Fore.RESET)


def command_setformat(cmd_raw):
    cmd = cmd_raw.split(' ')
    if len(cmd) != 2:
        print(parameters_amount_error("1"))
    if cmd[1] != "markdown" and cmd[1] != "plain":
        print(parameter_input_error("1", "markdown or plain", cmd[1]))
    config.set_config("Format", "Format", cmd[1])
