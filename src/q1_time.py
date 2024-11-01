import pandas as pd

from typing import List, Tuple
from datetime import datetime

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Carga datos a dataframe
    df = pd.read_json(file_path, lines=True)

    # Transforma campo date a fecha y username a columna independiente
    df['date'] = pd.to_datetime(df['date']).dt.date
    df['username'] = df['user'].apply(lambda x: x['username'])

    # Cuenta mensajes por fecha y obtiene los 10 primeros
    date_count = df['date'].value_counts().nlargest(10).index

    # Filtra por top 10
    df_top_dates = df[df['date'].isin(date_count)]

    # Obtiene los usuarios más activos para cada fehca
    most_active_users = (df_top_dates.groupby(['date', 'username']).size()
                         .reset_index(name='tweet_count')
                         .sort_values(['date', 'tweet_count'], ascending=[True, False])
                         .drop_duplicates('date'))

    # Convierte salida a lista con tuplas
    output = list(most_active_users[['date', 'username']].itertuples(index=False, name=None))
    
    return output