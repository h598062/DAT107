import os
import random
import string
import sys

if len(sys.argv) > 1:
	antall, cwd = sys.argv[1].split(" ")
	antall = int(antall)
	print(cwd)
else:
	antall = 100
	cwd = os.getcwd()
	print(cwd)

def lag_regnr():
    letters = string.ascii_uppercase
    return "".join(random.choices(letters, k=2)) + str(random.randint(10000, 99999))

f = open(cwd + "/regnr.txt", "w")

for i in range(0, antall):
	regnr = lag_regnr()
	f.write(f'{regnr}\n')
f.close()