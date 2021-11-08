import requests
import random
import time
import sys
import csv

if __name__ == '__main__':
    fakes = []
    n = 0
    while n <= 100:
        response = requests.get("https://api.namefake.com/portuguese-brazil/female/")
        if response.ok:
            fake_data = response.json()
            data = (random.randint(1000, 9999), fake_data['name'], fake_data['phone_w'])
            fakes.append(data)
            time.sleep(3)
            print(data)
        else:
            print("--------- error ---------")
            sys.exit()
        n += 1
    with open('dizimistas.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writerows(fakes)
