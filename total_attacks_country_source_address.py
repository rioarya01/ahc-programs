import json
import csv
from datetime import datetime

# Baca file JSON
with open('./data/data_ihp_january_with_country.json', 'r') as file:
    data = json.load(file)

# Buat dictionary untuk menyimpan total serangan per jam berdasarkan source_address dan country
attack_count_source_hourly = {}
attack_count_country_hourly = {}

# Proses data
for entry in data:
    time_str = entry['time']
    source_address = entry['fields']['source_address']
    country = entry['fields'].get('country')

    # Parsing time string ke datetime object dan ekstrak jamnya
    time_obj = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S%z")
    hour = time_obj.strftime('%H')  # Hanya jam dalam angka

    # Hitung total serangan berdasarkan source_address per jam
    if source_address not in attack_count_source_hourly:
        attack_count_source_hourly[source_address] = [0] * 24
    attack_count_source_hourly[source_address][int(hour)] += 1

    # Hitung total serangan berdasarkan country per jam
    if country not in attack_count_country_hourly:
        attack_count_country_hourly[country] = [0] * 24
    attack_count_country_hourly[country][int(hour)] += 1

# Tulis hasil source_address ke file CSV
with open('./data/total_attacks_source_address.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Tulis header
    headers = ['source_address'] + list(range(24))
    writer.writerow(headers)

    # Tulis data
    for source_address, counts in attack_count_source_hourly.items():
        writer.writerow([source_address] + counts)

print("Penghitungan total serangan berdasarkan source_address per jam selesai. Hasil tersimpan dalam file 'total_attacks_source_address.csv'!")

# Tulis hasil country ke file CSV
with open('./data/total_attacks_country.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Tulis header
    headers = ['country'] + list(range(24))
    writer.writerow(headers)

    # Tulis data
    for country, counts in attack_count_country_hourly.items():
        writer.writerow([country] + counts)

print("Penghitungan total serangan berdasarkan country per jam selesai. Hasil tersimpan dalam file 'total_attacks_country.csv'!")
