import command

if __name__ == "__main__":
    strin = input()
    while command.is_command(strin):
        command.run_command(strin)
        strin = input()
    exit()
