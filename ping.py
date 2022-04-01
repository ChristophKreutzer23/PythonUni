# Schreiben einer Datei Beispiel:

import os
from datetime import datetime
hostname = input("Geben Sie eine IP oder eine URL an: ")
response = os.system("ping " + hostname)
now = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

# and then check the response...
f = open("log.txt", "a")
if response == 0:
    f.writelines(now + " up " + hostname + "\n")
else:
    f.writelines(now + " down " + hostname + "\n")
f.close()
