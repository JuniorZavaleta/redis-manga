import redis
import csv

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.flushall()

with open('./labels.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader.next()
    i = 1
    for row in reader:
        r.hmset('L'+str(i), {'esp': row[0], 'eng': row[1]})
        i = i + 1

with open('./mangas.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader.next()
    i = 1
    for row in reader:
        r.hmset('M' + str(i), {'nombre': row[0], 'carpeta': row[1]})
        i = i + 1

with open('./mangalabels.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader.next()
    i = 1
    for row in reader:
        r.sadd('M{0}P{1}'.format(row[0], row[1]), *set(row[2].split('-')))
