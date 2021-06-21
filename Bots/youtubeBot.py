from selenium import webdriver
from time import sleep

busqueda = input("Que quiere buscar en Youtube: ")
busqueda = busqueda.replace(" ","+")
driver = webdriver.Chrome("./chromedriver")

#ingresar al video
driver.get(f"https://www.youtube.com/results?search_query={busqueda}")
sleep(2)

#Hundir el filtro de menos de 4 minutos
driver.find_element_by_xpath("//yt-formatted-string[contains(text(), 'Filtros')]").click()
driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[3]/ytd-search-filter-renderer[1]/a/div/yt-formatted-string').click()
sleep(4)
#Hundir el primer video que aparezca
driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img").click()
sleep(3)

#Ampliar la pantalla
driver.execute_script('document.getElementsByClassName("ytp-fullscreen-button ytp-button")[0].click()')
sleep(1)

#Omitir anuncios
driver.execute_script("document.getElementsByClassName('ytp-ad-skip-button ytp-button')[0].click()")
