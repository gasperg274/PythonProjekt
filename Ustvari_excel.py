
import os
import pandas as pd   
import requests      
from bs4 import BeautifulSoup 

url = 'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count=250'
novo = requests.get(url)
soup = BeautifulSoup(novo.content, 'html.parser')

#prazni seznami v katere bomo dodajali vrednosti
ime_filma = []
leto = []
cas = []
ocena = []
zanr = []
glasovi = []
zasluzek = []



#pomembne podatke shranimo v spremenljivko
podatki = soup.findAll('div', attrs= {'class': 'lister-item mode-advanced'})

#kličemo enega za drugim
for store in podatki:
    ime = store.h3.a.text
    ime_filma.append(ime)
    
    leto_izdaje = store.h3.find('span', class_ = 'lister-item-year text-muted unbold').text.replace('(', '').replace(')', '')
    leto.append(leto_izdaje)
    
    trajanje = store.p.find('span', class_ = 'runtime').text.replace(' min', '')
    cas.append(trajanje)
    
    rating = store.find('div', class_ = 'inline-block ratings-imdb-rating').text.replace('\n', '')
    ocena.append(rating)
    
    zanri = store.p.find('span',class_ = 'genre')
    try:
        zanr.append(zanri.text.replace('\n',''))
    except:
        zanr.append('')    
    #Zaradi istih atributov (glasov in zasluzka) moramo uporabiti indeksiranje
    glasovi_zasluzek = store.find_all('span', attrs = {'name': 'nv'})
    
    glasovali = glasovi_zasluzek[0].text
    glasovi.append(glasovali)
    
    zasl = glasovi_zasluzek[1].text if len(glasovi_zasluzek) >1 else '$140.20M'
    zasluzek.append(zasl)
            
    
#Uporaba knjiznice Pandas
podatki_filma = pd.DataFrame({'Ime filma': ime_filma, 'Leto izdaje': leto, 'Trajanje': cas, 'Zanr': zanr, 'Ocena': ocena,  'Glasovi': glasovi, 'Zasluzek': zasluzek})

#Shranjevanje in odpiranje excel dokumenta:
podatki_filma.to_excel("Podatki_o_filmih.xlsx")
podatki_filma.head(7)
os.system('Podatki_o_filmih.xlsx')#Odpremo novo izdelani excel datoteko

