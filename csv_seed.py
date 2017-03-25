import pandas as pd
import psycopg2
from psycopg2.extras import RealDictCursor


hostname = 'localhost'
username = 'postgres' #postgres is the owner in psql 
password = 'secret'
database = 'test'

#creates db
connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

#create cursor factory
# connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()#cursor_factory=RealDictCursor)



df = pd.read_csv('./combined_seed_tables.csv')

# pandas df['name'].to_list() fcn ???
names=df['name']
addresses=df['address']
images=df['image']
ratings=df['rating']
reviews=df['reviews']

names_list = [i for i in names]
addresses_list = [i for i in addresses]
images_list = [i for i in images]
ratings_list = [i for i in ratings]
reviews_list = [i for i in reviews]

#zip returns an iterator object, need to make it into list
facilities_list_tuple = list(zip(names_list, addresses_list, images_list, ratings_list, reviews_list))

# for row in facilities_tuple:
# 	print(row)


for row in facilities_list_tuple:
	cursor.execute('''
	INSERT INTO
	facilities (name, address, image, rating, reviews)
	VALUES (%s,%s,%s,%s,%s);
	''', row)

# ??? are used in sqlite, %s used in postgres - param styling.

cpt_codes=df['cpt_code']
# cpt_codes_list = df['cpt_code'].tolist()
# cpt_codes_list = df.cpt_code['val'].apply(lambda x: list(x))
# print(cpt_codes_list)

descriptions=df['description']





tot_prices=df['tot_price']
