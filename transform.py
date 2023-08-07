#Commercial imports and exports (2005 à 2021)
#Data from:
#https://www.data.gouv.fr/fr/datasets/imports-et-exports-commerciaux-2005-a-2021/

#This code creates a clean DataFrame to plot the following visualizations:
#-Imports and exports per partner (Great Britain, Central Western Europe, Switzerland, Italy and Spain)
#-Total imports and exports


#Import required libraries
import pandas as pd

#Open .xlxs file as pandas DataFrame
df=pd.read_excel('iec.xlsx')

#Order entries by date
df.sort_values(by=['date'])


#Create a second DataFrame with alltime balances for each partner. Calculations are made from the french point of view

#Add exports and imports
fromGB=int(df['gb_fr'].sum())
toGB=int(df['fr_gb'].sum())
fromCWE=int(df['cwe_fr'].sum())
toCWE=int(df['fr_cwe'].sum())
fromCH=int(df['ch_fr'].sum())
toCH=int(df['fr_ch'].sum())
fromIT=int(df['it_fr'].sum())
toIT=int(df['fr_it'].sum())
fromES=int(df['es_fr'].sum())
toES=int(df['fr_es'].sum())

fromTotal=fromCH+fromGB+fromCWE+fromIT+fromES
toTotal=toGB+toCWE+toCH+toIT+toES


#Calculate balance to find out if France exports more energy than it imports
balanceGB=toGB-fromGB
balanceCWE=toCWE-fromCWE
balanceCH=toCH-fromCH
balanceIT=toIT-fromIT
balanceES=toES-fromES

balanceTotal=toTotal-fromTotal

partners=pd.DataFrame({
    'Partner':['GB','CWE','CH','IT','ES','Total'],
    'Imports':[fromGB,fromCWE,fromCH,fromIT,fromES, fromTotal],
    'Exports':[toGB,toCWE,toCH,toIT,toES,toTotal],
    'Balance':[balanceGB,balanceCWE,balanceCH,balanceIT,balanceES,balanceTotal],
    'Country':['Great Britain','CWE','Switzerland','Italy','Spain','Total'],
    'Pays':['Great Britain','CWE','Switzerland','Italy','Spain','Total'],
    'Pais':['Gran Bretaña','ECO','Suiza','Italia','España','Total'],
    'Icon':['🇬🇧','🇩🇪 🇦🇹 🇧🇪 🇱🇺 🇳🇱','🇨🇭', '🇮🇹', '🇪🇸', 'Total']
})

#Review new DataFrame
print(partners)

#Save DataFrame to work in other scripts
partners.to_csv('partners.csv', index=0)
