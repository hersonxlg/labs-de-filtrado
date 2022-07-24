import pandas as pd
import matplotlib.pyplot as plt
import os, sys

# detectar ruta donde esta el ejecutable.
application_path = os.path.dirname(sys.executable)

df = pd.read_csv('market-price.csv')

x = df.Timestamp.apply(lambda datetime: datetime.split()[0])
y = df['market-price']

plt.plot(x,y)
plt.xticks(range(0,365,50))
plt.grid()
plt.show()
