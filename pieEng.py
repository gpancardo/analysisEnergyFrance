import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('partners.csv')

newLabel=[]

balances = data['Exports']
label = data['Country']

balances = balances[:-1]
label = label[:-1]

for i in label:
    txt=(str(label[i])+" "+str(balances[i]))
    newLabel.append(txt)

label=newLabel
print(label)

data=data.sort_values(by='Exports',ascending=True)

plt.pie(balances, labels=label, counterclock=False)

plt.xlabel("Energy in MWh")

plt.legend(loc="upper left")

plt.title("Total commercial energy exports\nbetween 2005 and 2021 for the French Republic", fontsize=9)

plt.show()