import sys
try:
  import google.colab
  IN_COLAB = True
except:
  IN_COLAB = False

if IN_COLAB:
    # montar el drive, que es donde tenemos el dataset
    from google.colab import drive
    drive.mount("/content/drive")
    data_dir = "/content/drive/MyDrive/2023/Publica/Alumnos/"
    sys.path.append(data_dir)
else:
    import os
    data_dir = os.path.dirname(__file__) + "/"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
matplotlib.use('TkAgg')

filename = data_dir + "bmw-clean.csv"
#Año y,precio x,consumo z
df = pd.read_csv(filename,usecols=['year','price','mpg'])
print(df)

fig,ax = plt.subplots(figsize=[10,8])
y=df['price']
z=df['year']
x=df['mpg']
p=ax.scatter(x=x,y=y,c=z)
fig.colorbar(p,ax=ax,label='AÑO')
ax.set_xlim(0,200)
ax.set_ylim(0,120000)
ax.set_xlabel('CONSUMO')
ax.set_ylabel('PRECIO')
ax.spines["right"].set_visible(False) # ocultar borde derecho
ax.spines["top"].set_visible(False) # ocultar borde superior
fig.tight_layout() # ajustar elementos al tamaño de la figura
plt.show()