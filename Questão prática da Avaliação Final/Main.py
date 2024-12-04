from Fila import Fila
class Torre:
    def __init__(self,id,nome,endereco):
        self.id = id
        self.nome = nome
        self.endereco= endereco

class Torres:
    def __init__(self):
        self.torres = []

class Apartamentos:
    def __init__(self):
        self.ap = []

class Apartamento:
    def __init__(self,id,numero,torre,vaga,proximo):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = proximo

def Cadastrar_Torre(self,id,nome,endereco):
    torre = Torre(id,nome,endereco)
    self.torres.append(torre)
    print(f'Torre {torre} foi cadastrado.')

def Remover_Torre(self):
    if self.esta_vazia():
        print("Nenhuma torre cadastrada")
    else:
         Remover_Torre = self.torres.pop()
         print(f'Torre {Remover_Torre} removida.')

def Cadastrar_Apartamento(self,id,numero,torre,vaga,proximo):
    apart = Apartamento(id,numero,torre,vaga,proximo)
    self.ap.append(apart)
    print(f'Apartamento {apart} adicionado.')

def Remover_Apartamento(self):
    if self.esta_vazia():
        print("Nenhum apartamento cadastrado")
    else:
         Remover_Apartamento = self.torres.pop()
         print(f'Apartamentp {Remover_Apartamento} removido.')

def esta_vazia(self):
    return len(self.torres) == 0

def menu():
    torres = Torres()
    ap = Apartamento()
    
    while True:
        print("\nMenu de Operações:")
        print("1. Adicionar torre")
        print("2. Remover torre")
        print("3. Adicionar apartamento")
        print("4. Remover apartamento")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id = int(input("Digite o id da torre: "))
            nome = input("Digite o nome: ")
            endereco = input("Digite o endereço: ")
            torres.Cadastrar_Torre(id,nome,endereco)
        elif opcao == "2":
            torres.Remover_Torre()
        elif opcao == "3":
            id = int(input("Digite o id: "))
            numero = input("Digite o numero do apartamento: ")
            torre = input("Digite sua a torre: ")
            vaga = int(input("Digite a vaga da garegem"))
            ap.Cadastrar_Apartamento(id,numero,torre,vaga)
        elif opcao == "4":
            ap.Remover_Apartamento()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
    

   
