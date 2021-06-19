from selenium import webdriver
from time import sleep
#el bot evade todos los contenidos explicitos
busqueda = input("que desea buscar en Google: ")
busqueda = busqueda.replace(" ","+")

driver = webdriver.Chrome('./chromedriver')

driver.get(f"https://www.google.com/search?q={busqueda}&rlz=1C1PRFI_enCO893CO893&oq={busqueda}&aqs=chrome..69i57.5390j0j9&sourceid=chrome&ie=UTF-8")

#hundir la primera pagina que aparezca
driver.execute_script("document.getElementsByClassName('LC20lb DKV0Md')[0].click()")
#maximizar la pantalla
driver.maximize_window()
