# Gerenciador de Estoque Simples
# Autor: Luiz Augusto Elias Souza Sacramento
# Inspirado na experiência no Varejão Auto Peças
# Gerenciador de Estoque Simples
# Todas as funções + menu interativo

estoque = {}  # chave = nome do item, valor = quantidade

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
        print(f"Item '{nome}' não encontrado ou quantidade insuficiente.")

def listar_estoque():
    if not estoque:
        print("O estoque está vazio no momento.")
        return
        
    print("\nEstoque atual:")
    for item, qtd in sorted(estoque.items()):
        print(f"  • {item}: {qtd}")
    verificar_estoque_baixo()

def verificar_estoque_baixo(limite=5):
    baixos = [item for item, qtd in estoque.items() if qtd < limite]
    if baixos:
        print(f"\n⚠️ Atenção - Estoque baixo (< {limite} unidades):")
        print("  " + ", ".join(baixos))

def menu():
    while True:
        print("\n" + "═"*40)
        print("         GERENCIADOR DE ESTOQUE")
        print("═"*40)
        print("  1  →  Adicionar itens")
        print("  2  →  Remover itens")
        print("  3  →  Ver estoque completo")
        print("  4  →  Sair")
        print("═"*40)
        
        opcao = input("Digite sua opção (1-4): ").strip()
        
        if opcao == "1":
            nome = input("Nome do item: ").strip()
            while True:
                try:
                    qtd = int(input("Quantidade a adicionar: "))
                    if qtd <= 0:
                        print("A quantidade deve ser positiva!")
                        continue
                    break
                except ValueError:
                    print("Digite apenas números inteiros!")
            adicionar_item(nome, qtd)
            
        elif opcao == "2":
            nome = input("Nome do item: ").strip()
            while True:
                try:
                    qtd = int(input("Quantidade a remover: "))
                    if qtd <= 0:
                        print("A quantidade deve ser positiva!")
                        continue
                    break
                except ValueError:
                    print("Digite apenas números inteiros!")
            remover_item(nome, qtd)
            
        elif opcao == "3":
            listar_estoque()
            
        elif opcao == "4":
            print("\nPrograma encerrado. Até a próxima!")
            break
            
        else:
            print("Opção inválida! Digite 1, 2, 3 ou 4.")

# Início do programa
if __name__ == "__main__":
    print("Bem-vindo ao Gerenciador de Estoque!")
    menu()