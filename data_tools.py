# Funciones creadas para diversos usos.

## Revista


def divide_in_ms(df, col, nd):
    """
    Para valores con contexto monetario.\n
    Factorizar en potencias de 1000.
    """
    pot = 1000 ** nd
    mstr  ='M' * nd
    df[f'{col}_{mstr}'] = df[col] / pot
    df[f'{col}_{mstr}'] = df[f'{col}_{mstr}'].agg(lambda x: round(x, 2))
    return df

### División de la República por regiones. 
region_norte = ['BCN','BCS','SON','CHH','SIN','DUR','COA','NLE','TAM']
region_sur = ['GRO','OAX','CHP','TAB','CAM','ROO','YUC']
region_oriente = ['VER','HID', 'PUE','TLA','MEX','CMX','MOR']
region_occidente = ['NAY','JAL','COL','MIC','ZAC','AGU','SLP','GUA','QUE']