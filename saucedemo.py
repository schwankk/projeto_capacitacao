from navigation import Browser, PageObjects, Waits
from file_manipulation import cria_csv, escreve_csv
from selenium.webdriver.common.by import By
import time

def saucedemo(first_name, last_name, postal_code):
    site_data = "https://www.saucedemo.com/v1/"
    file_path = './assets/produtos.csv'

    cria_csv(file_path)    

    driver = Browser.chrome_browser(site_data)    
    Waits.visible(driver, By.XPATH, '//*[@id="user-name"]')
    
    senha   = 'secret_sauce'
    usuario = 'standard_user'
    if Browser.elementoExiste(driver, '//input[@id="user-name"]'):
        Browser.preencheElemento(driver, '//input[@id="user-name"]', usuario)        
        Browser.preencheElemento(driver, '//input[@id="password"]', senha)
        time.sleep(1)
        Browser.clicaElemento(driver, '//input[@id="login-button"]')
        
        Waits.visible(driver, By.XPATH, '//div[@id="shopping_cart_container"]')
        time.sleep(2)
            
        item = 1                        
        for i in range(6):            
            row = (PageObjects.executa_saucedemo(driver, item))            
            escreve_csv(file_path, row)                        
            
            if item <= 3:
                Browser.clicaElemento(driver, f"/html/body/div/div[2]/div[2]/div/div[2]/div/div[{item}]/div[3]/button")
            
            item += 1
                    
        driver.get('https://www.saucedemo.com/v1/cart.html')
        time.sleep(3)
        Browser.clicaElemento(driver, '//*[@id="cart_contents_container"]/div/div[2]/a[2]')
        
        Browser.preencheElemento(driver, '//input[@id="first-name"]', first_name)
        Browser.preencheElemento(driver, '//input[@id="last-name"]', last_name)
        Browser.preencheElemento(driver, '//input[@id="postal-code"]', postal_code)
        time.sleep(2)
        Browser.clicaElemento(driver, '//*[@id="checkout_info_container"]/div/form/div[2]/input')
        
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.save_screenshot("./assets/audit/saucedemo.png")
                        
        driver.close()                