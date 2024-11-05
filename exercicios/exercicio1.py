class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome ='Praça'
restaurante_praca.categoria ='Gourmet'
restaurante_praca.ativo = True



restaurante_praca.categoria = 'Italiana'
print(restaurante_praca.categoria)

print(restaurante_praca.nome)

if restaurante_praca.ativo:
    print('Restaurante esta ativo')
else:
    print('Restaurante não esta ativo')


restaurante_praca.nome = 'Bistro'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

if restaurante_pizza.categoria == 'Fast Food':
    print('O restaurante é Fast Food')
else:
    print('O restaurante não é Fast Food')

if restaurante_pizza.ativo:
        print('Restaurante esta ativo')
else:
    print('Restaurante não esta ativo')


print (f'Nome: {restaurante_praca.nome}  | Categoria:  {restaurante_praca.categoria}')