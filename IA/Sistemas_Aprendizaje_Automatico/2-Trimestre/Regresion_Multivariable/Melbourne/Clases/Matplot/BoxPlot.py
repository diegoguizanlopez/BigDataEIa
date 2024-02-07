from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import MaxNLocator


class BoxPlot:


    def box_plot(types, dataFrame, num_xticks=10, by=None, deepColor="Black", faceColor="Black", color="Black", ballsColor="Gray"):
        """BOX PLOT 
    
        By DiegoGL
    
        Args:
            types (List): Lista de datos
            dataFrame (DataFrame): DataFrame de los datos
            num_xticks (int, optional): Número de ticks en el eje x. Defaults to 10.
            by (Columna): Columna que se comparará en el By. Defaults to None.
            deepColor (str, optional): Color del fondo.
            faceColor (str, optional): Face color.
            color (str, optional): Color fondo 2.
            ballsColor (str, optional): Color de las bolas.
        """
        num_cols = len(types)
        num_rows = num_cols // 2 if num_cols % 2 == 0 else num_cols // 2 + 1
        fig, axs = plt.subplots(num_rows, 2, figsize=(10, num_rows*5),squeeze=False)
        for index,i in enumerate(types):
            ax = axs[index // 2, index % 2]
            if i != by:
                dataFrame.plot.box(by=by, column=i, ax=ax,
                      color=color, notch=True, vert=True, patch_artist=True,
                      # BORDE
                      boxprops=dict(edgecolor=deepColor,  facecolor=faceColor, linewidth=2),
                      # LINEA DE EXTREMO
                      capprops=dict(color=deepColor, linewidth=2),
                      # BORDE LINEA UNIÓN
                      whiskerprops=dict(color=deepColor,linewidth=1),
                      # PUNTOS
                      flierprops=dict(color=deepColor, markerfacecolor=ballsColor, linestyle= "none", markeredgecolor="none", markersize=9),
                      # MEDIANA
                      medianprops=dict(color=deepColor),
                      # LINEA MEDIA
                      showmeans=True,
                      )
                ax.xaxis.set_major_locator(MaxNLocator(nbins=num_xticks))
            ax.yaxis.grid(True)
        if (num_cols-1) % 2 == 1:
            fig.delaxes(axs[(index) // 2, 1])
    