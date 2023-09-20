#Estudiantes: Andrea Caicedo
#             Edwin Pupiales
#             Jorge Vega
#             Jose Zambrano

import datetime

class TarjetaCodigo(object):
    #Inicializa la tarjeta
    def _init_(self):
        pass

    #Este hace que las def sean métodos estáticos de la clase principal.
    @staticmethod
    #Función para verificar el número de la tarjeta
    def numeroTarjeta(numTarjeta):
        if not numTarjeta.isdigit():
            return False
        if len(numTarjeta) != 16:
            return False
        return True
    #Este hace que las def sean métodos estáticos de la clase principal.
    @staticmethod
    #Función para verificar la fecha de vencimiento
    def fechaTarjeta(fecha):
        try:
            mes, año = fecha.split('/')
            mes = int(mes)
            año = int(año)
            if mes < 1 or mes > 12:
                return False
            # Comprobamos si la fecha es posterior a 2023, para validar la tarjeta.
            if datetime.date.today() >= datetime.date(year=2000 + año, month=mes, day=1):
                return False
        except:
            return False
        return True
    #Este hace que las def sean métodos estáticos de la clase principal.
    @staticmethod
    #Función para verificar el código de la tarjeta
    def codigoTarjeta(cod):
        if not cod.isdigit():
            return False
        if len(cod) != 3:
            return False
        return True
    
    #Este hace que las def sean métodos estáticos de la clase principal.
    @staticmethod
    #Función para verificar el saldo mayor que el valor a pagar
    def verificarSaldo(valorPagar,saldo):
        if not valorPagar.isdigit():
            return False
        if not saldo.isdigit():
            return False
        if valorPagar > saldo:
            return False
        return True

#Verifica si la tarjeta es válida
def verificarTarjeta(numTarjeta, fecha, cod, valorPagar, saldo):
    tarjeta_valida = False

    if TarjetaCodigo.numeroTarjeta(numTarjeta) and TarjetaCodigo.fechaTarjeta(fecha) and TarjetaCodigo.codigoTarjeta(cod) and TarjetaCodigo.verificarSaldo(valorPagar,saldo):
        tarjeta_valida = True

    if tarjeta_valida:
        print("La tarjeta de crédito es válida, pago aceptado.")
    else:
        print("La tarjeta de crédito no es válida, pago rechazado.")

# numTarjeta = input("Ingrese su número de tarjeta de crédito: ")
# fecha = input("Ingrese la fecha de expiración con formato (MM/YY) de su tarjeta de crédito: ")
# cod = input("Ingrese el código de verificación: ")
# valorPagar = input("Ingrese el valor a pagar: ")
# saldo = input("Ingrese el saldo actual de la tarjeta: ")

# verificarTarjeta(numTarjeta, fecha, cod, valorPagar, saldo)