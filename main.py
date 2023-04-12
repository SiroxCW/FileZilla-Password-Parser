
from bs4 import BeautifulSoup
from os import environ
from base64 import b64decode

print("\nListing all known FileZilla Connections...\n")

with open(rf'{environ["appdata"]}\FileZilla\recentservers.xml', 'r') as f:
    data = f.read()
Bs_data = BeautifulSoup(data, "xml")
servers = Bs_data.find_all("Server")

for i in servers:
    pw = "None"
    user = "None"
    host = "None"
    for l in str(i).splitlines():
        if l.startswith("<Host>"):
            host = l.replace("<Host>", "").replace("</Host>", "")
        if l.startswith("<User>"):
            user = l.replace("<User>", "").replace("</User>", "")
        if l.startswith('<Pass encoding="base64">'):
            pw = l.replace('<Pass encoding="base64">', '').replace("</Pass>", "")
    if not pw == "None":
        pw = str(b64decode(pw)).replace("b'", "").replace("'", "")

    print(f'''{host}  -->  {user}:{pw}''')
