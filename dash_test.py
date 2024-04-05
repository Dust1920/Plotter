





from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd



app = Dash(__name__)


app.layout = html.Div([
    html.H4('Analysis of the restaurant sales'),
    html.P("Mes del Año:"),
    dcc.Dropdown(id='month',
        options=['Enero','Febrero','Marzo','Abril','Mayo','Junio',
                 'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
        value='Marzo', clearable=False
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"),
    Input("month", "value"))
def generate_chart(month):
    folder = 'plot_data'
    data = pd.read_excel(f'{folder}\\GestionCreditos.xlsx', sheet_name=None)
    balance = data['Saldo al Corte']
    balance.set_index('TDC', inplace=True, drop=True)
    fig = px.pie(balance,
                 values = month,
                 names = balance.index,
                 title=f'Saldo al Corte del Mes de {month} 2024',
                 hole = 0.3)
    return fig
    

app.run_server(debug=True)