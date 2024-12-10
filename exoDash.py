from dash import Dash, Input, Output, callback,html,dash_table,dcc
import plotly.express as px
import pandas as pd
df = pd.read_csv('video_games_sales.csv')

shares = df.groupby('platform')['global_sales'].sum().reset_index()

fig = px.pie(shares,values='global_sales',names='platform')
@callback(
    Output(component_id='ploty-id',component_property='figure'),
    Input(component_id='pub-filter',component_property='value')
)
def update_graph(selected_pub):
    df_pub = df[df['publisher']== selected_pub]
    shares = df_pub.groupby('platform')['global_sales'].sum().reset_index()
    return px.pie(shares,values='global_sales',names='platform')

app = Dash()
app.layout = html.Div([
    html.H1(children='Game Sales'),
    dcc.Dropdown(id='pub-filter',options =[{'label':pub,"value":pub} for pub in df['publisher'].unique()],value=df['publisher'].unique()[0]),
    dcc.Graph(figure=fig,id='ploty-id')
])
app.run()

