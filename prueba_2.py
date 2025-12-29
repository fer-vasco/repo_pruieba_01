import sqlite3
import pandas as pd
from datetime import datetime, timedelta, UTC
import pytz


tabla_hs = "data/horas.db"


def conectar_con_SQL(tabla_sql=tabla_hs):
    return sqlite3.connect(tabla_sql)


def guardar_df_en_SQL(dataframe_para_sql, tabla_sql=tabla_hs):
    with conectar_con_SQL() as conn:
        dataframe_para_sql.to_sql(
            tabla_sql,
            conn,
            if_exists="append",  # o "append"
            index=False
        )
    print(f'df guardado en {tabla_sql}')


def cargar_base_de_datos(tabla_sql=tabla_hs):
    cadena = "SELECT * FROM '" + tabla_sql + "'"
    with conectar_con_SQL() as conn:
        return pd.read_sql(cadena, conn)



now = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))
now = now.replace(tzinfo=None)

df = pd.DataFrame(data = [now], columns=['hora'])
print(df)
guardar_df_en_SQL(df)

df2 = cargar_base_de_datos()
print(df2)