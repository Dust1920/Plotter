import math

golden_number = (1 + math.sqrt(5)) / 2

def golden_figbase(figure):
    dims = figure.get_size_inches()
    figure = figure.set_size_inches((dims[0], dims[0] / golden_number))
    return figure

def figure_base(figure):
    figure = figure.set_size_inches((20,12.36))
    return figure

def new_plot(type, data, ax, **kwargs):
    plots_database[type](data, ax, **kwargs)
    return 0

def barplot_df(df, col, ax, **kwargs):
    def_props = {
        'orientation' : 'bar',
        'rotation': 45,
        'title': 'Ramo 33',
        'color': 'g',
        'xlabel': 'Fondos',
        'ylabel': ' % respecto al Total',
        'fontsize': 14
    }
    act_text = kwargs.get('text', 1)
    props = kwargs.get('config', def_props)
    df[col].plot(kind=props['orientation'],
                 rot=props['rotation'],
                 color = props['color'],
                 title = props['title'],
                 xlabel=props['xlabel'],
                 ylabel=props['ylabel'],
                 fontsize=props['fontsize'],
                 ax = ax)
    if act_text:
        for container in ax.containers:
            ax.bar_label(container, fontsize = 12)


def boxplot(data, ax, **kwargs):
    return 0

def histplot(data, ax, **kwargs):
    return 0

def scatterplot(data, ax, **kwargs):
    return 0

def rectangularplot(data, ax, **kwargs):
    return 0

def pieplot(data, ax, **kwargs):
    return 0

plots_database = {
    'barplot' : barplot_df,
    'boxplot': boxplot,
    'histplot':histplot,
    'scatterplot':scatterplot,
    'rectangularplot':rectangularplot,
}