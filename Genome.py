from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

wiki_url = 'https://en.wikipedia.org/wiki/Genome'
wiki_data = urlopen(wiki_url)
wiki_html = wiki_data.read()
wiki_data.close()

page_soup = soup(wiki_data, 'html.parser')

genome_table = page_soup.findAll('table', {'class': 'wikitable'})

print(genome_table)