import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import base64
from dash.dependencies import Input, Output

app = dash.Dash()
app.layout = html.Div([
    dcc.RangeSlider(-20, 20, 1, value=[5, 15], id='my-range-slider'),
    html.Div(id='output-container-range-slider')
])

@app.callback(
    Output('output-container-range-slider', 'children'),
    [Input('my-range-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value[0]*value[1])

if __name__ == '__main__':
    app.run_server(debug=True)