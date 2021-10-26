import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# Some example data and its corresponding Plotly figure
df = pd.DataFrame(np.random.rand(10,2), columns=['A', 'B'])
fig = px.scatter(df, x='A', y='B')

# Structure of my page
app.layout = html.Div([
    html.H1('A simple dashboard'),
    html.Button('Generate Random Data', id='randomize', n_clicks=0),
    html.Div(id='display-value'),
    dcc.Graph(id="myGraph", figure=fig),
])

@app.callback(
    [Output('display-value', 'children'), Output('myGraph', 'figure')],
    [Input('randomize', 'n_clicks')],
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
    app.run_server(debug=True)