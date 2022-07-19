import dash
import dash_html_components as html

app = dash.Dash()

#style is going to be a dictionary where you essentially pass in css.
app.layout = html.Div(['this is the outermost div',
                        html.Div('this is an inner div',
                        style = {'color':'red','border':'2px red solid'}),
                        html.Div(['Another inner div'],
                        style = {'color':'blue', 'border':'3px blue solid'})],
                        style = {'color':'green','border':'2px green solid'})

if __name__ == '__main__':
    app.run_server()