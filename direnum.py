# Securitytrails.com

import requests

target = input("Enter target URL (e.g. http://192.168.1.101): ")
wordlist = input("Enter path to wordlist: ")

with open(wordlist, "r") as file:
    for line in file:
        directory = line.strip()
        url = f"{target}/{directory}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[+] Found: {url}")
