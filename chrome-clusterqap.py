import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ANO_PROPOSTA = '2023'
UF = 'SE'

""" Ignore certificate to bypass error """
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 5)
driver.get("https://clusterqap2.economia.gov.br/extensions/painel-transferencias-discricionarias-e-legais/painel-transferencias-discricionarias-e-legais.html")
driver.maximize_window()
time.sleep(2)

""" Entrar na Consulta Personalizada """
consulta_personalizada_btn = driver.find_element('xpath', '//a[contains(text(), "Consulta Personalizada")]')
consulta_personalizada_btn.click()

time.sleep(3)


""" Selecionar Ano Proposta """
ano_proposta_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="fltr-ano-proposta-cp"]')))
ano_proposta_btn.click()

keyboard.write(ANO_PROPOSTA)
ano_escolhido = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@id=0]')))
actions.move_to_element(ano_escolhido).click().perform()
confirm_ano = driver.find_element(By.XPATH, '//button[@title="Confirmar seleção" and @data-testid="actions-toolbar-confirm"]')
actions.move_to_element(confirm_ano).click().perform()


""" Selecionar UF """
uf_btn = driver.find_element(By.XPATH, '//div[@id="fltr-uf-cp"]')
uf_btn.click()

time.sleep(0.3)
keyboard.write(UF)
uf_escolhida = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@id=0]')))
actions.move_to_element(uf_escolhida).click().perform()
confirm_uf = driver.find_element(By.XPATH, '//button[@title="Confirmar seleção" and @data-testid="actions-toolbar-confirm"]')
actions.move_to_element(confirm_uf).click().perform()
time.sleep(1)

""" Selecionar Dimensões """
dimensoes = ['Órgão Concedente', 'UF', 'Município', 'Código IBGE', 'Código Programa', 'Nome Programa', 'Nº Proposta', 'Situação Proposta']
dim_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Dimensão")]')))
actions.move_to_element(dim_btn).click().perform()
time.sleep(0.5)

for dim in dimensoes:
    keyboard.write(dim)
    dim_escolhida = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@title="'+dim+'"]')))
    actions.move_to_element(dim_escolhida).click().perform()
    clear_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="lui-search__clear-button"]')))
    actions.move_to_element(clear_btn).click().perform()
    time.sleep(0.5)
    dim_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Pesquisar na caixa de listagem"]')))
    actions.move_to_element(dim_input).click().perform()
    time.sleep(0.3)

# Confirmar seleção
confirm_btn_dim = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="sel-toolbar-btn ng-scope sel-toolbar-confirm" and @title="Confirmar seleção"]')))
actions.move_to_element(confirm_btn_dim).click().perform()

# """ Selecionar Métricas """
metricas = ['Qtd. Propostas', 'VL Global Prop', 'VL Repasse Prop']
met_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Medida")]')))
actions.move_to_element(met_btn).click().perform()
time.sleep(0.5)

for met in metricas:
    keyboard.write(met)
    met_escolhida = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@title="'+met+'"]')))
    actions.move_to_element(met_escolhida).click().perform()
    clear_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="lui-search__clear-button"]')))
    actions.move_to_element(clear_btn).click().perform()
    time.sleep(0.5)
    met_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Pesquisar na caixa de listagem"]')))
    actions.move_to_element(met_input).click().perform()
    time.sleep(0.3)

# Confirmar seleção
confirm_btn_met = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="sel-toolbar-btn ng-scope sel-toolbar-confirm" and @title="Confirmar seleção"]')))
actions.move_to_element(confirm_btn_met).click().perform()

""" Baixar Excel """
btn_download = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@id="btn-export-consulta-personalizada"]')))
actions.move_to_element(btn_download).click().perform()

while keyboard.is_pressed('esc') != True:
    time.sleep(0.1)

driver.close()