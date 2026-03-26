Pipeline de ETL com Enriquecimento de IA (Gemini) 🚀
Este projeto demonstra um fluxo completo de Engenharia de Dados (ETL) utilizando Python. O script extrai dados de um arquivo CSV, realiza transformações estruturais (como identificação de bandeiras de cartão) e utiliza a API do Google Gemini para gerar mensagens de boas-vindas personalizadas para cada cliente.

🛠️ Tecnologias Utilizadas
Python 3.13+: Linguagem base do projeto.

Pandas: Biblioteca para manipulação e análise de dados (DataFrames).

Pathlib: Gestão inteligente de caminhos de arquivos e diretórios.

Google Generative AI: Integração com o modelo gemini-1.5-flash para processamento de linguagem natural.

📋 Estrutura do Projeto
Plaintext
projeto/
├── Dados/
│   ├── base_de_dados.csv          # Arquivo de entrada (Raw)
│   └── clientes_com_mensagens.csv # Resultado final (Output)
├── main.py                        # Script principal de ETL
└── README.md                      # Documentação
⚙️ Funcionalidades
Extração (Extract): Leitura automatizada de arquivos CSV em diretórios locais.

Transformação (Transform): * Identificação automática da bandeira do cartão (Visa/Mastercard) com base no dígito inicial.

Limpeza e padronização de dados.

Enriquecimento (IA): Conexão via API com o Gemini para criar saudações personalizadas de forma dinâmica.

Carga (Load): Criação automática de pastas de saída e salvamento dos dados processados em novo formato CSV.

🚀 Como Executar
1. Pré-requisitos
Certifique-se de ter o Python 3.9 ou superior instalado. No Windows 10/11, utilize:

Bash
pip install -U pandas google-generativeai
2. Configuração da API
Para que o enriquecimento de IA funcione, você precisará de uma chave de API:

Obtenha sua chave gratuita no Google AI Studio.

No arquivo main.py, substitua a variável CHAVE_API pelo seu código gerado.

3. Rodando o Script
Bash
python main.py
🧠 Conceitos Aplicados
Programação Modular: Funções isoladas para cada etapa do pipeline.

Tratamento de Exceções: Uso de blocos try/except para garantir a robustez contra arquivos corrompidos ou falhas de rede.

Rate Limiting: Implementação de time.sleep para respeitar os limites de requisição da API gratuita.
