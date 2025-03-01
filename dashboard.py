#import das bibliotecas  
import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json

# Definição da latitude e longitude central do Brasil
CENTER_LAT, CENTER_LON = -14.272572694355336, -51.25567404158474

# Exibir o diretório de trabalho atual pois estava dando erro
print("Diretório de trabalho atual:", os.getcwd())

# Caminho para o arquivo CSV
caminho_arquivo = "HIST_PAINEL_COVIDBR_13mai2021.csv"

# Carregamento do DataFrame
try:
    df = pd.read_csv(caminho_arquivo, sep=";")
    print("Arquivo carregado com sucesso!")
    print("Número de linhas e colunas:", df.shape)
    print("Valores faltantes por coluna:")
    print(df.isnull().sum())
    print("Amostra dos dados:")
    print(df.sample(5))
except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")

# Filtrar dados por estado (onde 'estado' não é nulo e 'codmun' é nulo)
df_states = df[(~df["estado"].isna()) & (df["codmun"].isna())]
print("\nDados filtrados por estado:")
print(df_states.head())

# Filtrar dados do Brasil (onde 'regiao' é 'Brasil')
df_brasil = df[df["regiao"] == "Brasil"]
print("\nDados do Brasil:")
print(df_brasil.head())

# Exportar DataFrames para CSV
df_states.to_csv("df_states.csv", index=False)
df_brasil.to_csv("df_brasil.csv", index=False)
print("\nDataFrames exportados para CSV com sucesso!")

# Carregar os DataFrames a partir dos arquivos CSV
df_states = pd.read_csv("df_states.csv")
df_brasil = pd.read_csv("df_brasil.csv")

# Filtrar dados para uma data específica
df_states_ = df_states[df_states["data"] == "2020-05-13"]

# Carregar o arquivo JSON com os dados geográficos do BRASIL
try:
    brazil_states = json.load(open("geojson/brazil_geo.json", "r"))
    print("\nArquivo JSON carregado com sucesso!")
except FileNotFoundError:
    print(f"Erro: O arquivo 'geojson/brazil_geo.json' não foi encontrado.")
except Exception as e:
    print(f"Erro ao carregar o arquivo JSON: {e}")

# Filtrando os dados do estado do Rio de Janeiro
df_data = df_states[df_states["estado"] == "RJ"]

# Definição das colunas a serem utilizadas
select_columns = {
    "casosAcumulado": "Casos Acumulados",
    "casosNovos": "Novos Casos",
    "obitosAcumulado": "Óbitos Totais",
    "obitosNovos": "Óbitos por dia"
}

# Instanciação do Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Criar o mapa de calor
fig = px.choropleth_mapbox(
    df_states_,
    locations="estado",
    color="casosNovos",
    center={"lat": -16.95, "lon": -47.78},
    geojson=brazil_states,
    color_continuous_scale="Redor",
    opacity=0.4,
    hover_data={"casosAcumulado": True, "casosNovos": True, "obitosNovos": True, "estado": True}
)

# Ajustar o layout do mapa
fig.update_layout(
    paper_bgcolor="#242424",
    autosize=True,
    margin=go.layout.Margin(l=0, r=0, t=0, b=0),
    showlegend=False,
    mapbox_style="carto-darkmatter"
)
# Criação do gráfico de para exibição dos dados
fig2 = go.Figure(layout={"template": "plotly_dark"})
fig2.add_trace(go.Scatter(x=df_data["data"], y=df_data["casosAcumulado"]))
fig2.update_layout(
    paper_bgcolor="#242424",
    plot_bgcolor="#242424",
    autosize=True,
    margin=dict(l=10, r=10, t=10, b=10)
)

