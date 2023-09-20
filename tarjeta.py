import re
from datetime import datetime

#Clase tarjeta 
class Tarjeta:


    #Función para verificar el numero de la tarjeta 
    def verificar_numero_tarjeta(num_tarjeta):
        if re.match(r'^\d{16}$', num_tarjeta):
            return True
        return False

    #Función para verificar la fecha de expiracion de la tarjeta 
    def verificar_fecha_expiracion(fecha_expiracion):
        if re.match(r'^(0[1-9]|1[0-2])\/([2-9]\d)$', fecha_expiracion):
            año_actual = datetime.now().year % 100
            año_expiracion = int(fecha_expiracion.split('/')[1])
            if año_expiracion > año_actual:
                return True
        return False

    #Función para verificar el codigo de verificación de la tarjeta 
    def verificar_codigo_verificacion(cod_verificacion):
        if re.match(r'^\d{3}$', cod_verificacion):
            return True
        return False

    #Función para verificar que la tarjeta sea valida
    def verificar_tarjeta_valida(num_tarjeta, fecha_expiracion, cod_verificacion):
        if  (
            Tarjeta.verificar_numero_tarjeta(num_tarjeta) and
            Tarjeta.verificar_fecha_expiracion(fecha_expiracion) and
            Tarjeta.verificar_codigo_verificacion(cod_verificacion)
            ):
            return True
        return False

    #Función para verificar si exoiste saldo disponible en la tarjeta
    def verificar_saldo_disponible(num_tarjeta, monto_compra):
        if num_tarjeta in Tarjeta.tarjetas_y_saldos:
            saldo_disponible = Tarjeta.tarjetas_y_saldos[num_tarjeta]
            if saldo_disponible >= monto_compra:
                return True
        return False



