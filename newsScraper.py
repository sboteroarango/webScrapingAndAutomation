#This Scraper gets all the titles and descriptions of the web page of the newspaper "El tiempo" at the "Finanzas Personales" section


from bs4 import BeautifulSoup
import requests
pagina = requests.get(f"https://www.eltiempo.com/economia/finanzas-personales").text
soup = BeautifulSoup(pagina, "html.parser")
descripciones = []
titulos = []
imagenes = []

soupTitulos = soup.find_all('h3',attrs={'class':'titulo'})
for titulo in soupTitulos:
  titulos.append(titulo.text)

cuadrosDeDescripciones = soup.find_all('div',attrs={'class':'lead','itemprop':'description'})
for cuadro in cuadrosDeDescripciones:
  descripciones.append(cuadro.find('a').text)


print(soupImagenes)
for titulo, descripcion in list(zip(titulos,descripciones)):
  print(f'{titulo}  :  {descripcion}')

