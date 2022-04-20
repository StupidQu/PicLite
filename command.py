import usr_token
import config
import logging


def is_command(cmd):
    if cmd == "exit":
        return False
    else:
        return True


def run_command(cmd_raw):
    cmd = cmd_raw.split(" ")
    if cmd[0] == "token":
        return command_token(cmd_raw)


def command_token(cmd_raw):
    cmd = cmd_raw.split(" ")
    if len(cmd) == 1:
        return
