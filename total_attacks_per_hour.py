import pandas as pd
import json

# Load JSON data dari file
with open('./data/data_ihp_january_with_country.json', 'r') as json_file:
    data_json = json.load(json_file)

# Membuat DataFrame dari JSON data
df = pd.DataFrame(data_json)

# Convert kolom 'time' ke datetime type dengan UTC
df['time'] = pd.to_datetime(df['time'], utc=True)

# Kalkulasi total attacks per jam
df['hour'] = df['time'].dt.hour
attacks_per_hour = df.groupby('hour').size()

# print(df['time'].head())

# Simpan hasil kedalam CSV file
attacks_per_hour.to_csv('./data/total_attacks_per_hour.csv', header=['Total Attacks'])
print("Data disimpan di file 'total_attacks_per_hour.csv'!")
