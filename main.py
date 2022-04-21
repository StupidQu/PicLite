import command
from config import is_section_exist, get_config, set_config
import logging


def logger_init():
    if is_section_exist("Runtime") == False:
        runtime = "0"
    else:
        runtime = get_config("Runtime", "Runtime")
    set_config("Runtime", "Runtime", (int(runtime) + 1))
    logging.basicConfig(filename=runtime, level=logging.DEBUG,
                        format="[%(levelname)s] %(message)s")


if __name__ == "__main__":
    # logger_init()
    strin = input()
    while command.is_command(strin):
        command.run_command(strin)
        strin = input()
    exit()
