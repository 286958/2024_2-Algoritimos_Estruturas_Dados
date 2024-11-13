class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'"{self.titulo}" escrito por "{self.autor}", com {self.paginas} páginas'

class PilhaDeLivros:
    def __init__(self):
        self.pilha = []

    def adicionar_livro(self, titulo, autor, paginas):
        livro = Livro(titulo, autor, paginas)
        self.pilha.append(livro)
        print(f'Livro {livro} foi adicionado à pilha.')

    def remover_livro(self):
        if self.esta_vazia():
            print("A pilha de livros está vazia, não há livros para remover.")
        else:
            livro_removido = self.pilha.pop()
            print(f'Livro {livro_removido} removido da pilha.')

    def mostrar_topo(self):
        if self.esta_vazia():
            print("A pilha de livros está vazia.")
        else:
            print(f'O livro no topo da pilha é: {self.pilha[-1]}')

    def mostrar_todos_livros(self):
        if self.esta_vazia():
            print("A pilha de livros está vazia.")
        else:
            print(f"Tamanho da pilha: {self.tamanho()} livro(s)")
            print("Livros na pilha:")
            for livro in reversed(self.pilha):
                print(f" - {livro}")

    def esta_vazia(self):
        return len(self.pilha) == 0

    def tamanho(self):
        return len(self.pilha)

def menu():
    pilha = PilhaDeLivros()
    
    while True:
        print("\nMenu de Operações:")
        print("1. Adicionar livro")
        print("2. Remover livro")
        print("3. Mostrar livro no topo")
        print("4. Mostrar todos os livros e o tamanho da pilha")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            paginas = int(input("Digite a quantidade de páginas: "))
            pilha.adicionar_livro(titulo, autor, paginas)
        elif opcao == "2":
            pilha.remover_livro()
        elif opcao == "3":
            pilha.mostrar_topo()
        elif opcao == "4":
            pilha.mostrar_todos_livros()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
