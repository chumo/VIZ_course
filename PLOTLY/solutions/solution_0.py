layout = go.Layout(
    title='Some Experiment',
    xaxis = dict(title = 'Some independent variable'),
    yaxis = dict(title = 'Some dependent variable')
    )

fig = go.Figure(data=data, layout=layout)

py.offline.iplot(fig)