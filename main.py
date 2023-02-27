import csv

import requests
from bs4 import BeautifulSoup

res = []
def getData(url):
    response = requests.get(url)


    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'class': 'kvtable'})

    rows = []
    for tr in table.find_all('tr'):
        td = tr.find_all('td')
        for td in tr.find_all('td'):
            res.append(td.text.strip().replace('\n', '').replace('\t', '').replace('\r', ''))
        
    return rows

urls = [
    'https://natbookcat.org.by/isgbi/marcview.do?id=361398&position=1',
    'https://natbookcat.org.by/isgbi/marcview.do?id=298058&position=4',
    'https://natbookcat.org.by/isgbi/marcview.do?id=322421&position=12',
    'https://natbookcat.org.by/isgbi/marcview.do?id=335777&position=13',
    'https://natbookcat.org.by/isgbi/marcview.do?id=341079&position=17',
    'https://natbookcat.org.by/isgbi/marcview.do?id=345109&position=48',
    'https://natbookcat.org.by/isgbi/marcview.do?id=341079&position=33',
    'https://natbookcat.org.by/isgbi/marcview.do?id=381840&position=68'
]


for url in urls:
    rows = getData(url)
for resRow in res:
    print(resRow)
with open('table_data.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(res)