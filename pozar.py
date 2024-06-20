import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

import matplotlib
matplotlib.use('TkAgg')

def forest_fire_simulation(size, p, f, r, steps):
    global forest, burned_forest, ax, img, slider_p, slider_f, slider_r

    # Inicjalizacja lasu
    forest = np.random.choice([0, 1], size=(size, size), p=[1-p, p])
    burned_forest = np.zeros((size, size), dtype=int)

    # Tworzenie własnej mapy kolorów
    colors = [(245/255, 245/255, 220/255), (34/255, 139/255, 34/255), (255/255, 10/255, 10/255)]
    cmap_name = 'custom_map'
    custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=256)

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.25)
    img = ax.imshow(forest, cmap=custom_cmap, interpolation='nearest', vmin=0, vmax=2)
    plt.colorbar(img, ax=ax, label='0 - Empty, 1 - Tree, 2 - Burning')

    # Definicja suwaków
    ax_f = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    ax_r = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')


    slider_f = Slider(ax_f, 'Lightning Prob. (f)', 0.0, 1.0, valinit=f, valstep=0.001)
    slider_r = Slider(ax_r, 'Regrowth Prob. (r)', 0.0, 1.0, valinit=r, valstep=0.01)

    def update(frame):
        global forest, burned_forest

        f = slider_f.val
        r = slider_r.val

        # Rozprzestrzenianie ognia
        for i in range(size):
            for j in range(size):
                if forest[i, j] == 1:
                    if i > 0 and forest[i-1, j] == 2:
                        burned_forest[i, j] = 2
                    elif i < size - 1 and forest[i+1, j] == 2:
                        burned_forest[i, j] = 2
                    elif j > 0 and forest[i, j-1] == 2:
                        burned_forest[i, j] = 2
                    elif j < size - 1 and forest[i, j+1] == 2:
                        burned_forest[i, j] = 2
                    else:
                        burned_forest[i, j] = 1
                elif forest[i, j] == 2:
                    burned_forest[i, j] = 0

        # Losowe wyładowanie pioruna na drzewie bez płonącego sąsiada
        for i in range(size):
            for j in range(size):
                if forest[i, j] == 1:
                    if (i == 0 or forest[i - 1, j] != 2) and (i == size - 1 or forest[i + 1, j] != 2) and (j == 0 or forest[i, j - 1] != 2) and (j == size - 1 or forest[i, j + 1] != 2):
                        if np.random.random() < f:
                            burned_forest[i, j] = 2


        # Nowe drzewo na pustym miejscu
        for i in range(size):
            for j in range(size):
                if forest[i, j] == 0 and np.random.random() < r:
                    burned_forest[i, j] = 1

        # Aktualizacja lasu
        forest = np.copy(burned_forest)

        # Wyświetlanie obrazu
        img.set_data(forest)
        ax.set_title('Forest Fire Simulation (Step {})'.format(frame))


    ani = FuncAnimation(fig, update, frames=steps, repeat=False, interval=20)
    plt.show()



