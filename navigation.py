from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Browser:
    def chrome_browser(site):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--enable-chrome-browser-cloud-management')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.binary_location = "C:/Users/andre_schwanke/Documents/Desenvolvimento/Python/curso/chrome-win64/chrome.exe"
        chrome_driver_path = "C:/Users/andre_schwanke/Documents/Desenvolvimento/Python/curso/chromedriver/chromedriver.exe"
        service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(options=chrome_options, service=service_options)

        driver.get(site)

        return (driver)
    
    def elementoExiste(driver, xpath):        
        existe = False
        
        elementos = driver.find_elements(By.XPATH, xpath)
        if len(elementos) > 0:
            existe = True    

        return existe 

    def clicaElemento(driver, xpath):
        retorno = False
        
        elemento = Waits.clickable(driver, By.XPATH, xpath)
        time.sleep(1)
        
        elemento = driver.find_element(By.XPATH, xpath)
        elemento.click()    
        
        print(f"Clicou em {xpath}")
        retorno = True        
            
        return retorno

    def textoDoElemento(driver, xpath):
        retorno = None
        
        elemento = Waits.clickable(driver, By.XPATH, xpath)
                
        retorno = driver.find_element(By.XPATH, xpath).text
            
        return retorno            

    def preencheElemento(driver, xpath, valor):
        retorno = False
        
        elemento = Waits.clickable(driver, By.XPATH, xpath)
                
        elemento = driver.find_element(By.XPATH, xpath)
        elemento.clear()
        elemento.send_keys(valor)
        retorno = True
        
        print(f"Preencheu {xpath} com {valor}")        
            
        return retorno

class Waits:
    def clickable(driver, by_type, selector):
        return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by_type, selector)))

    def visible(driver, by_type, selector):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by_type, selector)))

    def url(driver, by_type, selector):
        return WebDriverWait(driver, 10).until(EC.url_to_be((by_type, selector)))

class PageObjects:
    def executa_saucedemo(driver, item):
        
        nome = Waits.visible(driver, By.XPATH, f"/html/body/div/div[2]/div[2]/div/div[2]/div/div[{item}]/div[2]/a/div").text
        
        descricao = Waits.visible(driver, By.XPATH, f"/html/body/div/div[2]/div[2]/div/div[2]/div/div[{item}]/div[2]/div").text
                                                
        preco = Waits.visible(driver, By.XPATH, f"/html/body/div/div[2]/div[2]/div/div[2]/div/div[{item}]/div[3]/div").text

        return [nome, descricao, preco]
    
    def executa_fake_data(driver):
        first_name = Waits.visible(driver, By.XPATH, '//div[@class="address"]/h3[1]').text.split()[0]

        last_name = Waits.visible(driver, By.XPATH, '//div[@class="address"]/h3[1]').text.split()[-1]

        company = Waits.visible(driver, By.XPATH, '//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[17]/dd').text

        role = Waits.visible(driver, By.XPATH, '//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[18]/dd').text

        address = Waits.visible(driver, By.XPATH, '//div[@class="adr"]').text.splitlines()[0]

        email = Waits.visible(driver, By.XPATH, '//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[9]/dd[1]').text.splitlines()[0]

        phone_number = Waits.visible(driver, By.XPATH, '//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[4]/dd').text

        driver.refresh()

        return [first_name, last_name, role, company, address, email, phone_number]