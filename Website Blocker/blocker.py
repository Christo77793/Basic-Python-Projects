import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites_to_be_blocked = ["http://yts.mx/", "yts.mx", "https://www.youtube.com/", "www.youtube.com/", "youtube.com/"]
temp = 0

while temp == 0:

    if dt(dt.now().year, dt.now().month, dt.now().day, 19) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 21):
        print("Changes made")
        with open(hosts, 'r+') as file:
            content = file.read()
            for website in websites_to_be_blocked:
                if website in content:
                    pass
                else:
                    file.write(redirect + "                   " + website + "\n")
        print("Changes made")

    else:
        print("Changes not made")
        with open(hosts, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_to_be_blocked):
                    file.write(line)
            file.truncate()
        print("Changes not made")

    time.sleep(5)

    u_input = input("Stop? y/n ").lower
    if u_input == "y":
        temp += 1