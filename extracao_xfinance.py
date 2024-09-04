import requests
import pandas as pd
from openpyxl import Workbook

token = "c612a092017fc39036d10905bf6ce586"

headers = { "Authorization": f"Bearer {token}" }

url_category = "https://myfin-financial-management.bubbleapps.io/api/1.1/obj/category/"
url_recipient = "https://myfin-financial-management.bubbleapps.io/api/1.1/obj/recipient/"


def chamar_api_xfinance(url):
    response = requests.get( url, headers=headers )
    return response

response_category = chamar_api_xfinance( url_category )
response_recipient = chamar_api_xfinance( url_recipient )

category_ajustado_json = response_category.json()['response']['results']
recipient_ajustado_json = response_recipient.json()['response']['results']

df_category = pd.DataFrame( category_ajustado_json, columns=['Created Date', 'title', 'balance', '_id'] )
df_recipient = pd.DataFrame( recipient_ajustado_json, columns=['title', 'category_ref', 'photo', '_id'] )

df_category.to_excel( 'arquivos/Category.xlsx', index=False )
df_recipient.to_excel( 'arquivos/Recipitn.xlsx', index=False )

df_category.to_parquet( 'arquivos/Category.parquet', index=False )
df_recipient.to_parquet( 'arquivos/Recipitn.parquet', index=False )