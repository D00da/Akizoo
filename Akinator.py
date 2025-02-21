class No:
    def __init__(self, id, pergunta, sim=None, nao=None):
        self.id = id
        self.pergunta = pergunta
        self.altura = 1
        self.sim = sim  # Esquerda
        self.nao = nao  # Direita
        self.anterior = None
        self.proximo = None


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserir(self, no):
        if not self.head:
            self.head = no
            return
        elif not self.head.proximo:
            self.head.proximo = no
            self.tail = no
            return
        self.tail.proximo = no
        no.anterior = self.tail
        self.tail = no

    def exibir(self):
        atual = self.head
        while atual:
            print(atual.pergunta)
            atual = atual.proximo


class Akinator:
    def __init__(self):
        self.root = None
        lista = Lista()
        self.lista = lista

    def inserir(self, root, id, pergunta):
        if root is None:
            return No(id, pergunta)

        if id < root.id:
            if root.sim is None:
                root.sim = No(id, pergunta)
            else:
                self.inserir(root.sim, id, pergunta)
        else:
            if root.nao is None:
                root.nao = No(id, pergunta)
            else:
                self.inserir(root.nao, id, pergunta)

        root.altura = 1 + max(self.obter_altura(root.sim), self.obter_altura(root.nao))

        fator_balanceamento = self.obter_balanceamento(root)

        if fator_balanceamento > 1 and id < root.sim.id:
            return self.rotacionar_direita(root)
        if fator_balanceamento < -1 and id > root.nao.id:
            return self.rotacionar_esquerda(root)
        if fator_balanceamento > 1 and id > root.sim.id:
            root.sim = self.rotacionar_esquerda(root.sim)
            return self.rotacionar_direita(root)
        if fator_balanceamento < -1 and id < root.nao.id:
            root.nao = self.rotacionar_direita(root.nao)
            return self.rotacionar_esquerda(root)

        return root

    def remover(self, root, id):
        if not root:
            return root

        if id < root.id:
            root.sim = self.remover(root.sim, id)
        elif id > root.id:
            root.nao = self.remover(root.nao, id)
        else:
            if not root.sim:
                return root.nao
            elif not root.nao:
                return root.sim

            temp = self.obter_no_minimo(root.nao)
            root.id = temp.id
            root.pergunta = temp.pergunta
            root.nao = self.remover(root.nao, temp.id)

        root.altura = 1 + max(self.obter_altura(root.sim), self.obter_altura(root.nao))

        fator_balanceamento = self.obter_balanceamento(root)

        if fator_balanceamento > 1 and id < root.sim.id:
            return self.rotacionar_direita(root)
        if fator_balanceamento < -1 and id > root.nao.id:
            return self.rotacionar_esquerda(root)
        if fator_balanceamento > 1 and id > root.sim.id:
            root.sim = self.rotacionar_esquerda(root.sim)
            return self.rotacionar_direita(root)
        if fator_balanceamento < -1 and id < root.nao.id:
            root.nao = self.rotacionar_direita(root.nao)
            return self.rotacionar_esquerda(root)

        return root

    def rotacionar_esquerda(self, z):
        y = z.nao
        temp = y.sim
        y.sim = z
        z.nao = temp
        z.altura = 1 + max(self.obter_altura(z.sim), self.obter_altura(z.nao))
        y.altura = 1 + max(self.obter_altura(y.sim), self.obter_altura(y.nao))
        return y

    def rotacionar_direita(self, z):
        y = z.sim
        temp = y.nao
        y.nao = z
        z.sim = temp
        z.altura = 1 + max(self.obter_altura(z.sim), self.obter_altura(z.nao))
        y.altura = 1 + max(self.obter_altura(y.sim), self.obter_altura(y.nao))
        return y

    def obter_altura(self, root):
        if not root:
            return 0
        return root.altura

    def obter_balanceamento(self, root):
        if not root:
            return 0
        return self.obter_altura(root.sim) - self.obter_altura(root.nao)

    def obter_no_minimo(self, root):
        if root is None or root.sim is None:
            return root
        return self.obter_no_minimo(root.sim)

    # def mostrar_arvore(self, root, nivel=0):
    # if root is not None:
    # print(" " * (nivel * 4) + f"{root.pergunta}")
    # self.mostrar_arvore(root.sim, nivel + 1)
    # self.mostrar_arvore(root.nao, nivel + 1)

    def pre_order(self, root):
        if root:
            print(root.pergunta, end=" ")
            self.pre_order(root.sim)
            self.pre_order(root.nao)

    def in_order(self, root):
        if root:
            self.in_order(root.sim)
            print(root.pergunta, end=" ")
            self.in_order(root.nao)

    def post_order(self, root):
        if root:
            self.post_order(root.sim)
            self.post_order(root.nao)
            print(root.pergunta, end=" ")

    def interacao(self, root):
        if root is None:
            return

        if root.sim is None and root.nao is None:
            print("Você pensou em: " + root.pergunta)
            self.lista.inserir(root)
            opcao = input('Acertei ? (s/n):')
            opcao = opcao.lower()
            match opcao:
                case 's':
                    print("Agradeço por jogar!")
                case 'n':
                    resposta = input("No que você pensou ? ")
                    temp = root.id
                    self.remover(self.root, root.id)
                    self.inserir(self.root, temp, resposta)
            return

        resposta = input(root.pergunta + " (s/n): ")
        self.lista.inserir(root)

        if resposta.lower() == 's':
            if root.sim is not None:
                self.interacao(root.sim)
        elif resposta.lower() == 'n':
            if root.nao is not None:
                self.interacao(root.nao)
        else:
            print('Input inválido!')
            self.interacao(root)


def menu():
    akinator = Akinator()
    nos = [
        (4, "É um mamífero ?"), (2, "É um primata ?"), (1, "Macaco"),
        (3, "Cachorro"), (6, "É um réptil ?"), (5, "Lagarto"), (7, "Sapo")]
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
                    case _:
                        print("Opção inválida! Saindo do Menu de Debug!")
            case '3':
                print("Saindo...")
                break
            case _:
                print("Opção inválida")


if __name__ == "__main__":
    menu()