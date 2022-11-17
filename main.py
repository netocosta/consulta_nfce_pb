import time
import base64
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

if __name__ == "__main__":
    print("File one executed when ran directly")
    chave = sys.argv[1:][0]
    salvar_em = '.\\'

    
    try {
        # Opções do Selenium
        options = Options()
        options.binary_location = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        options.add_argument("--log-level=3")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        nav = webdriver.Edge(options=options)

        # Acessando o sistema da SEFAZ-PB
        nav.get('https://www4.sefaz.pb.gov.br/atf/seg/SEGf_AcessarFuncao.jsp?cdFuncao=FIS_1410&idSERVirtual=S&h=https://www.sefaz.pb.gov.br/ser/servirtual/credenciamento/info')
        nav.get('https://www4.sefaz.pb.gov.br/atf/fis/FISf_ConsultarNFCE.do?limparSessao=true&h=https://www.sefaz.pb.gov.br/ser/servirtual/credenciamento/info&idSERVirtual=S')
        
        # Inserindo a chave de acesso no campo INPUT
        nav.find_element(By.TAG_NAME, "input").send_keys(chave)
        time.sleep(1)
        # Clicando no Botão de consulta
        nav.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        # Encontrando a TAG da nota fiscal em imagem
        img = nav.find_element(By.XPATH, '//*[@id="relat_pdf"]/div/img')
        # Capturando o conteudo do atributo src da imagem e removendo informação desnecessária
        src = img.get_attribute('src').replace("data:image/gif;base64,", "")
        # Decodificando informação base64 da tag img.
        decoded_data = base64.b64decode(src)
        # Criando um arquivo de imagem
        img_file = open(salvar_em + chave + '.gif', 'wb')
        img_file.write(decoded_data)
        img_file.close()
        # Finalizando o webdrive do selenium
        nav.close()
    except: 
        nav.close()
        print("Houve um erro, não é possível continuar")
