# ⏱️📖 Desafio Da Sprint 3 📖⏱️

## Sumario 🔍🔍

- Nas pastas nomeadas com o nome "desafio" seguido de um número contem os modulos que guardam as funções do desafio.
- Em "manipulando_csv.py" estão as funções que abrem o csv usando scripts python para escrita e leitura.
- Em "realizando_etl" está o gatilho para executar as funções.
- Em "csv" está o arquivo csv selecionado para leitura.
- Em "etapas_txt" estão os arquivos txt que guardam as informações.

# Ator com Maior Número de Filmes

Este é um projeto Python simples que demonstra como encontrar o ator com o maior número de filmes em um conjunto de dados CSV.

## Como Usar

1. Certifique-se de ter Python instalado no seu sistema.

2. Clone o repositório:

   ```bash
   git clone git@github.com:CSetChip/da-lins.git

## Desafio 1 - funcoes_d1.py

O código contém as seguintes funcionalidades:

- `ator_com_maior_numero_de_filmes(filmes_dos_autores, nome_ator, numero_filmes)`: Uma função que recebe uma lista de atores e o número de filmes que eles fizeram e retorna o nome do ator com o maior número de filmes.

- `tratar_lista_filme_dos_atores(csv_dados, coluna_atores, coluna_filme)`: Uma função que lê um arquivo CSV contendo informações sobre atores e filmes, extrai os dados relevantes e retorna uma lista de atores e o número de filmes que eles fizeram.

- `execucao_d1()`: Função principal que utiliza as funções acima para encontrar o ator com o maior número de filmes e escrever o resultado em um arquivo de saída.

## Desafio 2 - funcoes_d2.py


O código contém as seguintes funcionalidades:

- `formatar_media(list_gross)`: Uma função que recebe uma lista de valores, calcula a média e a formata de acordo com o padrão especificado. Neste caso, a média é formatada para conter duas casas decimais e os pontos são removidos para que o resultado esteja no formato "XX.XX".

- `execucao_d2()`: Função principal que utiliza a função `formatar_media` para calcular e formatar a média de uma coluna específica de um arquivo CSV. O resultado é escrito em um arquivo de saída.

## Desafio 3 - funcoes_d3.py

O código contém as seguintes funcionalidades:

- `calculando_media_ator(data_lines, coluna_actor, coluna_media_por_filme)`: Uma função que recebe os dados do CSV, o índice da coluna do ator e o índice da coluna da média de receita por filme. Ele calcula a média da receita bruta por filme para cada ator, identifica o ator com a maior média e formata a média para remover decimais e pontos.

- `execucao_d3()`: Função principal que utiliza a função `calculando_media_ator` para calcular e formatar a média da receita bruta por filme dos atores. O ator com a maior média é identificado e o resultado é escrito em um arquivo de saída.

## Desafio 4 - funcoes_d4.py

O código contém as seguintes funcionalidades:

- `contagem_de_filmes(data_lines, coluna_actor)`: Uma função que recebe os dados do CSV e o índice da coluna do ator (#1 Movie). Ela conta quantas vezes cada filme de maior bilheteria aparece no conjunto de dados e retorna os resultados ordenados em ordem decrescente.

- `execucao_d4()`: Função principal que utiliza a função `contagem_de_filmes` para contar e ordenar os filmes por número de aparições. Os resultados são escritos em um arquivo de saída.

## Desafio 5 - funcoes_d5.py

O código contém as seguintes funcionalidades:

- `tratando_lista_receita_atores(colunas, data_lines)`: Uma função que recebe as colunas e os dados do CSV e extrai os nomes dos atores e suas receitas brutas dos filmes. Os resultados são ordenados em ordem decrescente de receita bruta.

- `execucao_d5()`: Função principal que utiliza a função `tratando_lista_receita_atores` para classificar os atores com base na receita bruta. Os resultados são escritos em um arquivo de saída.

## manipulando_csv

O código contém as seguintes funções:

- `abrir_csv(nome_csv)`

Esta função recebe o nome de um arquivo CSV como entrada, lê o arquivo e retorna três valores:
- `csv_dados`: Uma lista de listas contendo os dados do CSV.
- `colunas`: Uma lista com o nome das colunas do CSV.
- `data_lines`: Uma lista de listas contendo apenas as linhas de dados (excluindo o cabeçalho).

- `escrever_csv(nome_csv, texto)`: Esta função recebe o nome de um arquivo CSV e um texto como entrada, e escreve o texto no arquivo especificado.

- `escrever_csv_lista_para_d4(nome_csv, lista)`: Esta função recebe o nome de um arquivo CSV e uma lista de tuplas como entrada, onde cada tupla contém informações sobre filmes e contagem. Ela escreve os resultados no arquivo CSV com um padrão específico.

- `escrever_lista_csv_para_d5(nome_csv, lista)`: Esta função recebe o nome de um arquivo CSV e uma lista de tuplas como entrada, onde cada tupla contém informações sobre atores e receitas. Ela escreve os resultados no arquivo CSV com um padrão específico.

## realizando_etl

Este modulo chama as funções que ativam gatilho ETL