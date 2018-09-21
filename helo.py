import requests
from bs4 import BeautifulSoup

URL = "https://www.forbes.com/companies/77-bank"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())

quotes = []  # a list to store quotes

table = soup.find('div', attrs={'class': 'profile-info__wrap'})

i = 0
row_type = []
row_data = {}
row_data['Company'] = '77-bank'
for row in table.findAll('div', attrs={'class': 'profile-row'}):
    for data in row.findAll('span', attrs={'class': 'profile-row--type'}):
        row_type.append(data.text)
    for data in row.findAll('span', attrs={'class': 'profile-row--value'}):
        #print(row_type[i])
        row_data[row_type[i]] = data.text
        i = i+1


for x in row_data:
    print(x,':',row_data[x])
