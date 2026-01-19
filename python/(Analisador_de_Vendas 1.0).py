# Analisador de Vendas em CSV - Versão Amigável 2026
# Autor: Luiz Augusto Elias Souza Sacramento (adaptado/melhorado)
# Data: Janeiro/2026

import csv
import os
from collections import defaultdict


def limpar_valor(texto):
    """Converte valores brasileiros (com vírgula) para float"""
    if not texto:
        return 0.0
    texto = texto.strip()
    texto = texto.replace("R$", "").replace(" ", "")
    texto = texto.replace(".", "").replace(",", ".")
    try:
        return float(texto)
    except ValueError:
        return None


def analisar_vendas_modo_facil():
    print("\n" + "="*60)
    print("   ANALISADOR DE VENDAS - MODO FÁCIL (para iniciantes)   ")
    print("="*60 + "\n")

    while True:
        arquivo = input("Digite o nome do arquivo CSV (ex: vendas.csv): ").strip()

        # Tenta ajudar com a extensão
        if not arquivo.lower().endswith('.csv'):
            if os.path.exists(arquivo + '.csv'):
                arquivo += '.csv'
                print(f"→ Usando arquivo: {arquivo}")
            elif os.path.exists(arquivo):
                print(f"→ Usando arquivo: {arquivo}")
            else:
                print("Arquivo não encontrado. Tente novamente.\n")
                continue

        if not os.path.exists(arquivo):
            print(f"❌ Arquivo '{arquivo}' não encontrado!\n")
            continue

        break

    vendas = defaultdict(float)
    linhas_validas = 0
    linhas_com_erro = 0

    print("\nLendo o arquivo...")

    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            leitor = csv.reader(f)
            
            try:
                cabecalho = next(leitor)
                print("\nCabeçalho encontrado:", ", ".join(cabecalho))
                print("→ Considerando: Coluna 1 = Produto | Coluna 2 = Valor\n")
            except:
                print("Não foi possível ler o cabeçalho :(")
                cabecalho = ["Produto", "Valor"]

            for linha in leitor:
                if len(linha) < 2:
                    linhas_com_erro += 1
                    continue

                produto = linha[0].strip()
                valor_str = linha[1].strip()

                valor = limpar_valor(valor_str)

                if valor is None:
                    linhas_com_erro += 1
                    continue

                vendas[produto] += valor
                linhas_validas += 1

    except Exception as e:
        print(f"\n❌ Erro ao abrir o arquivo: {e}")
        return

    if linhas_validas == 0:
        print("\nNenhuma venda válida foi encontrada no arquivo :(")
        return

    # Ordena do maior para o menor os valores
    vendas_ordenadas = sorted(vendas.items(), key=lambda x: x[1], reverse=True)

    total = sum(vendas.values())

    print("\n" + "="*60)
    print(f"       RESULTADO - {linhas_validas} vendas processadas       ")
    print("="*60)

    print(f"\nTotal Geral de Vendas:  R$ {total:12,.2f}")
    print("-"*60)

    for produto, valor in vendas_ordenadas:
        print(f"{produto:.<45} R$ {valor:12,.2f}")

    print("-"*60)

    if linhas_com_erro > 0:
        print(f"\nAtenção: {linhas_com_erro} linhas tiveram problemas e foram ignoradas")

    print("\nBoa análise! 🚀\n")


def analisar_vendas_modo_avancado():
    print("\nModo avançado selecionado (mais opções em breve... por enquanto usa o mesmo analisador)")
    analisar_vendas_modo_facil()


def main():
    print("="*70)
    print("        ANALISADOR DE VENDAS EM CSV - 2026        ")
    print("="*70)

    while True:
        print("\nQual modo você prefere?")
        print("  1 - Modo FÁCIL     (recomendado para iniciantes)")
        print("  2 - Modo AVANÇADO  (para usuários mais experientes)")
        print("  0 - Sair\n")

        opcao = input("Escolha (1/2/0): ").strip()

        if opcao == "1":
            analisar_vendas_modo_facil()
        elif opcao == "2":
            analisar_vendas_modo_avancado()
        elif opcao in ["0", "sair", "exit", "q"]:
            print("\nAté a próxima análise! 👋\n")
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 0.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma encerrado pelo usuário. Até mais! 😊")