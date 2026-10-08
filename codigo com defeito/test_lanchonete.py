from lanchonete_atendimento import Cliente, FilaLanchonete

def test_cadastro_cliente():
    cliente = Cliente("João", 15)

    assert cliente.nome == "João"
    assert cliente.numero == 15

def test_ordem_da_fila():
    fila = FilaLanchonete()

    fila.adicionar_cliente("João", 1)
    fila.adicionar_cliente("Maria", 2)
    fila.adicionar_cliente("Pedro", 3)

    assert fila.atender_cliente() == "Atendendo: João - Senha: 1"
    assert fila.atender_cliente() == "Atendendo: Maria - Senha: 2"
    assert fila.atender_cliente() == "Atendendo: Pedro - Senha: 3"

def test_proximo_cliente():
    fila = FilaLanchonete()

    fila.adicionar_cliente("João", 1)
    fila.adicionar_cliente("Maria", 2)

    cliente = fila.proximo_cliente()

    assert cliente.nome == "João"
    assert cliente.numero == 1

def test_atendimento_remove_apenas_primeiro():
    fila = FilaLanchonete()

    fila.adicionar_cliente("João", 1)
    fila.adicionar_cliente("Maria", 2)
    fila.adicionar_cliente("Pedro", 3)

    fila.atender_cliente()

    assert fila.proximo_cliente().nome == "Maria"
    assert fila.quantidade_clientes() == 2

def test_quantidade_clientes():
    fila = FilaLanchonete()

    assert fila.quantidade_clientes() == 0

    fila.adicionar_cliente("João", 1)
    assert fila.quantidade_clientes() == 1

    fila.adicionar_cliente("Maria", 2)
    assert fila.quantidade_clientes() == 2

    fila.atender_cliente()
    assert fila.quantidade_clientes() == 1

def test_fila_vazia():
    fila = FilaLanchonete()

    assert fila.atender_cliente() == "Não há clientes na fila."


def test_proximo_cliente_fila_vazia():
    fila = FilaLanchonete()

    assert fila.proximo_cliente() is None


def test_fila_com_varios_clientes():
    fila = FilaLanchonete()

    clientes = [
        ("João", 1),
        ("Maria", 2),
        ("Pedro", 3),
        ("Ana", 4),
        ("Carlos", 5)
    ]

    for nome, numero in clientes:
        fila.adicionar_cliente(nome, numero)

    for nome, numero in clientes:
        assert fila.atender_cliente() == f"Atendendo: {nome} - Senha: {numero}"