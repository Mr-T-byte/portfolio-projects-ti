import os
import shutil
from pathlib import Path

def organizar_arquivos(diretorio):
    diretorio = Path(diretorio).resolve()  # transforma em caminho absoluto e resolve
    
    if not diretorio.exists():
        print(f"Erro: O diretório '{diretorio}' não existe.")
        return False
    if not diretorio.is_dir():
        print(f"Erro: '{diretorio}' não é um diretório.")
        return False

    # Definição das categorias (você pode adicionar mais!)
    categorias = {
        "Imagens":       [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff"],
        "Documentos":    [".pdf", ".doc", ".docx", ".odt", ".txt", ".rtf", ".md"],
        "Planilhas":     [".xls", ".xlsx", ".ods", ".csv"],
        "Apresentações": [".ppt", ".pptx", ".odp"],
        "Vídeos":        [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
        "Áudios":        [".mp3", ".wav", ".flac", ".m4a", ".ogg"],
        "Código":        [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php", ".sql"],
        "Compactados":   [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
        "Executáveis":   [".exe", ".msi", ".apk", ".bat", ".sh"],
        "Outros":        []   # pega tudo que não se encaixou
    }

    print(f"\nOrganizando arquivos em: {diretorio}")
    print("-" * 60)

    arquivos_movidos = 0
    por_categoria = {cat: 0 for cat in categorias}

    for item in diretorio.iterdir():
        if item.is_file():
            extensao = item.suffix.lower()
            movido = False

            for categoria, extensoes in categorias.items():
                if extensao in extensoes or (categoria == "Outros" and not movido):
                    pasta_destino = diretorio / categoria
                    pasta_destino.mkdir(exist_ok=True)

                    destino_final = pasta_destino / item.name
                    
                    # Evitar sobrescrever arquivo com mesmo nome
                    contador = 1
                    while destino_final.exists():
                        nome, ext = item.stem, item.suffix
                        destino_final = pasta_destino / f"{nome} ({contador}){ext}"
                        contador += 1

                    try:
                        shutil.move(str(item), str(destino_final))
                        print(f"Movido: {item.name:.<45} → {categoria}")
                        arquivos_movidos += 1
                        por_categoria[categoria] += 1
                        movido = True
                    except Exception as e:
                        print(f"Erro ao mover {item.name}: {e}")
                    break

    print("-" * 60)
    print(f"\nOrganização concluída!")
    print(f"Total de arquivos movidos: {arquivos_movidos}")

    if arquivos_movidos > 0:
        print("\nResumo por categoria:")
        for cat, qtd in por_categoria.items():
            if qtd > 0:
                print(f"  {cat:.<15} {qtd:3d} arquivo(s)")
    
    return True


def main():
    print("=== Organizador de Arquivos por Tipo ===\n")
    
    while True:
        print("Opções:")
        print("  1 - Organizar pasta atual (.)")
        print("  2 - Escolher outra pasta")
        print("  3 - Sair")
        
        escolha = input("\nDigite sua opção (1-3): ").strip()
        
        if escolha == "1":
            print()
            organizar_arquivos(".")
            
        elif escolha == "2":
            caminho = input("Digite o caminho da pasta (ou Enter para cancelar): ").strip()
            if caminho:
                print()
                organizar_arquivos(caminho)
            else:
                print("Operação cancelada.\n")
                
        elif escolha == "3":
            print("\nAté mais! 👋\n")
            break
            
        else:
            print("Opção inválida. Tente novamente.\n")
        
        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário. Até mais!")