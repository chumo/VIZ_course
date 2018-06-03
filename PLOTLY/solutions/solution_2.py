trace1 = go.Bar( x=['giraffes', 'orangutans', 'monkeys'], y=[20, 14, 23], name='SF Zoo', text=['giraffes', 'orangutans', 'monkeys'] )

trace2 = go.Bar( x=['giraffes', 'orangutans', 'monkeys'], y=[12, 18, 29], name='LA Zoo', text=['giraffes', 'orangutans', 'monkeys'] )

data = [trace1, trace2]

layout = go.Layout(barmode='group', #try out stack here 
                   paper_bgcolor='rgb(233,233,233)',
                   plot_bgcolor='rgb(233,233,233)',)

fig = go.Figure(data=data, layout=layout)

py.offline.iplot(fig)