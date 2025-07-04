import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, callback, html, dcc, Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# Some example data and its corresponding Plotly figure
df = pd.DataFrame(np.random.rand(10,2), columns=['A', 'B'])
fig = px.scatter(df, x='A', y='B')

# Structure of my page
app.layout = html.Div([
    html.H1(children='A simple dashboard'),
    html.Button(children='Generate Random Data', id='randomize', n_clicks=0),
    html.Div(id='display-value', children=None),
    dcc.Graph(id="myGraph", figure=fig),
])

@callback(
    Output(component_id='display-value', component_property='children'),
    Output(component_id='myGraph', component_property='figure'),
    Input(component_id='randomize', component_property='n_clicks'),
)
def do_something(n_clicks):
    # Regenerate the figure
    df = pd.DataFrame(np.random.rand(10,2), columns=['A', 'B'])
    fig = px.scatter(df, x='A', y='B')

    return [
        f'You have clicked {n_clicks} times',
        fig,
    ]

if __name__ == '__main__':
    app.run(debug=True)