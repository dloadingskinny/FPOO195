class GestorDatos:
    def __init__(self):
        # Usamos un diccionario para simular la base de datos de las cuentas
        self.cuentas = {}

    def registrar_usuario(self, nombre, edad):
        # Genera un número de cuenta único
        cuenta = self.generar_numero_cuenta()
        self.cuentas[cuenta] = {"nombre": nombre, "edad": edad, "saldo": 0.0}
        return cuenta

    def verificar_saldo(self, cuenta):
        # Verifica si la cuenta existe y retorna su saldo
        if cuenta in self.cuentas:
            return self.cuentas[cuenta]["saldo"]
        else:
            return None

    def modificar_saldo(self, cuenta, monto, operacion="deposito"):
        # Realiza un depósito o retiro dependiendo de la operación
        if cuenta in self.cuentas:
            if operacion == "deposito":
                self.cuentas[cuenta]["saldo"] += monto
            elif operacion == "retiro" and self.cuentas[cuenta]["saldo"] >= monto:
                self.cuentas[cuenta]["saldo"] -= monto
            else:
                return False  # Falla si intenta retirar más del saldo disponible
            return True
        return False

    def realizar_transferencia(self, origen, destino, monto):
        # Realiza una transferencia de una cuenta a otra
        if origen in self.cuentas and destino in self.cuentas and self.cuentas[origen]["saldo"] >= monto:
            self.cuentas[origen]["saldo"] -= monto
            self.cuentas[destino]["saldo"] += monto
            return True
        return False

    def generar_numero_cuenta(self):
        # Genera un número de cuenta aleatorio no usado anteriormente
        import random
        while True:
            cuenta = str(random.randint(10000, 99999))
            if cuenta not in self.cuentas:
                break
        return cuenta
