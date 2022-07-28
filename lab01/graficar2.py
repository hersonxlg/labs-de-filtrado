import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import platform as pf

df = pd.read_csv('market-price.csv')

x = df.Timestamp.apply(lambda datetime: datetime.split()[0])
y = df['market-price']

plt.plot(x,y)
plt.xticks(np.linspace(0,365,8,dtype=int))
plt.tick_params(labelsize=13)
plt.grid()
# Abrir la ventana de la grafica maximizada.
fig_manager = plt.get_current_fig_manager()
if pf.system() == 'Windows':
    fig_manager.window.showMaximized()
else:
    fig_manager.window.maximize()
plt.xlabel("Fecha", color="green", fontsize="17", fontweight="bold")
plt.ylabel("Precio en $", color="green", fontsize="17", fontweight="bold")
titulo = "Precio diario del Bitcoin durante el ultimo año."
plt.title(titulo, color="red", fontsize="24", fontweight="bold")
plt.show()
