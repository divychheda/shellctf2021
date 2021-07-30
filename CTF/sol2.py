import string
import requests

SERVER_BASE_URL = "http://34.92.214.217:8000" 

possibleCharset = string.digits + string.ascii_letters+ "}{-_!@#$%^&*()+=<>.,;':[]|`~"

s = requests.Session()

def getCookie(username):
    data = {"username":username}
    ret = s.post(SERVER_BASE_URL + "/genCookie",json=data)
    return ret.json()["cookie"]

print(getCookie("divy"))
