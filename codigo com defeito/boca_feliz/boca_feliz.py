estoque = {
    'pao': 10,
    'hamburguer': 12,
    'tomate': 5,
    'bacon': 5,
    'ovo': 5
}

cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}


def verificar_estoque(ingredientes):
    disponivel = True

    for ingrediente in set(ingredientes):
        if estoque.get(ingrediente, 0) < 1:
            print(f"Infelizmente acabou o {ingrediente}")
            disponivel = False

    return disponivel


def atualizar_estoque(ingredientes):
    for ingrediente in ingredientes:
        estoque[ingrediente] -= 1


def realizar_pedido(pedido):
    if pedido not in cardapio:
        print("Item não localizado no cardápio")

    ingredientes = cardapio.get(pedido, [])

    atualizar_estoque(ingredientes)

    if verificar_estoque(ingredientes):
        print(f"um {pedido} saindo no capricho!!!")


def main():
    while True:
        print("\n===== CARDÁPIO BOCA FELIZ =====")

        for produto in cardapio:
            print(produto)

        pedido = input("\nO que deseja pedir (0 para sair)? ")

        if pedido == '0':
            print("Encerrando o sistema...")
            break

        realizar_pedido(pedido)


if _name_ == "_main_":
    main()