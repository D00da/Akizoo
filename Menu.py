from Akinator import Akinator

def menu():
    akinator = Akinator()
    nos = [(1, "Humano"), (2, "É um hominídeo ?"), (3, "Macaco"), (4, "É um primata ?"), (5, "Gato"),
            (6, "É um felino ?"), (7, "Cachorro"), (8, "É um carnivora ?"), (9, "Baleia"), (10, "É aquático ?"),
            (11, "Cavalo"), (12, "É um placentário ?"), (13, "Canguru"), (14, "É um marsupial ?"), (15, "Ornitorrinco"),
            (16, "É um mamífero ?"), (17, "Tartaruga"), (18, "Tem casco ?"), (19, "Crocodilo"), (20, "É um crocodiliano ?"),
            (21, "Lagarto"), (22, "Tem patas ?"), (23, "Cobra"), (24, "É um réptil ?"), (25, "Salamandra"),
            (26, "Tem cauda ?"), (27, "Sapo"), (28, "É um anfíbio ?"), (29, "Galinha"), (30, "É um neognata ?"),
            (31, "Avestruz"), (32, "É uma ave ?"), (33, "Tilápia"), (34, "É um peixe ósseo ?"), (35, "Tubarão")]

    for id, pergunta in nos:
        akinator.root = akinator.inserir(akinator.root, id, pergunta)

    while True:
        print("=-" * 10)
        print("Akinator da Shopee")
        print("=-" * 10)
        print("1 - Começar Jogo")
        print("2 - Menu de Debug")
        print("3 - Sair")
        opcao = input("O que deseja fazer ? ")

        match opcao:
            case '1':
                akinator.interacao(akinator.root)
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
                        akinator.lista.exibir()
                    case '5':
                        print("Saindo...")
                    case '6':
                        akinator.mostrar_arvore(akinator.root)
                    case _:
                        print("Opção inválida! Saindo do Menu de Debug!")
            case '3':
                print("Saindo...")
                break
            case _:
                print("Opção inválida")


if __name__ == "__main__":
    menu()