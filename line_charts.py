from flask import got_request_exception
import numpy as np 
import plotly.offline as pyo
import plotly.graph_objs as go
np.random.seed(56)

x_val = np.linspace(0,1,100)
y_val = np.random.randn(100)

#line charts are referred to as a trace in plotly syntax
trace0 = go.Scatter(x = x_val, y = y_val+5, mode = "markers", name = 'markers')
trace1 = go.Scatter(x = x_val, y = y_val, mode = "lines", name = 'markers')
trace2 = go.Scatter(x = x_val, y = y_val-5, mode = "lines+markers", name = 'markers')

data = [trace0, trace1, trace2]

layout = go.Layout(title = 'Line Charts')

fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)
