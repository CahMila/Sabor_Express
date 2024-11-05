class Carro:
    def __init__ (self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

#estacioando e atribuindo valores
meu_carro = Carro (modelo = 'Siena', cor= 'Cinza', ano= 2012)

print(meu_carro.modelo)

class Restaurante:
    def __init__(self, nome, categoria, entrega, nota, ativo):
        self.nome = nome
        self.categoria = categoria
        self.entrega = entrega
        self.nota = nota
        self.ativo = ativo
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

#estanciando e atribuindo valores
novo_restaurante = Restaurante (nome = 'Picolle', categoria='Pizzaria',  entrega= True, nota=4.5, ativo=False)
print(novo_restaurante.categoria)

restaurante_modificado= Restaurante (nome='Nakato', categoria='Temakeria',entrega= True, nota=4.5, ativo=False)
print(restaurante_modificado)


class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
    
    def __str__(self):
        return f'{self.nome} | {self.email}'

#estanciando tres objetos
cliente1 = Cliente (nome='Camila', idade=35, email='camila_zetty@hotmail.com', telefone='0000-0000')
cliente2 = Cliente (nome='Zetty', idade=37, email='zetty_sant@hotmail.com', telefone='1111-1111')
cliente3 = Cliente (nome='Alguem', idade=42, email='alguem_alguem@hotmail.com', telefone='2222-2222')

print(cliente1)