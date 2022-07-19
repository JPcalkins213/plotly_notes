import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('gapminderDataFiveYear.csv')

print(df.head())


app = dash.Dash()

year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year), 'value':year})
#options = year_options has to be a list of dictionaries with a label and value that is why i created the for loop above
app.layout = html.Div(
                [dcc.Graph(id='graph'),
                dcc.Dropdown(id='year-picker',
                                options=year_options,
                                value=df['year'].min())
])

@app.callback(Output('graph', 'figure'),
                [Input('year-picker', 'value')])
def update_fig(selected_year):
    #data only for selected year from dropdown
    filtered_df = df[df['year']==selected_year]

    traces = []

    for cname in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent']==cname]
        traces.append(go.Scatter(x = df_by_continent['gdpPercap'],
                                    y = df_by_continent['lifeExp'],
                                    mode = 'markers',
                                    opacity=0.7,
                                    marker={'size':15},
                                    name=cname))

    return {'data': traces, 'layout': go.Layout(title = 'my plot')}

if __name__ == '__main__':
    app.run_server()
