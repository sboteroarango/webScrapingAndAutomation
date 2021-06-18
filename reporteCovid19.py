import requests
from datetime import datetime


diaDeHoy = (datetime.now()).day
pagina = (requests.get("https://api.covid19api.com/total/dayone/country/colombia")).json()
penUltimoReporte = pagina[-2]
ultimoReporte = pagina[-1]

casos = ultimoReporte["Confirmed"]
fallecidos = ultimoReporte["Deaths"]
recuperados = ultimoReporte["Recovered"] 
activos = ultimoReporte["Active"]

nuevosFallecidos = ultimoReporte["Deaths"] -penUltimoReporte["Deaths"]
nuevosCasos = ultimoReporte["Confirmed"] -penUltimoReporte["Confirmed"]
nuevosRecuperados = ultimoReporte["Recovered"] -penUltimoReporte["Recovered"]



print(f"""ReporteCOVID19 dia {diaDeHoy} del mes:\n{nuevosRecuperados:,} recuperados
{nuevosCasos:,} nuevos casos
{nuevosFallecidos:,} fallecidos


Total:

{recuperados:,} recuperados
{casos:,} casos 
{fallecidos:,} fallecidos 
18,557,906 muestras procesadas
{activos:,} casos activos""")

