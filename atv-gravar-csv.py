import psutil as p
import pandas as pd
import time
from datetime import datetime


continuar = True
dados = {
        "cpu" : [],
        "memoria" : [],
        "disco" : [],
        "data" : []
    }

while continuar:
    pergunta = input("Deseja capturar?(s/n): ").lower()
    cpu = p.cpu_percent()
    memoria = p.swap_memory().used
    disco = p.disk_usage('/').used
    data = datetime.now()

    dados["cpu"].append(cpu)
    dados["memoria"].append(memoria)
    dados["disco"].append(disco)
    dados["data"].append(data)
    print(dados)
    if pergunta == 'n':
        continuar = False
        df = pd.DataFrame(dados)
        df.to_csv("dados_psutil.csv", encoding="utf-8")
    else:
        continuar
