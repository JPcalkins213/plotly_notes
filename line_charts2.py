import pandas as pd
import plotly.offline as pyo 
import plotly.graph_objs as go 

df = pd.read_csv('nst-est2017-alldata.csv')
print(df.head())

#grabbing 6 new england states

df2 = df[df['DIVISION'] == '1']
df2.set_index('NAME', inplace=True)

#this is grabing the population column
pop_col = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[pop_col]

print(df2)

#using list comprehension to build the traces 
data = [go.Scatter(x = df2.columns, 
                   y = df2.loc[name], 
                   mode = 'lines', 
                   name = name) for name in df2.index]

pyo.plot(data)