from matplotlib import pyplot as plt
import numpy as np


class HeatMap():
    
    def heat_map(values,x,y,xlabel,ylabel,dataframe=True,textColor="lightblue",cmap="hot",figsize=(10,10),fontsize=10,weight=None):
        fig, axes = plt.subplots(figsize=figsize)
        im=plt.imshow(values, cmap=cmap, interpolation='nearest')
        axes.set_xticks(np.arange(len(x)), labels=xlabel)
        plt.setp(axes.get_xticklabels(), rotation=90, ha="right", rotation_mode="anchor")
        axes.set_yticks(np.arange(len(y)), labels=ylabel)
    
        for i in range(len(x)):
            for j in range(len(y)):
                v = values.iloc[i,j] if dataframe else values[i][j] # type: ignore
                axes.text(j, i, f"{v:.2f}",fontsize=fontsize,
                               ha="center", va="center", color=textColor,weight=weight)
    
        cbar = axes.figure.colorbar(im, ax=axes)
        cbar.ax.set_ylabel("Valores de mapa de calor", rotation=-90, va="bottom")
    
        plt.show()