-- Innlevering1
--drop table TABLE1;
create table TABLE1(
	BOMNR varchar(10),
	DATO timestamp,
	-- REGNR varchar(10) hvis vi skal støtte ikke-norske numre og
	-- lengste regnr eg fant i europa var 9 lang
	REGNR char(7),
	ETTERNAVN varchar(25),
	FORNAVN varchar(25),
	ADRESSE varchar(100),
	POSTNR char(5),
	TLF char(8),
	--https://dba.stackexchange.com/questions/37014/in-what-data-type-should-i-store-an-email-address-in-database
	EPOST varchar(320),
);
insert into TABLE1
values(
		"gvdsvfb",
		"2023-01-20 09:33:04",
		"SV69420",
		"Nordmann",
		"Ole",
		"Olav Kyrres gate 9",
		"5014",
		"22573000",
		"ole.nordmann@example.com"
	);