import matplotlib.pyplot as plt
import pandas as pd

partners=pd.read_csv('partners.csv')
partners=partners.sort_values(by='Balance',ascending=True)

plt.bar(partners['Pays'], partners['Balance'],label='Energie (MWh)', color='green')

plt.xlabel('Partenaire', fontsize=7)
plt.ylabel('Balance', fontsize=7)
plt.title("Balance des importations et exportations commerciaux\nd'énergie entre 2005 et 2021 pour la République Française", fontsize=9)

plt.xticks(fontsize=5)
plt.yticks(fontsize=5)

plt.legend(loc="upper left")

plt.savefig('totalFr.png')