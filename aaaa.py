import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

contatos_df = pd.read_excel("baseT.xlsx")
print(contatos_df)


navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

