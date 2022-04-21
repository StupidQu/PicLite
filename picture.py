import requests
import usr_token
import json
import os
from error import *

URL = "https://sm.ms/api/v2/"


def upload_image(path):
    if os.path.exists(path) == False:
        print(file_do_not_exist_error(path))
        return

    token = usr_token.Get_Token()
    if token is None:
        raise Exception("Token did not set.")
    url = 'https://sm.ms/api/v2/upload'
    params = {
        "format": "json",
        "ssl": True
    }
    files = {
        "smfile": open(path, "rb")
    }
    headers = {
        "Authorization": token
    }
    response = requests.post(url, params=params, headers=headers, files=files)
    result = json.loads(response.text)
    if result["success"] != True:
        raise Exception(upload_image_error(result["message"]))
    return result["data"]
