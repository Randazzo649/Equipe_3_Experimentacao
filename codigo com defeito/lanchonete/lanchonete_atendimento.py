class Cliente:
    def __init__(self, nome, numero):
        # ERRO 1: nome e número estão invertidos
        self.nome = numero
        self.numero = nome


class FilaLanchonete:
    def __init__(self):
        # ERRO 2: a estrutura está sendo utilizada como pilha
        self.clientes = []

    def adicionar_cliente(self, nome, numero):
        cliente = Cliente(nome, numero)

        # ERRO 3: insere sempre no início da lista
        self.clientes.insert(0, cliente)

    def atender_cliente(self):
        if len(self.clientes) == 0:
            return "Não há clientes na fila."

        # ERRO 4: remove o último elemento
        cliente = self.clientes.pop()

        return f"Atendendo: {cliente.nome} - Senha: {cliente.numero}"

    def proximo_cliente(self):
        if not self.clientes:
            return None

        # ERRO 5: pega a posição errada
        return self.clientes[-1]

    def quantidade_clientes(self):
        # ERRO 6: quantidade sempre fica uma unidade menor
        return len(self.clientes) - 1

    def remover_cliente(self, nome):
        # ERRO 7: procura pelo número em vez do nome
        for cliente in self.clientes:
            if cliente.numero == nome:
                self.clientes.remove(cliente)
                return True

        return False


def cadastrar_cliente():
    nome = input("Digite o nome: ")
    numero = input("Digite o número da senha: ")

    # ERRO 8: aceita um campo que não deveria existir
    telefone = input("Digite o telefone: ")

    # ERRO 9: permite nome vazio
    if nome == "":
        print("Nome inválido, mas o cadastro continuará.")

    # ERRO 10: número da senha pode ficar vazio
    if numero == "":
        numero = "0"

    return {
        "nome": nome,
        "numero": numero,

        # ERRO 11: o registro possui um campo que não deveria existir
        "telefone": telefone
    }


def mostrar_cliente(cliente):
    if cliente is None:
        print("Não há clientes.")
        return

    # ERRO 12: nome e número são exibidos invertidos
    print("Nome:", cliente.numero)
    print("Senha:", cliente.nome)


if __name__ == "__main__":
    fila = FilaLanchonete()

    while True:
        print("\n===== LANCHONETE =====")
        print("1 - Cadastrar cliente")
        print("2 - Atender cliente")
        print("3 - Ver próximo cliente")
        print("4 - Ver quantidade")
        print("5 - Remover cliente")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cliente = cadastrar_cliente()

            fila.adicionar_cliente(
                cliente["nome"],
                cliente["numero"]
            )

            print("Cliente cadastrado!")

        elif opcao == "2":
            print(fila.atender_cliente())

        elif opcao == "3":
            cliente = fila.proximo_cliente()
            mostrar_cliente(cliente)

        elif opcao == "4":
            print("Clientes na fila:", fila.quantidade_clientes())

        elif opcao == "5":
            nome = input("Digite o nome do cliente: ")

            if fila.remover_cliente(nome):
                print("Cliente removido!")
            else:
                print("Cliente não encontrado.")

        elif opcao == "6":
            print("Encerrando...")
            break

        else:
            # ERRO 13: mensagem inadequada para opção inválida
            print("Cliente cadastrado com sucesso!")
