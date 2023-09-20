import unittest
import tarjeta as tj

#Clase psara el test de tarjeta 
class TestTarjeta(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para cada prueba 
        pass
    #Test para verificar que la tarjeta sea valida
    #Debe contener 16 numeros 
    def test_verificar_numero_tarjeta(self):
        self.assertTrue(tj.Tarjeta.verificar_numero_tarjeta("1234567890123456"))
        self.assertFalse(tj.Tarjeta.verificar_numero_tarjeta("12345"))
        self.assertFalse(tj.Tarjeta.verificar_numero_tarjeta("abcdefg"))

    #Test para verificar la fecha de expiración de la tarjeta
    #Debe contener el mes y el año > al mes y año actual  
    def test_verificar_fecha_expiracion(self):
        self.assertTrue(tj.Tarjeta.verificar_fecha_expiracion("12/24"))#ooo
        self.assertTrue(tj.Tarjeta.verificar_fecha_expiracion("12/25"))
        self.assertFalse(tj.Tarjeta.verificar_fecha_expiracion("13/25"))
        self.assertFalse(tj.Tarjeta.verificar_fecha_expiracion("12/20"))
        self.assertFalse(tj.Tarjeta.verificar_fecha_expiracion("abc/def"))

    #Test para verificar el codigo de verificacion de la tarjeta
    #Debe contener 3 números 
    def test_verificar_codigo_verificacion(self):
        self.assertTrue(tj.Tarjeta.verificar_codigo_verificacion("123"))
        self.assertFalse(tj.Tarjeta.verificar_codigo_verificacion("12"))
        self.assertFalse(tj.Tarjeta.verificar_codigo_verificacion("abc"))

    #Test para verificar si la targeta es valida o no 
    #Debe contener los 16 numeros de una tarjeta, fecha: mes y  año > al mes y año actual, contener 3 números para el codigo de verificación
    def test_verificar_tarjeta_valida(self):
        self.assertTrue(tj.Tarjeta.verificar_tarjeta_valida("1234567890123456", "05/25", "123"))
        self.assertFalse(tj.Tarjeta.verificar_tarjeta_valida("12345", "01/23", "123"))
        self.assertFalse(tj.Tarjeta.verificar_tarjeta_valida("1234567890123456", "13/23", "123"))
        self.assertFalse(tj.Tarjeta.verificar_tarjeta_valida("1234567890123456", "01/20", "123"))
        self.assertFalse(tj.Tarjeta.verificar_tarjeta_valida("1234567890123456", "01/23", "abc"))

    #Test para verificar el saldo disponoible de la tarjeta 
    #Debe contener saldo disponible 
    def test_verificar_saldo_disponible(self):
        self.assertTrue(tj.Tarjeta.verificar_saldo_disponible("1234567890123456", 500))
        self.assertFalse(tj.Tarjeta.verificar_saldo_disponible("1234567890123456", 150000))
        self.assertFalse(tj.Tarjeta.verificar_saldo_disponible("9999999999999999", 500))

    def tearDown(self):
        # Limpieza después de cada prueba 
        pass

if __name__ == "__main__":
    unittest.main()
