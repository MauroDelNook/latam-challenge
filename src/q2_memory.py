import emoji
import json
import time
from typing import List, Tuple
from collections import defaultdict

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Diccionario para contar emojis
    emoji_count = defaultdict(int)
    
    # Abrimos archivo y buscamos por el campo renderedContent
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet.get("renderedContent", "")
            
            # Extraer emoji
            for char in content:
                if emoji.is_emoji(char):
                    emoji_count[char] += 1

    # Obtener el top 10 de emojis más usados
    top_10_emoji = sorted(emoji_count.items(), key=lambda x: x[1], reverse=True)[:10]
    time.sleep(2)

    return top_10_emoji