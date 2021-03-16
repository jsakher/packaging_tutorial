def format_date(df_bikes):
    df_bikes['date'] = df_bikes['date'] + 'T' + df_bikes['heure'] + ':00:00+01:00'
    df_bikes = df_bikes.drop(['mois', 'jour', 'heure'], axis = 1)
    return df_bikes