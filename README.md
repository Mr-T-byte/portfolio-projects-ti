estoque = {}  
def adicionar_item(nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f"Adicionado {quantidade} de {nome}. Estoque atual: {estoque[nome]}")

def remover_item(nome, quantidade):
    if nome in estoque and estoque[nome] >= quantidade:
        estoque[nome] -= quantidade
        print(f"Removido {quantidade} de {nome}. Estoque atual: {estoque[nome]}")
    else:
        print(f"Item {nome} não encontrado ou quantidade insuficiente.")

def listar_estoque():
    print("Estoque atual:")
    for item, qtd in estoque.items():
        print(f"- {item}: {qtd}")
    verificar_estoque_baixo()

def verificar_estoque_baixo(limite=5):
    baixos = [item for item, qtd in estoque.items() if qtd < limite]
    if baixos:
        print(f"Atenção: Itens com estoque baixo (< {limite}): {', '.join(baixos)}")

adicionar_item("Parafuso", 100)
adicionar_item("Óleo de Motor", 20)
remover_item("Parafuso", 10)
listar_estoque()
while True:
     opcao = input("Digite 'add', 'rem', 'list' ou 'sair': ")
     if opcao == 'add':
         nome = input("Nome do item: ")
         qtd = int(input("Quantidade: "))
         adicionar_item(nome, qtd)
     elif opcao == 'rem':
         nome = input("Nome do item: ")
         qtd = int(input("Quantidade: "))
         remover_item(nome, qtd)
     elif opcao == 'list':
         listar_estoque()
     elif opcao == 'sair':
         break
