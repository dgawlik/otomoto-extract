

import duckdb
import pandas as pd


frames = []


from pathlib import Path

path = Path('.')
files = [f for f in path.iterdir() if f.is_file() and f.suffix == '.json']

for f in files:
    frames.append(pd.read_json(f.name))


df_stacked = pd.concat(frames, axis=0)

import re

def power_to_int(pow):
    try:
        clean_pow = re.sub('\\s+KM', '', pow)
        return int(clean_pow)
    except:
        return -1
    
def mileage_to_int(mileage):
    try:
        clean_mileage = re.sub('\\s+km', '', mileage)
        clean_mileage = re.sub('\\s+', '', clean_mileage)
        return int(clean_mileage)
    except:
        return -1
    
def price_to_int(price):
    try:
        clean_price = re.sub('\\s+PLN', '', price)
        clean_price = re.sub('\\s+', '', clean_price)
        return int(clean_price)
    except:
        return -1

df_stacked['power'] = df_stacked['power'].apply(power_to_int)
df_stacked['mileage'] = df_stacked['mileage'].apply(mileage_to_int)
df_stacked['price'] = df_stacked['price'].apply(price_to_int)

rel = duckdb.query("SELECT * FROM df_stacked WHERE price < 15000")
rel.show(max_width=200, max_rows=1000)
