import os
import pandas as pd
import plotly.express as px
DATA_MAIN_PATH = os.path.join('data', 'meteo', 'fires', 'thermopoints.csv')

df_main = pd.read_csv(DATA_MAIN_PATH, sep=';', parse_dates=['dt'])
df_main['year'] = df_main['dt'].dt.year

data = df_main.groupby(['year', 'type_name']).agg({'type_id': 'count'}).reset_index()
print(data)
fig = px.bar(
    data,
    x='year',
    y='type_id',
    color='type_name',
    title='Fires in Russia',
    color_continuous_scale='Rainbow',
    labels={'year': 'Время, год',
            'type_id': 'Число пожаров',
            'type_name': 'Тип пожара'},
)

fig.show()
#hello
