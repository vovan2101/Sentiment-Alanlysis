from urllib import response
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['AMZN', 'AMD', 'FB']

news_tables = {}
for ticker in tickers:
    url = finviz_url + ticker

    req = Request(url=url, headers={'user-agent': 'my-app'})
    response = urlopen(req)
    
    html = BeautifulSoup(response, 'html')
    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table
    break

parsed_data = []

for ticker, news_table in news_tables.items():
    for row in news_table.findAll('tr'):
            title = row.text
            parsed_data.append([ticker, title])
        
print(parsed_data)



# amzn_data = news_tables['AMZN']
# amzn_rows = amzn_data.findAll('td')


# for index, row in enumerate(amzn_rows):
#     title = row.text
#     print(title)