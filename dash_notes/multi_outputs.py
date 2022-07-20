import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import base64
from dash.dependencies import Input, Output

df = pd.read_csv('./data/wheels.csv')
app = dash.Dash()

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
                dcc.RadioItems(id='wheels',
                                options=[{'label':i,'value':i}
                                for i in df['wheels'].unique()],
                                value=1),
                html.Div(id='wheels-output'),
                #this just leaves a good separation between the 2 divs and radio items
                html.Hr(),
                dcc.RadioItems(id='colors',
                                options=[{'label':i,'value':i}
                                for i in df['color'].unique()],
                                value='blue'),
                html.Div(id='colors-output'),
                html.Img(id='display-image', src='children',height=300)
],style={'fontFamily':'helvetica','fontSize':18})

@app.callback(Output('wheels-output','children'),
                [Input('wheels','value')])
def callback_a(wheels_value):
    return "you chose {}".format(wheels_value)

@app.callback(Output('colors-output','children'),
                [Input('colors','value')])
def callback_b(colors_value):
    return "you chose {}".format(colors_value)

@app.callback(Output('display-image','src'),
            [Input('wheels','value'),
            Input('colors','value')])
def callback_image(wheels,color):
    path = './data/images/'
    #this line is essentially telling the df 'gimme the pic with these amount of wheels and this color'
    return encode_image(path+df[(df['wheels']==wheels) & (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()