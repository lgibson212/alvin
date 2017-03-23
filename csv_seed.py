import pandas as pd

df = pd.read_csv('./combined_seed_tables.csv')

names=df['name']
addresses=df['address']
images=df['image']
ratings=df['rating']
reviews=df['reviews']


for i in names:
	print(i)





cpt_codes=df['cpt_code']
descriptions=df['description']





tot_prices=df['tot_price']
