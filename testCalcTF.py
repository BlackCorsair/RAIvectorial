#!venv/bin/python
from dbmanager import DBManager
from operator import itemgetter
import search

m = DBManager()

iquery = ['want', 'second', 'victory', 'guest', 'rica']
result = sorted(search.calcTF(iquery, m.relations, m.docs),
                key=itemgetter('doc'))

for r in result:
    print(r)
