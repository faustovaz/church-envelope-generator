"Get fake data from namefake api to generate a csv file for testing purposes."
import random
import time
import sys
import csv
import requests

DATA_LEN = 300

if __name__ == '__main__':
    fakes = []
    n = 0
    while n <= DATA_LEN:
        gender = "male" if  random.randint(0,1) == 0 else "female"
        response = requests.get(
                    f'https://api.namefake.com/portuguese-brazil/{gender}/')
        if response.ok:
            fake_data = response.json()
            data = (random.randint(1000, 9999),
                    fake_data['name'],
                    fake_data['phone_w'])
            fakes.append(data)
            time.sleep(5)
            print(data)
        else:
            print("Oops, something wrong with namefake api.")
            sys.exit()
        n += 1
    with open('fake_data.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writerows(fakes)
