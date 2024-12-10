import pandas as pd
import plotly.express as px
df = pd.read_csv('video_games_sales.csv')
df = df[df.name.str.contains('Devil May Cry')]
print(df.head())
print(df['publisher'].astype('category').cat.categories)
sales = df.groupby(['name','platform'])['global_sales'].sum().reset_index()
fig = px.sunburst(sales,path=['name','platform'],values='global_sales')

fig.show()
