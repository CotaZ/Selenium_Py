from TestCase.Login_page import login, autofirma

class Test_001_login:
    username: str = "malu"
    password: str = "12121"

    def test_homepagetitle(self, setup):
        self.driver = setup
        self.driver.close()

    def test_login(self, setup):

        self.driver = setup
        self.lp = login(self.driver)
        self.lp.waittime()
        self.lp.screenshot()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.screenshot()
        self.lp.wait()
        self.lp.setlogin()
        self.lp.wait()
        self.lp.setlogout()
        self.lp.screenshot()
        self.lp.wait()

    def test_prueba(self, setup):
        self.driver = setup
        self.lp = login(self.driver)
        self.lp.wait()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.waittime()
        self.lp.setlogin()
        self.lp.waittime()
        self.lp.setlogout()



    def test_Documentos_pendientes(self, setup):
        self.driver = setup
        self.lp = login(self.driver)
        self.lp.wait()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.wait()
        self.lp.setlogin()
        self.lp.wait()
        self.lp.SetFirmaDigital()
        self.lp.wait()
        self.lp.nuevo()
        self.lp.subirDocumento()
        self.lp.wait()
        self.lp.btnGuardar()
        self.lp.wait()

    def test_Autofirma(self, setup):
        self.driver = setup
        self.lp = login(self.driver)
        self.lp1 = autofirma(self.driver)
        self.lp.wait()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.wait()
        self.lp.setlogin()
        self.lp.wait()
        self.lp1.botonmenuvertical()
        self.lp.wait()
        self.lp1.botonconfiguracion()
        self.lp.wait()
        self.lp1.botonautofirma()
        self.lp.wait()
        self.lp1.btnnuevo()
        self.lp.wait()
        self.lp1.set_opencombo()
        self.lp.wait()
        self.lp1.set_equipo_1()
        self.lp.wait()
        self.lp1.set_tipodocumentos()
        self.lp.wait()
        self.lp1.set_texto()
        self.lp.wait()
        self.lp1.set_certificado()
        self.lp.wait()
        self.lp1.set_firmaqa()
        self.lp.wait()
        self.lp1.set_guardar()
        self.lp.wait()


    def test_prueba(self, setup):
        self.driver = setup
        self.lp = login(self.driver)
        self.lp.wait()
        self.lp.screenshot()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.screenshot()
        self.lp.wait()




