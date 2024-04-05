

def new_plot(type, data, ax, **kwargs):
    plots_database[type](data, ax, **kwargs)
    return 0

def barplot(data, ax, **kwargs):
    return 0

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
    'barplot' : barplot,
    'boxplot': boxplot,
    'histplot':histplot,
    'scatterplot':scatterplot,
    'rectangularplot':rectangularplot,
}