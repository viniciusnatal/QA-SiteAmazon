from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

from list import Iphone

#declarar pasta do executavel Chrome
navegador = webdriver.Chrome(executable_path= r'./chromedriver.exe')
#inserir url
navegador.get("https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2")

sleep(2)
nome = navegador.find_elements_by_css_selector("h2[class ='a-size-mini a-spacing-none a-color-base s-line-clamp-4']")
precoIphone = navegador.find_elements_by_class_name( 'a-price-whole ')

for value in nome:
    print(f'Modelo do Iphone: {value.text}')

for value in precoIphone:
    print( f'Preço do Iphone: R$ {value.text},00' )


#print(f'Modelo do Iphone: {nome.text}')
#print(f'Modelo do Iphone: R$ {precoIphone.text},00')




