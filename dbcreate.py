#!/usr/bin/python

import psycopg2
from psycopg2.extras import RealDictCursor


hostname = 'localhost'
username = 'postgres'
password = 'secret'
database = 'test'

connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

#create cursor factory
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor(cursor_factory=RealDictCursor)

#drop tables if exists...?
# cursor.execute('CREATE DATABASE test;')


cursor.execute('''
	CREATE TABLE test_tables (
	id serial PRIMARY KEY
	);'''
	)

connection.commit()
connection.close()


 
# if __name__ == "__main__":
# 	main()







