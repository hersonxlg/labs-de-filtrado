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
# Abrir la ventana de la grafica maximizada.
fig_manager = plt.get_current_fig_manager()
fig_manager.window.showMaximized()
plt.xlabel("Fecha", color="red", fontsize="14")
plt.ylabel("Precio", color="red", fontsize="14")
titulo = "Precio diario del Bitcoin durante el ultimo año."
plt.title(titulo, color="red", fontsize="17")
plt.show()
