from saucedemo import saucedemo
from fakturama import DesktopTools, FakturamaActivities
import fake_data
import pandas as pd

#Etapa 1 - Executa o Fakedata e gera a pessoa
fake_data.fake_data()

#Recupera a pessoa e envia por parametro para saucedemo
df = pd.read_csv(r".\assets\fake_data.csv")
for i, r in df.iterrows():
    if r.iloc[0] != 'Nome':                
        first_name = r.iloc[0]
        last_name  = r.iloc[1]        
saucedemo(first_name, last_name, '98000000')

#Cadastra o Contato
FakturamaActivities.cadastra_contato()

#Cadastrar os produtos no Fakturama
FakturamaActivities.cadastra_produtos()

#Realiza a ordem
FakturamaActivities.preenche_ordem()