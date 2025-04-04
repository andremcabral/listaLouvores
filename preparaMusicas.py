import os
# import time

# Caminho da pasta onde os arquivos TXT estão armazenados
caminho_origem = r"C:\ANDRE\LOUVORES"
# pasta_txt = caminho_origem

# Caminho da pasta onde os arquivos HTML serão salvos
caminho_destino = ""
pasta_html = (f".\\html\\{caminho_destino}")
# pasta_html = (f"{caminho_destino}\html")

# Caminho do arquivo de índice (será salvo fora da pasta_html)
# arquivo_indice = caminho_destino
arquivo_indice = pasta_html
# time.sleep(3)
# Função para ler o conteúdo dos arquivos .txt e processar os dados
catalogo={}
def processar_arquivo_txt(caminho_origem):
    with open(caminho_origem, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Dicionário para armazenar as informações
    informacoes = {
        "Título": "",
        "Artista": "",
        "Autor": "",
        "Tom": "",
        "BPM": "",
        "Tempo": ""
    }

    # Extraindo as informações do cabeçalho
    linhas = conteudo.split('\n')
    texto_principal = []
    for linha in linhas:
        if linha.startswith("Título:"):
            informacoes["Título"] = linha.replace("Título:", "").strip()
        elif linha.startswith("Artista:"):
            informacoes["Artista"] = linha.replace("Artista:", "").strip()
        elif linha.startswith("Autor:"):
            informacoes["Autor"] = linha.replace("Autor:", "").strip()
        elif linha.startswith("Tom:"):
            informacoes["Tom"] = linha.replace("Tom:", "").strip()
        elif linha.startswith("BPM:"):
            informacoes["BPM"] = linha.replace("BPM:", "").strip()
        elif linha.startswith("Tempo:"):
            informacoes["Tempo"] = linha.replace("Tempo:", "").strip()
        else:
            # O restante do texto
            texto_principal.append((linha.strip()).upper())
    catalogo[caminho_origem.split("\\")[3].split(".")[0]] = texto_principal

    if len(texto_principal)<5:
        print(caminho_origem.split("\\")[3].split(".")[0])
        # print(len(texto_principal), informacoes["Título"], sep="  >>  ")
        # print(texto_principal)
    return informacoes, "\n".join(texto_principal)

# Função para gerar o arquivo HTML
def gerar_html(nome_arquivo, informacoes, texto_principal):
    html_conteudo = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{informacoes['Título']}</title>
    <style>
        pre {{
            font-family: Verdana, Arial;
            margin: 10px;
        }}
        body {{
            font-family: Verdana;
            margin: 10px;            
            color: white;
            background-color: RGB(60,60,70);
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 10px;
        }}
        table, th, td {{
            border: 1px solid black;
        }}
        th, td {{
            padding: 4px;
            text-align: left;
        }}
    </style>
</head>
<body>
    <h1>{informacoes['Título']}</h1>
    <table>
        <tr><th width="100px">Título</th><td colspan=7>{informacoes['Título']}</td></tr>
        <tr><th width="100px">Artista</th><td>{informacoes['Artista']}</td>
            <th width="50px">Autor</th><td>{informacoes['Autor']}</td>
            <th width="50px">Tom</th><td>{informacoes['Tom']}</td>
            <th width="50px">BPM</th><td>{informacoes['BPM']}</td>
            <th width="50px">Tempo</th><td>{informacoes['Tempo']}</td>
        </tr>
    </table>
    <pre>{texto_principal}</pre>
</body>
</html>"""

    # Salvando o conteúdo HTML no arquivo
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(html_conteudo)
def gerar_html_resumo():
    html_conteudo = ''
    for item in catalogo:
        html_conteudo_novo = f"""<!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                pre {{
                    font-family: Verdana, Arial;
                    margin: 20px;
                }}
                body {{
                    font-family: Verdana;
                    margin: 20px;            
                    color: white;
                    background-color: RGB(60,60,70);
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-bottom: 20px;
                }}
                table, th, td {{
                    border: 1px solid black;
                }}
                th, td {{
                    padding: 8px;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <h1>{item}</h1>
            <pre>{catalogo[item]}</pre>
        </body>
        </html>"""
        html_conteudo = f"{html_conteudo}\n\n{html_conteudo_novo}"
    # Salvando o conteúdo HTML no arquivo
    with open("catalogo.html", 'w', encoding='utf-8') as f:
        f.write(html_conteudo)
    # print(item[0])

# Função para processar todos os arquivos TXT em uma pasta
def processar_pasta(caminho_origem, pasta_html):
    # Cria a pasta de saída se não existir
    # if not os.path.exists(pasta_html):
    #     os.makedirs(pasta_html)
    # Lista para armazenar os nomes dos arquivos HTML gerados
    arquivos_html = []
    for nome_arquivo in os.listdir(caminho_origem):
        if nome_arquivo.endswith(".txt"):
            caminho_arquivo = os.path.join(caminho_origem, nome_arquivo)
            informacoes, texto_principal = processar_arquivo_txt(caminho_arquivo)
            # print(len(texto_principal), nome_arquivo, sep="  >>  ")
            nome_html = os.path.splitext(nome_arquivo)[0] + ".html"
            caminho_html = os.path.join(pasta_html, nome_html)
            gerar_html(caminho_html, informacoes, texto_principal)
            arquivos_html.append(nome_html)
            # print(f"Arquivo HTML gerado: {caminho_html}")
    # Gerar o arquivo de índice
    gerar_indice(pasta_html, arquivos_html)
    gerar_html_resumo()

# Função para gerar o arquivo de índice HTML
def gerar_indice(pasta_html, arquivos_html):
    indice_conteudo = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Índice de Músicas</title>
    <style>
        .div-fixa {
            position: fixed; /* Faz a div ficar fixa */
            top: 0; /* Fixa no topo */
            left: 0; /* Alinha à esquerda */
            width: 100%; /* Ocupa a largura toda da página */
            background-color: darkgray; /* Cor de fundo */
            # color: white; /* Cor do texto */
            padding: 10px; /* Espaçamento interno */
            z-index: 1000; /* Garante que fique acima de outros elementos */
        }        
        .conteudo {
            margin-top: 5px; /* O conteúdo começa abaixo da div fixa */
            # background: linear-gradient(to bottom, #f0f0f0, #dcdcdc);
        }
        iframe {
            width: 90%;
            height: 1000px;
            border: none;
            margin-top: 0px;
            color: red;
            background-color: lightgray;
            display: none; /* Inicialmente escondido */
        }
        body {
            font-family: Verdana;
            color: white;
            background-color: black;
            padding-top: 5px; /* Ajuste para o conteúdo não ficar escondido por baixo */
            padding-botton: 10px
        }

        ul {
            list-style-type: none;
        }
        li {
            margin: 10px 0;
        }
        a {
            text-decoration: none;
            color: white;
            text-transform: uppercase;
        }
        #search-box {
            margin-bottom: 10px;
            margin-left: 30px;
            padding: 10px;
            font-size: 18px;
            width: 80%;
        }
    </style>
</head>
<body>
<!--<div class="div-fixa">-->
<!--&lt;!&ndash;<h1 align="center">Índice de Músicas Cadastradas</h1>&ndash;&gt;-->
<!--&lt;!&ndash;<div width="60%">&ndash;&gt;-->
<!--    -->
<!--&lt;!&ndash;    <br>&ndash;&gt;-->
<!--&lt;!&ndash;    Clique no nome para abrir a letra abaixo ou no '>>>' para abrir em nova aba&ndash;&gt;-->
<!--</div>-->
<div class="conteudo">
<input type="text" id="search-box" placeholder="Digite o nome para buscar..." onkeyup="searchList()">
    <ul id="music-list">"""
    for index, arquivo in enumerate(arquivos_html):
        indice_conteudo += f'<li>{index+1} - <a href="html\\{arquivo}" target="_blank"> >>> </a>'
        indice_conteudo += f"""<a href="javascript:void(0);" onclick="toggleIframe('html/{arquivo}', this)"> {arquivo.split(".html")[0]} </a></li>"""
    indice_conteudo += '<li>//-//</li>'"""
</ul>
</div>
<script>
    // Função de busca
    function searchList() {
        // Obtém o valor do campo de busca
        var query = document.getElementById('search-box').value.toUpperCase(); // Converter para maiúsculo

        // Obtém a lista de músicas (corrigir ID de 'music-list' caso esteja correto)
        var listItems = document.getElementById('music-list').getElementsByTagName('li'); // Lista de itens (musicas)

        // Percorre os itens da lista e verifica se o texto do item contém a busca
        for (var i = 0; i < listItems.length; i++) {
            var itemText = listItems[i].textContent || listItems[i].innerText; // Obtém o texto do item

            // Verifica se o item contém o texto da busca (usando toUpperCase para ignorar diferenças de maiúsculas/minúsculas)
            if (itemText.toUpperCase().includes(query)) { // Verifica se o texto do item contém a busca
                listItems[i].style.display = ''; // Exibe o item
            } else {
                listItems[i].style.display = 'none'; // Esconde o item
            }
        }
    }


    function toggleIframe(fileName, linkElement) {
        // Verifica se já existe um iframe abaixo do link
        var existingIframe = linkElement.nextElementSibling;

        // Se já existir um iframe
        if (existingIframe && existingIframe.tagName === 'IFRAME') {
            // Verifica se o iframe já está visível
            if (existingIframe.style.display === 'block') {
                // Se o iframe já estiver visível, oculta-o
                existingIframe.style.display = 'none'; // Esconde o iframe
            } else {
                // Se o iframe não estiver visível, exibe-o novamente
                existingIframe.style.display = 'block'; // Exibe o iframe
            }
        } else {
            // Se não houver um iframe, cria um novo iframe e adiciona abaixo do link
            var iframe = document.createElement('iframe');
            iframe.src = fileName;
            iframe.style.display = 'block'; // Exibe o iframe
            linkElement.parentElement.appendChild(iframe); // Adiciona o iframe abaixo do link
        }
    }
</script>
</body>
</html>"""

    # Salvando o arquivo de índice
    caminho_indice = os.path.join(caminho_destino, "index.html")
    with open(caminho_indice, 'w', encoding='utf-8') as f:
        f.write(indice_conteudo)

    print(f"Arquivo de índice gerado: {caminho_indice}")

# Caminho da pasta onde os arquivos TXT estão armazenados e a pasta de saída para os arquivos HTML
# pasta_txt = "caminho/para/sua/pasta_txt"
# pasta_html = "caminho/para/sua/pasta_html"

# Processar todos os arquivos na pasta
processar_pasta(caminho_origem, pasta_html)
