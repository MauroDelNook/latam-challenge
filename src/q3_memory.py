import json
import time
from typing import List, Tuple
from collections import Counter

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_count = Counter()
    
    # Procesar archivo y obtener los usuarios mencionados
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            mentioned_users = tweet.get("mentionedUsers", [])

            # Revisar que usuarios mencionados sea una lista
            if isinstance(mentioned_users, list):
                for user in mentioned_users:
                    username = user.get("username", "")
                    if username:
                        mention_count[username] += 1

    # Obtener el top 10 de usuario
    top_10_mentions = mention_count.most_common(10)
    time.sleep(2)
    
    return top_10_mentions