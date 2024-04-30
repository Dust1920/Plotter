import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class Plotter:
    def __init__(self, data, dims, size) -> None:
        self.data = data
        self.dims = dims
        self.figsize = size
        self.figure, self.axes = plt.subplots(nrows=dims[0], ncols=dims[1], figsize = (20,20))
        pass
    def barplot(self, ax_pos, col_x):
        self.data[col_x].plot(kind = 'bar', ax = self.axes[ax_pos])
    def boxplot(self, ax_pos, col_x):
        self.data[col_x].plot(kind = 'box', ax = self.axes[ax_pos])


data = pd.DataFrame({'A':[1,2,4],'B':[3,4,6]})


plot_1 = Plotter(data, (2,2), (20,20))

plot_1.boxplot((0,0), 'B')
plt.show()