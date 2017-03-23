#!/usr/bin/python

import psycopg2
from psycopg2.extras import RealDictCursor


hostname = 'localhost'
username = 'postgres' #postgres 
password = 'secret'
database = 'test'

#creates db
connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

#create cursor factory
# connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()#cursor_factory=RealDictCursor)

# cursor.execute('CREATE DATABASE test;')

cursor.execute('''
	DROP TABLE IF EXISTS procedure_type CASCADE;
''')

cursor.execute('''
	CREATE TABLE procedure_type (
	id SERIAL PRIMARY KEY,
	cpt_code VARCHAR,
	description TEXT
	);
''')

cursor.execute('''
	DROP TABLE IF EXISTS facilities CASCADE;
''')

cursor.execute('''
	CREATE TABLE facilities (
	id SERIAL PRIMARY KEY,
	name TEXT,
	address TEXT,
	image BYTEA,
	rating DECIMAL,
	reviews TEXT
	);
''')

cursor.execute('''
	DROP TABLE IF EXISTS geolocations CASCADE;
''')

cursor.execute('''
	CREATE TABLE geolocations (
	id SERIAL PRIMARY KEY,
	id_facilities INTEGER,
	latitude VARCHAR,
	longitude VARCHAR,
	FOREIGN KEY (id_facilities) REFERENCES facilities(id)
	);
''')

cursor.execute('''
	DROP TABLE IF EXISTS procedures CASCADE;
	''')

cursor.execute('''
	CREATE TABLE procedures (
	id SERIAL PRIMARY KEY,
	id_procedure_types INTEGER,
	id_facilities INTEGER,
	tot_price INTEGER,
	FOREIGN KEY (id_procedure_types) REFERENCES procedure_type(id),
	FOREIGN KEY (id_facilities) REFERENCES facilities(id)
	);
''')


connection.commit()
connection.close()


 
# if __name__ == "__main__":
# 	main()







