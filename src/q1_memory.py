import json
import time

from typing import List, Tuple
from datetime import datetime
from collections import defaultdict

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Diccionario para contar los tweet por día
    date_count = defaultdict(int)
    # Diccionario para contar los weet por día de los usuarios
    user_count = defaultdict(lambda: defaultdict(int))

    # Procesar el JSON
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            date = datetime.fromisoformat(tweet["date"]).date()
            user = tweet["user"]["username"]

            # Contar fecha y usuario
            date_count[date] += 1
            user_count[date][user] += 1

    # Top 10 de días por cantidad de mensajes
    top_10_dates = sorted(date_count.items(), key=lambda x: -x[1])[:10]

    # Encuentra al usuario más activo para cada fecha
    output = []
    for date, i in top_10_dates:
        # Usuario más activo para fecha en particular
        top_user = max(user_count[date], key=user_count[date].get)
        output.append((date, top_user))

    # Ordenar por fecha ascendente
    output_final = sorted(output, key=lambda x: x[0])
    time.sleep(2)

    return output_final
