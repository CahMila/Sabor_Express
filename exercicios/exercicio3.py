class Pessoa:
    def __init__(self, nome= '', idade= 0, profissão= ''):
        self.nome = nome
        self.idade = idade
        self.profissão = profissão
    
    def __str__(self):
        return f'{self.nome}, {self.idade} anos {self.profissão}'
    
    @property
    def saudaçao(self):
        if self.profissão:
            return f'Olá, sou {self.nome}! e trabalho como {self.profissão}.'
        else:
            f'Ola, sou {self.nome}!'
    
    def aniversario(self):
        self.idade += 1

    
pessoa1 = Pessoa(nome= 'Camila', idade= 35, profissão ='Desenvolvedora')
pessoa2 = Pessoa(nome='Elizete', idade=37, profissão='RH')
pessoa3 = Pessoa(nome= 'Marisa', idade= 57)

print('Informações Iniciais')
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa2.aniversario()

print("Informações após aniversario:")
print(pessoa1)
print(pessoa2)

print(pessoa1.saudaçao)
print(pessoa2.saudaçao)