from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(data=[
        go.Candlestick(
            x=df['Date'],
            open=df['AAPL.Open'], 
            high=df['AAPL.High'],
            low=df['AAPL.Low'], 
            close=df['AAPL.Close']
        )
    ])

fig.update_layout(
    xaxis_rangeslider_visible=False,
    paper_bgcolor="#454032",
    plot_bgcolor="#5c5542",
    font_color="#fff"
)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)