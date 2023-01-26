-- Innlevering1
--drop table PASSERINGER;
create table PASSERINGER(
	BOMNR varchar(10),
	DATO timestamp,
	-- REGNR varchar(10) hvis vi skal støtte ikke-norske numre og
	-- lengste regnr eg fant i europa var 9 lang
	REGNR char(7) FOREIGN KEY,
);
--drop table REGISTRERINGSNUMRE;
create table REGISTRERINGSNUMRE(
	-- REGNR varchar(10) hvis vi skal støtte ikke-norske numre og
	-- lengste regnr eg fant i europa var 9 lang
	REGNR char(7) PRIMARY KEY,
	ETTERNAVN varchar(25),
	FORNAVN varchar(25),
	ADRESSE varchar(100),
	POSTNR char(5),
	TLF char(8),
	--https://dba.stackexchange.com/questions/37014/in-what-data-type-should-i-store-an-email-address-in-database
	EPOST varchar(320),
	-- når den blir opprettet skal den være 0, deretter øke med 1 for hver passering
	PASSERINGER int
);
insert into REGISTRERINGSNUMRE
values(
		"SV69420",
		"Nordmann",
		"Ole",
		"Olav Kyrres gate 9",
		"5014",
		"22573000",
		"ole.nordmann@example.com"
	);
-- logikk i passeringer tabell skal automatisk øke passeringer for denne regnummer i regnummer tabell
insert into PASSERINGER
values(
		"gvdsvfb",
		"2023-01-20 09:33:04",
		"SV69420",
	);