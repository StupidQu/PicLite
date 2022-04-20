import usr_token
import command

if __name__ == "__main__":
    strin = input()
    if command.is_command(strin):
        command.run_command(strin)
    else:
        exit()
