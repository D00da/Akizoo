class No:
    def __init__(self, id, pergunta, sim=None, nao=None):
        self.id = id
        self.pergunta = pergunta
        self.altura = 1
        self.sim = sim  # Esquerda
        self.nao = nao  # Direita
        self.anterior = None
        self.proximo = None

class Interacao:
    def __init__(self, tipo):
        self.tipo = tipo
        self.proximo = None
        self.anterior = None

#Armazenar tentativas de adivinhação
class Tentativas:
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

#Armazenar as interações em tempo real
class Interacoes:
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
            print(atual.tipo)
            atual = atual.proximo

class Akinator:
    def __init__(self):
        self.root = None
        tentativas = Tentativas()
        self.tentativas = tentativas
        interacoes = Interacoes()
        self.interacoes = interacoes

    def inserir(self, root, id, pergunta):
        if root is None:
            return No(id, pergunta)

        if id < root.id:
            root.sim = self.inserir(root.sim, id, pergunta)
        else:
            root.nao = self.inserir(root.nao, id, pergunta)

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

    def pre_order(self, root, nivel=0):
        if root:
            print(" " * (nivel * 4) + f"{root.id},{root.pergunta}")
            self.pre_order(root.sim, nivel + 1)
            self.pre_order(root.nao, nivel + 1)

    def in_order(self, root, nivel=0):
        if root:
            self.in_order(root.sim, nivel + 1)
            print(" " * (nivel * 4) + f"{root.id},{root.pergunta}")
            self.in_order(root.nao, nivel + 1)

    def post_order(self, root, nivel=0):
        if root:
            self.post_order(root.sim, nivel + 1)
            self.post_order(root.nao, nivel + 1)
            print(" " * (nivel * 4) + f"{root.id},{root.pergunta}")

    def userInput(self, root):
        if root is None:
            return

        if root.sim is None and root.nao is None:
            print("Você pensou em: " + root.pergunta)
            self.tentativas.inserir(root)
            opcao = input('Acertei ? (s/n): ')
            opcao = opcao.lower()
            match opcao:
                case 's':
                    print("Agradeço por jogar!")
                    self.interacoes.inserir(Interacao("Sim"))
                case 'n':
                    resposta = input("No que você pensou ? ")
                    self.interacoes.inserir(Interacao("Não"))
                    temp = root.id
                    self.remover(self.root, root.id)
                    self.inserir(self.root, temp, resposta)
            return

        resposta = input(root.pergunta + " (s/n): ")
        self.tentativas.inserir(root)

        if resposta.lower() == 's':
            self.interacoes.inserir(Interacao("Sim"))
            if root.sim is not None:
                self.userInput(root.sim)
        elif resposta.lower() == 'n':
            self.interacoes.inserir(Interacao("Não"))
            if root.nao is not None:
                self.userInput(root.nao)
        else:
            print('Input inválido!')
            self.userInput(root)