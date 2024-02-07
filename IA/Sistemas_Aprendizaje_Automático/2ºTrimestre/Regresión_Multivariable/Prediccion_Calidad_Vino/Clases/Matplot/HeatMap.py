from matplotlib import pyplot as plt
import numpy as np


class HeatMap():
    
    def heat_map(values,x,y,xlabel,ylabel,dataframe=True,textColor="lightblue",cmap="hot",figsize=(10,10),fontsize=10,weight=None):
        """Heat Map de DataSet

        Args:
            values (_type_): Valores a usar en HeatMap
            x (_type_): Valores en X
            y (_type_): Valores en Y
            xlabel (_type_): Labels en X
            ylabel (_type_): Labels en Y
            dataframe (bool, optional): Si es un DataFrame
            textColor (str, optional): Color del Texto. Defaults to "lightblue".
            cmap (str, optional): Tipo de Cmap. Defaults to "hot".
            figsize (tuple, optional): Tamaño. Defaults to (10,10).
            fontsize (int, optional): Tamaño de letra. Defaults to 10.
            weight (_type_, optional): Peso. Defaults to None.
        """
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