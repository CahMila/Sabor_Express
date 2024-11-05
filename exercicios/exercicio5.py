class Livro:
    def __init__(self, titulo, autor, ano_publicacao, disponivel ):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f'Livro: {self.titulo} | Autor: {self.autor} | Ano de publicação: {self.ano_publicacao}'
    
    def emprestar(self):
        self.disponivel = False
    
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis


livro1 = Livro('A Cabana', 'William P. Young', 2007, True)
livro2 = Livro ('Os segredos da mente milionaria', 'T. Harv Eker', 2005, True)
livro3 = Livro ('Aprendendo Python', 'John Doe', 2022, True)

Livro.livros = [livro1, livro2, livro3] 
print(livro1)
print(livro2)
print(f'Antes de emprestar: Livro disponivel? {livro3.disponivel}')
livro3.emprestar()
print(f'Depois de emprestar: Livro esta disponivel? {livro3.disponivel}')



