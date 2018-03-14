#!venv/bin/python
from dbmanager import DBManager
import search

m = DBManager()

iquery = ['want', 'second', 'victory', 'guest', 'rica']
result = search.calcTF(iquery, m.relations, m.docs)

for r in result:
    print(r)
