letrasCadastradas = {}
# Abre o arquivo em modo leitura e gravação
with open('C:\ANDRE\CASA\letras.txt', 'r', encoding = 'UTF-8') as arquivo:
    # Lê o conteúdo do arquivo
    conteudo = arquivo.read()
# # Substitui os caracteres desejados
# # conteudo = conteudo.replace('\n', '')
# # # Abre o arquivo novamente, desta vez para sobrescrever o conteúdo
# with open('arquivo2.txt', 'w') as file:
#     # Escreve o conteúdo alterado no arquivo
#     file.write(conteudo)
# print('************************************************************************************************************')
# with open('arquivo2.txt', 'r', encoding = 'windows-1252') as arquivo:
#     conteudo = arquivo.readlines()

# print(conteudo)

# Inicializa o dicionário
musicas = {}

# Separa o conteúdo por "================================================================================================================================"
blocos = conteudo.split(
    "\n================================================================================================================================\n")

# Itera sobre cada bloco e cria o dicionário
for bloco in blocos:
    linhas = bloco.strip().split('\n')
    titulo = ""
    artista = ""
    letra = []

    for linha in linhas:
        if linha.startswith("Título:"):
            titulo = linha.replace("Título: ", "").strip()
        elif linha.startswith("Artista:"):
            artista = linha.replace("Artista: ", "").strip()
        else:
            letra.append(linha.strip())

    # Adiciona ao dicionário
    if titulo and artista:
        musicas[titulo] = {
            'Artista': artista,
            'Letra': '\n'.join(letra)
        }

# Exibe o dicionário resultante
print(musicas.keys())
for chave in musicas.keys():
    print(chave)
    print(musicas[chave]['Artista'])
    print(musicas[chave]['Letra'])
    musicas[chave]


def salvar_como_html(titulo, artista, letra):
    # Cria o conteúdo HTML
    html_conteudo = f"""
    <html>
    <head>
        <title>{titulo}</title>
    </head>
    <body>
        <h1>{titulo}</h1>
        <h2>Artista: {artista}</h2>
        <pre>{letra}</pre>
    </body>
    </html>
    """

    # Salva o conteúdo em um arquivo HTML com o nome do título
    titulo = titulo.replace("/", "__")
    titulo = titulo.replace("?", "___")
    nome_arquivo = f"{titulo}.html"
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write(html_conteudo)


# Itera sobre o dicionário e salva cada item como um arquivo HTML
for titulo, info in musicas.items():
    salvar_como_html(titulo, info['Artista'], info['Letra'])

print("Arquivos HTML salvos com sucesso!")


# titulo = ''
# for linha in conteudo:
#     # print(f'LINHA: {linha}')
#     linha = linha.replace('\n','')
#     # print(f'LINHA2: {linha}')
#     if '================================================================================================================================' in linha:
#         pass
#     else:
#         if 'Título' in linha:
#             # print(f'LINHA COM TÍTULO: {linha}')
#             titulo = linha.split('Título: ')[1].replace("\n","")
#             # print(f'TITULO: {titulo}')
#             if titulo in letrasCadastradas:
#                 print('titulo existe')
#                 letrasCadastradas[titulo].append(' + ')
#                 # print('teste 1')
#                 # print(f'TAMANHO DA LINHA: {len(letrasCadastradas[titulo])}')
#                 # print(f'TIPO DA LINHA: {type(letrasCadastradas[titulo])}')
#                 # print(f'TITULO: {titulo}')
#                 # print(f'LINHA: {linha.split("Título: ")[1]}')
#                 # letrasCadastradas[titulo] = letrasCadastradas[titulo].append(linha)
#             # print(linha.split('Título: ')[1].replace("\n",""))
#             else:
#                 print('titulo NÃO existe')
#                 letrasCadastradas[titulo]=f"ok para {titulo}"
#                 # print('teste 2')
#                 # letrasCadastradas[titulo]=linha
#                 # print(f'TAMANHO DA LINHA: {len(letrasCadastradas[titulo])}')
#                 # print(f'TIPO DA LINHA: {type(letrasCadastradas[titulo])}')
#                 # print(f'TITULO: {titulo}')
#                 # print(f'LINHA: {linha.split("Título: ")[1]}')
#
#     #     # letrasCadastradas[linha.split("Título: ")[1].replace("\n","")].append(linha)
#     #     # Se a chave existir, adiciona uma linha
#     #     if linha.split('Título: ')[1].replace("\n","") in letrasCadastradas:
#     #         letrasCadastradas[linha.split('Título: ')[1].replace("\n","")].append(linha)
#     #     else:
#     #         # Caso contrário, cria uma nova chave com o dado
#     #         letrasCadastradas[linha.split('Título: ')[1].replace("\n","")] = [linha]
#     # else:
#     #     # Se a chave não existir, cria uma nova chave
#     #     if linha.split('Título: ')[1].replace("\n","") not in letrasCadastradas:
#     #         letrasCadastradas[linha.split('Título: ')[1].replace("\n","")] = [linha.split('Título: ')[1].replace("\n","")]
#
#
# # for linha in letrasCadastradas:
# #     print(linha)
# print(letrasCadastradas.keys())
# print(letrasCadastradas.values())