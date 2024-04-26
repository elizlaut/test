import requests
import csv

key = 'YY5A8WY7KTYS7Z86'

CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=YY5A8WY7KTYS7Z86'


with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for name in my_list:
        print(name[1])