# Definição do layout da aplicação Dash
app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Img(id="logo", src=app.get_asset_url("logo_dark.png"), height=50),
                html.H5("Evolução COVID-19"),
                dbc.Button("BRASIL", color="primary", id="location", size="lg")
            ], style={}),
            html.P("Informe a Data na Qual Deseja Obter Informações:", style={"margin-top": "40px"}),
            html.Div(id="div-test", children=[
                dcc.DatePickerSingle(
                    id="date-picker",
                    min_date_allowed=df_brasil["data"].min(),
                    max_date_allowed=df_brasil["data"].max(),
                    initial_visible_month=df_brasil["data"].min(),
                    date=df_brasil["data"].max(),
                    display_format="MMMM D, YYYY",
                    style={"border": "0px solid black"}
                )
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Span("Casos recuperados"),
                            html.H3(style={"color": "#adfc92"}, id="casos-recuperados-text"),
                            html.Span("Em acompanhamento"),
                            html.H5(id="em-acompanhamento-text"),
                        ])
                    ], color="light", outline=True, style={
                        "margin-top": "10px",
                        "box-shadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)",
                        "color": "#FFFFFF"
                    })
                ], md=4),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Span("Casos confirmados totais"),
                            html.H3(style={"color": "#389fd6"}, id="casos-confirmados-text"),
                            html.Span("Novos casos na data"),
                            html.H5(id="novos-casos-text"),
                        ])
                    ], color="light", outline=True, style={
                        "margin-top": "10px",
                        "box-shadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)",
                        "color": "#FFFFFF"
                    })
                ], md=4),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Span("Óbitos confirmados"),
                            html.H3(style={"color": "#DF2935"}, id="obitos-text"),
                            html.Span("Óbitos na data"),
                            html.H5(id="obitos-na-data-text"),
                        ])
                    ], color="light", outline=True, style={
                        "margin-top": "10px",
                        "box-shadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)",
                        "color": "#FFFFFF"
                    })
                ], md=4),
            ], className="g-0"),  # Substitui no_gutters por className="g-0" pois estava dando erro a versão atualizou
            html.Div([
                html.P("Selecione que tipo de dados deseja visualizar:", style={"margin-top": "25px"}),
                dcc.Dropdown(
                    id="location-dropdown",
                    options=[{"label": j, "value": i} for i, j in select_columns.items()],
                    value="casosNovos",
                    style={"margin-top": "10px"}
                ),
                dcc.Graph(id="line-graph", figure=fig2)
            ]),
        ], md=5, style={"padding": "25px", "background-color": "#242424"}),
        dbc.Col([
            dcc.Loading(id="loading-1", type="default",
                        children=[
                            dcc.Graph(id="cloropleth-map", figure=fig, style={"height": "100vh", "margin-right": "10px"})
                            ]
                        )
        ], md=7)
    ], className="g-0"),  # Substituido no_gutters por className="g-0" 
    fluid=True
)

#date="2020-05-10" teste do local estado e data
location="RO"

# Callbacks do Dash para interatividade e atualização dos dados
# Callback para atualizar os textos com os dados do status da pandemia
# Interatividade do Dash e funções
@app.callback(
    [
        Output("casos-recuperados-text", "children"),
        Output("em-acompanhamento-text", "children"),
        Output("casos-confirmados-text", "children"),
        Output("novos-casos-text", "children"),
        Output("obitos-text", "children"),
        Output("obitos-na-data-text", "children"),
    ],
    [Input("date-picker", "date"), Input("location", "children")]
    )
