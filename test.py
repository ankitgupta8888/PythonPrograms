from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

responseMain = urlopen('http://money.cnn.com/magazines/fortune/global500/2013/full_list')
soup = BeautifulSoup(responseMain.read())
responseMain.close()
print(soup)
induslist = soup.find(id="filter3")

f500list = soup.find(class_="list profits")

f = csv.writer(open("f500.csv", "wb"))
f.writerow(["Rank", "Name", "Revenues", "Profits", "Assets", "Employees", "Total stockholders' equity",
            "Total return to investors: 1 yr. annual rate (%)", "Total return to investors: 5 yr. annual rate (%)",
            "Total return to investors: 10 yr. annual rate (%)", "EPS (2012$)", "EPS 1 yr", "EPS 5 yr", "EPS 10 yr",
            "ProfitRevenue %", "ProfitAssets %", "ProfitStockholder'sEquity %", "State", "Industry"])

indusnames = induslist.find_all('option')

for company in f500list.find_all('a'):
    spans = company.find_all('span')

    rank = str(spans[0].get_text()).strip()
    name = str(spans[1].get_text()).strip()
    revenue = str(spans[3].get_text()).strip()
    profits = str(spans[4].get_text()).strip()
    assets = str(spans[5].get_text()).strip()
    employees = str(spans[6].get_text()).strip()
    SHEq = str(spans[7].get_text()).strip()
    RTI = str(spans[8].get_text()).strip()
    RTI5 = str(spans[9].get_text()).strip()
    RTI10 = str(spans[10].get_text()).strip()
    EPS = str(spans[11].get_text()).strip()
    EPS1 = str(spans[12].get_text()).strip()
    EPS5 = str(spans[13].get_text()).strip()
    EPS10 = str(spans[14].get_text()).strip()
    PCTR = str(spans[15].get_text()).strip()
    PCTA = str(spans[16].get_text()).strip()
    PCTSHE = str(spans[17].get_text()).strip()
    State = str(spans[18].get_text()).strip()

    for names in indusnames:
        if str(spans[19].get_text()).strip() == names['value']:
            Indus = names.get_text()
            break

    f.writerow(
        [rank, name, revenue, profits, assets, employees, SHEq, RTI, RTI5, RTI10, EPS, EPS1, EPS5, EPS10, PCTR, PCTA,
         PCTSHE, State, Indus])