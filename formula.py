from urllib.request import urlopen
import json
import pandas as pd
import time
from datetime import datetime


def getapicardata(numdrive, sessao):
    url = f"https://api.openf1.org/v1/car_data?driver_number={numdrive}&session_key={sessao}"
    response = urlopen(url)
    dados = json.loads(response.read().decode('utf-8'))
    return dados

def percorreapi(dados):
    df = pd.DataFrame(dados)
    for i, row in df.iterrows():
        if i + 1 < len(df):  
            proxima_linha = df.iloc[i + 1]
            segant = row['date']
            segprox = proxima_linha['date']
            delay = deltatime(segprox, segant)
        if row['speed'] != 0:   
            time.sleep(delay)
            return row

def deltatime(segprox, segant):
    segant = segant.split("+")
    segant = segant[0]
    segant = segant.replace("T", " ")
    segprox = segprox.split("+")
    segprox = segprox[0]
    segprox = segprox.replace("T", " ")
    datamaior = parse_datetime(segprox)
    datamenor = parse_datetime(segant)
    delta = datamaior - datamenor
    return delta.total_seconds()

def parse_datetime(data):
    try:
        return datetime.strptime(data, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        return datetime.strptime(data, "%Y-%m-%d %H:%M:%S")

