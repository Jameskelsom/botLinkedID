from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


class linkedin:
    def setUp(self):
        self.login = ""
        self.senha = ""
        self.url = "https://www.linkedin.com/"
        self.perfil = []
        self.perfilAcessado = []
        self.driver = webdriver.Chrome()
        self.cont = 0

    def loginApp(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_name('session_key').clear()
        driver.find_element_by_name('session_key').send_keys(self.login)
        driver.find_element_by_name('session_password').clear()
        driver.find_element_by_name('session_password').send_keys(self.senha)
        driver.find_element_by_xpath(
            '/html/body/main/section[1]/div[2]/form/button').click()

    def carregarPerfil(self):
        q = int(input("Carregar quantos perfis? "))
        for i in range(1, q):
            self.perfil.append(str(input(f"Digite o {i}º perfi: ")))

    def capturarPerfil(self):
        driver = self.driver
        sleep(2)
        if len(driver.find_elements_by_class_name('pv-browsemap-section a')) > 0:
            for perfil in driver.find_elements_by_class_name('pv-browsemap-section a'):
                self.perfil.append(str(perfil.get_attribute('href')))
                print(f"→→ Capturado: {perfil.get_attribute('href')}")

    def aguardeApp(self):
        driver = self.driver
        tempo = random.randint(1, 100)
        print(f"    Aguarde: {tempo} segundos")
        for i in range(tempo):
            sleep(1)
            scrollY = random.randint(1, 1000)
            script = f"window.scrollTo(0,{scrollY})"
            driver.execute_script(script)

    def inicarBuscar(self):
        driver = self.driver
        for perfil in self.perfil:
            if perfil not in self.perfilAcessado:
                self.cont = self.cont+1
                self.perfilAcessado.append(perfil)
                driver.get(perfil)
                print(f"{self.cont} - Acessando: {perfil} | Qtd coletada: {len(self.perfil)}")
                self.capturarPerfil()
                # self.aguardeApp()

l = linkedin()
l.setUp()
l.loginApp()
l.carregarPerfil()
l.inicarBuscar()
