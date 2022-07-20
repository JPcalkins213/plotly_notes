import dash
import pandas as pd
import numpy as np
from dash import dcc 
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash()
#creating a text box and an h1 that shows what was typed in the h1
#html.Button
app.layout = html.Div([
            dcc.Input(id='number-in', value=1, style={'fontSize':24}),
            html.Button(id='submit', n_clicks=0,children='Submit Here',style={'fontSize':24}),
            html.H1(id='number-out')
])

@app.callback(Output('number-out','children'),
                [Input('submit', 'n_clicks')],
                [State('number-in','value')])
def output(n_clicks,number):
    return f"{number} was typed in, and button was clicked {n_clicks} times"

if __name__ == '__main__':
    app.run_server()