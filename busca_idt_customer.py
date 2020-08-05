import pandas as pd
import json
import requests
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup 


retornoFim = pd.DataFrame()

arqCustomer = pd.read_csv('docs.csv', sep=";")

for codCust in arqCustomer['codigo']:
    try:
        url = (f"http://wwwww/api-/accounts?legacyCustomerId={codCust}")
        response = requests.get(url, verify=False)

        post = json.loads(response.content)

        retorno = pd.json_normalize(post)

        retorno = retorno[['safePayUserId','legacyCustomerId']] 
        retornoFim = pd.concat([retorno, retornoFim])

    except Exception as err:
        print(err)
        print(codCust)
        print(post)

retornoFim.to_csv('resultado_safepay_customer.csv',sep=';', index=False)
#print(retornoFim.shape)


