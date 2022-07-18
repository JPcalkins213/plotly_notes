import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x = random_x, 
                   y = random_y,
                   mode = 'markers', 
                   marker = dict(
                    size = 12,
                    color = 'rgb(51,204,153)',
                    symbol = 'pentagon',
                    line = {'width':2}
                   ))]
#this will allow you to name the plot and axes, and will let you choose what happens when hovering over a plot
layout = go.Layout(title = "hello first plot",
                            #these do the same thing but plotly docs use the "yaxis" syntax
                            xaxis = {'title': 'random x'},
                            yaxis = dict(title = 'random y'),
                            hovermode = 'closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(data, filename = 'scatter.html')