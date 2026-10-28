# PlantGuide

Aplicativo mobile em Python para consultar plantas, visualizar informações básicas e navegar entre uma tela inicial, catálogo de plantas e detalhes de cada item.

## Visão geral

Este projeto é uma pequena aplicação em KivyMD que:

- exibe uma tela de boas-vindas;
- lista plantas em cartões em uma tela de índice;
- permite abrir o detalhe de uma planta selecionada;
- carrega dados de um banco SQLite local;
- usa imagens locais armazenadas na pasta `resources`.

A estrutura atual do projeto é simples e foi desenvolvida como protótipo/estudo, sem pipeline de build, testes automatizados ou gerenciamento de dependências via arquivo de configuração.

## Estrutura do projeto

```text
PlantGuide/
├── main.py                  # ponto de entrada da aplicação
├── path_resolver.py         # resolve caminhos para recursos locais
├── database/
│   ├── __init__.py
│   ├── database_func.py     # criação do SQLite e consultas
│   ├── seed.py              # dados iniciais das plantas
│   └── __pycache__/
├── screens/
│   ├── __init__.py
│   ├── welcome_screen.py    # tela inicial
│   ├── plant_index.py       # tela com a listagem de plantas
│   ├── plant_detail.py      # tela de detalhes da planta
│   └── __pycache__/
├── widgets/
│   ├── __init__.py
│   ├── plant_card.py        # construção dos cartões da listagem
│   └── __pycache__/
├── resources/
│   ├── card/                # imagens da listagem
│   ├── detail/              # imagens da tela de detalhes
│   └── welcome.jpg          # imagem da tela inicial
├── README.md
└── __pycache__/
```

## Como funciona

- `main.py` cria a aplicação `JosehApp` e inicia o banco de dados.
- `database/start_db()` cria a tabela `plants` em SQLite e insere os dados iniciais se ainda não existirem.
- `database/seed.py` contém a lista inicial de plantas.
- `widgets/plant_card.py` gera os cartões clicáveis do catálogo.
- `screens/plant_detail.py` busca a planta selecionada e monta os dados exibidos na tela de detalhe.
- `resources/` armazena imagens usadas pelo app, e os nomes dos arquivos precisam corresponder ao campo `search_name` das plantas.

## Requisitos

- Python 3.10+ (o projeto foi escrito para ambiente Python moderno)
- KivyMD
- Kivy

Como o projeto não possui um `requirements.txt`, as dependências precisam ser instaladas manualmente.

Exemplo:

```bash
pip install kivymd
```

Se o ambiente estiver sem Kivy, normalmente será necessário também:

```bash
pip install kivy
```

## Execução

Na raiz do projeto:

```bash
python main.py
```

## Banco de dados

O banco é criado em tempo de execução dentro do diretório de dados do app (`app.user_data_dir`), em um arquivo chamado `plants.db`.

Isso significa que:

- o banco não é versionado no repositório;
- ele é gerado automaticamente na primeira execução;
- os dados iniciais são carregados por `database/seed.py`.

## Dados iniciais

O projeto inclui uma lista fixa de plantas, como:

- Manjericão
- Hortelã
- Alecrim
- Salsa
- Tomate
- Alface
- Pimentão
- Cenoura
- Lavanda
- Girassol
- Calêndula
- Babosa
- Planta-jade
- Bananeira
- Morangueiro

## Limitações atuais

Este projeto é um protótipo e possui algumas limitações importantes:

- Não há `requirements.txt` ou ambiente reproduzível definido no projeto.
- Não há testes automatizados.
- Não há arquivos de configuração para build ou empacotamento.
- As imagens precisam existir manualmente em `resources/card` e `resources/detail`.
- Os nomes dos arquivos devem seguir o padrão de `search_name` para que a tela de detalhe funcione corretamente.
- O app é simples e não implementa filtros, busca avançada, edição de plantas, persistência de usuário, ou navegação complexa.
- A lógica de banco e UI está concentrada em poucos arquivos, sem separação mais robusta para um projeto maior.
- O app depende de um modelo de dados rígido e não escalável para uso real.

## Melhorias sugeridas

- adicionar `requirements.txt`;
- incluir imagens faltantes ou geração automática de assets;
- criar testes unitários para banco e telas;
- separar melhor a lógica de dados da UI;
- implementar busca, filtros e mais campos de planta;
- adicionar suporte a internacionalização / tradução;
- configurar build para Android ou desktop.

## Observação

O código atual funciona como um MVP educativo para demonstrar navegação em KivyMD, uso de SQLite e organização de telas por módulos. Ele não é um projeto empresarial completo, mas serve como base para extensão.
