import matplotlib.pyplot as plt
import pandas as pd

partners=pd.read_csv('partners.csv')
partners=partners.sort_values(by='Balance',ascending=True)

plt.bar(partners['Pais'], partners['Balance'],label='Energía (MWh)', color='green')

plt.xlabel('Socio', fontsize=7)
plt.ylabel('Balance', fontsize=7)
plt.title("Balance de importaciones y exportaciones comerciales\nde energía entre 2005 y 2021 por la República Francesa", fontsize=9)

plt.xticks(fontsize=5)
plt.yticks(fontsize=5)

plt.legend(loc="upper left")

plt.savefig('totalEs.png')