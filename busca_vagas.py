import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = True
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

# Lista de termos a serem pesquisados
termos_pesquisa = ['java', 'react', 'desenvolvedor', 'dev']
# Data mínima das vagas
data_minima = datetime.strptime('01-11-2024', '%d-%m-%Y') 
# Lista de termos indesejados (se vc quer vagas JR, remova marcações de SR, PL, etc)
termos_indesejados = ['estágio', 'pleno', 'senior', 'sênior', 'pl', 'sr', 'especialista', 'trainee', 'II', 'III']

vagas = []

for termo in termos_pesquisa:    
    driver.get(f"https://portal.gupy.io/job-search/term={termo}")
    time.sleep(5)  # Tempo de espera para carregar a página (ajuste conforme necessário)

    cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'sc-evZas') and contains(@class, 'bdbCHA') and contains(@class, 'sc-4d881605-2') and contains(@class, 'evSPWd')]")
    
    for card in cards:
        nome_vaga = card.find_element(By.XPATH, ".//h3").text
        nome_empresa = card.find_element(By.XPATH, ".//p[contains(@class, 'sc-bBXxYQ')]").text
        
        try:
            localizacao = card.find_element(By.CSS_SELECTOR, "div[aria-label^='Local de trabalho']").text
        except:
            localizacao = "Não informado"

        try:
            modalidade = card.find_element(By.CSS_SELECTOR, "div[aria-label^='Modelo de trabalho']").text
        except:
            modalidade = "Modalidade não especificada"

        try:
            tipo_contrato = card.find_element(By.CSS_SELECTOR, "div[aria-label^='Essa vaga é do tipo']").text
        except:
            tipo_contrato = "Tipo de contrato não especificado"
        
        data_publicacao_texto = card.find_element(By.CSS_SELECTOR, "p.sc-bBXxYQ.eJcDNr.sc-d9e69618-0.iUzUdL").text
        data_publicacao_str = data_publicacao_texto.split(": ")[1]
        data_publicacao = datetime.strptime(data_publicacao_str, '%d/%m/%Y')

        if data_publicacao >= data_minima:
            vagas.append({
                "Nome da Vaga": nome_vaga,
                "Nome da Empresa": nome_empresa,
                "Localização": localizacao,
                "Modalidade": modalidade,
                "Tipo de Contrato": tipo_contrato,
                "Data de Publicação": data_publicacao.strftime('%d/%m/%Y'),  
                "Termo de Pesquisa": termo               
            })

vagas_filtradas = []

for vaga in vagas:
    nome_vaga = vaga['Nome da Vaga']
    deve_manter = True
    
    for termo in termos_indesejados:
        if termo.lower() in nome_vaga.lower():
            deve_manter = False
            break  
    
    if deve_manter:
        vagas_filtradas.append(vaga)

vagas_filtradas = sorted(vagas_filtradas, key=lambda x: datetime.strptime(x["Data de Publicação"], '%d/%m/%Y'), reverse=True)

with open("vagas.csv", "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["Nome da Vaga", "Nome da Empresa", "Localização", "Modalidade", "Tipo de Contrato", "Data de Publicação", "Termo de Pesquisa"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(vagas_filtradas)

driver.quit()
print("CSV criado com sucesso!")
