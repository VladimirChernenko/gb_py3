from requests import get
from datetime import date
from time import strptime

file = get('http://www.cbr.ru/scripts/XML_daily.asp')

def currency_rates(charcode):
    file_x = get('http://www.cbr.ru/scripts/XML_daily.asp')
    print(date(*strptime(' '.join(file_x.headers['Date'].split()[1: 4]), '%d %b %Y')[:3]), end=', ')
    try:
        file_x = [i.replace('<',' ', ).replace('>', ' ').split() for i in file_x.text.split('Valute')[1:] if len(i) > 12]
        print(charcode ,{i[5]: float(i[-3].replace(',', '.')) * float(i[8]) for i in file_x}[charcode.upper()])
    except KeyError:
        print(None)


