import json
import geoip2.database

# Path ke database GeoIP, sesuaikan dengan path di sistem Anda
reader = geoip2.database.Reader('./lib/GeoLite2-Country.mmdb')

# Fungsi untuk mendapatkan informasi negara berdasarkan source address
def get_country(source_address):
    try:
        response = reader.country(source_address)
        return response.country.names['en']
    except geoip2.errors.AddressNotFoundError:
        return None

# Load data JSON dari luar (dalam kasus ini, dari file JSON)
def load_json_data(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        data = json.load(file)
    return data

# Simpan data JSON ke file
def save_json_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Path ke file JSON yang berisi data log Honeypot
input_file_path = './data/data_ihp_january.json'
output_file_path = './data/data_ihp_january_with_country.json'

# Load data JSON dari file dengan encoding yang sesuai
json_data = load_json_data(input_file_path, encoding='utf-8')

# Proses setiap entri data untuk menambahkan atribut "country" ke dalam "fields"
for entry in json_data:
    source_address = entry['fields']['source_address']
    country_code = get_country(source_address)
    
    if country_code:
        entry['fields']['country'] = country_code

# Simpan data JSON yang telah diperbarui ke file baru
save_json_data(json_data, output_file_path)

print('Data dengan atribut country berhasil disimpan ke file baru!')
