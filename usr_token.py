import requests
import json
import config


URL = "https://sm.ms/api/v2/"


def web_get_token(usr, pwd):
    url = URL + "token"
    data = {
        "username": usr,
        "password": pwd
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        raise "The status_code != 200 (token.py/patch_token)"

    result = json.loads(response.text)
    return result["data"]["token"]


def Get_Token(usr="", pwd=""):
    if config.is_exist("token"):
        return config.get_config("token", "token")
    else:
        if usr == "" or pwd == "":
            return None
        token = web_get_token(usr, pwd)
        config.set_config("token", "token", token)
        return token
