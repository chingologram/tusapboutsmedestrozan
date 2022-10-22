# import requests
# import time
# import json
# import praw
# import unidecode
# import boto3
# import numpy as np
# import os
# from os import path
# import PIL
# import random
# from wordcloud import WordCloud
# import nltk

import praw
import json
import random
import boto3
import os
import math


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return f"hsl(209, 59%, {random.randint(40,70)}%)"

def tusapboutsmedestrozan(evt, context):
    s3 = boto3.client('s3')

    # credenciales en praw.ini, no versionado
    # se necesita un archivo praw.ini con client_id, client_secret, password, username, user_agent
    reddit = praw.Reddit()

    poema = """
	A cada minuto
	tus apbouts me destrozan.
	Tus posts, tus comentarios, tus daunvouts, también.
	Son una galleta
	que me carcome.
	Asi me quedo
	cada vez más 
	comprimido.
	Nos escroleamos
	a nosotros mismos
	dándole efecinco
	a la soledad.
"""

    url = os.getenv("POST_URL")
    s = reddit.submission(url=url)

    marcas = s.num_comments + abs(s.score) - 1

    random.seed(0)

    poema = list(poema)

    i = 0
    while i < marcas:
        pos = random.randint(0, len(poema))
        if poema[pos] in ("\n", "\t", ",", "."):
            continue
        if poema[pos] == '░':
            poema[pos] = '▒'
            continue
        if poema[pos] == '▒':
            poema[pos] ='▓'
            continue
        poema[pos] = '░'
        i += 1

    poema = "".join(poema)

    s.edit(poema + "\n\n\nhttps://github.com/nmercado1986/tusapboutsmedestrozan")
