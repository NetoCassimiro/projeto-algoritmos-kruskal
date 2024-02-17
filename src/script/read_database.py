# Abre o arquivo de base de dados localizado em "src/database/celegansneural.gml" e armazena em 'arq'
arq = open("src/database/celegansneural.gml")

# Lê todas as linhas do arquivo e armazena em 'lines'
lines = arq.readlines()

# Função responsável por extrair e formatar os dados, representando nós e arestas
def get_nodes_and_edges():
    # Listas para armazenar informações dos nós e arestas
    list_edges = []
    list_nodes = []

    # Loop para percorrer todas as linhas da base de dados e extrair informações de nós e arestas
    for i in range(len(lines)):
        # Tratamento da linha atual removendo espaços extras e dividindo em palavras
        current_line = lines[i]
        current_line = " ".join(current_line.split())
        current_line = current_line.split(' ')

        # Se a linha indica a presença de um nó na base de dados
        if current_line[0] == 'node':
            # Extrai o ID do nó, que está localizado 2 linhas abaixo da linha com a string "node"
            line_id = lines[i + 2]
            line_id = " ".join(line_id.split())
            value_id = int(line_id.split(' ')[1])
            
            # Extrai o rótulo (label) do nó, que está localizado 3 linhas abaixo da linha com a string "node"
            line_label = lines[i + 3]
            line_label = " ".join(line_label.split())
            value_label = line_label.split(' ')[1]
            value_label = value_label.replace('"', '')

            # Adiciona as informações do nó à lista de nós
            list_nodes.append({
                'id': str(value_id),
                'label': value_label,
            })

            # Pula 3 linhas para evitar a leitura de informações internas do nó adicionado
            i = i + 3

        # Se a linha indica a presença de uma aresta na base de dados
        if current_line[0] == 'edge':
            # Extrai a fonte (source) da aresta, localizada 2 linhas abaixo da linha com a string "edge"
            line_source = lines[i + 2]
            line_source = " ".join(line_source.split())
            value_source = int(line_source.split(' ')[1])

            # Extrai o destino (target) da aresta, localizado 3 linhas abaixo da linha com a string "edge"
            line_target = lines[i + 3]
            line_target = " ".join(line_target.split())
            value_target = int(line_target.split(' ')[1])

            # Extrai o peso (weight) da aresta, localizado 4 linhas abaixo da linha com a string "edge"
            line_weight = lines[i + 4]
            line_weight = " ".join(line_weight.split())
            value_weight = int(line_weight.split(' ')[1])

            # Adiciona as informações da aresta à lista de arestas
            list_edges.append((str(value_source), str(value_target), value_weight))

            # Pula 4 linhas para evitar a leitura de informações internas da aresta adicionada
            i = i + 4

    # Retorna a lista contendo informações dos nós e arestas
    return [list_nodes, list_edges]