import os
import re

# Caminho da pasta
PASTA = os.path.dirname(os.path.abspath(__file__))

for nome_arquivo in os.listdir(PASTA):
    caminho = os.path.join(PASTA, nome_arquivo)

    # Ignora pastas
    if not os.path.isfile(caminho):
        continue

    # Procura texto entre parênteses
    resultado = re.search(r"\((.*?)\)", nome_arquivo)

    if resultado:
        texto = resultado.group(1)

        # Lê o conteúdo do arquivo
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

        # Adiciona o comentário na primeira linha
        novo_conteudo = f"# {texto}\n{conteudo}"

        # Salva o arquivo
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(novo_conteudo)

        # Remove os parênteses do nome
        novo_nome = re.sub(r"\s*\(.*?\)", "", nome_arquivo)

        novo_caminho = os.path.join(PASTA, novo_nome)

        # Renomeia o arquivo
        os.rename(caminho, novo_caminho)

        print(f"Processado: {nome_arquivo} -> {novo_nome}")

print("Concluído!")