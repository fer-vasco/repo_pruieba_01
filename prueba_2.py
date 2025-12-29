import sqlite3
import pandas as pd
from datetime import datetime, timedelta, UTC
import pytz
from db_2 import guardar_df_en_SQL, cargar_base_de_datos



now = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))
now = now.replace(tzinfo=None)

df = pd.DataFrame(data = [now], columns=['hora'])
print(df)
guardar_df_en_SQL(df)

df2 = cargar_base_de_datos()
print(df2)