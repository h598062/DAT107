import os
import random
import sys

if len(sys.argv) > 1:
	antall, cwd = sys.argv[1].split(" ")
	antall = int(antall)
	print(cwd)
else:
	antall = 100
	cwd = os.getcwd()
	print(cwd)

etternavnFil = open(cwd + "/etternavn.txt", "rt")
fornavnFil = open(cwd + "/fornavn.txt", "rt")

etternavnListe = etternavnFil.readlines()
fornavnListe = fornavnFil.readlines()

utfil = open(cwd + "/navneliste.txt", "w")

for i in range(0, antall):
	etternavn = random.choice(etternavnListe).strip()
	fornavn = random.choice(fornavnListe).strip()
	utfil.write(f'{fornavn} {etternavn}\n')

etternavnFil.close()
fornavnFil.close()
utfil.close()
