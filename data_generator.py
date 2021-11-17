"Get fake data from namefake api to generate a csv file for testing purposes."
import random
import time
import sys
import csv
import requests

DATA_LEN = 300

def get_months_csv():
    "Return a matrix with each row containing a X for each month."
    rows, template = [], [''] * 13
    for i in range(13):
        template[i] = 'X'
        rows.append(template)
        template = [''] * 13
    return rows


if __name__ == '__main__':
    fakes = []
    n = 0
    while n <= DATA_LEN:
        gender = "male" if  random.randint(0,1) == 0 else "female"
        response = requests.get(
                    f'https://api.namefake.com/portuguese-brazil/{gender}/')
        if response.ok:
            fake_data = response.json()
            person_code = random.randint(1000, 9999)
            months_rows = get_months_csv()
            for month_row in months_rows:
                data = (person_code,
                        fake_data['name'],
                        fake_data['phone_w'])
                data = data + tuple(month_row)
                fakes.append(data)
            time.sleep(5)
            print(data)
        else:
            print("Oops, something wrong with namefake api.")
            sys.exit()
        n += 1
    with open('fake_data.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writerow([
                        'person_code', 'person_name', 'person_phone', 'JAN',
                        'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET',
                        'OUT', 'NOV', 'DEZ', 'EXT'])
        writer.writerows(fakes)
