trace2 = go.Bar( x=['giraffes', 'orangutans', 'monkeys'], y=[12, 18, 29], name='LA Zoo' )

data = [trace1, trace2]

layout = go.Layout(barmode='group') #try out stack here

fig = go.Figure(data=data, layout=layout)

py.offline.iplot(fig)