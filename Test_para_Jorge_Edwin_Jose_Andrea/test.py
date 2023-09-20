import unittest
import datetime
from tarjetaCodigo import TarjetaCodigo



class TestTarjetaCodigo(unittest.TestCase):
    #cambioooo
    def setUp(self):
        # Configuración inicial para cada prueba 
        pass   


     #Test para verificar que la tarjeta sea valida
    #Debe contener 16 numeros 
    def test_numeroTarjeta(self):
        # Casos de prueba para numeroTarjeta
        self.assertTrue(TarjetaCodigo.numeroTarjeta("1234567890123456"))  
        self.assertFalse(TarjetaCodigo.numeroTarjeta("1234"))  
        self.assertFalse(TarjetaCodigo.numeroTarjeta("abcdefg"))  



    #Test para verificar la fecha de expiración de la tarjeta
    #Debe contener el mes y el año > al mes y año actual  
    def test_fechaTarjeta(self):
        # Casos de prueba para fechaTarjeta
        self.assertTrue(TarjetaCodigo.fechaTarjeta("12/24"))  
        self.assertTrue(TarjetaCodigo.fechaTarjeta("12/25"))  
        self.assertFalse(TarjetaCodigo.fechaTarjeta("13/20"))  
        self.assertTrue(TarjetaCodigo.fechaTarjeta("05/24")) 
        self.assertFalse(TarjetaCodigo.fechaTarjeta("abc/def"))

        
    #Test para verificar el codigo de verificacion de la tarjeta
    #Debe contener 3 números 
    def test_codigoTarjeta(self):
        # Casos de prueba para codigoTarjeta
        self.assertTrue(TarjetaCodigo.codigoTarjeta("321")) 
        self.assertFalse(TarjetaCodigo.codigoTarjeta("11"))  
        self.assertFalse(TarjetaCodigo.codigoTarjeta("abc"))  


    #Test para verificar el saldo disponoible de la tarjeta 
    #Debe contener saldo disponible 
    def test_verificarSaldo(self):
        # Casos de prueba para verificarSaldo
        #primero valor a pagar , segundo saldo 
        self.assertTrue(TarjetaCodigo.verificarSaldo("100", "500"))  
        self.assertFalse(TarjetaCodigo.verificarSaldo("600", "500"))  
        self.assertFalse(TarjetaCodigo.verificarSaldo("bcf", "500")) 
   

    #cambioo
    def tearDown(self):
        # Limpieza después de cada prueba 
        pass

if __name__ == '__main__':
    unittest.main()