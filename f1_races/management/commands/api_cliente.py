from urllib.request import urlopen
import json

def getapicardata(numdrive, sessao, date):
    url = f"https://api.openf1.org/v1/car_data?driver_number={numdrive}&session_key={sessao}&date={date}"
    response = urlopen(url)
    dados = json.loads(response.read().decode('utf-8'))
    return dados

