import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv('mpg.csv')

app = dash.Dash()

features = df.columns

app.layout = html.Div([ 
    html.Div([
        dcc.Dropdown()
    ]),
    html.Div([
        dcc.Dropdown()
    ]),
    dcc.Graph(id='feature-graphic')
])
