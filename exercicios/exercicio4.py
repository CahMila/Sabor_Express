class ContaBancaria:
    def __init__(self, titutar, saldo):
        self.titular = titutar
        self._saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'Conta de {self.titular} -  saldo: R$ {self._saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

conta1 = ContaBancaria ('João', 1500)
conta2 = ContaBancaria ('Jose', 3200)

print(conta1)
print (conta2)

    

conta3 = ContaBancaria ('Paulo', 5200)
print(f'Antes de ativar a conta: Conta ativa ? {conta3._ativo}')

ContaBancaria.ativar_conta(conta3)
print(f'Depois de ativar: Conta ativa? {conta3._ativo}')

print (conta3)