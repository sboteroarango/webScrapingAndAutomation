import requests
from bs4 import BeautifulSoup
busqueda = input('De que busqueda quiere saber todos los titulos: ')
print()
busqueda = busqueda.replace(' ','+')
pagina = requests.get(f'https://www.google.com/search?q={busqueda}&rlz=1C1PRFI_enCO893CO893&oq={busqueda}++&aqs=chrome..69i57j46i39j0i67i395j46i395j0i67i395j0l4j0i271.329288j1j9&sourceid=chrome&ie=UTF-8').text
soup = BeautifulSoup(pagina,'lxml')

titulos =soup.find_all('h3')
for x in titulos:
    print(x.text)
    print()
