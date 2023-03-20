class CuentaBancaria:
    def __init__(self, num_cuenta, nombre_titular, balance, monto):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance
        self.monto = monto

    def depositar (self, monto):
        if monto > 0:
         self.balance += monto

mi_cuenta = CuentaBancaria( "5682", "Vanesa Cabanay", 0, 80000)
print(mi_cuenta)