import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options=[{'label':'New york city',
                            'value':'NYC'},
                            {'label':'san francisco',
                            'value':'SF'}],
                #this is setting the default value for the dropdown to san francisco
                value = 'SF'),
                #here im making a slider that goes from -10 to 10 in a step of .5
                html.Label('slider'),
                dcc.Slider(min=-10,max=10,step=0.5,value=0),

                html.Label('some radio items'),
                dcc.RadioItems(options=[{'label':'New york city',
                                            'value':'NYC'},
                                            {'label':'san francisco',
                                            'value':'SF'}])
])

if __name__ == '__main__':
    app.run_server()
