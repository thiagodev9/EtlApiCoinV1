# ETL API Coin

## Descrição
Este projeto implementa um processo ETL (Extract, Transform, Load) utilizando Python para coletar, transformar e carregar dados de APIs de criptomoedas. O projeto utiliza a biblioteca `requests` para fazer requisições HTTP e manipular os dados obtidos.

## Funcionalidades
- Extração de dados de APIs de criptomoedas
- Transformação dos dados para o formato desejado
- Carregamento dos dados em um banco de dados ou arquivo
- Automatização do processo ETL

## Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/etl-api-coin.git
cd etl-api-coin
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração
1. Crie um arquivo `.env` na raiz do projeto
2. Adicione suas variáveis de ambiente conforme o exemplo em `.env.example`

## Uso
```bash
python src/main.py
```

## Estrutura do Projeto
```
etl-api-coin/
├── src/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   └── main.py
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Contribuição
1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato
Seu Nome - [@seutwitter](https://twitter.com/seutwitter)
Link do Projeto: [https://github.com/seu-usuario/etl-api-coin](https://github.com/seu-usuario/etl-api-coin)
# EtlApiCoinV1
