import time
import os
import pyautogui
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import datetime

import pandas

class login:
    text_username = "//*[@id='cardContainer']/div/div/div[2]/div[1]/div/div/input"
    text_password = "//*[@id='cardContainer']/div/div/div[2]/div[2]/div/div/input"
    boton_login = "//*[@id='cardContainer']/div/div/div[2]/div[3]/div/button"
    boton_logout = "//*[@id='header2']/div/div[2]/div[2]/div/a/div/svg"
    conf_logout = "/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]"
    cerrar = "//*[@id='header2']/div/div[2]/div[2]/div/a/div"
    salir = "button[class='sonda_btn sonda_btn--primary']"
    menu_vertical = "//*[@id='header2']/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div[5]"
    btnfirma = "//*[@id='header2']/div/div[3]/div[1]/div/div/div[1]/div[2]/div/div/div/div[5]/div/div/div[1]/span/div/div[2]"
    documentos_pendientes = "//div[@class='sonda_sidebar-menu_item-text'][normalize-space()='Lista de documentos pendientes']"
    btn_nuevo = "//button[normalize-space()='Nuevo']"
    destino_usuario = "//*[@id='rc_select_2']"
    seleccionaradm = "//div[contains(text(),'ADM - ADM')]"
    subirarchivo = "//*[@id='user-uploader-form']/div[2]/div[2]/div/span/div[1]/span/button"
    Guardardocumento= "//button[normalize-space()='Guardar']"
    btneditar = "//button[@id='sinKey14']"


    def __init__(self, driver):
        self.driver = driver
    def screenshot(self):
        #esta funcionan toma el screenshot
        screenshot = pyautogui.screenshot()
        # esta funcion le da un formato al screenshot .png he ingresa a la hora que se saco
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"captura_{timestamp}.png"
        #aca ingresamos la ruta en donde queremos que se guarden las fotos
        ruta_guardado = "C:/Users/ttoledoa/Desktop/PROYECTOS/ATO/OrangeTest/screenshots/" + filename

        # esta funcion el .save guarda las fotos y entre () en la ruta que deseamos que se guarde
        screenshot.save(ruta_guardado)

        #aqui ingresamos una afirmacion indicando que se guardo en la ruta indicada
        os.makedirs(os.path.dirname(ruta_guardado), exist_ok=True)
        print(f"- Screenshot tomado y guardado en ruta: {ruta_guardado}")

    def setusername(self, username):
        try:
            wait = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.text_username)))
            print("-Usuario Encontrado")
            wait.click()
            try:
                wait.send_keys(username)
                print("-datos enviados con exito: " + username)
            except ElementNotInteractableException:
                print("-no se pueden enviar los datos")

        except NoSuchElementException:
            print("-elemento no encontrado")

    def setpassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password).send_keys(password)

    def setlogin(self):

        login = self.driver.find_element(By.XPATH, self.boton_login)
        login.click()
        print("-login realizado con Exito")

    def setlogout(self):
        wait = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.cerrar)))
        try:
            wait.click()
            print("boton cerrar encontrado")
            try:
                cerrar_1 = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, self.salir)))
                cerrar_1.click()
                print("se a cerrado sesion con exito")
            except NoSuchElementException:
                print("elemento boton salir no encontrado")
        except NoSuchElementException:
            print("localizador boton cerrar no encontrado")

    def SetFirmaDigital(self):
        self.driver.find_element(By. XPATH, self.menu_vertical).click()
        print("menu encontrado")
        self.wait()
        self.driver.find_element(By. XPATH, self.btnfirma).click()
        print("btn menu firma digital encontrado")
        self.wait()
        self.driver.find_element(By. XPATH, self.documentos_pendientes).click()
        print("documentos pendientes encontrado")

    def nuevo(self):
        implicitwait = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.btn_nuevo)))
        implicitwait.click()
        print("boton nuevo encontrado")
        try:
            abrir = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.destino_usuario)))
            abrir.click()
            print("elemento combo box abierto")
            try:
                seleccionar_adm = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.seleccionaradm)))
                seleccionar_adm.click()
                print("elemento seleccionar ADM encontradoo")
            except NoSuchElementException:
                print("elemento seleccionar ADM no enontrado")
        except NoSuchElementException:
            print("elemento combobox no encontrado")
    def subirDocumento(self):
        #esta funcion permite subir un documento solo se debe agregar la ruta al cuadro de dialogo de carga de archivos
        self.driver.find_element(By.XPATH, self.subirarchivo).click()
        time.sleep(3)
        archivo_a_subir = os.path.abspath('C:/Users/ttoledoa/Desktop/PROYECTOS/ATO/412356 Firma Digital/DOCUMENTOS PARA FIRMAR/DOCUMENTOTXT.txt')
        pyautogui.write(archivo_a_subir)
        pyautogui.press("enter")

    def btnGuardar(self):
        #A continuacion se busca el elemento del boton guardar
        try:
            #Guardar = WebDriverWait(self.driver, 15).until(ec.presence_of_element_located((By.LINK_TEXT, self.Guardardocumento)))
            Guardar = self.driver.find_element(By.XPATH, self.Guardardocumento)
            Guardar.click()
            print("boton guardar encontrado")
        except NoSuchElementException:
            print("boton guardar no encontrado")

    def editarDocumentos(self):
        self.driver.find_element(By.XPATH, self.btneditar)

    def buscarpagina(self):
        page_source = self.driver.page_source
        if "ADM" in page_source:
            print("el mensaje de exito se muestra en la pagina")
        else:
            print("el mensaje de exito no se encuentra en la pantalla")
    def wait(self):
        return time.sleep(3)

    def waittime(self):
        return time.sleep(5)


    def Longwait(self):
        return time.sleep(8)
