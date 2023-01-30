# Lager all testdata
# alle filene under kan også kjøres seperat
import os
import subprocess
import sys

antall = sys.argv[1] if len(sys.argv) > 1 else 100

p = "testdata/"

args = f"{antall} {os.getcwd()}\\{p}"
subprocess.run(["python", "-Xfrozen_modules=off", f"./{p}generer_navneliste.py", args], stdout=sys.stdout, check=True)
subprocess.run(["python", "-Xfrozen_modules=off", f"./{p}generer_regnr.py", args], stdout=sys.stdout, check=True)
subprocess.run(["python", "-Xfrozen_modules=off", f"./{p}generer_kundedata.py", args], stdout=sys.stdout, check=True)
subprocess.run(["python", "-Xfrozen_modules=off", f"./{p}generer_passeringerdata.py", args], stdout=sys.stdout, check=True)
