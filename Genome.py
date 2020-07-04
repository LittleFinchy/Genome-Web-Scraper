from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

wiki_url = 'https://en.wikipedia.org/wiki/Genome'
wiki_data = urlopen(wiki_url)
wiki_html = wiki_data.read()
wiki_data.close()

page_soup = soup(wiki_html, 'html.parser')

genome_table = page_soup.findAll('table', {'class': 'wikitable'})
genome_table = genome_table[0]

headers = genome_table.findAll('th', {})

header_titles = []
for header in headers:
    header_titles.append(header.text[:-1])

rows = genome_table.findAll('tr', {})

data = rows[1:]
first_row = data[0]
first_row_data = first_row.findAll('td', {})

data_texts = []
for data_text in first_row_data:
    data_texts.append(data_text.text[:-1])

table_rows = []
for row in data:
    table_row = []
    row_data = row.findAll('td', {})
    for data_point in row_data:
        table_row.append(data_point.text[:-1])
    table_rows.append(table_row)
print(table_rows)