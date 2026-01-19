# Backup Automatizado de Arquivos - Versão Interativa
# Autor: adaptado/melhorado
# Data: Janeiro/2026

import shutil
import os
import datetime
from pathlib import Path


def limpar_nome_arquivo(nome):
    """Remove caracteres problemáticos para nomes de pasta"""
    proibidos = '<>:"/\\|?*'
    for char in proibidos:
        nome = nome.replace(char, '_')
    return nome.strip()


def escolher_arquivos_e_pastas(origem_base):
    """Permite ao usuário selecionar arquivos e pastas para backup"""
    print("\n" + "═" * 60)
    print("   SELECIONE O QUE DESEJA FAZER BACKUP   ")
    print("═" * 60)
    
    itens = []
    for item in sorted(os.listdir(origem_base)):
        caminho_completo = os.path.join(origem_base, item)
        if os.path.isfile(caminho_completo):
            tipo = "ARQUIVO"
        elif os.path.isdir(caminho_completo):
            tipo = "PASTA "
        else:
            continue
            
        print(f"  [{len(itens)+1:2d}]  {tipo}  →  {item}")
        itens.append(caminho_completo)
    
    print("\nDigite os números dos itens que deseja incluir (separados por espaço)")
    print("Exemplos:")
    print("  1 3 5         → só os itens 1, 3 e 5")
    print("  1-5           → itens de 1 até 5")
    print("  all           → tudo")
    print("  Enter vazio   → nada (sair)")
    
    selecao = input("\nSua escolha: ").strip().lower()
    
    if not selecao or selecao == "0":
        print("Nenhum item selecionado. Backup cancelado.")
        return []
    
    if selecao == "all":
        return itens
    
    escolhidos = []
    partes = selecao.replace(",", " ").split()
    
    for parte in partes:
        if '-' in parte:
            try:
                inicio, fim = map(int, parte.split('-'))
                for i in range(inicio-1, min(fim, len(itens))):
                    escolhidos.append(itens[i])
            except:
                print(f"Ignorando intervalo inválido: {parte}")
        else:
            try:
                idx = int(parte) - 1
                if 0 <= idx < len(itens):
                    escolhidos.append(itens[idx])
                else:
                    print(f"Número fora do intervalo: {parte}")
            except:
                print(f"Ignorando entrada inválida: {parte}")
    
    return list(set(escolhidos))  # remove duplicatas


def fazer_backup_interativo():
    print("\n" + "═" * 70)
    print("       BACKUP AUTOMATIZADO - Versão Interativa 2026       ")
    print("═" * 70)
    
    # 1. Pasta de origem
    while True:
        origem = input("\nPasta que deseja fazer backup (Enter = pasta atual): ").strip()
        if not origem:
            origem = os.getcwd()
        
        origem = os.path.abspath(origem)
        
        if not os.path.exists(origem):
            print("→ Pasta não encontrada. Tente novamente.")
            continue
        if not os.path.isdir(origem):
            print("→ O caminho informado não é uma pasta.")
            continue
        break
    
    print(f"\nPasta de origem selecionada: {origem}")
    
    # 2. Seleção dos arquivos/pastas
    itens_para_backup = escolher_arquivos_e_pastas(origem)
    
    if not itens_para_backup:
        print("\nNenhum arquivo/pasta selecionado. Operação cancelada.\n")
        return
    
    # 3. Pasta de destino
    destino_padrao = os.path.join(os.path.expanduser("~"), "Backups")
    destino = input(f"\nPasta onde salvar os backups (Enter = {destino_padrao}): ").strip()
    
    if not destino:
        destino = destino_padrao
    
    destino = os.path.abspath(destino)
    os.makedirs(destino, exist_ok=True)
    
    # 4. Criar pasta com data/hora
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d_%Hh%M")
    nome_backup = f"Backup_{data_hora}"
    pasta_backup = os.path.join(destino, nome_backup)
    os.makedirs(pasta_backup, exist_ok=True)
    
    print(f"\nCriando backup em: {pasta_backup}")
    print("Itens sendo copiados...")
    
    contador = 0
    for item in itens_para_backup:
        nome_item = os.path.basename(item)
        destino_item = os.path.join(pasta_backup, nome_item)
        
        try:
            if os.path.isfile(item):
                shutil.copy2(item, destino_item)
                print(f"  ✓  {nome_item}")
                contador += 1
            elif os.path.isdir(item):
                shutil.copytree(item, destino_item, dirs_exist_ok=True)
                print(f"  ✓  {nome_item}/  (pasta completa)")
                contador += 1
        except Exception as e:
            print(f"  ✗  Erro ao copiar {nome_item}: {e}")
    
    print("\n" + "═" * 60)
    print(f"BACKUP FINALIZADO! {contador} itens copiados com sucesso")
    print(f"Local: {pasta_backup}")
    print("═" * 60 + "\n")


if __name__ == "__main__":
    try:
        while True:
            fazer_backup_interativo()
            
            novamente = input("\nDeseja fazer outro backup? (s/n): ").strip().lower()
            if novamente not in ['s', 'sim', 'y']:
                print("\nObrigado por usar o Backup Interativo! Até a próxima! 🚀\n")
                break
                
            print("\n" + "─" * 70 + "\n")
            
    except KeyboardInterrupt:
        print("\nPrograma interrompido. Seus arquivos estão seguros! 😊")