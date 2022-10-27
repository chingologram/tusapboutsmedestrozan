import praw
import time
import json
import random
import boto3
import os
import math
from lark import Lark, Transformer, Tree, Token, Visitor

def everyfifteenseconds(evt, context):
    start = time.time()
    while True:
        tusapboutsmedestrozan(evt, context)
        time.sleep(15)
        duration = time.time() - start
        if duration > 45.0:
            break


class PoemTransformer(Transformer):

    def __init__(self) -> None:
        super().__init__()

    def transform(self, tree: Tree):
        return super().transform(tree)

    def character(self, t):
        t[0].value = "%s\u0336" % t[0].value
        return Tree('strokecharacter', t)

    def strokecharacter(self, t):
        t[0].value = '▓'
        return Tree('bloque', t)

    def separator(self, t):
        return Tree('separator', t)

    def bloque(self, t):
        return Tree('bloque', t) 


def transformar(poema, veces):
    grammar = '''
        start: (strokecharacter | bloque | character | separator )*
        separator: "," | " " | "." | "\\n" | "\\t" 
        strokecharacter: /\w\u0336/
        character: /\w/
        bloque: "▓"


    '''

    random.seed(0)

    l = Lark(grammar, keep_all_tokens=True)
    r = l.parse(poema)

    chars = [ c for c in r.find_data('character') ]

    i = 0
    while i < veces:
        position = random.randint(0, len(r.children) - 1)
        if r.children[position].data in [ 'separator' ]:
            continue
        transformer = PoemTransformer()
        r.children[position] = transformer.transform(r.children[position])
        i+=1


    poema = ""
    r= r.copy()
    for i in r.scan_values(lambda x: isinstance(x, Token)):
        poema += i.value
    return poema


def tusapboutsmedestrozan(evt, context):
    s3 = boto3.client('s3')

    data = s3.get_object(Bucket="tusapboutsmedestrozan", Key="post_url")
    post_url = data['Body'].read().encode('utf-8')

    # credenciales en praw.ini, no versionado
    # se necesita un archivo praw.ini con client_id, client_secret, password, username, user_agent
    reddit = praw.Reddit()

    poema = """
	Tus apbouts me destrozan.
	Tus comentarios
    tus daunvouts
    también.
    La materia es secreto.
	El número
    una distancia irresoluble.
    Somos una criptografía mutua.
    Colgados de una nube de muerte
	nos escroleamos a nosotros mismos.
	Le damos efecinco
	a la soledad.
"""

    s = reddit.submission(url=post_url)

    marcas = s.num_comments + abs(s.score) # + (time.time() - s.created_utc) // 60 - 20

    poema = transformar(poema, marcas)

    s.edit(poema + "\n\n\nhttps://github.com/nmercado1986/tusapboutsmedestrozan\n\n\n(https://instagram.com/chingologram)[@Chingologram]")


if __name__ == "__main__":
    
    poema = """
	Tus apbouts me destrozan.
	Tus comentarios
	tus posts
	tus daunvouts
	también.
	La materia es secreto.
	El número
	una distancia irresoluble.
	Somos una criptografía mutua,
	colgados de una nube de muerte
	nos escroleamos a nosotros mismos.
	Le damos efecinco
	a la soledad.
"""

    for i in range(1, 1000):
        print(i)
        print(transformar(poema, i))
