# Lager en sql fil med passeringer som kan legges inn i database
import os
import random
import datetime
import sys

if len(sys.argv) > 1:
	antall, cwd = sys.argv[1].split(" ")
	antall = int(antall)
	print(cwd)
else:
	antall = 100
	cwd = os.getcwd()
	print(cwd)

utfil = open(cwd + "/../testpasseringerdata.sql", "w")
utfil.write(f"-- Dette er en automatisk generert fil. Legger inn {antall} passeringer inn i passeringer tabell\n")

regnrfil = open(cwd + "/regnr.txt", "rt")
regnrliste = regnrfil.readlines()

start_date = datetime.datetime(2023, 1, 15)
end_date = datetime.datetime(2023, 1, 27)

start_time = datetime.datetime.combine(datetime.datetime.today(), datetime.time(0, 0, 0))
end_time = datetime.datetime.combine(datetime.datetime.today(), datetime.time(23, 59, 59))

for i in range(0, antall):
	regnr = random.choice(regnrliste).strip()
	bomnr = random.randint(100, 131)
	pris = 5 * round(random.randint(20, 50) / 5)

	random_date = start_date + datetime.timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
	dato = random_date.strftime("%Y-%m-%d")

	delta = datetime.timedelta(seconds=random.randint(0, int((end_time - start_time).total_seconds())))
	random_datetime = start_time + delta
	random_time = random_datetime.time()
	tid = random_time.strftime("%H:%M:%S")

	utlinje = f'insert into passeringer (bomnr, dato, tidspunkt, regnr, pris) values(\'{bomnr}\',\'{dato}\',\'{tid}\',\'{regnr}\',{pris});\n'
	utfil.write(utlinje)

regnrfil.close()
utfil.close()
