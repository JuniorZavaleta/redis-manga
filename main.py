import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Mangas
r.hmset('M1', {'nombre': "Aisazu Ni Wa Irarenai", 'carpeta': "AisazuNihaIrarenai"})

# Etiquetas
r.hmset('L1', {'esp': 'Futbol', 'eng': 'Soccer'})

# Paginas de cada manga con sus etiquetas
r.sadd('M1P1', '1', '2')
