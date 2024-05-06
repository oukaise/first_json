import requests

link = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(link)

if response.status_code == 200:
    data = response.json()
    #pprint.pprint(data)
else:
    print("Ошибка: ", response.status_code)

data_with_valute = data['Valute']
 
def coin_data():
    all_data = []
    for keys, values in data_with_valute.items():
        row = [keys]

        row.append(values["ID"])
        row.append(values["NumCode"])
        row.append(values["CharCode"])
        row.append(values["Nominal"])
        row.append(values["Name"])
        row.append(values["Value"])
        row.append(values["Previous"])
        
        all_data.append(row)

    return all_data

