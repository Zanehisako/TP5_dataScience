import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('video_games_sales.csv')
df_dream_cast:pd.DataFrame = df.loc[df['platform'] == 'DS']
df_ps3:pd.DataFrame = df.loc[df['platform'] == 'PS3']
print(df_dream_cast)
df_sales = df_dream_cast.groupby('year')['global_sales'].sum()
df_sales_ps3= df_ps3.groupby('year')['global_sales'].sum()
print(df_sales)

plt.plot(df_sales.index,df_sales.values)
plt.plot(df_sales_ps3.index,df_sales_ps3.values)


#2 methode
fig,ax1 = plt.subplots()

ax1.set_xlabel('years')
ax1.set_ylabel('sales')
ax1.plot(df_sales.index,df_sales.values,color = 'blue')

ax2 = ax1.twinx()

ax2.set_xlabel('years')
ax2.set_ylabel('sales')
ax2.plot(df_sales_ps3.index,df_sales_ps3.values,color = 'orange',linestyle='--')

df_sales_ps3 = df_sales_ps3.reset_index()
max = df_sales_ps3['global_sales'].max()
max_year = df_sales_ps3.loc[df_sales_ps3['global_sales'].idxmax(),'year']
ax2.annotate(f'pique des vents:{max}',xy=(max_year,max),arrowprops=dict(facecolor='blue',arrowstyle='simple'),fontsize=12,color='blue')
fig.tight_layout()

df_ps3_pc_x360 = df[df['platform'].isin(['PS3','PC','X360'])]
vents_par_platform= df_ps3_pc_x360.groupby(['year','platform'])['global_sales'].sum().reset_index(['platform','year'])

fig,ax1 = plt.subplots()
sns.barplot(x="year",y="global_sales",hue="platform",data=vents_par_platform)



df_nes_gb = df[df['platform'].isin(['GB','NES'])]
vents_par_platform= df_nes_gb.groupby(['year','platform'])['jp_sales'].sum().reset_index(['platform','year'])


fig,ax1 = plt.subplots()
sns.boxplot(x="year",y="jp_sales",data=vents_par_platform)

plt.show()
