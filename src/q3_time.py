import pandas as pd

from collections import Counter
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Cargar dataframe
    df = pd.read_json(file_path, lines=True)

    # Extraer usuarios mencionados desde la lista dentro de campo username
    all_mentions = []
    for mentions in df['mentionedUsers'].dropna():
        all_mentions.extend([user['username'] for user in mentions if 'username' in user])

    # Contar menciones y filtrar por top 10
    mention_count = Counter(all_mentions)
    top_10_mentions = mention_count.most_common(10)
    
    return top_10_mentions
