import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('players.csv')
plt.figure(figsize=(10,6))
sns.histplot(x=df['height_in_cm'],kde=True)
heightes_market_value = df.groupby('sub_position')['highest_market_value_in_eur'].sum().reset_index()
print(heightes_market_value)
sns.barplot(x='sub_position',y='highest_market_value_in_eur',data=heightes_market_value)
plt.xticks(rotation=90)
plt.show()