def display_status(date, location):
    if location=="BRASIL":
        df_data_on_date = df_brasil[df_brasil["data"]==date]
    else:
        df_data_on_date = df_states[(df_states["estado"] == location) & (df_states["data"] == date)]
    
    df_data_on_date["Recuperadosnovos"]
    recuperados_novos = "-" if df_data_on_date["Recuperadosnovos"].isna().values[0] else f'{int(df_data_on_date["Recuperadosnovos"].values[0]):,}'.replace(",", ".")
    acompanhamento_novos = "-" if df_data_on_date["emAcompanhamentoNovos"].isna().values[0] else f'{int(df_data_on_date["emAcompanhamentoNovos"].values[0]):,}'.replace(",", ".")
    casos_acumulados = "-" if df_data_on_date["casosAcumulado"].isna().values[0] else f'{int(df_data_on_date["casosAcumulado"].values[0]):,}'.replace(",", ".")
    casos_novos = "-" if df_data_on_date["casosNovos"].isna().values[0] else f'{int(df_data_on_date["casosNovos"].values[0]):,}'.replace(",", ".")
    obitos_acumulado = "-" if df_data_on_date["obitosAcumulado"].isna().values[0] else f'{int(df_data_on_date["obitosAcumulado"].values[0]):,}'.replace(",", ".")
    obitos_novos = "-" if df_data_on_date["obitosNovos"].isna().values[0] else f'{int(df_data_on_date["obitosNovos"].values[0]):,}'.replace(",", ".")
    return (recuperados_novos,
            acompanhamento_novos,
            casos_acumulados,
            casos_novos,
            obitos_acumulado,
            obitos_novos,)
    
    
    # Callback para gerar o gráfico de linha ou barra de acordo com os dados selecionados
@app.callback(Output("line-graph", "figure"),
              [
                  Input("location-dropdown", "value"), Input("location", "children"),
              ]
              )
def plot_line_graph(ploty_type, location):
    if location == "BRASIL":
        df_data_on_location = df_brasil.copy()
    else:
        df_data_on_location = df_states[df_states["estado"] == location]
        
    bar_plots = ["casosNovos", "obitosNovos"]
    
    fig2 = go.Figure(layout={"template": "plotly_dark"})
    if ploty_type in bar_plots:
        fig2.add_trace(go.Bar(x=df_data_on_location["data"], y=df_data_on_location[ploty_type]))
    else:
        fig2.add_trace(go.Scatter(x=df_data_on_location["data"], y=df_data_on_location[ploty_type]))
        
    fig2.update_layout(
        paper_bgcolor="#242424",
        plot_bgcolor="#242424",
        autosize=True,
        margin=dict(l=10, r=10, b=10, t=10),
        )
    return fig2

@app.callback(
    Output("cloropleth-map", "figure"),  # Corrigido o ID do componente que estava causando erro
    [Input("date-picker", "date")]  # Corrigido o nome da propriedade que estava causando erro
)
def update_map(date):
    df_data_on_states = df_states[df_states["data"] == date]
    
    fig = px.choropleth_mapbox(
        df_data_on_states,
        locations="estado",
        geojson=brazil_states,
        center={"lat": CENTER_LAT, "lon": CENTER_LON},  # nome da variável não esquecer
        zoom=4,
        color="casosAcumulado",
        color_continuous_scale="Redor",  # nome da escala de cores
        opacity=0.55,
        hover_data={"casosAcumulado": True, "casosNovos": True, "obitosNovos": True, "estado": False}
    )
    
    fig.update_layout(
        paper_bgcolor="#242424",
        mapbox_style="carto-darkmatter",
        autosize=True,
        margin=go.layout.Margin(l=0, r=0, t=0, b=0),
        showlegend=False
    )
    
    return fig  # Adicionado o retorno da figura

from dash import callback_context  # Importe o callback_context corretamente


# Callback para atualizar a localização baseada em cliques no mapa
@app.callback(
    Output("location", "children"),  
    [Input("cloropleth-map", "clickData"), Input("location", "n_clicks")]  #
)
def update_location(click_data, n_clicks):
    changed_id = [p["prop_id"] for p in callback_context.triggered][0]
    # Atualiza a localização se houver um clique no mapa
    if click_data is not None and changed_id != "location.n_clicks":  
        state = click_data["points"][0]["location"]
        return "{}".format(state)  
    else:
        return "BRASIL"

# Rodando o Dash local 
if __name__ == "__main__":
    app.run_server(debug=True)
