# Encapsular una logica de creacion en una clase
# Publico = atributo
# Protegido = _atributo
# Privado = __atributo


class CuentaBancaria:
    def __init__(self, titular, saldo) -> None:
        self.titular = titular
        self._saldo = saldo
        self.__numero_cuenta = "12345"

    def mostrar_info_cuenta(self):
        print(f"Titular : {self.titular}")
        print(f"Saldo {self._saldo}")
        print(f"Numero de cuenta { self.__numero_cuenta}")


cuenta = CuentaBancaria("Luis", 200)
cuenta.mostrar_info_cuenta()

print(cuenta.titular)
print(cuenta._saldo)
print(cuenta.__numero_cuenta)
