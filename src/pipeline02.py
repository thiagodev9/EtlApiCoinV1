import time
import requests
from tinydb import TinyDB
from datetime import datetime

def extract():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    dados= response.json()
    return dados

def transform(dados):
    valor = dados ["data"] ["amount"]
    criptomoeda = dados ["data"] ["base"]
    moeda = dados ["data"] ["currency"]
    timestamp = datetime.now().timestamp()
    
    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }
    return dados_transformados

def salvar_dados_tinydb(dados, db_name = "bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print(f"Dados salvos com sucesso!")
    

if __name__ == "__main__":
    while True:
        dados = extract()
        dados = transform(dados)
        salvar_dados_tinydb(dados)
        time.sleep(15)


