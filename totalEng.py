#Designs a bar chart with MWh exports per country
import matplotlib.pyplot as plt
import pandas as pd

partners=pd.read_csv('partners.csv')
partners=partners.sort_values(by='Balance',ascending=True)

plt.bar(partners['Country'], partners['Balance'],label='Energy (MWh)', color='green')

plt.xlabel('Partner', fontsize=7)
plt.ylabel('Balance', fontsize=7)
plt.title("Balance of commercial energy imports and exports\nbetween 2005 and 2021 for the French Republic", fontsize=9)

plt.xticks(fontsize=5)
plt.yticks(fontsize=5)

plt.legend(loc="upper left")

plt.savefig('totalEng.png')