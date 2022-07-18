import plotly.offline as pyo
import plotly.graph_objs as go 
import pandas as pd

df = pd.read_csv('2018WinterOlympics.csv')
print(df)

#plotting out the totals

data = [go.Bar(x = df['NOC'], y = df["Total"])]
layout = go.Layout(title = 'Medals')
fig = go.Figure(data = data, layout = layout)
#pyo.plot(fig)


#displaying totals and types of medals

#The gold Bar/Column
trace1 = go.Bar(x = df['NOC'], 
                y=df['Gold'], 
                name='Gold', 
                marker = {'color': '#FFD700'})

#The silver Bar/Column
trace2 = go.Bar(x = df['NOC'],
                y = df['Silver'],
                name = "Silver",
                marker = {'color' : '#9EA0A1'})

#The bronze Bar/Column
trace3 = go.Bar(x = df['NOC'],
                y = df['Bronze'],
                name = "Bronze",
                marker = {'color' : '#CD7F32'})

data = [trace1, trace2, trace3]
layout = go.Layout(title = 'Medals')
#if wanting a stacked barchart comment above and uncomment below
# layout = go.Layout(title = 'Medals', barmode = 'stacked')
fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)