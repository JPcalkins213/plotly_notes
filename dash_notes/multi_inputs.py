import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv('./data/mpg.csv')

app = dash.Dash()

features = df.columns

app.layout = html.Div([ 
    html.Div([
        dcc.Dropdown(id='xaxis',
                        #this is seeting each column in features as a label
                        options=[{'label':i, 'value':i}for i in features],
                        value='displacement')
    ],style={'width':'50%','display':'inline-block'}),
    html.Div([
        dcc.Dropdown(id='yaxis',
                    options=[{'label':i, 'value':i}for i in features],
                        value='mpg')
    ],style={'width':'50%','display':'inline-block'}),
    dcc.Graph(id='feature-graphic')
],style={'padding':10})

@app.callback(Output('feature-graphic', 'figure'),
                [Input('xaxis','value'),
                Input('yaxis','value')])
def update_graph(xaxis_name,yaxis_name):
    return {'data':[go.Scatter(x=df[xaxis_name],
                                y=df[yaxis_name],
                                text = df['name'],
                                mode = 'markers',
                                marker={'size':15,
                                        'opacity':0.5,
                                        'line':{'width':0.5,'color':'black'}})], 
            'layout':go.Layout(title = "MPG")}


if __name__ == '__main__':
    app.run_server()