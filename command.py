import usr_token
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
    else:
        raise not_a_command_error(cmd[0])


def command_token(cmd_raw):
    cmd = cmd_raw.split(" ")
    if len(cmd) == 1:
        token = usr_token.Get_Token()
    elif len(cmd) == 3:
        token = usr_token.Get_Token(cmd[1], cmd[2])
    else:
        raise parameters_amount_error("0 or 2")
    print(token)
    return token
