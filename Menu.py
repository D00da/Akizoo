from Akinator import Akinator
from Nos import nos

def menu():
    akinator = Akinator()
    nodos = nos()

    for id, pergunta in nodos:
        akinator.root = akinator.inserir(akinator.root, id, pergunta)

    while True:
        print("=-" * 15)
        print("Akizoo (Akinator de Animais)")
        print("=-" * 15)
        print("1 - Começar Jogo")
        print("2 - Menu de Debug")
        print("3 - Sair")
        opcao = input("O que deseja fazer ? ")

        match opcao:
            case '1':
                akinator.userInput(akinator.root)
            case '2':
                print("=-" * 10)
                print("Menu de Debug")
                print("=-" * 10)
                print("1 - Mostrar árvore (PRE-ORDER)")
                print("2 - Mostrar árvore (IN-ORDER)")
                print("3 - Mostrar árvore (POST-ORDER)")
                print("4 - Lista de interações")
                print("5 - Sair")
                opcao = input("O que deseja fazer ? ")
                match opcao:
                    case '1':
                        akinator.pre_order(akinator.root)
                    case '2':
                        akinator.in_order(akinator.root)
                    case '3':
                        akinator.post_order(akinator.root)
                    case '4':
                        akinator.tentativas.exibir()
                        akinator.interacoes.exibir()
                    case '5':
                        print("Saindo...")
                    case _:
                        print("Opção inválida! Saindo do Menu de Debug!")
            case '3':
                print("Saindo...")
                break
            case _:
                print("Opção inválida")


if __name__ == "__main__":
    menu()