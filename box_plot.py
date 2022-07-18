import plotly.offline as pyo 
import plotly.graph_objs as go

y = [1,14,14,15,16,18,19,20,20,23,24,26,27,28,29,33,54]

# for pointpos if its negative it will offset to left and vise versa for right
data = [go.Box(y=y, boxpoints = 'all', jitter = 0.3, pointpos = 0)]
# to only show the outliers as points uncomment below and comment above
# data = [go.Box(y=y, boxpoints = 'outliers')]
pyo.plot(data)