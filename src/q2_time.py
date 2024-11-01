import pandas as pd
import emoji

from collections import Counter
from typing import List, Tuple

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Usamos dataframe
    df = pd.read_json(file_path, lines=True)

    # Contador para emojis
    emoji_count = Counter()

    # Iteración por fila del dataframe
    for content in df['renderedContent']:
        if isinstance(content, str):
            
            # Contar emojis por cada caracter en cada tweet
            for char in content:
                if emoji.is_emoji(char):
                    emoji_count[char] += 1

    # Obtener el Top 10
    top_10_emoji = emoji_count.most_common(10)
    
    return top_10_emoji