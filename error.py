def parameters_amount_error(parm_amount):
    return "Requires " + parm_amount +  "  parameters, but provides more or less."


def not_a_command_error(cmd):
    return cmd + " is not a command."


def parameter_input_error(parm, need, input):
    return "Parameter " + parm + " must be " + need + ", but the input is " + input + "."


def upload_image_error(message):
    return "Upload image failed! message:" + message