#--------------------------------------------------------------------------------------------------------------------
class autofirma:
    #1
    btnvertical = "//div[@class='sonda_navbar-menu-icon']//*[name()='svg']"
    #2
    configuracionautofirma = "//div[contains(text(),'Configuración Firmas')]"

    confirmadigital = "//body[1]/main[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/span[1]/div[1]"
    #4
    btnautofirma = "//div[@class='sonda_sidebar-menu_item-text'][normalize-space()='Configuración Auto Firmas']"
    #5
    btn_nuevo = "//button[normalize-space()='Nuevo']"
    #6
    combo_agente = "//div[@name='idAgente']//input[@id='rc_select_0']"
    #7
    SCLNTB7016641 = "//div[contains(text(),'SCLNTB7016641')]"
    SCLNTB6599375 = "//div[contains(text(),'SCLNTB6599375')]"
    combo_documentos = "//input[@id='rc_select_1']"
    texto_plano = "//div[contains(text(),'ARCH. TEXTO PLANO')]"
    imagen = "//div[contains(text(),'ARCH. IMAGEN(JPG)')]"
    combo_certificado = "//input[@id='rc_select_2']"
    firmaqa = "//div[contains(text(),'Firma QA')]"
    guardar_firma = "/html[1]/body[1]/main[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/button[1]/*[name()='svg'][1]"
    def __init__(self, driver):
        self.driver = driver

    #1
    def botonmenuvertical(self):
        self.driver.find_element(By.XPATH, self.btnvertical).click()
    #2
    def botonconfiguracion(self):
        self.driver.find_element(By.XPATH, self.configuracionautofirma).click()
    #4
    def botonautofirma(self):
        self.driver.find_element(By.XPATH,self.btnautofirma).click()
    #5
    def btnnuevo(self):
        self.driver.find_element(By.XPATH, self.btn_nuevo).click()
    #6 y 7
    def set_opencombo(self):
        self.driver.find_element(By.XPATH, self.combo_agente).click()

    def set_equipo_1(self):
        self.driver.find_element(By.XPATH, self.SCLNTB7016641).click()

    def set_tipodocumentos(self):
        self.driver.find_element(By.XPATH, self.combo_documentos).click()
    def set_texto(self):
        self.driver.find_element(By.XPATH, self.texto_plano).click()
    def set_imagen(self):
        self.driver.find_element(By.XPATH, self.imagen).click()

    def set_certificado(self):
        self.driver.find_element(By.XPATH, self.combo_certificado).click()
        print()

    def set_firmaqa(self):
        self.driver.find_element(By.XPATH, self.firmaqa).click()
        print("firma seleccionada")

    def set_guardar(self):
        self.driver.find_element(By.XPATH, self.guardar_firma).click()
        print("-autofirma guardada con exito")